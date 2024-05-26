from custom_test_runner import CustomTestRunner
from e2e.constructor import E2ETestList
from unit.constructor import UnitTestList


if __name__ == "__main__":
    CustomTestRunner(test_case_list=[E2ETestList(), UnitTestList()]).start_test()
