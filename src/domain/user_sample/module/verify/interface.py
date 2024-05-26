from abc import ABCMeta, abstractmethod

from domain.user_sample.module.verify.basemodel import VerifyInfo


class UserSampleVerifyInterface(metaclass=ABCMeta):
    @abstractmethod
    def send_email(self, email: str, auth_code: str) -> bool:
        pass

    @abstractmethod
    def check_verify(self, verify_info: VerifyInfo) -> bool:
        pass
