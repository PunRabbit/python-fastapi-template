from abc import ABCMeta, abstractmethod


class UserSampleSessionInterface(metaclass=ABCMeta):
    @abstractmethod
    def enter_session(self, user_id: str) -> None:
        pass
