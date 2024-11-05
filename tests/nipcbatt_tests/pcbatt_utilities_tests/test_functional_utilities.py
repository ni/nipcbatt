"""Provides unit tests related to functional_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from nipcbatt.pcbatt_utilities import functional_utilities


class TestFunctionalUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.functional_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        self.counter = 0

    def tearDown(self):
        self.counter = 0

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_repeat(self):
        """Unit test of functional_utilities.repeat"""  # noqa: D415, W505, D202 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

        @functional_utilities.repeat(10)
        def increment():
            self.counter = 1 + self.counter

        increment()
        self.assertEqual(10, self.counter)


if __name__ == "__main__":
    unittest.main()
