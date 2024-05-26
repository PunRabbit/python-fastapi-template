from abc import ABCMeta, abstractmethod


class UserSampleEncryptionInterface(metaclass=ABCMeta):
    @abstractmethod
    def encrypt_message(self, message: str) -> str:
        pass

    @abstractmethod
    def decrypt_message(self, message: str) -> str:
        pass
