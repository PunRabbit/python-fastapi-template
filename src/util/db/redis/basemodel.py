from pydantic import BaseModel


class RedisConfig(BaseModel):
    url: str
    port: int
    index: int
