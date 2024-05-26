from dataclasses import dataclass

from unit.user.test_sample import UserUnitTest


@dataclass(frozen=True)
class UnitTestList:
    user: UserUnitTest = UserUnitTest()
