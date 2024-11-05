"""This module provides check of functions in 
nipcbatt.pcbatt_library_code.ni_845x_i2c_spi_communications.ni_845x_helper_functions package"""

import importlib.metadata
import logging
import sys
import unittest

from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_utilities.native_interop_utilities import (
    create_native_stdcall_win_function,
)


class TestCreateNativeStdCallWinFunction(unittest.TestCase):
    """Defines a test fixture that checks
    `_create_native_stdcall_win_function` function is ready to use.

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand([("is_none", None), ("is_empty", ""), ("is_whitespace", " ")])
    def test_create_native_stdcall_win_function_fails_if_dll_path(
        self, test_name: str, dll_path: str
    ):
        """unit test of _create_native_stdcall_win_function."""
        logging.debug("Running with %s", test_name)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            create_native_stdcall_win_function(
                dll_path=dll_path,
                function_name=None,
                return_value_type=str,
                arguments_types=[],
            )

        # Assert
        self.assertEqual(
            "The string value dll_path is None, empty or whitespace.",
            str(ctx.exception),
        )

    @parameterized.expand([("none", None), ("empty", ""), ("whitespace", " ")])
    def test_create_native_stdcall_win_function_fails_if_function_name_is_invalid(
        self, test_name: str, function_name: str
    ):
        """unit test of _create_native_stdcall_win_function."""
        logging.debug("Running with %s", test_name)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            create_native_stdcall_win_function(
                dll_path="kernel32.dll",
                function_name=function_name,
                return_value_type=str,
                arguments_types=[],
            )

        # Assert
        self.assertEqual(
            "The string value function_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_create_native_stdcall_win_function_fails_if_library_not_exist(self):
        """unit test of _create_native_stdcall_win_function."""
        # Arrange

        # Act
        with self.assertRaises(FileNotFoundError) as ctx:
            create_native_stdcall_win_function(
                dll_path="library_not_exist.dll",
                function_name="function",
                return_value_type=str,
                arguments_types=[],
            )

        # Assert
        self.assertEqual(
            "file 'library_not_exist.dll' not found",
            str(ctx.exception),
        )

    def test_create_native_stdcall_win_function_fails_if_function_not_found(self):
        """unit test of _create_native_stdcall_win_function."""
        # Arrange

        # Act
        with self.assertRaises(AttributeError) as ctx:
            create_native_stdcall_win_function(
                dll_path="kernel32.dll",
                function_name="function_not_exist",
                return_value_type=str,
                arguments_types=[],
            )

        # Assert
        self.assertEqual(
            "function 'function_not_exist' not found",
            str(ctx.exception),
        )


if __name__ == "__main__":
    unittest.main()
