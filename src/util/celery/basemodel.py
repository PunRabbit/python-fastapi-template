from pydantic import BaseModel


class CeleryConfig(BaseModel):
    broker_url: str
    name: str
