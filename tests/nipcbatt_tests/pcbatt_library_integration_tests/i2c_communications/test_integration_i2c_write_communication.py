"""This module provides test of integration of I2CWriteCommunication."""

import importlib.metadata
import logging
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions


class TestIntegrationI2cWriteCommunication(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `I2cWriteCommunication` class.

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
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_integration_i2c_write_communication(self):
        """Integration test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_communication.I2cWriteCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with nipcbatt.I2cWriteCommunication() as communication:
            communication.initialize("USB-8452")

            device_parameters = nipcbatt.I2cDeviceParameters(
                enable_i2c_pullup_resistor=False,
                voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33,
            )
            communication_parameters = nipcbatt.I2cCommunicationParameters(
                device_address=73,
                clock_rate_kilohertz=400,
                addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_7_BIT,
                ack_poll_timeout_milliseconds=0,
            )
            write_parameters = nipcbatt.I2cWriteParameters(
                number_of_bytes_per_page=2,
                delay_between_page_write_operations_milliseconds=10,
                data_to_be_written=numpy.array([26, 192, 30, 120, 50]),
                memory_address_parameters=nipcbatt.MemoryAddressParameters(
                    memory_address=0,
                    address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                    address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                ),
            )
            configuration = nipcbatt.I2cWriteCommunicationConfiguration(
                device_parameters=device_parameters,
                communication_parameters=communication_parameters,
                write_parameters=write_parameters,
            )

            print(f"parameters = {configuration}")
            communication.configure_and_write_data(configuration=configuration)


if __name__ == "__main__":
    unittest.main()
