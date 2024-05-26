from redis import Redis, ConnectionError, TimeoutError
from overrides import override
from dependency_injector.wiring import inject, Provide

from domain.health.repo.interface import HealthRepoInterface
from util.db.redis.redis_module import RedisModule
from container.util.util_container import UtilContainer


class RedisHealthRepoManager(HealthRepoInterface):
    @inject
    def __init__(self, redis_module: RedisModule = Provide[UtilContainer.redis_module]):
        self.redis_module: RedisModule = redis_module

    @override
    def ping_to_db(self) -> bool:
        try:
            client: Redis = self.redis_module.get_con()
            client.ping()
            return True
        except (ConnectionError, TimeoutError):
            return False
