"""This module provides test of integration of I2CReadCommunication."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions


class TestIntegrationI2cReadCommunication(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `I2cReadCommunication` class.

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

    @unittest.skipIf(
        not (
            _ni_845x_functions.is_ni_845x_installed() and _ni_845x_functions.ni_845x_device_exists()
        ),
        "The execution of test is skipped"
        + " because Ni-845x driver is not installed or no NI 845x device found on system.",
    )
    def test_integration_i2c_read_communication(self):
        """Integration test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_read_communication.I2cReadCommunication
        """
        with nipcbatt.I2cReadCommunication() as communication:
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
            read_parameters = nipcbatt.I2cReadParameters(
                number_of_bytes_to_read=2,
                memory_address_parameters=nipcbatt.MemoryAddressParameters(
                    memory_address=0,
                    address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                    address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                ),
            )
            configuration = nipcbatt.I2cReadCommunicationConfiguration(
                device_parameters=device_parameters,
                communication_parameters=communication_parameters,
                read_parameters=read_parameters,
            )

            print(f"parameters = {configuration}")
            results = communication.configure_and_read_data(configuration=communication)
            print(f"results = {results}")
            self.assertIsNotNone(None, results)
            self.assertIsInstance(results, nipcbatt.I2cReadCommunicationData)


if __name__ == "__main__":
    unittest.main()
