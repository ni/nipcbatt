"""This module provides test of integration of SpiWriteCommunication."""

import importlib.metadata
import logging
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions


class TestIntegrationSpiWriteCommunication(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `SpiWriteCommunication` class.

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
    def test_integration_spi_write_communication(self):
        """Integration test of
        nipcbatt.pcbatt_library.spi_communications.spi_write_communication.SpiWriteCommunication
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with nipcbatt.SpiWriteCommunication() as communication:
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
            write_parameters = nipcbatt.SpiWriteParameters(
                number_of_bytes_per_page=1,
                delay_between_page_write_operations_milliseconds=500,
                data_to_be_written=numpy.array(
                    [
                        175,
                        166,
                        174,
                        175,
                        129,
                        207,
                        174,
                        175,
                        1,
                        129,
                        32,
                        129,
                        96,
                        129,
                        96,
                        129,
                        207,
                        174,
                    ]
                ),
                memory_address_parameters=nipcbatt.MemoryAddressParameters(
                    memory_address=0,
                    address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                    address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                ),
            )
            configuration = nipcbatt.SpiWriteCommunicationConfiguration(
                device_parameters=device_parameters,
                communication_parameters=communication_parameters,
                write_parameters=write_parameters,
            )

            print(f"parameters = {configuration}")
            communication.configure_and_write_data(configuration=configuration)


if __name__ == "__main__":
    unittest.main()
