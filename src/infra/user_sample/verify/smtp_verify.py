from overrides import override

from domain.user_sample.module.verify.interface import UserSampleVerifyInterface
from domain.user_sample.module.verify.basemodel import VerifyInfo


class UserSampleSmtpManager(UserSampleVerifyInterface):
    def __init__(self):
        pass

    @override
    def send_email(self, email: str, auth_code: str) -> bool:
        pass

    @override
    def check_verify(self, verify_info: VerifyInfo) -> bool:
        pass
