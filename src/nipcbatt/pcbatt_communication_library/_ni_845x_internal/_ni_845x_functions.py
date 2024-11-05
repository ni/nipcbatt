"""Private module that provides a set of ni-845x functions
used in pcbatt_communication library modules."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (341 > 100 characters) (auto-generated noqa)

from ctypes import (
    POINTER,
    byref,
    c_char_p,
    c_int32,
    c_uint8,
    c_uint16,
    c_uint32,
    c_uint64,
    create_string_buffer,
)
from typing import Dict, List, Type, Union

import numpy
from varname import nameof

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    DevicesFindResultData,
    Ni845xI2cAddressingType,
    Ni845xPullupStatus,
    Ni845xVoltageLevel,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.native_interop_utilities import (
    check_dll_availability,
    create_native_stdcall_win_function,
)
from nipcbatt.pcbatt_utilities.platform_utilities import (
    is_python_windows_32bits,
    is_python_windows_64bits,
)


class _Ni845xFunctionsNames:
    """Constants defining NI-845X functions names"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)

    NI_845X_OPEN = "ni845xOpen"
    NI_845X_CLOSE = "ni845xClose"
    NI_845X_DEVICE_LOCK = "ni845xDeviceLock"
    NI_845X_DEVICE_UNLOCK = "ni845xDeviceUnlock"
    NI_845X_SET_IO_VOLTAGE_LEVEL = "ni845xSetIoVoltageLevel"
    NI_845X_SET_TIMEOUT = "ni845xSetTimeout"
    NI_845X_FIND_DEVICE = "ni845xFindDevice"
    NI_845X_FIND_DEVICE_NEXT = "ni845xFindDeviceNext"
    NI_845X_CLOSE_FIND_DEVICE_HANDLE = "ni845xCloseFindDeviceHandle"
    NI_845X_I2C_CONFIGURATION_OPEN = "ni845xI2cConfigurationOpen"
    NI_845X_I2C_CONFIGURATION_CLOSE = "ni845xI2cConfigurationClose"
    NI_845X_SPI_CONFIGURATION_OPEN = "ni845xSpiConfigurationOpen"
    NI_845X_SPI_CONFIGURATION_CLOSE = "ni845xSpiConfigurationClose"
    NI_845X_I2C_READ = "ni845xI2cRead"
    NI_845X_I2C_WRITE = "ni845xI2cWrite"
    NI_845X_I2C_WRITE_READ = "ni845xI2cWriteRead"
    NI_845X_SPI_WRITE_READ = "ni845xSpiWriteRead"
    NI_845X_I2C_SET_PULLUP_ENABLE = "ni845xI2cSetPullupEnable"
    NI_845X_I2C_CONFIGURATION_SET_ADDRESS = "ni845xI2cConfigurationSetAddress"
    NI_845X_I2C_CONFIGURATION_SET_CLOCK_RATE = "ni845xI2cConfigurationSetClockRate"
    NI_845X_I2C_CONFIGURATION_SET_ADDRESS_SIZE = "ni845xI2cConfigurationSetAddressSize"
    NI_845X_I2C_CONFIGURATION_SET_ACK_POLL_TIMEOUT = "ni845xI2cConfigurationSetAckPollTimeout"
    NI_845X_I2C_CONFIGURATION_GET_ADDRESS = "ni845xI2cConfigurationGetAddress"
    NI_845X_I2C_CONFIGURATION_GET_CLOCK_RATE = "ni845xI2cConfigurationGetClockRate"
    NI_845X_I2C_CONFIGURATION_GET_ADDRESS_SIZE = "ni845xI2cConfigurationGetAddressSize"
    NI_845X_I2C_CONFIGURATION_GET_ACK_POLL_TIMEOUT = "ni845xI2cConfigurationGetAckPollTimeout"
    NI_845X_SPI_CONFIGURATION_SET_CHIP_SELECT = "ni845xSpiConfigurationSetChipSelect"
    NI_845X_SPI_CONFIGURATION_SET_CLOCK_RATE = "ni845xSpiConfigurationSetClockRate"
    NI_845X_SPI_CONFIGURATION_SET_CLOCK_PHASE = "ni845xSpiConfigurationSetClockPhase"
    NI_845X_SPI_CONFIGURATION_SET_CLOCK_POLARITY = "ni845xSpiConfigurationSetClockPolarity"
    NI_845X_SPI_CONFIGURATION_GET_CHIP_SELECT = "ni845xSpiConfigurationGetChipSelect"
    NI_845X_SPI_CONFIGURATION_GET_CLOCK_RATE = "ni845xSpiConfigurationGetClockRate"
    NI_845X_SPI_CONFIGURATION_GET_CLOCK_PHASE = "ni845xSpiConfigurationGetClockPhase"
    NI_845X_SPI_CONFIGURATION_GET_CLOCK_POLARITY = "ni845xSpiConfigurationGetClockPolarity"
    NI_845X_STATUS_TO_STRING = "ni845xStatusToString"


NI_845X_DLL = "Ni845x.dll"

MAX_BYTE_VALUE = 255
WRITE_INSTRUCTION = 0x2
READ_INSTRUCTION = 0x3
FIRST_FOUR_BYTES_MASK = 0xF


def ni_845x_open_impl(device_name: str) -> int:
    """Opens the specific NI-845x device.

    Args:
        device_name (str): The name of the device to be opened.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xOpen` function from `ni845x.dll`.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    device_name_buffer = create_string_buffer(device_name.encode("ascii"))
    handle_type = _get_handle_type()
    device_handle = handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_OPEN, device_name_buffer, byref(device_handle)
    )

    return device_handle.value


def ni_845x_close_impl(device_handle: int):
    """Closes a previously opened device.

    Args:
        device_handle (int):
            The device handle to be closed.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xClose` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(_Ni845xFunctionsNames.NI_845X_CLOSE, handle_type(device_handle))


def ni_845x_device_lock_impl(device_handle: int):
    """Locks NI 845x devices for access by a single thread.

    Args:
        device_handle (int):
            The device handle to be locked.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xDeviceLock`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(_Ni845xFunctionsNames.NI_845X_DEVICE_LOCK, handle_type(device_handle))


def ni_845x_device_unlock_impl(device_handle: int):
    """Unlocks NI 845x devices.

    Args:
        device_handle (int):
            The device handle to be unlocked.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xUnlock` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(_Ni845xFunctionsNames.NI_845X_DEVICE_UNLOCK, handle_type(device_handle))


def ni_845x_set_io_voltage_level_impl(
    device_handle: int,
    voltage_level: Ni845xVoltageLevel,
):
    """Modifies the voltage output from a DIO port on an NI 845x device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        voltage_level (_Ni845xVoltageLevel):
            The desired voltage level.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSetIoVoltageLevel`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SET_IO_VOLTAGE_LEVEL,
        handle_type(device_handle),
        c_uint8(voltage_level),
    )


def ni_845x_set_timeout_impl(device_handle: int, timeout_milliseconds: int):
    """Modifies the global timeout for operations when using an NI 845x device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        timeout_milliseconds (int):
            The timeout value in milliseconds.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSetTimeout`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SET_TIMEOUT,
        handle_type(device_handle),
        timeout_milliseconds,
    )


def ni_845x_find_device_impl() -> DevicesFindResultData:
    """Finds an NI 845x device and returns the total number of NI 845x devices present.

    Returns:
        DevicesFindResultData: Tuple representing
            the name of the first device found,
            the handle identifying this search session (this handle is used as an input in
            ni845xFindDeviceNext and ni845xCloseFindDeviceHandle)
            and the total number of NI-845x devices found in the system.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xFindDevice`
            function from `ni845x.dll`.
    """
    string_buffer_length = 1024
    string_buffer = create_string_buffer(string_buffer_length)
    handle_type = _get_handle_type()
    find_device_handle = handle_type()
    number_of_devices_found = c_uint32()

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_FIND_DEVICE,
        string_buffer,
        byref(find_device_handle),
        byref(number_of_devices_found),
    )

    return DevicesFindResultData(
        str(string_buffer.value.decode()),
        find_device_handle.value,
        number_of_devices_found.value,
    )


def ni_845x_find_device_next_impl(find_device_handle: int) -> str:
    """Finds subsequent devices after `ni845xFindDevice` has been called.

    Args:
        find_device_handle (int):
            The device handle returned from `ni845xFindDevice`.

    Returns:
        str: The name of the next NI-845x device found.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xFindDeviceNext`
            function from `ni845x.dll`.
    """
    string_buffer_length = 1024
    string_buffer = create_string_buffer(string_buffer_length)
    handle_type = _get_handle_type()

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_FIND_DEVICE_NEXT,
        handle_type(find_device_handle),
        string_buffer,
    )

    return str(string_buffer.value.decode())


def ni_845x_close_find_device_handle_impl(find_device_handle: int):
    """Closes the handles created by `ni845xFindDevice`.

        Args:
            find_device_handle (int):
                The find device handle to be closed.
    (
        Raises:
            PCBATTCommunicationException:
                Raised when an error occured while calling `ni845xCloseFindDeviceHandle`
                function from `ni845x.dll`.
    """  # noqa: D214 - Section is over-indented (auto-generated noqa)
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_CLOSE_FIND_DEVICE_HANDLE,
        handle_type(find_device_handle),
    )


def ni_845x_i2c_configuration_open_impl() -> int:
    """Creates a new NI-845x I2C configuration.

    Returns:
        int:
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cConfigurationOpen`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    configuration_handle = handle_type()

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_OPEN,
        byref(configuration_handle),
    )

    return configuration_handle.value


def ni_845x_i2c_configuration_close_impl(configuration_handle: int):
    """Closes an I2C I/O configuration.

    Args:
        configuration_handle (int):
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cConfigurationClose`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_CLOSE,
        handle_type(configuration_handle),
    )


def ni_845x_spi_configuration_open_impl() -> int:
    """Creates a new NI-845x SPI configuration.

    Returns:
        int:
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSpiConfigurationOpen`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    configuration_handle = handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_OPEN,
        byref(configuration_handle),
    )

    return configuration_handle.value


def ni_845x_spi_configuration_close_impl(configuration_handle: int):
    """Closes an SPI configuration.

    Args:
        configuration_handle (int):
            The configuration handle.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSpiConfigurationClose`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_CLOSE,
        handle_type(configuration_handle),
    )


def ni_845x_i2c_read_impl(
    device_handle: int,
    configuration_handle: int,
    read_data_array: numpy.ndarray,
):
    """Reads an array of data from an I2C slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni845xOpen`.
        configuration_handle (int):
            The configuration handle.
        read_data_array (numpy.ndarray):
            A numpy array that receives the data read from I2C device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cRead` function from `ni845x.dll`.
    """
    if read_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )

    read_data_array_buffer = read_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    handle_type = _get_handle_type()
    number_of_data_read = c_uint32()

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_READ,
        handle_type(device_handle),
        handle_type(configuration_handle),
        c_uint32(read_data_array.size),
        byref(number_of_data_read),
        read_data_array_buffer,
    )


def ni_845x_i2c_write_impl(
    device_handle: int,
    configuration_handle: int,
    write_data_array: numpy.ndarray,
):
    """Writes an array of data to an I2C slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        configuration_handle (int):
            The configuration handle.
        write_data_array (numpy.ndarray):
            A numpy array containing the data to be written to I2C device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cWrite` function from `ni845x.dll`.
    """
    if write_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )

    write_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_WRITE,
        handle_type(device_handle),
        handle_type(configuration_handle),
        c_uint32(write_data_array.size),
        write_data_array_buffer,
    )


def ni_845x_i2c_write_read_impl(
    device_handle: int,
    configuration_handle: int,
    write_data_array: numpy.ndarray,
    read_data_array: numpy.ndarray,
):
    """Performs a write followed by read (combined format) on an I2C slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        configuration_handle (int):
            The configuration handle.
        write_data_array (numpy.ndarray):
            A numpy array containing the data to be written to I2C device.
        read_data_array (numpy.ndarray):
            A numpy array that receives the data read from I2C device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cWriteRead`
            function from `ni845x.dll`.
    """
    if write_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )
    if read_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )

    write_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    read_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    handle_type = _get_handle_type()

    number_of_data_read = c_uint32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_WRITE_READ,
        handle_type(device_handle),
        handle_type(configuration_handle),
        c_uint32(write_data_array.size),
        write_data_array_buffer,
        c_uint32(read_data_array.size),
        byref(number_of_data_read),
        read_data_array_buffer,
    )


def ni_845x_spi_write_read_impl(
    device_handle: int,
    configuration_handle: int,
    write_data_array: numpy.ndarray,
    read_data_array: numpy.ndarray,
):
    """Exchanges an array of data with an SPI slave device.

    Args:
        device_handle (int):
            The device handle returned from `ni845xOpen`.
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        write_data_array (numpy.ndarray):
            A numpy array containing the data to be written to SPI device.
        read_data_array (numpy.ndarray):
            A numpy array that receives the data read from SPI device.

    Raises:
        TypeError:
            raised if the type of numpy array is not `numpy.ubyte`.
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xSpiWriteRead`
            function from `ni845x.dll`.
    """
    if write_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )
    if read_data_array.dtype != numpy.ubyte:
        raise TypeError(
            PCBATTCommunicationExceptionMessages.INVALID_NUMPY_ARRAY_TYPE_ARGS_1.format(numpy.ubyte)
        )

    write_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    read_data_array_buffer = write_data_array.ctypes.data_as(
        POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte))
    )

    handle_type = _get_handle_type()

    number_of_data_read = c_uint32(read_data_array.size)

    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_WRITE_READ,
        handle_type(device_handle),
        handle_type(configuration_handle),
        c_uint32(write_data_array.size),
        write_data_array_buffer,
        byref(number_of_data_read),
        read_data_array_buffer,
    )


def ni_845x_i2c_set_pullup_enable_impl(
    device_handle: int,
    pullup_status: Ni845xPullupStatus,
):
    """Enables or disables the onboard pullup resistors for I2C operations.

    Args:
        device_handle (int):
            The device handle returned from `ni_845x_open`.
        pullup_status (_Ni845xPullupStatus):
            The status for the pullup resistors.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling `ni845xI2cSetPullupEnable`
            function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_SET_PULLUP_ENABLE,
        handle_type(device_handle),
        c_uint8(pullup_status),
    )


def ni_845x_i2c_configuration_set_address_impl(
    configuration_handle: int,
    address: int,
):
    """Sets the configuration's I2C slave address.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        address (int):
            Specifies the address of the I2C Slave device.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetAddress` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ADDRESS,
        handle_type(configuration_handle),
        c_uint16(address),
    )


def ni_845x_i2c_configuration_set_clock_rate_impl(
    configuration_handle: int,
    clock_rate_kilohertz: int,
):
    """Sets the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        clock_rate_kilohertz (int):
            Specifies the I2C clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetClockRate` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_CLOCK_RATE,
        handle_type(configuration_handle),
        c_uint16(clock_rate_kilohertz),
    )


def ni_845x_i2c_configuration_set_addressing_type_impl(
    configuration_handle: int,
    addressing_type: Ni845xI2cAddressingType,
):
    """Sets the configuration addressing type.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        addressing_type (_Ni845xI2cAddressingType):
            The addressing scheme to use when addressing
            the I2C slave device this configuration describes.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetAddressSize` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ADDRESS_SIZE,
        handle_type(configuration_handle),
        c_int32(addressing_type),
    )


def ni_845x_i2c_configuration_set_ack_poll_timeout_impl(
    configuration_handle: int,
    timeout_milliseconds: int,
):
    """Sets the configuration ACK poll timeout in milliseconds.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.
        timeout_milliseconds (int):
            Specifies the I2C ACK poll timeout in milliseconds.
            When this value is zero, ACK polling is disabled.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationSetAckPollTimeout` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ACK_POLL_TIMEOUT,
        handle_type(configuration_handle),
        c_uint16(timeout_milliseconds),
    )


def ni_845x_i2c_configuration_get_address_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration address.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        int: The configuration address

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetAddress` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    address = c_uint16()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ADDRESS,
        handle_type(configuration_handle),
        byref(address),
    )

    return address.value


def ni_845x_i2c_configuration_get_clock_rate_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        int: The clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetClockRate` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    clock_rate = c_uint16()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_CLOCK_RATE,
        handle_type(configuration_handle),
        byref(clock_rate),
    )

    return clock_rate.value


def ni_845x_i2c_configuration_get_addressing_type_impl(
    configuration_handle: int,
) -> Ni845xI2cAddressingType:
    """Retrieves the configuration addressing type.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        Ni845xI2cAddressingType: the configuration addressing type.
    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetAddressSize` function from `ni845x.dll`.
    """  # noqa: D410, D411, W505 - Missing blank line after section (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (141 > 100 characters) (auto-generated noqa)
    handle_type = _get_handle_type()

    addressing_type = c_int32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ADDRESS_SIZE,
        handle_type(configuration_handle),
        byref(addressing_type),
    )

    return Ni845xI2cAddressingType(addressing_type.value)


def ni_845x_i2c_configuration_get_ack_poll_timeout_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration ACK poll timeout in milliseconds.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xI2cConfigurationOpen`.

    Returns:
        int: The ACK poll timeout, in milliseconds.
    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xI2cConfigurationGetAckPollTimeout` function from `ni845x.dll`.
    """  # noqa: D410, D411, W505 - Missing blank line after section (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (141 > 100 characters) (auto-generated noqa)
    handle_type = _get_handle_type()

    timeout = c_uint16()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ACK_POLL_TIMEOUT,
        handle_type(configuration_handle),
        byref(timeout),
    )

    return timeout.value


def ni_845x_spi_configuration_set_chip_select_impl(
    configuration_handle: int,
    chip_select: int,
):
    """Sets the configuration chip select.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        chip_select (int):
            The chip select line for this configuration.
    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetChipSelect` function from `ni845x.dll`.
    """  # noqa: D411 - Missing blank line before section (auto-generated noqa)
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CHIP_SELECT,
        handle_type(configuration_handle),
        c_uint32(chip_select),
    )


def ni_845x_spi_configuration_set_clock_rate_impl(
    configuration_handle: int,
    clock_rate_kilohertz: int,
):
    """Sets the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        clock_rate_kilohertz (int):
            Specifies the SPI clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockRate` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_RATE,
        handle_type(configuration_handle),
        c_uint16(clock_rate_kilohertz),
    )


def ni_845x_spi_configuration_set_clock_phase_impl(
    configuration_handle: int,
    clock_phase: SpiConfigurationClockPhase,
):
    """Sets the configuration clock phase.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        clock_phase (SpiConfigurationClockPhase):
            The positioning of the data bits relative to the clock edges for the SPI Port.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockPhase` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_PHASE,
        handle_type(configuration_handle),
        c_int32(clock_phase),
    )


def ni_845x_spi_configuration_set_clock_polarity_impl(
    configuration_handle: int,
    clock_polarity: SpiConfigurationClockPolarity,
):
    """Sets the configuration clock polarity.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.
        clock_polarity (SpiConfigurationClockPolarity):
            The clock line idle state for the SPI Port (clock polarity).

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockPolarity` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_POLARITY,
        handle_type(configuration_handle),
        c_int32(clock_polarity),
    )


def ni_845x_spi_configuration_get_chip_select_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration chip select value.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        int: The chip select.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationGetChipSelect` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()
    chip_select = c_uint32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CHIP_SELECT,
        handle_type(configuration_handle),
        byref(chip_select),
    )

    return chip_select.value


def ni_845x_spi_configuration_get_clock_rate_impl(
    configuration_handle: int,
) -> int:
    """Retrieves the configuration clock rate in kilohertz.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        int: The clock rate in kilohertz.

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationGetClockRate` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    clock_rate = c_uint16()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_RATE,
        handle_type(configuration_handle),
        byref(clock_rate),
    )

    return clock_rate.value


def ni_845x_spi_configuration_get_clock_phase_impl(
    configuration_handle: int,
) -> SpiConfigurationClockPhase:
    """Retrieves the configuration clock phase.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        SpiConfigurationClockPhase:
            The positioning of the data bits relative to
            the clock edges for the SPI Port (clock phase).

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationSetClockPhase` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    clock_phase = c_int32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_PHASE,
        handle_type(configuration_handle),
        byref(clock_phase),
    )

    return SpiConfigurationClockPhase(clock_phase.value)


def ni_845x_spi_configuration_get_clock_polarity_impl(
    configuration_handle: int,
) -> SpiConfigurationClockPolarity:
    """Retrieves the configuration clock polarity.

    Args:
        configuration_handle (int):
            The configuration handle returned from `ni845xSpiConfigurationOpen`.

    Returns:
        SpiConfigurationClockPolarity:
            The clock line idle state for the SPI Port (clock polarity).

    Raises:
        PCBATTCommunicationException:
            Raised when an error occured while calling
            `ni845xSpiConfigurationGetClockPolarity` function from `ni845x.dll`.
    """
    handle_type = _get_handle_type()

    clock_polarity = c_int32()
    invoke_ni_845x_function(
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_POLARITY,
        handle_type(configuration_handle),
        byref(clock_polarity),
    )

    return SpiConfigurationClockPolarity(clock_polarity.value)


def invoke_ni_845x_function(function_name: str, *args):
    """Invokes a function from `ni845x.dll`.

    Args:
        function_name (str): the name of function from `ni845x.dll`.

    Raises:
        ValueError:
            Raised if `function_name` is None, empty or whitespace.
        PCBATTCommunicationException:
            Raised if `function_name` does not exist.
            Raised when an error occured while calling
            the function with `function_name` from `ni845x.dll`.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(function_name, nameof(function_name))
    function_arguments_types = []
    handle_type = _get_handle_type()
    functions_argument_types = _create_ni_845x_functions_arguments_types(handle_type)

    try:
        function_arguments_types = functions_argument_types[function_name]
    except Exception as e:
        raise PCBATTCommunicationException(
            message=PCBATTCommunicationExceptionMessages.FUNCTION_CALL_FAILED_ARGS_2.format(
                function_name, str(e)
            )
        ) from e

    status = None
    try:
        function_to_call = create_native_stdcall_win_function(
            dll_path=NI_845X_DLL,
            function_name=function_name,
            return_value_type=c_int32,
            arguments_types=function_arguments_types,
        )
        status = function_to_call(
            *args,
        )
    except Exception as e:
        raise PCBATTCommunicationException(
            message=PCBATTCommunicationExceptionMessages.FUNCTION_CALL_FAILED_ARGS_2.format(
                function_name, str(e)
            )
        ) from e

    if status is None:
        return

    if status != 0:
        status_description = _get_status_description(status)
        raise PCBATTCommunicationException(
            message=PCBATTCommunicationExceptionMessages.FUNCTION_CALL_FAILED_ARGS_2.format(
                function_name, status_description
            )
        )


def is_ni_845x_installed() -> bool:
    """Checks whether NI-845x drivers are installed on local system."""
    try:
        check_dll_availability("ni845x.dll")
        return True
    except FileNotFoundError:
        return False


def ni_845x_device_exists() -> bool:
    """Checks whether at least a NI-845x device is present on local system."""
    try:
        find_results = ni_845x_find_device_impl()
        ni_845x_close_impl(find_results.device_handle)
        return find_results.number_of_devices_found != 0
    except PCBATTCommunicationException:
        return False


def convert_memory_address_to_data_bytes_array(
    memory_address: int,
    address_type: DataMemoryAddressType,
    address_endianness: DataMemoryAddressEndianness,
) -> List[int]:
    """Convert the memory address to an array of bytes used for
    device communication.

    Args:
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.
        address_endianness (DataMemoryAddressEndianness):
            The address endianness.

    Returns:
        List[int]: The array of bytes.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    if address_type == DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE:
        return _create_one_byte_array(memory_address)

    if address_endianness == DataMemoryAddressEndianness.LITTLE_ENDIAN:
        return _create_two_bytes_array_little_endian(memory_address)

    return _create_two_bytes_array_big_endian(memory_address)


def create_command_for_spi_read_communication_impl(
    memory_address: int,
    address_type: DataMemoryAddressType,
    address_endianness: DataMemoryAddressEndianness,
    number_of_bytes_to_read: int,
) -> List[int]:
    """Create an array of data bytes representing
    the read command used during SPI communication.

    Args:
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.
        address_endianness (DataMemoryAddressEndianness):
            The address endianness.
        number_of_bytes_to_read:
            The number of bytes to read.
    Returns:
        List[int]: The created array.
    """  # noqa: D205, D411, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)
    instruction_value = _compute_spi_communication_command(
        READ_INSTRUCTION,
        memory_address,
        address_type,
    )

    spi_read_instruction_array = [instruction_value]
    spi_read_instruction_array.extend(
        convert_memory_address_to_data_bytes_array(memory_address, address_type, address_endianness)
    )
    spi_read_instruction_array.extend([0] * number_of_bytes_to_read)

    return spi_read_instruction_array


def create_command_for_spi_write_communication_impl(
    memory_address: int,
    address_type: DataMemoryAddressType,
    address_endianness: DataMemoryAddressEndianness,
    number_of_bytes_to_write: int,
) -> List[int]:
    """Create an array of data bytes representing
    the write command used during SPI communication.

    Args:
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.
        address_endianness (DataMemoryAddressEndianness):
            The address endianness.
        number_of_bytes_to_write:
            The number of bytes to write.

    Returns:
        List[int]: The created array.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    instruction_value = _compute_spi_communication_command(
        WRITE_INSTRUCTION,
        memory_address,
        address_type,
    )

    spi_write_instruction_array = [instruction_value]
    spi_write_instruction_array.extend(
        convert_memory_address_to_data_bytes_array(memory_address, address_type, address_endianness)
    )
    spi_write_instruction_array.extend([0] * number_of_bytes_to_write)

    return spi_write_instruction_array


def _get_status_description(status: int) -> str:
    """Converts a status code into a descriptive string.

    Args:
        status (int): Status code returned from an NI-845x function from `ni845x.dll`.

    Returns:
        str: The description of the status code.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    string_buffer_length = 1024
    string_buffer = create_string_buffer(string_buffer_length)

    function_to_call = create_native_stdcall_win_function(
        dll_path=NI_845X_DLL,
        function_name=_Ni845xFunctionsNames.NI_845X_STATUS_TO_STRING,
        return_value_type=None,
        arguments_types=[
            # int32, status code returned from an NI-845x function from `ni845x.dll`.
            c_int32,
            # uint32, Size of the buffer that receives
            # the description of the status code (in bytes).
            c_uint32,
            # c_char_p, buffer that receives the description of the status code.
            c_char_p,
        ],
    )

    function_to_call(
        c_int32(status),
        c_uint32(string_buffer_length),
        string_buffer,
    )
    return str(string_buffer.value.decode())


def _get_handle_type() -> Union[c_uint32, c_uint64]:
    """Retrieves the type of handle used by NI-845x functions
    according to the platform on which the Python executable runs.."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (363 > 100 characters) (auto-generated noqa)
    if is_python_windows_64bits():
        return c_uint64
    if is_python_windows_32bits():
        return c_uint32

    raise PCBATTCommunicationException(
        PCBATTCommunicationExceptionMessages.INVALID_OS_ENVIRONMENT_FOR_PYTHON
    )


def _create_one_byte_array(memory_address: int) -> List[int]:
    """creates an array with one byte element.

    Args:
        value (int): the value to add in the array.

    Returns:
        List[int]: The created array.
    """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)
    return [
        # The less significant byte of a short value.
        numpy.ubyte(memory_address & MAX_BYTE_VALUE),
    ]


def _create_two_bytes_array_little_endian(
    memory_address: int,
) -> List[int]:
    """creates an array with two bytes with little endianness.

    Args:
        memory_address (int): the value to add in the array.

    Returns:
        List[int]: The created array.
    """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)
    return [
        # The most significant byte of a short value.
        (memory_address >> 8) & MAX_BYTE_VALUE,
        # The less significant byte of a short value.
        memory_address & MAX_BYTE_VALUE,
    ]


def _create_two_bytes_array_big_endian(
    memory_address: int,
) -> List[int]:
    """creates an array with two bytes with big endianness.

    Args:
        memory_address (int): the value to add in the array.

    Returns:
        List[int]: The created array.
    """  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)
    return [
        # The less significant byte of a short value.
        memory_address & MAX_BYTE_VALUE,
        # The most significant byte of a short value.
        (memory_address >> 8) & MAX_BYTE_VALUE,
    ]


def _compute_spi_communication_command(
    command_code: int, memory_address: int, address_type: DataMemoryAddressType
) -> int:
    """Computes the value of command used for SPI communications

    Args:
        command_code (int): The code of the command.
        memory_address (int):
            The address where data are stored in device memory.
        address_type (DataMemoryAddressType):
            The type of address in device memory.

    Returns:
        int: the computed value for the command.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    if address_type == DataMemoryAddressType.ADDRESS_ENCODED_ON_ONE_BYTE:
        # For address encoded on one byte,
        # some SPI devices require that the 4th bit
        # should be set with the 9th bit of memory address.
        return command_code + ((memory_address >> 5) & FIRST_FOUR_BYTES_MASK)

    return command_code


def _create_ni_845x_functions_arguments_types(
    handle_type: Union[c_uint32, c_uint64]
) -> Dict[str, List[Type]]:
    "Creates a dictionary containing the names of functions with the list of types of arguments."
    return {
        _Ni845xFunctionsNames.NI_845X_OPEN: [
            # c_char_p, resource name string corresponding to the NI 845x device to be opened.
            c_char_p,
            # POINTER(c_uint32 | c_uint64), pointer to the device handle.
            POINTER(handle_type),
        ],
        _Ni845xFunctionsNames.NI_845X_CLOSE: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_DEVICE_LOCK: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_DEVICE_UNLOCK: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_SET_IO_VOLTAGE_LEVEL: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
            # c_uint8, the voltage level.
            c_uint8,
        ],
        _Ni845xFunctionsNames.NI_845X_SET_TIMEOUT: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
            # c_uint32, the timeout value.
            c_uint32,
        ],
        _Ni845xFunctionsNames.NI_845X_FIND_DEVICE: [
            # c_char_p, buffer that receives the name of NI-845x device.
            c_char_p,
            # POINTER(c_uint32 | c_uint64), pointer on the find device handle.
            POINTER(handle_type),
            # c_uint8, the voltage level.
            POINTER(c_uint32),
        ],
        _Ni845xFunctionsNames.NI_845X_FIND_DEVICE_NEXT: [
            # c_uint32 | c_uint64, the find device handle.
            handle_type,
            # c_char_p, buffer that receives the name of NI-845x device.
            c_char_p,
        ],
        _Ni845xFunctionsNames.NI_845X_CLOSE_FIND_DEVICE_HANDLE: [
            # c_uint32 | c_uint64, the find device handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_OPEN: [
            # POINTER(c_uint32 | c_uint64), pointer to the I2C configuration handle.
            POINTER(handle_type),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_CLOSE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_OPEN: [
            # POINTER(c_uint32 | c_uint64), pointer to the I2C configuration handle.
            POINTER(handle_type),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_CLOSE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_READ: [
            # c_uint32 | c_uint64, pointer to the device handle.
            handle_type,
            # c_uint32 | c_uint64, pointer to the I2C configuration handle.
            handle_type,
            # c_uint32, the size of the data array.
            c_uint32,
            # POINTER(c_uint32), receives the number of data read.
            POINTER(c_uint32),
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_WRITE: [
            # c_uint32 | c_uint64, pointer to the device handle.
            handle_type,
            # c_uint32 | c_uint64, pointer to the I2C configuration handle.
            handle_type,
            # c_uint32, the size of the data array to write.
            c_uint32,
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_WRITE_READ: [
            # c_uint32 | c_uint64, pointer to the device handle.
            handle_type,
            # c_uint32 | c_uint64, pointer to the I2C configuration handle.
            handle_type,
            # c_uint32, the size of the data array to write.
            c_uint32,
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
            # c_uint32, the size of the data array to read.
            c_uint32,
            # POINTER(c_uint32), receives the number of data read.
            POINTER(c_uint32),
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_WRITE_READ: [
            # c_uint32 | c_uint64, pointer to the device handle.
            handle_type,
            # c_uint32 | c_uint64, pointer to the I2C configuration handle.
            handle_type,
            # c_uint32, the size of the data array to write.
            c_uint32,
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
            # POINTER(c_uint32), receives the number of data read.
            POINTER(c_uint32),
            # pointer to an array of bytes uint8
            POINTER(numpy.ctypeslib.as_ctypes_type(numpy.ubyte)),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_SET_PULLUP_ENABLE: [
            # c_uint32 | c_uint64, the device handle.
            handle_type,
            # c_uint8, the voltage level.
            c_uint8,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ADDRESS: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the address.
            c_uint16,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_CLOCK_RATE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the clock rate.
            c_uint16,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ADDRESS_SIZE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, the addressing type.
            c_int32,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_SET_ACK_POLL_TIMEOUT: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the ACK poll timeout.
            c_uint16,
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ADDRESS: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the clock rate.
            POINTER(c_uint16),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_CLOCK_RATE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, pointer on the clock rate.
            POINTER(c_uint16),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ADDRESS_SIZE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, pointer on the addressing type.
            POINTER(c_int32),
        ],
        _Ni845xFunctionsNames.NI_845X_I2C_CONFIGURATION_GET_ACK_POLL_TIMEOUT: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, pointer on the ACK poll timeout.
            POINTER(c_uint16),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CHIP_SELECT: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint32, the chip select.
            c_uint32,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_RATE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, the clock rate.
            c_uint16,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_PHASE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, the clock phase.
            c_int32,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_SET_CLOCK_POLARITY: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, the clock polarity.
            c_int32,
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CHIP_SELECT: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint32, pointer on the clock rate.
            POINTER(c_uint32),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_RATE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_uint16, pointer on the clock rate.
            POINTER(c_uint16),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_PHASE: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, pointer on the clock phase.
            POINTER(c_int32),
        ],
        _Ni845xFunctionsNames.NI_845X_SPI_CONFIGURATION_GET_CLOCK_POLARITY: [
            # c_uint32 | c_uint64, the configuration handle.
            handle_type,
            # c_int32, pointer on the clock polarity.
            POINTER(c_int32),
        ],
    }
