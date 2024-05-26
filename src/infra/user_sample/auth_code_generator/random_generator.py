from overrides import override

from domain.user_sample.module.auth_code_generator.interface import (
    UserSampleAuthGenInterface,
)


class UserSampleRandomGenManager(UserSampleAuthGenInterface):
    def __init__(self):
        pass

    @override
    def gen_auth_code(self, user_id: str) -> str:
        pass
