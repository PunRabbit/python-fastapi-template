class DBInfraException(Exception):
    def __init__(self, msg: str):
        self.msg: str = msg

    def __str__(self):
        return self.msg


class AlChemyConnectionError(DBInfraException):
    def __init__(self, msg: str):
        super().__init__(msg=msg)


class PyMongoConnectionError(DBInfraException):
    def __init__(self, msg: str):
        super().__init__(msg=msg)


class RedisConnectionError(DBInfraException):
    def __init__(self, msg: str):
        super().__init__(msg=msg)
