from abc import ABCMeta, abstractmethod


class HealthRepoInterface(metaclass=ABCMeta):
    @abstractmethod
    def ping_to_db(self) -> bool:
        pass
