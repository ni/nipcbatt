"""Provides I2C communication with NI-845x devices."""

import numpy

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    Ni845xI2cAddressingType,
    Ni845xPullupStatus,
)
from nipcbatt.pcbatt_communication_library.ni_845x_devices import Ni845xDevicesHandler
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)


class Ni845xI2cDevicesHandler(Ni845xDevicesHandler):
    """Defines handler on I2C communication devices."""

    def __init__(self) -> None:
        """Default initialization of new `Ni845xI2cDevicesHandler` object."""
        super().__init__()
        self._configuration_handle = _ni_845x_functions.ni_845x_i2c_configuration_open_impl()

    def close(self):
        """Closes a previously opened device.

        Raises:
            PCBATTCommunicationException:
                Raised when an error occured while calling `ni845xClose` function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_i2c_configuration_close_impl(self._configuration_handle)
        super().close()

    @property
    def configuration(self):
        """Gets an instance of `Ni845xI2cConfiguration` used to configure I2C communication."""
        return Ni845xI2cConfiguration(self._configuration_handle)

    def read_data(self, number_of_bytes_to_read: int) -> numpy.ndarray[numpy.ubyte]:
        """Reads a collection of data bytes from an I2C slave device.

        Args:
            number_of_bytes_to_read (int): The number of bytes to read.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cRead` function from `ni845x.dll`

        Returns:
            numpy.ndarray[numpy.ubyte]: A `numpy.ndarray`
            of bytes containing data that have been read.
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        data_bytes_array = numpy.zeros(
            shape=(number_of_bytes_to_read),
            dtype=numpy.ubyte,
        )

        _ni_845x_functions.ni_845x_i2c_read_impl(
            device_handle=self._devices_handler,
            configuration_handle=self._configuration_handle,
            read_data_array=data_bytes_array,
        )

        return data_bytes_array

    def write_data(self, data_bytes_to_be_written: numpy.ndarray[numpy.ubyte]):
        """Writes a collection of data bytes to an I2C slave device.

        Args:
            data_bytes_to_be_written (numpy.ndarray[numpy.ubyte]): The number of bytes to write.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                the type of numpy array is not `numpy.ubyte` or
                an error occured while calling `ni845xI2cRead` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_i2c_write_impl(
            device_handle=self._devices_handler,
            configuration_handle=self._configuration_handle,
            write_data_array=data_bytes_to_be_written,
        )

    def write_and_read_data(
        self,
        data_bytes_to_be_written: numpy.ndarray[numpy.ubyte],
        number_of_bytes_to_read: int,
    ) -> numpy.ndarray[numpy.ubyte]:
        """Performs a write followed by read (combined format) on an I2C slave device.

        Args:
            data_bytes_to_be_written (numpy.ndarray[numpy.ubyte]): The number of bytes to write.
            number_of_bytes_to_read (int): The number of bytes to read.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cWriteRead` function from `ni845x.dll`

        Returns:
            numpy.ndarray[numpy.ubyte]: A `numpy.ndarray`
            of bytes containing data that have been read.
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        data_bytes_array = numpy.zeros(
            shape=(number_of_bytes_to_read),
            dtype=numpy.ubyte,
        )

        _ni_845x_functions.ni_845x_i2c_write_read_impl(
            device_handle=self._devices_handler,
            configuration_handle=self._configuration_handle,
            write_data_array=data_bytes_to_be_written,
            read_data_array=data_bytes_array,
        )

        return data_bytes_array

    def enable_pullup_resistors(self, enable: bool):
        """Enable or disables the on-board pullup resistors for I2C operations.

        Args:
            enable (bool):
               `False`: Pullup resistors are disabled.
               `True`: Pullup resistors are enabled.


        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cSetPullupEnable`
                function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_i2c_set_pullup_enable_impl(
            device_handle=self._devices_handler,
            pullup_status=(
                Ni845xPullupStatus.PULLUP_ENABLE if enable else Ni845xPullupStatus.PULLUP_DISABLE
            ),
        )


class Ni845xI2cConfiguration:
    """Defines methods used to configure I2C communication on a I2C device."""

    def __init__(self, configuration_handle: int) -> None:
        """Initializes an instance of
        `Ni845xI2cConfiguration` with specific values.

        Args:
            configuration_handle (int): The configuration handle.
        """
        self._configuration_handle = configuration_handle

    @property
    def address(self) -> int:
        """Gets the configuration address.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xI2cConfigurationGetAddress`
                function from `ni845x.dll`

        Returns:
            int: The configuration address.
        """
        return _ni_845x_functions.ni_845x_i2c_configuration_get_address_impl(
            configuration_handle=self._configuration_handle
        )

    @address.setter
    def address(self, val: int):
        """Sets the configuration's I2C slave address.

        Args:
            val (int): Specifies the address of the I2C Slave device.
        """
        _ni_845x_functions.ni_845x_i2c_configuration_set_address_impl(
            configuration_handle=self._configuration_handle, address=val
        )

    @property
    def clock_rate_kilohertz(self) -> int:
        """Gets the clock rate of the configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationGetClockRate`
                function from `ni845x.dll`

        Returns:
            int: The configuration address.
        """
        return _ni_845x_functions.ni_845x_i2c_configuration_get_clock_rate_impl(
            configuration_handle=self._configuration_handle
        )

    @clock_rate_kilohertz.setter
    def clock_rate_kilohertz(self, val: int):
        """Sets the clock rate of the configuration.

        Args:
            val (int): Specifies the I2C clock rate in kilohertz.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationSetClockRate`
                function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_i2c_configuration_set_clock_rate_impl(
            configuration_handle=self._configuration_handle, clock_rate_kilohertz=val
        )

    @property
    def addressing_type(self) -> Ni845xI2cAddressingType:
        """Gets the type of address used for configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationGetAddressSize`
                function from `ni845x.dll`

        Returns:
            int: the type of address used for configuration.
        """
        return _ni_845x_functions.ni_845x_i2c_configuration_get_addressing_type_impl(
            configuration_handle=self._configuration_handle
        )

    @addressing_type.setter
    def addressing_type(self, val: Ni845xI2cAddressingType):
        """Sets the type of address used for configuration.

        Args:
            val (int): the type of address used for configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationSnoetAddressSize`
                function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_i2c_configuration_set_addressing_type_impl(
            configuration_handle=self._configuration_handle, addressing_type=val
        )

    @property
    def ack_poll_timeout_milliseconds(self) -> int:
        """Gets the I2C ACK (acknowledge) polling timeout in milliseconds.
           When this value is zero, ACK polling is disabled.
           Otherwise, the read or write procedures call ACK polling
           until an acknowledge (ACK) is detected or the timeout is reached.

        Raises:
            PCBATTCommunicationException:
                Raised when
                an error occured while calling `ni845xI2cConfigurationGetAckPollTimeout`
                function from `ni845x.dll`

        Returns:
            int: The I2C ACK (acknowledge) polling timeout in milliseconds.
        """
        return _ni_845x_functions.ni_845x_i2c_configuration_get_ack_poll_timeout_impl(
            configuration_handle=self._configuration_handle
        )

    @ack_poll_timeout_milliseconds.setter
    def ack_poll_timeout_milliseconds(self, val: int):
        """Sets the I2C ACK (acknowledge) polling timeout in milliseconds.
           When this value is zero, ACK polling is disabled.
           Otherwise, the read or write procedures call ACK polling
           until an acknowledge (ACK) is detected or the timeout is reached.

        Args:
            val (int): the I2C ACK (acknowledge) polling timeout in milliseconds.
        """
        _ni_845x_functions.ni_845x_i2c_configuration_set_ack_poll_timeout_impl(
            configuration_handle=self._configuration_handle, timeout_milliseconds=val
        )
