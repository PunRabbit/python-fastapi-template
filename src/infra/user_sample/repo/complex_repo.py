from overrides import override
from dependency_injector.wiring import inject, Provide

from domain.user_sample.repo.interface import UserSampleRepoInterface
from domain.user_sample.repo.interface import UserInsertInfo, UserWaitInfo, UserBaseInfo
from container.util.util_container import UtilContainer
from util.db.rdb.alchemy_module import AlchemyModule
from util.db.mongo.pymongo_module import PyMongoModule
from util.db.redis.redis_module import RedisModule


class UserSampleComplexRepoManager(UserSampleRepoInterface):
    @inject
    def __init__(
        self,
        maria_module: AlchemyModule = Provide[UtilContainer.rdb_module],
        mongo_module: PyMongoModule = Provide[UtilContainer.mongo_module],
        redis_module: RedisModule = Provide[UtilContainer.redis_module],
    ):
        self.maria_module: AlchemyModule = maria_module
        self.mongo_module: PyMongoModule = mongo_module
        self.redis_module: RedisModule = redis_module

    @override
    def insert_user(self, user_info: UserInsertInfo) -> bool:
        pass

    @override
    def find_user(self, user_id: str) -> UserBaseInfo:
        pass

    @override
    def insert_wait_list(self, user_wait_info: UserWaitInfo) -> bool:
        pass

    @override
    def find_wait_list(self, user_id: str) -> UserWaitInfo:
        pass

    @override
    def delete_wait_list(self, user_id: str) -> UserWaitInfo:
        pass
