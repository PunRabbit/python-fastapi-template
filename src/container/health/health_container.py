from dependency_injector.containers import DeclarativeContainer, WiringConfiguration
from dependency_injector.providers import Configuration, Container, Singleton

from container.config.config_container import ConfigContainer
from util.discover.module_discover import discover_python_modules
from domain.health.service.interface import HealthServiceInterface
from domain.health.repo.interface import HealthRepoInterface
from application.health.application import HealthApplication
from infra.health.repo.redis.repo import RedisHealthRepoManager
from infra.health.repo.rdb.repo import MariaHealthRepoManager
from infra.health.repo.mongo.repo import MongoHealthRepoManager


class HealthContainer(DeclarativeContainer):
    _custom_config: Configuration = Container(ConfigContainer).config

    _redis_manager: HealthRepoInterface = Singleton(RedisHealthRepoManager)
    _rdb_manager: HealthRepoInterface = Singleton(MariaHealthRepoManager)
    _mongo_manager: HealthRepoInterface = Singleton(MongoHealthRepoManager)

    health_service: HealthServiceInterface = Singleton(
        HealthApplication, _rdb_manager, _mongo_manager, _redis_manager
    )

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=discover_python_modules()
    )
