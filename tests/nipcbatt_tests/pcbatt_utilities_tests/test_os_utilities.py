"""Provides unit tests related to os_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)

import logging
import platform
import sys
import unittest

from parameterized import parameterized

from nipcbatt.pcbatt_utilities import os_utilities


class TestOsUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.os_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

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

    @parameterized.expand(
        [
            ("C:/windows/explorer.exe", True),
            ("../winload.exe", False),
            ("./kernel32.dll", False),
        ]
    )
    def test_is_path_absolute_should_not_fail(self, file_path: str, expected_value: bool):
        """Unit test of nipcbatt.pcbatt_utilities.os_utilities.is_path_absolute"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)
        self.assertEqual(expected_value, os_utilities.is_path_absolute(file_path))

    @parameterized.expand(
        [
            ("C:\\windows", "C:\\windows\\explorer.exe", "explorer.exe"),
            ("..", "..\\winload.exe", "winload.exe"),
            (
                "C:\\Program Files",
                "C:\\Program Files\\Python310\\Scripts\\pip.exe",
                "Python310",
                "Scripts",
                "pip.exe",
            ),
        ]
    )
    def test_combine_path_components_should_not_fail(
        self, path: str, expected_combined_path: str, *paths: str
    ):
        """Unit test of nipcbatt.pcbatt_utilities.os_utilities.combine_path_components"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (277 > 100 characters) (auto-generated noqa)

        self.assertEqual(expected_combined_path, os_utilities.combine_path_components(path, *paths))
