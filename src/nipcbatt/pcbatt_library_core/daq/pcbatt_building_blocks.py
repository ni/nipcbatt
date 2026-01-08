# pylint: disable=W0707, W0719, W0702
"""Defines the base classes used by PCBA Test Toolkit building blocks"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (183 > 100 characters) (auto-generated noqa)

from abc import ABC, abstractmethod
from typing import Callable

import nidaqmx
import nidaqmx.constants
import nidaqmx.system
import nidaqmx.system.storage.persisted_channel
import nidaqmx.utils
import pyvisa

from nipcbatt.pcbatt_communication_library.ni_845x_i2c_communication_devices import (
    Ni845xI2cDevicesHandler,
)
from nipcbatt.pcbatt_communication_library.ni_845x_spi_communication_devices import (
    Ni845xSpiDevicesHandler,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryChannelNotCompatibleWithGenerationException,
    PCBATTLibraryChannelNotCompatibleWithMeasurementException,
    PCBATTLibraryException,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)


class BuildingBlockUsingInstrument(ABC):
    """Defines the base methods for initialization and release"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (176 > 100 characters) (auto-generated noqa)

    def __init__(self, *args, **kwargs):
        """Constructor that initializes instrument."""
        self._instrument = self.__class__._instrument_factory()
        self._initialize(*args, **kwargs)

    def __enter__(self):
        """Magic method called when 'with' is called."""
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        """Magic method called at end of 'with' is call block."""
        self._close()

    def __del__(self):
        """Destructor that calls _close() method."""
        self._close()

    @classmethod
    @abstractmethod
    def _instrument_factory(cls):
        """Initializes the instrument.

        Raises:
            NotImplementedError: raised when cleared directly.
        """
        raise NotImplementedError()

    def _initialize(self, *args, **kwargs):
        if len(args) == 0:
            return

        self._invoke("initialize", *args, **kwargs)

    def _close(self):
        try:
            self._invoke("close")
        finally:
            if hasattr(self, "_instrument"):
                del self._instrument

    def _invoke(self, method_name: str, *args, **kwargs):
        try:
            method = getattr(self, method_name)

            if isinstance(method, Callable):
                method(*args, **kwargs)
        except AttributeError as exception:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.CLASS_DOES_NOT_IMPLEMENT_METHOD_ARGS_2.format(
                    type(self).__name__, method_name
                )
            ) from exception


class BuildingBlockUsingDAQmx(BuildingBlockUsingInstrument):
    """Defines Building block that uses DAQmx task for instrument management."""

    @classmethod
    def _instrument_factory(cls) -> nidaqmx.Task:
        """Creates a DAQmx task instance.
        Returns:
            nidaqmx.Task: the type of instrument.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return nidaqmx.Task()

    @property
    def is_task_initialized(self) -> bool:
        """Checks whether the task is initialized.

        Returns:
            bool: True, if the task is initialized with channel(s)
        """
        task_is_initialized: bool = False
        try:
            task_is_initialized = len(self.task.channel_names) != 0
        finally:
            return task_is_initialized

    @property
    def task(self) -> nidaqmx.Task:
        """Defines the instance of DAQmx task.

        Returns:
            nidaqmx.Task: the type of instrument.
        """
        return self._instrument

    def contains_only_global_virtual_channels(self, channel_expression: str) -> bool:
        """Check whether the channel expression contains
           only global virtual channels defined in NI MAX.
        Args:
            channel_expression (str): the channel expression

        Returns:
            bool: True if the channel expression
            only contains global virtual channels defined in NI MAX.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        channel_names_in_expression = nidaqmx.utils.unflatten_channel_string(
            channel_names=channel_expression
        )

        global_channel_names = (
            self.__class__._daqmx_local_system().global_channels.global_channel_names
        )

        return all(
            channel_name in global_channel_names for channel_name in channel_names_in_expression
        )

    @classmethod
    def _daqmx_local_system(cls) -> nidaqmx.system.System:
        """Gets the local DAQmx system.

        Returns:
            nidaqmx.system.System: The instance of the local DAQmx system.
        """
        return nidaqmx.system.System.local()

    def verify_measurement_type(self, measurement_type: nidaqmx.constants.UsageTypeAI):
        """Verifies the DAQ handler channels are compatible with the measurement type.

        Args:
            measurement_type (nidaqmx.constants.UsageTypeAI): type of the measurement.
        """
        if all(channel.ai_meas_type == measurement_type for channel in self.task.ai_channels):
            return

        raise PCBATTLibraryChannelNotCompatibleWithMeasurementException(measurement_type)

    def verify_generation_type(self, generation_type: nidaqmx.constants.UsageTypeAO):
        """Verifies the DAQ handler channels are compatible with the generation type.

        Args:
            generation_type (nidaqmx.constants.UsageTypeAI): type of the generation.
        """
        if all(channel.ao_output_type == generation_type for channel in self.task.ai_channels):
            return

        raise PCBATTLibraryChannelNotCompatibleWithGenerationException(generation_type)

    def add_global_channels(self, global_channel_expression: str):
        """Add global channels (defined in the channel expression)
        to the DAQmx task.

        Args:
            global_channel_expression (str):
                Expression representing the name of
                a global channel in DAQ System.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        global_channels_names = nidaqmx.utils.unflatten_channel_string(
            channel_names=global_channel_expression
        )
        self.task.add_global_channels(
            [
                nidaqmx.system.storage.persisted_channel.PersistedChannel(global_channel_name)
                for global_channel_name in global_channels_names
            ]
        )


class BuildingBlockUsingNi845xI2cDevice(BuildingBlockUsingInstrument):
    """Defines building block that uses NI-845x devices handler for I2C communication."""

    @classmethod
    def _instrument_factory(cls) -> Ni845xI2cDevicesHandler:
        """Creates a NI-845x I2C device handler.
        Returns:
            Ni845xI2cDevicesHandler: the type of instrument.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return Ni845xI2cDevicesHandler()

    @property
    def is_devices_handler_initialized(self) -> bool:
        """Checks whether the device handler is initialized.

        Returns:
            bool: True, if the device handler is initalized.
        """
        return self.devices_handler.is_initialized()

    @property
    def devices_handler(self) -> Ni845xI2cDevicesHandler:
        """Defines the instance of devices handler.

        Returns:
            Ni845xI2cDevicesHandler: the type of instrument.
        """
        return self._instrument


class BuildingBlockUsingNi845xSpiDevice(BuildingBlockUsingInstrument):
    """Defines building block that uses NI-845x devices handler for SPI communication."""

    @classmethod
    def _instrument_factory(cls) -> Ni845xSpiDevicesHandler:
        """Creates a NI 845x device handler.
        Returns:
            Ni845xSpiDevicesHandler: the type of instrument.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return Ni845xSpiDevicesHandler()

    @property
    def is_devices_handler_initialized(self) -> bool:
        """Checks whether the devices handler is initialized.

        Returns:
            bool: True, if the devices handler is initalized.
        """
        return self.devices_handler.is_initialized()

    @property
    def devices_handler(self) -> Ni845xSpiDevicesHandler:
        """Defines the instance of device handler.

        Returns:
            Ni845xSpiDevicesHandler: the type of instrument.
        """
        return self._instrument


class BuildingBlockUsingVisa(BuildingBlockUsingInstrument):
    """Defines Building block that uses
    serial device handler (NI-VISA) for instrument management."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self._serial_device_handler = None

    @classmethod
    def _instrument_factory(cls) -> pyvisa.ResourceManager:
        """Creates a NI-VISA resource manager.
        Returns:
            pyvisa.ResourceManager: the type of resource manager.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return pyvisa.ResourceManager()

    @property
    def is_serial_device_handler_initialized(self) -> bool:
        """Checks whether the serial device handler is initialized.

        Returns:
            bool: True, if the serial device handler is initialized.
        """
        return self._serial_device_handler is not None

    @property
    def serial_device_handler(self) -> pyvisa.resources.SerialInstrument:
        """Defines the instance of device handler.

        Returns:
            pyvisa.resources.SerialInstrument: the type of instrument.
        """
        if self._serial_device_handler is not None:
            return self._serial_device_handler

        raise PCBATTLibraryException(
            PCBATTLibraryExceptionMessages.VISA_SERIAL_DEVICE_NOT_INITIALIZED
        )

    def open_serial_device(self, serial_device_name: str):
        """Opens a serial device with the specific name.

        Args:
            serial_device_name (str): The name of the serial device.
        """
        self._serial_device_handler = self._instrument.open_resource(serial_device_name)

    def close_serial_device(self):
        """Closes the serial device."""
        self._serial_device_handler.close()
        self._serial_device_handler = None
