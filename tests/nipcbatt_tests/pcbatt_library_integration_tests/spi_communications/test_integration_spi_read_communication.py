"""This module provides test of integration of SpiReadCommunication."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions


class TestIntegrationSpiReadCommunication(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `SpiReadCommunication` class.

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
    def test_integration_spi_read_communication(self):
        """Integration test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_communication.SpiReadCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with nipcbatt.SpiReadCommunication() as communication:
            communication.initialize("USB-8452")

            device_parameters = nipcbatt.SpiDeviceParameters(
                voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33,
            )
            communication_parameters = nipcbatt.SpiCommunicationParameters(
                chip_select=0,
                clock_rate_kilohertz=1000,
                clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE,
                clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
            )
            read_parameters = nipcbatt.SpiReadParameters(
                number_of_bytes_to_read=32,
                memory_address_parameters=nipcbatt.MemoryAddressParameters(
                    memory_address=0,
                    address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                    address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                ),
            )
            configuration = nipcbatt.SpiReadCommunicationConfiguration(
                device_parameters=device_parameters,
                communication_parameters=communication_parameters,
                read_parameters=read_parameters,
            )

            print(f"parameters = {configuration}")
            results = communication.configure_and_read_data(configuration=configuration)
            print(f"results = {results}")
            self.assertIsNotNone(results)
            self.assertIsInstance(results, nipcbatt.SpiReadCommunicationData)


if __name__ == "__main__":
    unittest.main()
