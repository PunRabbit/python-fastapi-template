from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from domain.health.service.interface import HealthServiceInterface
from container.health.health_container import HealthContainer
from core.constant.constructor import CONSTANT


health_router: APIRouter = APIRouter(tags=[CONSTANT.CONTROLLER_TAG.HEALTH_TAG_NAME])


@health_router.get("/ping/db")
@inject
def ping_db(
    service: HealthServiceInterface = Depends(Provide[HealthContainer.health_service]),
):
    return service.check_db_health()
