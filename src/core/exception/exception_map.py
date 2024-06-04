from fastapi import status
from typing import Dict, Tuple, Type

from core.exception.exception_class import *


"""
Write down Exception Info for FastAPI Global HTTP Exception Handler.

key : Exception Type
value : (HTTP Status Code, Error Info Message string)
"""
EXCEPTION_MAP: Dict[Type[Exception], Tuple[int, str]] = {
    DBInfraException: (status.HTTP_503_SERVICE_UNAVAILABLE, "Database Infra Exception")
}
