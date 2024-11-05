"""Provides communication with NI-845x devices."""

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import Ni845xVoltageLevel
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
)


class Ni845xDevicesHandler:
    """Defines methods used to handle NI-845x devices."""

    def __init__(self) -> None:
        """Default initialization of new `Ni845xI2cDevicesHandler` object"""
        self._devices_handler = None

    def is_initialized(self) -> bool:
        """_summary_

        Returns:
            bool: _description_
        """
        return self._devices_handler is not None

    def open(self, device_name: str):
        """Opens the specific NI-845x device.

        Args:
            device_name (str): The name of the device to be opened.

        Raises:
            PCBATTLibraryException:
                Raised when an error occured while calling `ni845xOpen` function from `ni845x.dll`
        """
        self._devices_handler = _ni_845x_functions.ni_845x_open_impl(device_name)

    def close(self):
        """Closes a previously opened device.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xClose` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_close_impl(self._devices_handler)
        self._devices_handler = None

    def lock(self):
        """Locks the device for access by a single thread.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xLock` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_device_lock_impl(self._devices_handler)

    def unlock(self):
        """Unlocks the device.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xUnlock` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_device_unlock_impl(self._devices_handler)

    def set_input_output_voltage_level(self, voltage_level: Ni845xVoltageLevel):
        """Sets the I/O voltage level supported by the device.

        Args:
            voltage_level (Ni845xVoltageLevel): The voltage level.

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSetIoVoltageLevel` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_set_io_voltage_level_impl(self._devices_handler, voltage_level)

    def set_timeout(self, timeout_milliseconds: int):
        """_summary_

        Args:
            timeout_milliseconds (int): _description_

        Raises:
            PCBATTLibraryException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSetTimeout` function from `ni845x.dll`
        """
        if self._devices_handler is None:
            raise PCBATTLibraryException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        _ni_845x_functions.ni_845x_set_timeout_impl(self._devices_handler, timeout_milliseconds)
