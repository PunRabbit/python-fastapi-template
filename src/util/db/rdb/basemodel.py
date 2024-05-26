from pydantic import BaseModel


class RDBConfig(BaseModel):
    url: str
