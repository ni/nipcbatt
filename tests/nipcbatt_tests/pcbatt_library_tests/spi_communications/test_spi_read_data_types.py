"""This module provides SPI read communication data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import numpy
from varname import nameof

import nipcbatt


class TestSpiReadParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiReadParameters` class is ready to use.

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

    def test_spi_read_parameters_init_fails_when_memory_address_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        """
        expected_number_of_bytes_to_read = 7

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiReadParameters(
                    number_of_bytes_to_read=expected_number_of_bytes_to_read,
                    memory_address_parameters=None,
                )
            )

        self.assertEqual(
            "The object memory_address_parameters is None.",
            str(ctx.exception),
        )

    def test_spi_read_parameters_init_fails_when_number_of_bytes_to_read_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        """
        expected_number_of_bytes_to_read = 0
        expected_memory_address_parameters = nipcbatt.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiReadParameters(
                    number_of_bytes_to_read=expected_number_of_bytes_to_read,
                    memory_address_parameters=expected_memory_address_parameters,
                )
            )

        self.assertEqual(
            "The value number_of_bytes_to_read must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_read_parameters_init_fails_when_number_of_bytes_to_read_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        """
        expected_number_of_bytes_to_read = -7
        expected_memory_address_parameters = nipcbatt.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiReadParameters(
                    number_of_bytes_to_read=expected_number_of_bytes_to_read,
                    memory_address_parameters=expected_memory_address_parameters,
                )
            )

        self.assertEqual(
            "The value number_of_bytes_to_read must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_read_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadParameters.
        """
        expected_number_of_bytes_to_read = 7
        expected_memory_address_parameters = nipcbatt.MemoryAddressParameters(
            memory_address=50,
            address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
            address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
        )

        instance = nipcbatt.SpiReadParameters(
            number_of_bytes_to_read=expected_number_of_bytes_to_read,
            memory_address_parameters=expected_memory_address_parameters,
        )

        actual_number_of_bytes_to_read = instance.number_of_bytes_to_read
        actual_memory_address_parameters = instance.memory_address_parameters

        self.assertEqual(expected_number_of_bytes_to_read, actual_number_of_bytes_to_read)
        self.assertEqual(
            expected_memory_address_parameters,
            actual_memory_address_parameters,
        )


class TestSpiReadCommunicationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiReadCommunicationConfiguration` class is ready to use.

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

    def test_spi_read_communication_configuration_init_fails_when_device_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        """
        # Arrange
        expected_communication_parameters = nipcbatt.SpiCommunicationParameters(
            chip_select=50,
            clock_rate_kilohertz=100,
            clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
        )
        expected_communication_read_parameters = nipcbatt.SpiReadParameters(
            number_of_bytes_to_read=7,
            memory_address_parameters=nipcbatt.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiReadCommunicationConfiguration(
                    device_parameters=None,
                    communication_parameters=expected_communication_parameters,
                    read_parameters=expected_communication_read_parameters,
                )
            )

        # Assert
        self.assertEqual("The object device_parameters is None.", str(ctx.exception))

    def test_spi_read_communication_configuration_init_fails_when_communication_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        """
        # Arrange
        expected_device_parameters = nipcbatt.SpiDeviceParameters(
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )
        expected_communication_read_parameters = nipcbatt.SpiReadParameters(
            number_of_bytes_to_read=7,
            memory_address_parameters=nipcbatt.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiReadCommunicationConfiguration(
                    device_parameters=expected_device_parameters,
                    communication_parameters=None,
                    read_parameters=expected_communication_read_parameters,
                )
            )

        # Assert
        self.assertEqual("The object communication_parameters is None.", str(ctx.exception))

    def test_spi_read_communication_configuration_init_fails_when_read_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        """
        # Arrange
        expected_device_parameters = nipcbatt.SpiDeviceParameters(
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )
        expected_communication_parameters = nipcbatt.SpiCommunicationParameters(
            chip_select=50,
            clock_rate_kilohertz=100,
            clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
        )

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiReadCommunicationConfiguration(
                    device_parameters=expected_device_parameters,
                    communication_parameters=expected_communication_parameters,
                    read_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object read_parameters is None.", str(ctx.exception))

    def test_spi_read_communication_configuration(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationConfiguration.
        """
        expected_device_parameters = nipcbatt.SpiDeviceParameters(
            voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_18,
        )
        expected_communication_parameters = nipcbatt.SpiCommunicationParameters(
            chip_select=50,
            clock_rate_kilohertz=100,
            clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
            clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
        )
        expected_communication_read_parameters = nipcbatt.SpiReadParameters(
            number_of_bytes_to_read=7,
            memory_address_parameters=nipcbatt.MemoryAddressParameters(
                memory_address=128,
                address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
                address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
            ),
        )

        instance = nipcbatt.SpiReadCommunicationConfiguration(
            device_parameters=expected_device_parameters,
            communication_parameters=expected_communication_parameters,
            read_parameters=expected_communication_read_parameters,
        )

        actual_device_parameters = instance.device_parameters
        actual_communication_parameters = instance.communication_parameters
        actual_communication_read_parameters = instance.read_parameters

        self.assertEqual(expected_device_parameters, actual_device_parameters)
        self.assertEqual(
            expected_communication_parameters,
            actual_communication_parameters,
        )
        self.assertEqual(
            expected_communication_read_parameters, actual_communication_read_parameters
        )


class TestSpiReadCommunicationData(unittest.TestCase):
    """Defines a test fixture that checks
    `TestSpiReadCommunicationData` class is ready to use.

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

    def test_spi_read_communication_data_init_fails_when_data_bytes_read_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationData.
        """
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiReadCommunicationData(
                    data_bytes_read=None,
                )
            )

        self.assertEqual(
            "The object data_bytes_read is None.",
            str(ctx.exception),
        )

    def test_spi_read_communication_data_init_fails_when_data_bytes_read_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationData.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiReadCommunicationData(
                    data_bytes_read=numpy.array([]),
                )
            )

        self.assertEqual(
            "The iterable data_bytes_read of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_spi_read_communication_data(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_read_data_types.SpiReadCommunicationData.
        """
        expected_data_bytes_read_count = 30
        expected_data_bytes_read_list = list(
            random.randint(0, 255) for i in range(0, expected_data_bytes_read_count)
        )
        expected_data_bytes_read = numpy.array(expected_data_bytes_read_list, dtype=numpy.ubyte)

        instance = nipcbatt.SpiReadCommunicationData(data_bytes_read=expected_data_bytes_read)

        actual_data_bytes_read = instance.data_bytes_read

        self.assertTrue(numpy.array_equal(a1=expected_data_bytes_read, a2=actual_data_bytes_read))


if __name__ == "__main__":
    unittest.main()
