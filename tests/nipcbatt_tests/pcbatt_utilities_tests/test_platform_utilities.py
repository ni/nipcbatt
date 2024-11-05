"""Provides unit tests related to platform_utilities.py module"""

import logging
import platform
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_utilities import platform_utilities


class TestPlatformUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.platform_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

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

    def test_is_python_windows_32bits(self):
        """Unit test of pcbatt_utilities.platform_utilities.is_python_windows_32bits"""
        is_python_32_bits = platform_utilities.is_python_windows_32bits()
        logging.debug("%s = %s", nameof(is_python_32_bits), is_python_32_bits)
        self.assertIn(is_python_32_bits, [False, True])

    def test_is_python_windows_64bits(self):
        """Unit test of pcbatt_utilities.platform_utilities.is_python_windows_64bits"""
        is_python_64_bits = platform_utilities.is_python_windows_64bits()
        logging.debug("%s = %s", nameof(is_python_64_bits), is_python_64_bits)
        self.assertIn(is_python_64_bits, [False, True])


if __name__ == "__main__":
    unittest.main()
