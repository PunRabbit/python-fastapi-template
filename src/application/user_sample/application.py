from overrides import override

from domain.user_sample.service.basemodel import UserRegisterInfo
from domain.user_sample.service.interface import UserSampleServiceInterface
from domain.user_sample.repo.interface import UserSampleRepoInterface
from domain.user_sample.module.verify.interface import UserSampleVerifyInterface
from domain.user_sample.module.encryption.interface import UserSampleEncryptionInterface
from domain.user_sample.module.session.interface import UserSampleSessionInterface
from domain.user_sample.module.auth_code_generator.interface import (
    UserSampleAuthGenInterface,
)
from domain.user_sample.repo.basemodel import UserInsertInfo, UserWaitInfo, UserBaseInfo
from domain.user_sample.module.verify.basemodel import VerifyInfo


class UserSampleApplication(UserSampleServiceInterface):
    def __init__(
        self,
        repo: UserSampleRepoInterface,
        verify_manager: UserSampleVerifyInterface,
        encryption_manager: UserSampleEncryptionInterface,
        auth_code_gen_manager: UserSampleAuthGenInterface,
        session_manager: UserSampleSessionInterface,
    ):
        self.repo: UserSampleRepoInterface = repo
        self.verify_manager: UserSampleVerifyInterface = verify_manager
        self.encryption_manager: UserSampleEncryptionInterface = encryption_manager
        self.auth_code_gen_manager: UserSampleAuthGenInterface = auth_code_gen_manager
        self.session_manager: UserSampleSessionInterface = session_manager

    @override
    def register_wait_list(self, register_info: UserRegisterInfo) -> bool:
        encrypted_info: UserRegisterInfo = UserRegisterInfo(
            user_id=register_info.user_id,
            name=register_info.name,
            email=register_info.email,
            password=self.encryption_manager.encrypt_message(
                message=register_info.password
            ),
            age=register_info.age,
            phone_number=register_info.phone_number,
        )

        auth_code: str = self.auth_code_gen_manager.gen_auth_code(
            user_id=register_info.user_id
        )

        self.verify_manager.send_email(email=register_info.email, auth_code=auth_code)

        self.repo.insert_wait_list(
            user_wait_info=UserWaitInfo(
                **encrypted_info.model_dump(), auth_code=auth_code
            )
        )

        return True

    @override
    def confirm_register(self, user_id: str, auth_code: str) -> bool:
        find_wait_info: UserWaitInfo = self.repo.find_wait_list(user_id=user_id)

        self.verify_manager.check_verify(
            verify_info=VerifyInfo(
                auth_code=find_wait_info.auth_code,
                email=find_wait_info.email,
                user_id=user_id,
            )
        )

        self.repo.insert_user(
            user_info=UserInsertInfo(**find_wait_info.model_dump(), confirmation=True)
        )

        return True

    @override
    def login(self, user_id: str, password: str) -> bool:
        user_info: UserBaseInfo = self.repo.find_user(user_id=user_id)

        if password == self.encryption_manager.decrypt_message(
            message=user_info.password
        ):
            self.session_manager.enter_session(user_id=user_id)
            return True
        else:
            return False
