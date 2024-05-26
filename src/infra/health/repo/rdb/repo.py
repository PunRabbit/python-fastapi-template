from overrides import override
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from dependency_injector.wiring import inject, Provide

from domain.health.repo.interface import HealthRepoInterface
from util.db.rdb.alchemy_module import AlchemyModule
from container.util.util_container import UtilContainer


class MariaHealthRepoManager(HealthRepoInterface):
    @inject
    def __init__(self, rdb_module: AlchemyModule = Provide[UtilContainer.rdb_module]):
        self.rdb_module: AlchemyModule = rdb_module

    @override
    def ping_to_db(self) -> bool:
        with self.rdb_module.get_session() as con_session:
            try:
                con_session.execute(text("SELECT 1"))
                return True
            except OperationalError:
                return False
