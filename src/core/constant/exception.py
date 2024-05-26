from dataclasses import dataclass


@dataclass(frozen=True)
class ExceptionConstant:
    BASE_ERROR_MESSAGE: str = "This is base Exception Message."

    SQLALCHEMY_CONNECTION_ERROR: str = (
        "Sqlalchemy Connection Error while try to Connecting"
    )
    PYMONGO_CONNECTION_ERROR: str = "Pymongo Connection Error while trying to Connecting"
    REDIS_CONNECTION_ERROR: str = "Redis Connection Error while trying to Connecting"
