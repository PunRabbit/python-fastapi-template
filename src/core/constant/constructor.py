from dataclasses import dataclass

from core.constant.exception import ExceptionConstant
from core.constant.controller_tag import ControllerTag


@dataclass(frozen=True)
class CoreConstructor:
    EXCEPTION: ExceptionConstant = ExceptionConstant()
    CONTROLLER_TAG: ControllerTag = ControllerTag()


CONSTANT: CoreConstructor = CoreConstructor()
