from overrides import override

from domain.user_sample.module.session.interface import UserSampleSessionInterface


class UserSampleFastAPISessionManager(UserSampleSessionInterface):
    def __init__(self):
        pass

    @override
    def enter_session(self, user_id: str) -> None:
        pass
