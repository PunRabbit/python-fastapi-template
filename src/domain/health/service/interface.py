from abc import ABCMeta, abstractmethod

from domain.health.service.basemodel import DBHealthResult


class HealthServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def check_db_health(self) -> DBHealthResult:
        pass
