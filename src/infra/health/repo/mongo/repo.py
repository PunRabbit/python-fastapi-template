from overrides import override
from pymongo.errors import ConnectionFailure
from dependency_injector.wiring import inject, Provide

from domain.health.repo.interface import HealthRepoInterface
from util.db.mongo.pymongo_module import PyMongoModule
from container.util.util_container import UtilContainer


class MongoHealthRepoManager(HealthRepoInterface):
    @inject
    def __init__(self, mongo_module: PyMongoModule = Provide[UtilContainer.mongo_module]):
        self.mongo_module: PyMongoModule = mongo_module

    @override
    def ping_to_db(self) -> bool:
        try:
            client = self.mongo_module.take_connection()
            client.admin.command("ping")
            return True
        except ConnectionFailure:
            return False
