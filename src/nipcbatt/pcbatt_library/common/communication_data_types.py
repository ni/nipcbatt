"""Defines datatypes that are common to communication building blocks based on I2C/SPI protocols."""

from varname import nameof

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class MemoryAddressParameters(PCBATestToolkitData):
    """Defines the settings used to specify data
    memory address format in communication device."""

    def __init__(
        self,
        memory_address: int,
        address_type: DataMemoryAddressType,
        address_endianness: DataMemoryAddressEndianness,
    ):
        """Initializes an instance of
        `MemoryAddressSettings` with specific values.

        Args:
            memory_address (int):
                The address where data are stored in device memory.
            address_type (DataMemoryAddressType):
                The type of address in device memory.
            address_endianness (DataMemoryAddressEndianness):
                The address endianness.
        """
        self._memory_address = memory_address
        self._address_type = address_type
        self._address_endianness = address_endianness

    @property
    def memory_address(self) -> int:
        """Gets the address where data are stored in device memory."""
        return self._memory_address

    @property
    def address_type(self) -> DataMemoryAddressType:
        """Gets the type of address in device memory."""
        return self._address_type

    @property
    def address_endianness(self) -> DataMemoryAddressEndianness:
        """Gets the address endianness."""
        return self._address_endianness


class MemoryPageCharacteristics(PCBATestToolkitData):
    """Characteristics of a page in the device memory.
    A page is a sub-collection of the data bytes
    starting at specific index in the data collection and a specific length."""

    def __init__(
        self,
        index_in_data_bytes_array: int,
        number_of_bytes_in_page: int,
        data_memory_address: int,
    ) -> None:
        """Initializes an instance of
        `MemoryPageCharacteristics` with specific values.

        Args:
            index_in_data_bytes_array (int):
                The index of first byte of the page in the data bytes array.
            number_of_bytes_in_page (int):
                The number of data bytes in a page.
            data_memory_address (int):
                The address value where the page will be stored.

        Raises:
            ValueError:
                Raised when
                `index_in_data_bytes_array` is negative,
                `number_of_bytes_in_page` is negative or equal to zero,
                `data_memory_address` is negative.
        """
        Guard.is_greater_than_or_equal_to_zero(
            index_in_data_bytes_array, nameof(index_in_data_bytes_array)
        )
        Guard.is_greater_than_zero(number_of_bytes_in_page, nameof(number_of_bytes_in_page))
        Guard.is_greater_than_or_equal_to_zero(data_memory_address, nameof(data_memory_address))

        self._index_in_data_bytes_array = index_in_data_bytes_array
        self._number_of_bytes_in_page = number_of_bytes_in_page
        self._data_memory_address = data_memory_address

    @property
    def index_in_data_bytes_array(self) -> int:
        """Gets the index of first byte of the page in the data collection."""
        return self._index_in_data_bytes_array

    @property
    def number_of_bytes_in_page(self) -> int:
        """Gets The number of data bytes in a page."""
        return self._number_of_bytes_in_page

    @property
    def data_memory_address(self) -> int:
        """Gets The address value where the page will be stored."""
        return self._data_memory_address
