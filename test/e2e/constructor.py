from dataclasses import dataclass

from e2e.user.test_sample import UserE2ETest


@dataclass(frozen=True)
class E2ETestList:
    user: UserE2ETest = UserE2ETest()
