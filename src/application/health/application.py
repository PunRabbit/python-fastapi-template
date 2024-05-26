from overrides import override

from domain.health.service.interface import HealthServiceInterface
from domain.health.service.basemodel import DBHealthResult
from domain.health.repo.interface import HealthRepoInterface


class HealthApplication(HealthServiceInterface):
    def __init__(
        self,
        rdb_health_manger: HealthRepoInterface,
        mongo_health_manger: HealthRepoInterface,
        redis_health_manager: HealthRepoInterface,
    ):
        self.rdb_health_manager: HealthRepoInterface = rdb_health_manger
        self.mongo_health_manager: HealthRepoInterface = mongo_health_manger
        self.redis_health_manager: HealthRepoInterface = redis_health_manager

    @override
    def check_db_health(self) -> DBHealthResult:
        return DBHealthResult(
            rdb=self.rdb_health_manager.ping_to_db(),
            mongo=self.mongo_health_manager.ping_to_db(),
            redis=self.redis_health_manager.ping_to_db(),
        )
