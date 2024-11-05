"""This module provides unit tests for functions defined in
nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (378 > 100 characters) (auto-generated noqa)

import importlib.metadata
import logging
import sys
import unittest
from random import random
from typing import List

from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    Ni845xI2cAddressingType,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_utilities.native_interop_utilities import check_dll_availability


def _is_ni_845x_installed():
    try:
        check_dll_availability("ni845x.dll")
        return True
    except FileNotFoundError:
        return False


class TestInvokeNi845xFunction(unittest.TestCase):
    """Defines a test fixture that checks
    `_invoke_ni_845x_function` function is ready to use.

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand([("is_none", None), ("is_empty", ""), ("is_whitespace", " ")])
    def test_invoke_ni_845x_function_fails_if_function_name(self, test_name, function_name):
        """unit test of _get_function_from_native_library."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        logging.debug("running test_invoke_ni_845x_function_fails_if_function_name_%s", test_name)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            _ni_845x_functions.invoke_ni_845x_function(
                function_name=function_name,
            )

        # Assert
        self.assertEqual(
            "The string value function_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_invoke_ni_845x_function_fails_if_function_name_does_not_exist(self):
        """unit test of _get_function_from_native_library."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(PCBATTCommunicationException) as ctx:
            _ni_845x_functions.invoke_ni_845x_function(
                function_name="ni845xFunctionNotExist",
            )

        # Assert
        self.assertEqual(
            "Failed to call function ni845xFunctionNotExist: 'ni845xFunctionNotExist'.",
            str(ctx.exception),
        )


class TestI2cConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    functions related to I2C configuration are ready to use.

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_open_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_open."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (156 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertNotEqual(
            first=0,
            second=configuration_handle,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_open_should_not_fail(self):
        """unit test of ni_845x_spi_configuration_open."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (156 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertNotEqual(
            first=0,
            second=configuration_handle,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_set_address_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_set_address."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_address = int(random() * 65535)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_set_address_impl(
            configuration_handle, expected_address
        )
        actual_address = _ni_845x_functions.ni_845x_i2c_configuration_get_address_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_address,
            second=actual_address,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_set_clock_rate_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_set_clock_rate."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_clock_rate = int(random() * 500)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_set_clock_rate_impl(
            configuration_handle, expected_clock_rate
        )
        actual_clock_rate = _ni_845x_functions.ni_845x_i2c_configuration_get_clock_rate_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_clock_rate,
            second=actual_clock_rate,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_set_addressing_type_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_set_addressing_type."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_addressing_type = Ni845xI2cAddressingType.ADDRESSING_10_BIT

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_set_addressing_type_impl(
            configuration_handle, expected_addressing_type
        )
        actual_addressing_type = (
            _ni_845x_functions.ni_845x_i2c_configuration_get_addressing_type_impl(
                configuration_handle
            )
        )
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_addressing_type,
            second=actual_addressing_type,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_i2c_configuration_set_ack_poll_timeout_should_not_fail(self):
        """unit test of ni_845x_i2c_configuration_set_ack_poll_timeout."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_ack_poll_timeout = int(random() * 20000)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()
        _ni_845x_functions.ni_845x_i2c_configuration_set_ack_poll_timeout_impl(
            configuration_handle, expected_ack_poll_timeout
        )
        actual_ack_poll_timeout = (
            _ni_845x_functions.ni_845x_i2c_configuration_get_ack_poll_timeout_impl(
                configuration_handle
            )
        )
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_ack_poll_timeout,
            second=actual_ack_poll_timeout,
        )


class TestSpiConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    functions related to SPI configuration are ready to use.

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_set_chip_select_should_not_fail(self):
        """unit test of ni_845x_spi_configuration_set_chip_select."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_chip_select = int(random() * 100)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_set_chip_select_impl(
            configuration_handle, expected_chip_select
        )
        actual_chip_select = _ni_845x_functions.ni_845x_spi_configuration_get_chip_select_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_chip_select,
            second=actual_chip_select,
        )

    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_set_clock_rate_should_not_fail(self):
        """unit test of ni_845x_spi_configuration_set_clock_rate."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_clock_rate = int(random() * 20000)

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_rate_impl(
            configuration_handle, expected_clock_rate
        )
        actual_clock_rate = _ni_845x_functions.ni_845x_spi_configuration_get_clock_rate_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_clock_rate,
            second=actual_clock_rate,
        )

    @parameterized.expand(
        [
            (
                "CLOCK_PHASE_FIRST_EDGE",
                SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE,
            ),
            (
                "CLOCK_PHASE_SECOND_EDGE",
                SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            ),
        ]
    )
    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_set_clock_phase_should_not_fail(
        self, test_name: str, clock_phase: SpiConfigurationClockPhase
    ):
        """unit test of ni_845x_spi_configuration_set_clock_phase."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)
        logging.debug("Running with %s", test_name)
        # Arrange
        expected_clock_phase = clock_phase

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_phase_impl(
            configuration_handle, expected_clock_phase
        )
        actual_clock_phase = _ni_845x_functions.ni_845x_spi_configuration_get_clock_phase_impl(
            configuration_handle
        )
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_clock_phase,
            second=actual_clock_phase,
        )

    @parameterized.expand(
        [
            (
                "CLOCK_POLARITY_IDLE_HIGH",
                SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_HIGH,
            ),
            (
                "CLOCK_POLARITY_IDLE_LOW",
                SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
            ),
        ]
    )
    @unittest.skipIf(
        not _is_ni_845x_installed(),
        "The execution of test is skipped because Ni-845x driver is not installed.",
    )
    def test_ni_845x_spi_configuration_set_clock_polarity_should_not_fail(
        self, test_name: str, clock_polarity: SpiConfigurationClockPolarity
    ):
        """unit test of ni_845x_spi_configuration_set_clock_polarity."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)
        logging.debug("Running with %s", test_name)
        # Arrange
        expected_clock_polarity = clock_polarity

        # Act
        configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_polarity_impl(
            configuration_handle, expected_clock_polarity
        )
        actual_clock_polarity = (
            _ni_845x_functions.ni_845x_spi_configuration_get_clock_polarity_impl(
                configuration_handle
            )
        )
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(configuration_handle)

        # Assert
        self.assertEqual(
            first=expected_clock_polarity,
            second=actual_clock_polarity,
        )


class TestConvertMemoryAddressToDataBytesArray(unittest.TestCase):
    """Defines a test fixture that checks
    function `convert_memory_address_to_data_bytes_array` is ready to use.

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            (
                "one byte little endian",
                12,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                DataMemoryAddressEndianness.LITTLE_ENDIAN,
                [12],
            ),
            (
                "one byte big endian",
                12,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                DataMemoryAddressEndianness.BIG_ENDIAN,
                [12],
            ),
            (
                "one byte little endian with 2-bytes sized value",
                3852,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                DataMemoryAddressEndianness.LITTLE_ENDIAN,
                [12],
            ),
            (
                "one byte big endian with 2-bytes sized value",
                3852,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                DataMemoryAddressEndianness.BIG_ENDIAN,
                [12],
            ),
            (
                "two bytes little endian",
                12,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                DataMemoryAddressEndianness.LITTLE_ENDIAN,
                [0, 12],
            ),
            (
                "two bytes big endian",
                12,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                DataMemoryAddressEndianness.BIG_ENDIAN,
                [12, 0],
            ),
            (
                "two bytes little endian with 2-bytes sized value",
                3852,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                DataMemoryAddressEndianness.LITTLE_ENDIAN,
                [15, 12],
            ),
            (
                "two bytes big endian with 2-bytes sized value",
                3852,
                DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                DataMemoryAddressEndianness.BIG_ENDIAN,
                [12, 15],
            ),
        ]
    )
    def test_convert_memory_address_to_data_bytes_array(
        self,
        test_case_name: str,
        memory_address: int,
        address_type: DataMemoryAddressType,
        address_endianness: DataMemoryAddressEndianness,
        expected_bytes_array: List[int],
    ):
        """unit test of convert_memory_address_to_data_bytes_array."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (245 > 100 characters) (auto-generated noqa)

        logging.debug("running %s.", test_case_name)

        actual_bytes_array = _ni_845x_functions.convert_memory_address_to_data_bytes_array(
            memory_address=memory_address,
            address_type=address_type,
            address_endianness=address_endianness,
        )

        self.assertListEqual(expected_bytes_array, actual_bytes_array)


if __name__ == "__main__":
    unittest.main()
