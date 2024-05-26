from dependency_injector.providers import Container, Configuration, Singleton
from dependency_injector.containers import DeclarativeContainer, WiringConfiguration

from container.config.config_container import ConfigContainer
from util.discover.module_discover import discover_python_modules
from util.db.mongo.pymongo_module import PyMongoModule
from util.db.mongo.basemodel import MongoConfig
from util.db.rdb.alchemy_module import AlchemyModule
from util.db.rdb.basemodel import RDBConfig
from util.db.redis.redis_module import RedisModule
from util.db.redis.basemodel import RedisConfig


class UtilContainer(DeclarativeContainer):
    _custom_config: Configuration = Container(ConfigContainer).config

    mongo_module: PyMongoModule = Singleton(
        PyMongoModule,
        MongoConfig(host=_custom_config.mongo.host(), port=_custom_config.mongo.port()),
    )

    rdb_module: AlchemyModule = Singleton(
        AlchemyModule, RDBConfig(url=_custom_config.rdb.host())
    )

    redis_module: RedisModule = Singleton(
        RedisModule,
        RedisConfig(
            url=_custom_config.redis.host(),
            port=_custom_config.redis.port(),
            index=_custom_config.redis.index(),
        ),
    )

    wiring_config: WiringConfiguration = WiringConfiguration(
        modules=discover_python_modules()
    )
