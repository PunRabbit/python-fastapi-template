from pydantic import BaseModel


class VerifyInfo(BaseModel):
    email: str
    user_id: str
    auth_code: str
