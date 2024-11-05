# pylint: disable=W0707, W0719, W0702, W0212
"""Defines the exceptions that can be raised during execution of PCBA Test Toolkit"""

import nidaqmx.constants

from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)


class PCBATTLibraryException(Exception):
    """Defines base class for all exception raised by
    `nipcatt.pcbatt_library` and `nipcatt.pcbatt_library_core` modules."""

    def __init__(self, message: str):
        super().__init__(message)


class PCBATTLibraryChannelNotCompatibleWithMeasurementException(PCBATTLibraryException):
    """Raised if the global virtual channels are not compatible with the type of measurement."""

    def __init__(
        self,
        measurement_type: nidaqmx.constants.UsageTypeAI,
    ) -> None:
        """Initializes an instance of `PCBATTLibraryChannelNotCompatibleWithMeasurementException`.

        Args:
            measurement_type (nidaqmx.constants.UsageTypeAI): The type of measurement.
        """
        super().__init__(
            PCBATTLibraryExceptionMessages.ANALOG_INPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1.format(
                measurement_type.name
            )
        )


class PCBATTLibraryChannelNotCompatibleWithGenerationException(PCBATTLibraryException):
    """Raised if the global virtual channels are not compatible with the type of generation."""

    def __init__(
        self,
        measurement_type: nidaqmx.constants.UsageTypeAO,
    ) -> None:
        """Initializes an instance of `PCBATTLibraryChannelNotCompatibleWithGenerationException`.

        Args:
            measurement_type (nidaqmx.constants.UsageTypeAO): The type of generation.
        """
        super().__init__(
            PCBATTLibraryExceptionMessages.ANALOG_INPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1.format(
                measurement_type.name
            )
        )
