from pydantic import BaseModel


class AppConfig(BaseModel):
    host: str
    port: int


class ErrorResponse(BaseModel):
    info: str
    message: str
