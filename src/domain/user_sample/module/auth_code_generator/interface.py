from abc import ABCMeta, abstractmethod


class UserSampleAuthGenInterface(metaclass=ABCMeta):
    @abstractmethod
    def gen_auth_code(self, user_id: str) -> str:
        pass
