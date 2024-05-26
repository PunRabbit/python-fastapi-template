import redis

from util.db.redis.basemodel import RedisConfig
from core.exception.exception_class import RedisConnectionError
from core.constant.constructor import CONSTANT


class RedisModule:
    def __init__(self, config: RedisConfig):
        self.config: RedisConfig = config

        try:
            self.pool = redis.ConnectionPool(
                host=self.config.url, port=self.config.port, db=self.config.index
            )
        except Exception as e:
            raise RedisConnectionError(
                msg=f"{CONSTANT.EXCEPTION.REDIS_CONNECTION_ERROR} / {e.__str__()}"
            )

    def get_con(self) -> redis.Redis:
        return redis.Redis(connection_pool=self.pool, decode_responses=True)
