"""Provides unit tests related to iterable_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (176 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from nipcbatt.pcbatt_utilities import iterable_utilities


class TestIterableUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.iterable_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

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

    def test_count_invalid_input(self):
        """Unit test of iterable_utilities.count"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        self.assertRaises(ValueError, lambda: iterable_utilities.count(None))

    def test_count(self):
        """Unit test of iterable_utilities.count"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        self.assertEqual(first=0, second=iterable_utilities.count([])[0])
        self.assertEqual(first=1, second=iterable_utilities.count([1])[0])
        self.assertEqual(first=2, second=iterable_utilities.count([1, "aa"])[0])

        self.assertEqual(first=10, second=iterable_utilities.count(range(0, 10))[0])


if __name__ == "__main__":
    unittest.main()
