from overrides import override

from domain.user_sample.module.encryption.interface import UserSampleEncryptionInterface


class UserSampleAESManager(UserSampleEncryptionInterface):
    def __init__(self):
        pass

    @override
    def encrypt_message(self, message: str) -> str:
        pass

    @override
    def decrypt_message(self, message: str) -> str:
        pass
