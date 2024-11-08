"""Constants for DC voltage generation data types."""

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library.dc_voltage_generations.dc_voltage_data_types import (
    DcVoltageGenerationConfiguration,
)


@dataclasses.dataclass
class ConstantsForDcVoltageGeneration:
    """Constants used as Initial and defauls values for DC Voltage generation configuration"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (205 > 100 characters) (auto-generated noqa)

    INITIAL_AO_OUTPUT_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    INITIAL_RANGE_MIN_VOLTS = 0.0
    INITIAL_RANGE_MAX_VOLTS = 1.0
    INITIAL_AO_VOLTAGE_UNITS = nidaqmx.constants.VoltageUnits.VOLTS

    DEFAULT_AO_OUTPUT_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_RANGE_MIN_VOLTS = -10.0
    DEFAULT_RANGE_MAX_VOLTS = 10.0
    DEFAULT_OUTPUT_VOLTAGES = [1.2]


DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS = VoltageGenerationChannelParameters(
    range_min_volts=ConstantsForDcVoltageGeneration.DEFAULT_RANGE_MIN_VOLTS,
    range_max_volts=ConstantsForDcVoltageGeneration.DEFAULT_RANGE_MAX_VOLTS,
)

DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION = DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
    output_voltages=ConstantsForDcVoltageGeneration.DEFAULT_OUTPUT_VOLTAGES,
)
