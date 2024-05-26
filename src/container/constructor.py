from dataclasses import dataclass
from dependency_injector.containers import DeclarativeContainer

from container.config.config_container import ConfigContainer
from container.util.util_container import UtilContainer
from container.user_sample.user_sample_conatiner import UserSampleContainer
from container.health.health_container import HealthContainer


@dataclass(frozen=True)
class ContainerConstructor:
    config: DeclarativeContainer = ConfigContainer()
    util: DeclarativeContainer = UtilContainer()
    user_sample: DeclarativeContainer = UserSampleContainer()
    health: DeclarativeContainer = HealthContainer()
