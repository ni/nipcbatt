"""This module provides communication data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt


class TestMemoryAddressParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `MemoryAddressParameters` class is ready to use.

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

    def test_memory_address_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.common.communication_data_types.MemoryAddressParameters.
        """
        expected_memory_address = 7
        expected_address_type = nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE
        expected_address_endianness = nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN

        instance = nipcbatt.MemoryAddressParameters(
            memory_address=expected_memory_address,
            address_type=expected_address_type,
            address_endianness=expected_address_endianness,
        )

        actual_memory_address = instance.memory_address
        actual_address_type = instance.address_type
        actual_address_endianness = instance.address_endianness

        self.assertEqual(expected_memory_address, actual_memory_address)
        self.assertEqual(
            expected_address_type,
            actual_address_type,
        )
        self.assertEqual(expected_address_endianness, actual_address_endianness)


if __name__ == "__main__":
    unittest.main()
