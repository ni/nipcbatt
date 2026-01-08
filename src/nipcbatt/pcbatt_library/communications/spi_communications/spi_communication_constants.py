""" Constants data types for SPI communications."""

import dataclasses

import numpy

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    Ni845xVoltageLevel,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_library.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.spi_communications.spi_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library.spi_communications.spi_read_data_types import (
    SpiReadCommunicationConfiguration,
    SpiReadParameters,
)
from nipcbatt.pcbatt_library.spi_communications.spi_write_data_types import (
    SpiWriteCommunicationConfiguration,
    SpiWriteParameters,
)


@dataclasses.dataclass
class ConstantsForSpiCommunication:
    """Constants used for SPI communication."""

    DEFAULT_VOLTAGE_LEVEL = Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    DEFAULT_CHIP_SELECT = 0
    DEFAULT_CLOCK_RATE_KILOHERTZ = 100
    DEFAULT_CLOCK_PHASE = SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE
    DEFAULT_CLOCK_POLARITY = SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW
    DEFAULT_NUMBER_OF_BYTES_TO_READ = 128
    DEFAULT_MEMORY_ADDRESS = 0
    DEFAULT_MEMORY_ADDRESS_TYPE = DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE
    DEFAULT_MEMORY_ADDRESS_ENDIANNESS = DataMemoryAddressEndianness.BIG_ENDIAN
    DEFAULT_NUMBER_OF_BYTES_PER_PAGE = 128
    DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS = 5


DEFAULT_SPI_DEVICE_PARAMETERS = SpiDeviceParameters(
    voltage_level=ConstantsForSpiCommunication.DEFAULT_VOLTAGE_LEVEL,
)

DEFAULT_SPI_COMMUNICATION_PARAMETERS = SpiCommunicationParameters(
    chip_select=ConstantsForSpiCommunication.DEFAULT_CHIP_SELECT,
    clock_rate_kilohertz=ConstantsForSpiCommunication.DEFAULT_CLOCK_RATE_KILOHERTZ,
    clock_phase=ConstantsForSpiCommunication.DEFAULT_CLOCK_PHASE,
    clock_polarity=ConstantsForSpiCommunication.DEFAULT_CLOCK_POLARITY,
)

DEFAULT_SPI_READ_PARAMETERS = SpiReadParameters(
    number_of_bytes_to_read=ConstantsForSpiCommunication.DEFAULT_NUMBER_OF_BYTES_TO_READ,
    memory_address_parameters=MemoryAddressParameters(
        memory_address=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS,
        address_type=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_TYPE,
        address_endianness=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS,
    ),
)

DEFAULT_SPI_WRITE_PARAMETERS = SpiWriteParameters(
    number_of_bytes_per_page=ConstantsForSpiCommunication.DEFAULT_NUMBER_OF_BYTES_PER_PAGE,
    delay_between_page_write_operations_milliseconds=(
        ConstantsForSpiCommunication.DEFAULT_DELAY_BETWEEN_PAGE_WRITE_OPERATIONS_MILLISECONDS
    ),
    data_to_be_written=numpy.zeros(shape=1, dtype=numpy.ubyte),
    memory_address_parameters=MemoryAddressParameters(
        memory_address=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS,
        address_type=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_TYPE,
        address_endianness=ConstantsForSpiCommunication.DEFAULT_MEMORY_ADDRESS_ENDIANNESS,
    ),
)

DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION = SpiReadCommunicationConfiguration(
    device_parameters=DEFAULT_SPI_DEVICE_PARAMETERS,
    communication_parameters=DEFAULT_SPI_COMMUNICATION_PARAMETERS,
    read_parameters=DEFAULT_SPI_READ_PARAMETERS,
)

DEFAULT_SPI_WRITE_COMMUNICATION_CONFIGURATION = SpiWriteCommunicationConfiguration(
    device_parameters=DEFAULT_SPI_DEVICE_PARAMETERS,
    communication_parameters=DEFAULT_SPI_COMMUNICATION_PARAMETERS,
    write_parameters=DEFAULT_SPI_WRITE_PARAMETERS,
)
