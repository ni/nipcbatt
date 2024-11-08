# pylint: disable=W0707, W0719, W0702, W0212
"""Defines the exceptions that can be raised during execution of PCBA Test Toolkit"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (196 > 100 characters) (auto-generated noqa)

import nidaqmx.constants

from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)


class PCBATTLibraryException(  # noqa: N818 - exception name 'PCBATTLibraryException' should be named with an Error suffix (auto-generated noqa)
    Exception
):
    """Defines base class for all exception raised by
    `nipcatt.pcbatt_library` and `nipcatt.pcbatt_library_core` modules."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (367 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, message: str
    ):
        super().__init__(message)


class PCBATTLibraryChannelNotCompatibleWithMeasurementException(  # noqa: N818 - exception name 'PCBATTLibraryChannelNotCompatibleWithMeasurementException' should be named with an Error suffix (auto-generated noqa)
    PCBATTLibraryException
):
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


class PCBATTLibraryChannelNotCompatibleWithGenerationException(  # noqa: N818 - exception name 'PCBATTLibraryChannelNotCompatibleWithGenerationException' should be named with an Error suffix (auto-generated noqa)
    PCBATTLibraryException
):
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
