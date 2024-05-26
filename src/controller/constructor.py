from dataclasses import dataclass
from fastapi import APIRouter

from controller.user_sample.user_sample_controller import user_sample_router
from controller.health.health_controller import health_router


@dataclass(frozen=True)
class ControllerConstructor:
    """
    You have to write down prefix for every 'dataclass' below.
    Route Injector will read that prefix for injection.
    If you want to no prefix, just leave that prefix as "". not "/".
    """

    prefix: str = ""

    @dataclass(frozen=True)
    class UserSample:
        prefix: str = "/sample"
        user_sample: APIRouter = user_sample_router

    @dataclass(frozen=True)
    class Health:
        prefix: str = "/health"
        health: APIRouter = health_router

    user_sample: UserSample = UserSample()
    health: Health = Health
