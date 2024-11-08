"""Provides unit tests related to numeric_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from nipcbatt.pcbatt_utilities import numeric_utilities


class TestNumericUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.numeric_utilities`.

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

    def test_invert_value(self):
        """Unit test of numeric_utilities.invert_value"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        self.assertEqual(1, numeric_utilities.invert_value(1))
        self.assertEqual(2, numeric_utilities.invert_value(0.5))
        self.assertRaises(ValueError, numeric_utilities.invert_value, 0)

    def test_absolute_value(self):
        """Unit test of numeric_utilities.absolute_value"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)
        self.assertEqual(1, numeric_utilities.absolute_value(-1))
        self.assertEqual(1, numeric_utilities.absolute_value(1))

    def test_percent_of(self):
        """Unit test of numeric_utilities.percent_of"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
        self.assertEqual(0, numeric_utilities.percent_of(0, 100))
        self.assertEqual(0.5, numeric_utilities.percent_of(0.5, 100))
        self.assertEqual(1, numeric_utilities.percent_of(1, 100))
        self.assertEqual(10, numeric_utilities.percent_of(10, 100))
        self.assertEqual(50, numeric_utilities.percent_of(50, 100))
        self.assertEqual(100, numeric_utilities.percent_of(100, 100))

        self.assertRaises(ValueError, numeric_utilities.percent_of, -10, 100)

    def test_from_percent_to_decimal_ratio(self):
        """Unit test of numeric_utilities.percent_of"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
        self.assertEqual(1, numeric_utilities.from_percent_to_decimal_ratio(percent=100))
        self.assertEqual(0, numeric_utilities.from_percent_to_decimal_ratio(percent=0))
        self.assertEqual(0.5, numeric_utilities.from_percent_to_decimal_ratio(percent=50))


if __name__ == "__main__":
    unittest.main()
