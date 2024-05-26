from pydantic import BaseModel


class UserWaitReq(BaseModel):
    userId: str
    name: str
    email: str
    password: str
    age: int
    phoneNumber: str


class UserRegisterReq(BaseModel):
    userId: str
    authCode: str


class UserLoginReq(BaseModel):
    userId: str
    password: str
