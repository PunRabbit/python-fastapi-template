from pydantic import BaseModel


class MongoConfig(BaseModel):
    host: str
    port: int
