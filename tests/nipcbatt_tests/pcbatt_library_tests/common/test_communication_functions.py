"""This module provides communication functions check."""

import importlib.metadata
import logging
import sys
import unittest
from typing import List

from parameterized import parameterized
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library.common.communication_functions import (
    compute_pages_characteristics,
    create_command_for_spi_read_communication,
    create_command_for_spi_write_communication,
)


class TestComputePagesCharacteristics(unittest.TestCase):
    """Defines a test fixture that checks
    function `compute_pages_characteristics` is ready to use.

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

    @parameterized.expand(
        [
            (
                "one page",
                0,
                48,
                128,
                [
                    nipcbatt.MemoryPageCharacteristics(0, 48, 0),
                ],
            ),
            (
                "three pages starting at 12",
                12,
                340,
                128,
                [
                    nipcbatt.MemoryPageCharacteristics(0, 116, 12),
                    nipcbatt.MemoryPageCharacteristics(116, 128, 128),
                    nipcbatt.MemoryPageCharacteristics(244, 96, 256),
                ],
            ),
            (
                "three pages starting at 56",
                56,
                159,
                96,
                [
                    nipcbatt.MemoryPageCharacteristics(0, 40, 56),
                    nipcbatt.MemoryPageCharacteristics(40, 96, 96),
                    nipcbatt.MemoryPageCharacteristics(136, 23, 192),
                ],
            ),
        ]
    )
    def test_compute_pages_characteristics(
        self,
        test_case_name: str,
        memory_start_address: int,
        number_of_bytes_to_write: int,
        number_of_bytes_per_page: int,
        expected_pages_characteristics: List[nipcbatt.MemoryPageCharacteristics],
    ):
        """unit test of compute_pages_characteristics."""
        logging.debug("running %s.", test_case_name)

        actual_pages_characteristics = compute_pages_characteristics(
            data_memory_start_address=memory_start_address,
            number_of_bytes_to_write=number_of_bytes_to_write,
            number_of_bytes_per_page=number_of_bytes_per_page,
        )
        self.assertListEqual(expected_pages_characteristics, actual_pages_characteristics)


class TestCreateArrayForSpiReadInstruction(unittest.TestCase):
    """Defines a test fixture that checks
    function `create_array_for_spi_read_instruction` is ready to use.

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

    @parameterized.expand(
        [
            (
                "one byte little endian 5 data bytes",
                12,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                5,
                [0x3, 12, 0, 0, 0, 0, 0],
            ),
            (
                "one byte little endian with 4th bit set 5 data bytes",
                268,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                5,
                # 0x3 | 0x8 => 11
                [11, 12, 0, 0, 0, 0, 0],
            ),
            (
                "two bytes little endian 7 data bytes",
                3852,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                7,
                [0x3, 15, 12, 0, 0, 0, 0, 0, 0, 0],
            ),
            (
                "two bytes big endian 7 data bytes",
                3852,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                7,
                [0x3, 12, 15, 0, 0, 0, 0, 0, 0, 0],
            ),
        ]
    )
    def test_create_array_for_spi_read_instruction(
        self,
        test_case_name: str,
        memory_address: int,
        address_type: nipcbatt.DataMemoryAddressType,
        address_endianness: nipcbatt.DataMemoryAddressEndianness,
        number_of_byte_to_read: int,
        expected_bytes_array: List[int],
    ):
        """unit test of create_array_for_spi_read_instruction."""

        logging.debug("running %s.", test_case_name)

        actual_bytes_array = create_command_for_spi_read_communication(
            address_parameters=nipcbatt.MemoryAddressParameters(
                memory_address=memory_address,
                address_type=address_type,
                address_endianness=address_endianness,
            ),
            number_of_bytes_to_read=number_of_byte_to_read,
        ).tolist()

        self.assertListEqual(expected_bytes_array, actual_bytes_array)


class TestCreateArrayForSpiWriteInstruction(unittest.TestCase):
    """Defines a test fixture that checks
    function `create_array_for_spi_write_instruction` is ready to use.

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

    @parameterized.expand(
        [
            (
                "one byte little endian 5 data bytes",
                12,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                5,
                [0x2, 12, 0, 0, 0, 0, 0],
            ),
            (
                "one byte little endian with 4th bit set 5 data bytes",
                268,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                5,
                # 0x2 | 0x8 => 11
                [10, 12, 0, 0, 0, 0, 0],
            ),
            (
                "two bytes little endian 7 data bytes",
                3852,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                7,
                [0x2, 15, 12, 0, 0, 0, 0, 0, 0, 0],
            ),
            (
                "two bytes big endian 7 data bytes",
                3852,
                nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
                7,
                [0x2, 12, 15, 0, 0, 0, 0, 0, 0, 0],
            ),
        ]
    )
    def test_create_array_for_spi_write_instruction(
        self,
        test_case_name: str,
        memory_address: int,
        address_type: nipcbatt.DataMemoryAddressType,
        address_endianness: nipcbatt.DataMemoryAddressEndianness,
        number_of_bytes_to_write: int,
        expected_bytes_array: List[int],
    ):
        """unit test of create_array_for_spi_write_instruction."""

        logging.debug("running %s.", test_case_name)

        actual_bytes_array = create_command_for_spi_write_communication(
            address_parameters=nipcbatt.MemoryAddressParameters(
                memory_address=memory_address,
                address_type=address_type,
                address_endianness=address_endianness,
            ),
            number_of_bytes_to_write=number_of_bytes_to_write,
        ).tolist()

        self.assertListEqual(expected_bytes_array, actual_bytes_array)


if __name__ == "__main__":
    unittest.main()
