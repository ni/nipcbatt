""" I2C communication data types """

import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class I2cWriteParameters(PCBATestToolkitData):
    """Defines the parameters used to perform write operations on I2C device."""

    def __init__(
        self,
        number_of_bytes_per_page: int,
        delay_between_page_write_operations_milliseconds: int,
        data_to_be_written: numpy.ndarray[numpy.ubyte],
        memory_address_parameters: MemoryAddressParameters,
    ):
        """Initializes an instance of
        `I2cWriteParameters` with specific values.

        Args:
            number_of_bytes_per_page (int):
                The number of bytes per page.
            delay_between_page_write_operations_milliseconds (int):
                The delay time between two page write operations, in ms.
            data_to_be_written (numpy.ndarray[numpy.ubyte]):
                A numpy array containing the data to be written to I2C device.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            TypeError:
                raised if the type of numpy array is not `numpy.ubyte`.
            ValueError:
                Raised when
                `number_of_bytes_per_page` is negative or equal to zero,
                `delay_between_page_write_operations_milliseconds` is negative,
                `memory_address_parameters` is None.
        """
        Guard.is_greater_than_zero(number_of_bytes_per_page, nameof(number_of_bytes_per_page))
        Guard.is_greater_than_or_equal_to_zero(
            delay_between_page_write_operations_milliseconds,
            nameof(delay_between_page_write_operations_milliseconds),
        )
        Guard.is_not_none(memory_address_parameters, nameof(memory_address_parameters))
        Guard.is_not_none(data_to_be_written, nameof(data_to_be_written))
        Guard.is_not_empty(data_to_be_written, nameof(data_to_be_written))

        if data_to_be_written.dtype != numpy.ubyte:
            raise TypeError(
                PCBATTLibraryExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
            )

        self._number_of_bytes_per_page = number_of_bytes_per_page
        self._delay_between_page_write_operations_milliseconds = (
            delay_between_page_write_operations_milliseconds
        )
        self._data_to_be_written = data_to_be_written
        self._memory_address_parameters = memory_address_parameters

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `I2cWriteParameters` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """
        if isinstance(value_to_compare, self.__class__):
            return (
                self._number_of_bytes_per_page == value_to_compare._number_of_bytes_per_page
                or self._delay_between_page_write_operations_milliseconds
                == value_to_compare._delay_between_page_write_operations_milliseconds
                or numpy.array_equal(self._data_to_be_written, value_to_compare._data_to_be_written)
                or self._memory_address_parameters == value_to_compare._memory_address_parameters
            )

        return False

    @property
    def number_of_bytes_per_page(self) -> int:
        """Gets the number of bytes per page."""
        return self._number_of_bytes_per_page

    @property
    def delay_between_page_write_operations_milliseconds(self) -> int:
        """Gets the delay time between two page write operations, in ms."""
        return self._delay_between_page_write_operations_milliseconds

    @property
    def data_to_be_written(self) -> numpy.ndarray[numpy.ubyte]:
        """Gets the numpy array containing the data to be written to I2C device."""
        return self._data_to_be_written

    @property
    def memory_address_parameters(self) -> MemoryAddressParameters:
        """Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address."""
        return self._memory_address_parameters


class I2cWriteCommunicationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the I2C Write communication."""

    def __init__(
        self,
        device_parameters: I2cDeviceParameters,
        communication_parameters: I2cCommunicationParameters,
        write_parameters: I2cWriteParameters,
    ):
        """Initializes an instance of
        `I2cWriteCommunicationConfiguration` with specific values.

        Args:
            device_parameters (I2cDeviceParameters):
                An instance of `I2cDeviceParameters` that represents
                the parameters used for settings of I2C device for communications.
            communication_parameters (I2cCommunicationParameters):
                An instance of `I2cCommunicationParameters` that represents
                the parameters used for settings of I2C communication.
            write_parameters (I2cWriteParameters):
                An instance of `I2cWriteParameters` that represents
                the parameters used for settings of I2C Write communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `write_parameters` is None.
        """
        Guard.is_not_none(device_parameters, nameof(device_parameters))
        Guard.is_not_none(communication_parameters, nameof(communication_parameters))
        Guard.is_not_none(write_parameters, nameof(write_parameters))

        self._device_parameters = device_parameters
        self._communication_parameters = communication_parameters
        self._write_parameters = write_parameters

    @property
    def device_parameters(self) -> I2cDeviceParameters:
        """Gets an instance of `I2cDeviceParameters` that represents
        the parameters used for settings of I2C device for communications."""
        return self._device_parameters

    @property
    def communication_parameters(self) -> I2cCommunicationParameters:
        """Gets an instance of `I2cCommunicationParameters` that represents
        the parameters used for settings of I2C communication."""
        return self._communication_parameters

    @property
    def write_parameters(self) -> I2cWriteParameters:
        """Gets an instance of `I2cWriteParameters` that represents
        the parameters used for settings of I2C Write communication."""
        return self._write_parameters
