import uvicorn
from dataclasses import is_dataclass, dataclass
from typing import Dict, List
from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from container.config.config_container import ConfigContainer
from controller.constructor import ControllerConstructor
from core.exception.exception_map import EXCEPTION_MAP
from util.app.basemodel import AppConfig, ErrorResponse


class AppBuilder:
    @inject
    def __init__(self, config: dict = Provide[ConfigContainer.config]):
        self.app: FastAPI = FastAPI()
        self.config: AppConfig = AppConfig(**config.get("app"))

        self._route_injection(
            injection_maps=[
                self._gen_injection_map(router_class=ControllerConstructor())
            ],
            apps=[self.app],
        )

        self._create_exception_handler()

    def run(self):
        uvicorn.run(self.app, port=self.config.port, host=self.config.host)

    @classmethod
    def _route_injection(
        cls, injection_maps: List[Dict[str, List[APIRouter]]], apps: List[FastAPI]
    ):
        if len(injection_maps) != len(apps):
            raise Exception("Args Length must be Same")
        [
            target_app.include_router(router, prefix=prefix)
            for injection_map, target_app in zip(injection_maps, apps)
            for prefix, routers in injection_map.items()
            for router in routers
        ]

    @classmethod
    def _gen_injection_map(cls, router_class: dataclass) -> Dict[str, List[APIRouter]]:
        injection_map: Dict[str, List[APIRouter]] = {}

        def _split_router(routes_class: dataclass, parent_prefix: str = ""):
            current_prefix: str = parent_prefix + routes_class.prefix
            target_routers = injection_map.setdefault(current_prefix, [])

            for attr_value in vars(routes_class).values():
                if is_dataclass(attr_value):
                    _split_router(routes_class=attr_value, parent_prefix=current_prefix)
                elif isinstance(attr_value, APIRouter):
                    target_routers.append(attr_value)

        _split_router(routes_class=router_class)
        return injection_map

    def _create_exception_handler(self):
        @self.app.exception_handler(Exception)
        async def global_exception_handler(request: Request, exc: Exception):
            for exception_type, (status_code, name) in EXCEPTION_MAP.items():
                if isinstance(exc, exception_type):
                    return JSONResponse(
                        status_code=status_code,
                        content=ErrorResponse(info=name, message=exc.__str__()).dict(),
                    )

            return JSONResponse(
                status_code=500,
                content=ErrorResponse(
                    info="UnChecked Error", message=exc.__str__()
                ).dict(),
            )
