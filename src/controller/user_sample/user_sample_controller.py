from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from container.user_sample.user_sample_conatiner import UserSampleContainer
from controller.user_sample.req import UserRegisterReq, UserWaitReq, UserLoginReq
from domain.user_sample.service.interface import UserSampleServiceInterface
from domain.user_sample.service.basemodel import UserRegisterInfo
from core.constant.constructor import CONSTANT


user_sample_router: APIRouter = APIRouter(
    tags=[CONSTANT.CONTROLLER_TAG.USER_SAMPLE_TAG_NAME]
)


@user_sample_router.post("/register/wait")
@inject
def register_wait(
    req: UserWaitReq,
    service: UserSampleServiceInterface = Depends(
        Provide[UserSampleContainer.user_service]
    ),
):
    return service.register_wait_list(
        register_info=UserRegisterInfo(
            user_id=req.userId,
            email=req.email,
            password=req.password,
            age=req.age,
            name=req.name,
            phone_number=req.phoneNumber,
        )
    )


@user_sample_router.post("/register/confirm")
@inject
def register_confirm(
    req: UserRegisterReq,
    service: UserSampleServiceInterface = Depends(
        Provide[UserSampleContainer.user_service]
    ),
):
    return service.confirm_register(user_id=req.userId, auth_code=req.authCode)


@user_sample_router.post("/login")
@inject
def login(
    req: UserLoginReq,
    service: UserSampleServiceInterface = Depends(
        Provide[UserSampleContainer.user_service]
    ),
):
    return service.login(user_id=req.userId, password=req.password)
