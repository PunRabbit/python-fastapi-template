from pydantic import BaseModel


class AppConfig(BaseModel):
    host: str
    port: int
