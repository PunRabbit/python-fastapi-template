import coverage
from dataclasses import dataclass
from unittest import TestResult, TestSuite, TextTestRunner, TestCase
from typing import List, Any


class CustomTestRunner(TextTestRunner):
    """
    Custom test runner that runs a list of test cases grouped together from dataclasses.
    """

    def __init__(self, test_case_list: List[dataclass], verbosity: int = 2):
        """
        Initializes the custom test runner.
        :param test_case_list: List of dataclasses containing test cases.
        :param verbosity: Level of verbosity for test output.
        """
        super().__init__(verbosity=verbosity)
        self.test_case_list: List[dataclass] = test_case_list

    def start_test(self) -> TestResult:
        """
        Executes the tests and generates a code coverage report.
        Starts coverage measurement, runs the tests, stops coverage measurement,
        and prints the coverage report.
        :return: TestResult object containing the results of the test run.
        """
        cov: coverage.Coverage = coverage.Coverage()
        cov.start()
        result: TestResult = self.run(self._set_runners())
        cov.stop()
        cov.report()
        return result

    def _set_runners(self) -> TestSuite:
        """
        Collects all test cases from the provided dataclasses, groups them into a TestSuite,
        and returns the TestSuite.
        :return: TestSuite containing all test cases.
        """
        suite: TestSuite = TestSuite()
        for target_instance in self._find_instances_in_dataclasses():
            suite = self._combine_test_to_suite(
                init_suite=suite, target_instance=target_instance
            )
        return suite

    def _find_instances_in_dataclasses(self) -> List[Any]:
        """
        Extracts test instances from the dataclasses provided.
        :return: List of test instances derived from the dataclasses.
        """
        target_instances: List[Any] = []
        for case in self.test_case_list:
            attributes: List[Any] = [
                getattr(case, attr)
                for attr in dir(case)
                if not attr.startswith("_") and not attr.startswith("__")
            ]
            target_instances.extend(attributes)
        return target_instances

    def _combine_test_to_suite(
        self, init_suite: TestSuite, target_instance: Any
    ) -> TestSuite:
        """
        Adds the given test instances to the provided TestSuite.
        :param init_suite: The initial TestSuite to which tests will be added.
        :param target_instance: The test instance containing test methods.
        :return: TestSuite with the added test methods.
        """
        if isinstance(target_instance, TestCase):
            method_list: List[str] = self._find_test_methods(target_instance)
            for method_name in method_list:
                init_suite.addTest(target_instance.__class__(method_name))
        return init_suite

    @staticmethod
    def _find_test_methods(target_instance: TestCase) -> List[str]:
        """
        Identifies all test methods in the given test instance.
        Test methods are identified by the prefix "test_".
        :param target_instance: The test case instance to search for test methods.
        :return: List of test method names.
        """
        return [method for method in dir(target_instance) if method.startswith("test_")]
