from pydantic import BaseModel


class DBHealthResult(BaseModel):
    rdb: bool
    mongo: bool
    redis: bool
