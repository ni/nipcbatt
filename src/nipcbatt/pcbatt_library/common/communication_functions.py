"""Defines functions that are common to communication building blocks based on I2C/SPI protocols."""

from typing import List

import numpy

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_library.common.communication_data_types import (
    MemoryAddressParameters,
    MemoryPageCharacteristics,
)


def create_command_for_i2c_communications(
    address_parameters: MemoryAddressParameters,
) -> numpy.ndarray[numpy.ubyte]:
    """Creates an array of data bytes
    representing the command for I2C communications.

    Args:
        address_parameters (MemoryAddressParameters):
            An instance of `MemoryAddressParameters` representing the address for device access.

    Returns:
        numpy.ndarray[numpy.ubyte]: The array of bytes representing the command.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    return numpy.array(
        _ni_845x_functions.convert_memory_address_to_data_bytes_array(
            address_parameters.memory_address,
            address_parameters.address_type,
            address_parameters.address_endianness,
        ),
        dtype=numpy.ubyte,
    )


def create_command_for_spi_read_communication(
    address_parameters: MemoryAddressParameters,
    number_of_bytes_to_read: int,
) -> numpy.ndarray[numpy.ubyte]:
    """Creates an array of data bytes
    representing the command for SPI read communication.

    Args:
        address_parameters (MemoryAddressParameters):
            An instance of `MemoryAddressParameters` representing the address for device access.
        number_of_bytes_to_read (int):
            The number of bytes to read from SPI device.

    Returns:
        numpy.ndarray[numpy.ubyte]: The array of bytes representing the command.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    return numpy.array(
        _ni_845x_functions.create_command_for_spi_read_communication_impl(
            memory_address=address_parameters.memory_address,
            address_type=address_parameters.address_type,
            address_endianness=address_parameters.address_endianness,
            number_of_bytes_to_read=number_of_bytes_to_read,
        ),
        dtype=numpy.ubyte,
    )


def create_command_for_spi_write_communication(
    address_parameters: MemoryAddressParameters,
    number_of_bytes_to_write: int,
) -> numpy.ndarray[numpy.ubyte]:
    """Creates an array of data bytes
    representing the instruction for SPI write communication.

    Args:
        address_parameters (MemoryAddressParameters):
            An instance of `MemoryAddressParameters` representing the address for device access.
        number_of_bytes_for_access (int):
            The number of bytes to write to SPI device.

    Returns:
        numpy.ndarray[numpy.ubyte]: The array of bytes representing the instruction.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    return numpy.array(
        _ni_845x_functions.create_command_for_spi_write_communication_impl(
            address_parameters.memory_address,
            address_parameters.address_type,
            address_parameters.address_endianness,
            number_of_bytes_to_write,
        ),
        dtype=numpy.ubyte,
    )


def compute_pages_characteristics(
    data_memory_start_address: int,
    number_of_bytes_to_write: int,
    number_of_bytes_per_page: int,
) -> List[MemoryPageCharacteristics]:
    """Computes the list of contiguous pages that will contain data bytes to write to device.

    Args:
        data_memory_start_address (int):
            The address where data bytes will be written.
            This is also the address of the first page.
        number_of_bytes_to_write (int):
            The total number of bytes to write to device.
        number_of_bytes_per_page (int):
            The number of bytes in a memory page.
    Returns:
        List[MemoryPageCharacteristics]:
            A list of `MemoryPageCharacteristics` representing
            the zone of memory pages where data will be written.
    """  # noqa: D411 - Missing blank line before section (auto-generated noqa)
    pages_characteristics = []

    current_page_address = data_memory_start_address
    current_index_in_data_bytes_array = 0

    # The first page contains enough data bytes to fit at start EEPROM address.
    # So that, Data Memory Address + Current Number Of Bytes In Page =>
    # Start Address of the next Page.
    current_number_of_bytes_in_page = (
        data_memory_start_address // number_of_bytes_per_page + 1
    ) * number_of_bytes_per_page - data_memory_start_address

    while current_index_in_data_bytes_array < number_of_bytes_to_write:
        # if this is the last page to add,
        # the number of bytes is the number of bytes to write - the current index
        number_ob_bytes_in_page = (
            current_number_of_bytes_in_page
            if (current_index_in_data_bytes_array + current_number_of_bytes_in_page)
            < number_of_bytes_to_write
            else number_of_bytes_to_write - current_index_in_data_bytes_array
        )
        page_chatacteristics = MemoryPageCharacteristics(
            index_in_data_bytes_array=current_index_in_data_bytes_array,
            number_of_bytes_in_page=number_ob_bytes_in_page,
            data_memory_address=current_page_address,
        )
        pages_characteristics.append(page_chatacteristics)

        current_index_in_data_bytes_array += current_number_of_bytes_in_page
        current_page_address += current_number_of_bytes_in_page
        current_number_of_bytes_in_page = number_of_bytes_per_page

    return pages_characteristics
