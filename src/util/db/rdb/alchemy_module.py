from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from util.db.rdb.basemodel import RDBConfig
from core.constant.constructor import CONSTANT
from core.exception.exception_class import AlChemyConnectionError


class AlchemyModule:
    def __init__(self, config: RDBConfig):
        self.config: RDBConfig = config
        try:
            self.engine: Engine = create_engine(url=self.config.url)
            self.session: sessionmaker = sessionmaker(bind=self.engine)
            self.base = declarative_base()
        except Exception as e:
            raise AlChemyConnectionError(
                msg=f"{CONSTANT.EXCEPTION.SQLALCHEMY_CONNECTION_ERROR} / {e.__str__()}"
            )

    def get_session(self):
        return self.session()
