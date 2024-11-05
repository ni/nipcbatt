"""This module provides I2C write communication data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt


class TestI2cWriteParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cWriteParameters` class is ready to use.

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

    def test_i2c_write_parameters_init_fails_when_memory_address_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.zeros(shape=10),
                    memory_address_parameters=None,
                )
            )

        self.assertEqual(
            "The object memory_address_parameters is None.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_data_to_be_written_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=None,
                    memory_address_parameters=nipcbatt.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The object data_to_be_written is None.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_data_to_be_written_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.array([]),
                    memory_address_parameters=nipcbatt.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The iterable data_to_be_written of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_number_of_bytes_per_page_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cWriteParameters(
                    number_of_bytes_per_page=-128,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.array([0, 2]),
                    memory_address_parameters=nipcbatt.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The value number_of_bytes_per_page must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_number_of_bytes_per_page_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cWriteParameters(
                    number_of_bytes_per_page=0,
                    delay_between_page_write_operations_milliseconds=10,
                    data_to_be_written=numpy.array([0, 2]),
                    memory_address_parameters=nipcbatt.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The value number_of_bytes_per_page must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters_init_fails_when_delay_between_page_write_operations_milliseconds_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cWriteParameters(
                    number_of_bytes_per_page=128,
                    delay_between_page_write_operations_milliseconds=-10,
                    data_to_be_written=numpy.array([0, 2]),
                    memory_address_parameters=nipcbatt.MemoryAddressParameters(
                        memory_address=50,
                        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                        address_endianness=nipcbatt.DataMemoryAddressEndianness.LITTLE_ENDIAN,
                    ),
                )
            )

        self.assertEqual(
            "The value delay_between_page_write_operations_milliseconds must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_i2c_write_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteParameters.
        """
        expected_number_of_bytes_per_page = 128
        expected_delay_between_page_write_operations_milliseconds = 10
        expected_data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        expected_data_to_be_written = numpy.array(
            expected_data_to_be_written_list, dtype=numpy.ubyte
        )
        expected_memory_address_parameters = nipcbatt.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        instance = nipcbatt.I2cWriteParameters(
            number_of_bytes_per_page=expected_number_of_bytes_per_page,
            delay_between_page_write_operations_milliseconds=(
                expected_delay_between_page_write_operations_milliseconds
            ),
            data_to_be_written=expected_data_to_be_written,
            memory_address_parameters=expected_memory_address_parameters,
        )

        actual_number_of_bytes_per_page = instance.number_of_bytes_per_page
        actual_delay_between_page_write_operations_milliseconds = (
            instance.delay_between_page_write_operations_milliseconds
        )
        actual_data_to_be_written = instance.data_to_be_written
        actual_memory_address_parameters = instance.memory_address_parameters

        self.assertEqual(expected_number_of_bytes_per_page, actual_number_of_bytes_per_page)
        self.assertEqual(
            expected_delay_between_page_write_operations_milliseconds,
            actual_delay_between_page_write_operations_milliseconds,
        )
        self.assertTrue(
            numpy.array_equal(a1=expected_data_to_be_written, a2=actual_data_to_be_written)
        )
        self.assertEqual(
            expected_memory_address_parameters,
            actual_memory_address_parameters,
        )


class TestI2cWriteCommunicationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cWriteCommunicationConfiguration` class is ready to use.

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

    def test_i2c_write_communication_configuration_init_fails_when_device_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        """
        # Arrange
        data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        data_to_be_written = numpy.array(data_to_be_written_list, dtype=numpy.ubyte)

        communication_parameters = nipcbatt.I2cCommunicationParameters(
            device_address=50,
            addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT,
            clock_rate_kilohertz=100,
            ack_poll_timeout_milliseconds=1000,
        )

        communication_write_parameters = nipcbatt.I2cWriteParameters(
            number_of_bytes_per_page=128,
            delay_between_page_write_operations_milliseconds=10,
            data_to_be_written=data_to_be_written,
            memory_address_parameters=nipcbatt.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cWriteCommunicationConfiguration(
                    device_parameters=None,
                    communication_parameters=communication_parameters,
                    write_parameters=communication_write_parameters,
                )
            )

        # Assert
        self.assertEqual("The object device_parameters is None.", str(ctx.exception))

    def test_i2c_write_communication_configuration_init_fails_when_communication_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        """
        # Arrange
        data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        data_to_be_written = numpy.array(data_to_be_written_list, dtype=numpy.ubyte)

        device_parameters = nipcbatt.I2cDeviceParameters(
            enable_i2c_pullup_resistor=True,
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )

        communication_write_parameters = nipcbatt.I2cWriteParameters(
            number_of_bytes_per_page=128,
            delay_between_page_write_operations_milliseconds=10,
            data_to_be_written=data_to_be_written,
            memory_address_parameters=nipcbatt.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cWriteCommunicationConfiguration(
                    device_parameters=device_parameters,
                    communication_parameters=None,
                    write_parameters=communication_write_parameters,
                )
            )

        # Assert
        self.assertEqual("The object communication_parameters is None.", str(ctx.exception))

    def test_i2c_write_communication_configuration_init_fails_when_write_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        """
        # Arrange
        device_parameters = nipcbatt.I2cDeviceParameters(
            enable_i2c_pullup_resistor=True,
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )

        communication_parameters = nipcbatt.I2cCommunicationParameters(
            device_address=50,
            addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT,
            clock_rate_kilohertz=100,
            ack_poll_timeout_milliseconds=1000,
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cWriteCommunicationConfiguration(
                    device_parameters=device_parameters,
                    communication_parameters=communication_parameters,
                    write_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object write_parameters is None.", str(ctx.exception))

    def test_i2c_write_communication_configuration(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types.I2cWriteCommunicationConfiguration.
        """
        data_to_be_written_list = list(random.randint(0, 255) for i in range(0, 100))
        data_to_be_written = numpy.array(data_to_be_written_list, dtype=numpy.ubyte)

        expected_device_parameters = nipcbatt.I2cDeviceParameters(
            enable_i2c_pullup_resistor=True,
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )

        expected_communication_parameters = nipcbatt.I2cCommunicationParameters(
            device_address=50,
            addressing_type=nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT,
            clock_rate_kilohertz=100,
            ack_poll_timeout_milliseconds=1000,
        )

        expected_communication_write_parameters = nipcbatt.I2cWriteParameters(
            number_of_bytes_per_page=128,
            delay_between_page_write_operations_milliseconds=10,
            data_to_be_written=data_to_be_written,
            memory_address_parameters=nipcbatt.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        instance = nipcbatt.I2cWriteCommunicationConfiguration(
            device_parameters=expected_device_parameters,
            communication_parameters=expected_communication_parameters,
            write_parameters=expected_communication_write_parameters,
        )

        # Assert
        actual_device_parameters = instance.device_parameters
        actual_communication_parameters = instance.communication_parameters
        actual_communication_write_parameters = instance.write_parameters

        self.assertEqual(expected_device_parameters, actual_device_parameters)
        self.assertEqual(
            expected_communication_parameters,
            actual_communication_parameters,
        )
        self.assertEqual(
            expected_communication_write_parameters,
            actual_communication_write_parameters,
        )


if __name__ == "__main__":
    unittest.main()
