""" I2C read communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (152 > 100 characters) (auto-generated noqa)

import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class I2cReadParameters(PCBATestToolkitData):
    """Defines the parameters used to perform read operations on I2C device."""

    def __init__(
        self,
        number_of_bytes_to_read: int,
        memory_address_parameters: MemoryAddressParameters,
    ):
        """Initializes an instance of
        `I2cReadParameters` with specific values.

        Args:
            number_of_bytes_to_read (int):
                The number of bytes to read.
            memory_address_parameters (MemoryAddressParameters):
                An instance of `MemoryAddressParameters` that specifies
                the format of memory address.

        Raises:
            ValueError:
                Raised when
                `number_of_bytes_to_read` is negative or equal to zero,
                `memory_address_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(number_of_bytes_to_read, nameof(number_of_bytes_to_read))
        Guard.is_not_none(memory_address_parameters, nameof(memory_address_parameters))

        self._number_of_bytes_to_read = number_of_bytes_to_read
        self._memory_address_parameters = memory_address_parameters

    @property
    def number_of_bytes_to_read(self) -> int:
        """Gets thhe number of bytes to read."""
        return self._number_of_bytes_to_read

    @property
    def memory_address_parameters(self) -> MemoryAddressParameters:
        """Gets an instance of `MemoryAddressParameters` that specifies
        the format of memory address."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (333 > 100 characters) (auto-generated noqa)
        return self._memory_address_parameters


class I2cReadCommunicationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the I2C Read communication."""

    def __init__(
        self,
        device_parameters: I2cDeviceParameters,
        communication_parameters: I2cCommunicationParameters,
        read_parameters: I2cReadParameters,
    ):
        """Initializes an instance of
        `I2cReadCommunicationConfiguration` with specific values.

        Args:
            device_parameters (I2cDeviceParameters):
                An instance of `I2cDeviceParameters` that represents
                the parameters used for settings of I2C device for communications.
            communication_parameters (I2cCommunicationParameters):
                An instance of `I2CCommunicationParameters` that represents
                the parameters used for settings of I2C communication.
            read_parameters (I2cReadParameters):
                An instance of `I2cReadParameters` that represents
                the parameters used for settings of I2C Read communication.

        Raises:
            ValueError:
                Raised when
                `device_parameters` is None,
                `communication_parameters` is None,
                `communication_read_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(device_parameters, nameof(device_parameters))
        Guard.is_not_none(communication_parameters, nameof(communication_parameters))
        Guard.is_not_none(read_parameters, nameof(read_parameters))

        self._device_parameters = device_parameters
        self._communication_parameters = communication_parameters
        self._read_parameters = read_parameters

    @property
    def device_parameters(self) -> I2cDeviceParameters:
        """Gets an instance of `I2cDeviceParameters` that represents
        the parameters used for settings of I2C device for communications."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (370 > 100 characters) (auto-generated noqa)
        return self._device_parameters

    @property
    def communication_parameters(self) -> I2cCommunicationParameters:
        """Gets an instance of `I2cCommunicationParameters` that represents
        the parameters used for settings of I2C communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
        return self._communication_parameters

    @property
    def read_parameters(self) -> I2cReadParameters:
        """Gets an instance of `I2cReadParameters` that represents
        the parameters used for settings of I2C Read communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
        return self._read_parameters


class I2cReadCommunicationData(PCBATestToolkitData):
    """Defines data obtained after I2C read communication on I2C device."""

    def __init__(self, data_bytes_read: numpy.ndarray[numpy.ubyte]):
        """Initializes an instance of
        `I2cReadCommunicationData` with specific values.

        Args:
            data_bytes_read (numpy.ndarray):
                The array of data bytes read from I2C Device.

        Raises:
            ValueError:
                Raised when `data_bytes_read` is None or empty,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(data_bytes_read, nameof(data_bytes_read))
        Guard.is_not_empty(data_bytes_read, nameof(data_bytes_read))

        self._data_bytes_read = data_bytes_read

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `I2CReadCommunicationData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if isinstance(value_to_compare, self.__class__):
            return numpy.allclose(self._data_bytes_read, value_to_compare._data_bytes_read)

        return False

    @property
    def data_bytes_read(self) -> numpy.ndarray[numpy.ubyte]:
        """Gets the array of data bytes read from I2C Device."""
        return self._data_bytes_read
