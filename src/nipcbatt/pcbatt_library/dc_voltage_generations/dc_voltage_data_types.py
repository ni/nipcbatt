""" DC Voltage data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (140 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcVoltageGenerationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of DC Voltage generation."""

    def __init__(
        self,
        voltage_generation_range_parameters: VoltageGenerationChannelParameters,
        output_voltages: List[float],
    ) -> None:
        """Initializes an instance of `DcVoltageGenerationConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                The settings of the terminal for all channel for DC voltage generation.
            output_voltages (List[float]):
                specifies the actual output voltage to generate on the selected channel(s).
                Each element of the array corresponds to a channel in the task.
                The order of the channels in the array corresponds to the order in which you add the channels to the task in the Initialize method.

        Raises:
            ValueError:
                If the input `voltage_generation_range_parameters' does not contain a valid object.
                If the input `output_voltages' is an empty array.
        """  # noqa: W505 - doc line too long (147 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            voltage_generation_range_parameters,
            nameof(voltage_generation_range_parameters),
        )
        Guard.is_not_empty(output_voltages, nameof(output_voltages))

        self._voltage_generation_range_parameters = voltage_generation_range_parameters
        self._output_voltages = output_voltages

    @property
    def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters:
        """
        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for DC voltage generation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_generation_range_parameters

    @property
    def output_voltages(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of output voltages to be generated at the selected channel(s).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._output_voltages
