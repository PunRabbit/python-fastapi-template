from pydantic import BaseModel


class UserRegisterInfo(BaseModel):
    user_id: str
    name: str
    email: str
    password: str
    age: int
    phone_number: str
