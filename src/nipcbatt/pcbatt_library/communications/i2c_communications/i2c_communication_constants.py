""" Constants data types for I2C communications."""

import dataclasses

import numpy

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    Ni845xI2cAddressingType,
    Ni845xVoltageLevel,
)
from nipcbatt.pcbatt_library.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types import (
    I2cReadCommunicationConfiguration,
    I2cReadParameters,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types import (
    I2cWriteCommunicationConfiguration,
    I2cWriteParameters,
)


@dataclasses.dataclass
class ConstantsForI2cCommunication:
    """Constants used for I2C communication."""

    DEFAULT_ENABLE_I2C_PULLUP_RESISTOR = False
    DEFAULT_VOLTAGE_LEVEL = Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    DEFAULT_DEVICE_ADDRESS = 0x50
    DEFAULT_CLOCK_RATE_KILOHERTZ = 100
    DEFAULT_ADDRESSING_TYPE = Ni845xI2cAddressingType.ADDRESSING_7_BIT
    DEFAULT_ACK_POLL_TIMEOUT_MILLISECONDS = 0
    DEFAULT_NUMBER_OF_BYTES_TO_READ = 128
    DEFAULT_MEMORY_ADDRESS = 0
    DEFAULT_MEMORY_ADDRESS_TYPE = DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE
    DEFAULT_MEMORY_ADDRESS_ENDIANNESS = DataMemoryAddressEndianness.BIG_ENDIAN
    DEFAULT_NUMBER_OF_BYTES_PER_PAGE = 128
    DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS = 4


DEFAULT_I2C_DEVICE_PARAMETERS = I2cDeviceParameters(
    enable_i2c_pullup_resistor=ConstantsForI2cCommunication.DEFAULT_ENABLE_I2C_PULLUP_RESISTOR,
    voltage_level=ConstantsForI2cCommunication.DEFAULT_VOLTAGE_LEVEL,
)

DEFAULT_I2C_COMMUNICATION_PARAMETERS = I2cCommunicationParameters(
    device_address=ConstantsForI2cCommunication.DEFAULT_DEVICE_ADDRESS,
    addressing_type=ConstantsForI2cCommunication.DEFAULT_ADDRESSING_TYPE,
    clock_rate_kilohertz=ConstantsForI2cCommunication.DEFAULT_CLOCK_RATE_KILOHERTZ,
    ack_poll_timeout_milliseconds=(
        ConstantsForI2cCommunication.DEFAULT_ACK_POLL_TIMEOUT_MILLISECONDS
    ),
)

DEFAULT_I2C_READ_PARAMETERS = I2cReadParameters(
    number_of_bytes_to_read=ConstantsForI2cCommunication.DEFAULT_NUMBER_OF_BYTES_TO_READ,
    memory_address_parameters=MemoryAddressParameters(
        memory_address=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS,
        address_type=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_TYPE,
        address_endianness=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS,
    ),
)

DEFAULT_I2C_WRITE_PARAMETERS = I2cWriteParameters(
    number_of_bytes_per_page=ConstantsForI2cCommunication.DEFAULT_NUMBER_OF_BYTES_PER_PAGE,
    delay_between_page_write_operations_milliseconds=(
        ConstantsForI2cCommunication.DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS
    ),
    data_to_be_written=numpy.zeros(shape=1, dtype=numpy.ubyte),
    memory_address_parameters=MemoryAddressParameters(
        memory_address=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS,
        address_type=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_TYPE,
        address_endianness=ConstantsForI2cCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS,
    ),
)

DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION = I2cReadCommunicationConfiguration(
    device_parameters=DEFAULT_I2C_DEVICE_PARAMETERS,
    communication_parameters=DEFAULT_I2C_COMMUNICATION_PARAMETERS,
    read_parameters=DEFAULT_I2C_READ_PARAMETERS,
)

DEFAULT_I2C_WRITE_COMMUNICATION_CONFIGURATION = I2cWriteCommunicationConfiguration(
    device_parameters=DEFAULT_I2C_DEVICE_PARAMETERS,
    communication_parameters=DEFAULT_I2C_COMMUNICATION_PARAMETERS,
    write_parameters=DEFAULT_I2C_WRITE_PARAMETERS,
)
