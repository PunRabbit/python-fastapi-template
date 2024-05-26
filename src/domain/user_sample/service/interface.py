from abc import ABCMeta, abstractmethod

from domain.user_sample.service.basemodel import UserRegisterInfo


class UserSampleServiceInterface(metaclass=ABCMeta):
    @abstractmethod
    def register_wait_list(self, register_info: UserRegisterInfo) -> bool:
        pass

    @abstractmethod
    def confirm_register(self, user_id: str, auth_code: str) -> bool:
        pass

    @abstractmethod
    def login(self, user_id: str, password: str) -> bool:
        pass
