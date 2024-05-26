import yaml
from celery_instance import Celery
from typing import List

from util.celery.basemodel import CeleryConfig


class CeleryBuilder:
    def __init__(self, modules: List[str]):
        self.modules: List[str] = modules
        self.config: CeleryConfig = CeleryConfig(**self._load_config().get("celery"))

    def build(self):
        return Celery(
            self.config.name,
            broker=self.config.broker_url,
            backend=self.config.broker_url,
            include=self.modules,
        )

    @classmethod
    def _load_config(cls):
        with open("core/config.yaml", "r") as file:
            config: dict = yaml.safe_load(file)
            working_environment: str = config.get("environment").get("work_env")
            return config.get(working_environment)
