from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Container, Singleton

from container.config.config_container import ConfigContainer
from util.discover.module_discover import discover_python_modules
from domain.user_sample.service.interface import UserSampleServiceInterface
from domain.user_sample.repo.interface import UserSampleRepoInterface
from domain.user_sample.module.verify.interface import UserSampleVerifyInterface
from domain.user_sample.module.session.interface import UserSampleSessionInterface
from domain.user_sample.module.encryption.interface import UserSampleEncryptionInterface
from domain.user_sample.module.auth_code_generator.interface import (
    UserSampleAuthGenInterface,
)
from application.user_sample.application import UserSampleApplication
from infra.user_sample.repo.complex_repo import UserSampleComplexRepoManager
from infra.user_sample.verify.smtp_verify import UserSampleSmtpManager
from infra.user_sample.session.fastapi_session import UserSampleFastAPISessionManager
from infra.user_sample.auth_code_generator.random_generator import (
    UserSampleRandomGenManager,
)
from infra.user_sample.encryption.aes_encryption import UserSampleAESManager


class UserSampleContainer(DeclarativeContainer):
    _custom_config: Configuration = Container(ConfigContainer).config

    _user_repo: UserSampleRepoInterface = Singleton(UserSampleComplexRepoManager)
    _user_verify: UserSampleVerifyInterface = Singleton(UserSampleSmtpManager)
    _user_session: UserSampleSessionInterface = Singleton(UserSampleFastAPISessionManager)
    _user_auth_code: UserSampleAuthGenInterface = Singleton(UserSampleRandomGenManager)
    _user_encrypt: UserSampleEncryptionInterface = Singleton(UserSampleAESManager)

    user_service: UserSampleServiceInterface = Singleton(
        UserSampleApplication,
        _user_repo,
        _user_verify,
        _user_encrypt,
        _user_auth_code,
        _user_session,
    )

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=discover_python_modules()
    )
