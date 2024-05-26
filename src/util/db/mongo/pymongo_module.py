from pymongo.mongo_client import MongoClient

from core.exception.exception_class import PyMongoConnectionError
from core.constant.constructor import CONSTANT
from util.db.mongo.basemodel import MongoConfig


class PyMongoModule:
    def __init__(self, config: MongoConfig):
        self.config: MongoConfig = config
        try:
            self.client: MongoClient = MongoClient(
                host=self.config.host,
                port=self.config.port,
                document_class=dict,
                connect=True,
            )
        except Exception as e:
            raise PyMongoConnectionError(
                msg=f"{CONSTANT.EXCEPTION.PYMONGO_CONNECTION_ERROR} / {e.__str__()}"
            )

    def take_connection(self) -> MongoClient:
        return self.client
