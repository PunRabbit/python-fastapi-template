from pydantic import BaseModel


class UserBaseInfo(BaseModel):
    user_id: str
    name: str
    email: str
    password: str
    age: int
    phone_number: str


class UserWaitInfo(UserBaseInfo):
    auth_code: str


class UserInsertInfo(UserBaseInfo):
    confirmation: bool
