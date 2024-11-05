"""This module provides SpiReadCommunication check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions


class TestSpiReadCommunication(unittest.TestCase):
    """Defines a test fixture that checks the `SpiReadCommunication` class.

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
    def test_spi_read_communication(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_communication.SpiReadCommunication
        """
        with nipcbatt.SpiReadCommunication() as communication:
            communication.initialize("USB-8452")

            configuration = nipcbatt.DEFAULT_SPI_WRITE_COMMUNICATION_CONFIGURATION

            print(f"parameters = {configuration}")
            results = communication.configure_and_read_data(configuration=communication)
            print(f"results = {results}")
            self.assertIsNotNone(None, results)
            self.assertIsInstance(results, nipcbatt.SpiReadCommunicationData)


if __name__ == "__main__":
    unittest.main()
