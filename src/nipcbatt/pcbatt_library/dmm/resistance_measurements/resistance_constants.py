"""Constants data types for Resistance Measurements."""

import dataclasses

from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.constants import ConstantsForDcRmsMeasurements
from nipcbatt.pcbatt_library.dmm.resistance_measurements.resistance_data_types import (
    ResistanceMeasurementConfiguration,
    ResistanceMeasurementFunctionParameters,
    ResistanceRangeAndFunctions,
)


@dataclasses.dataclass
class ConstantsForDcRmsResistanceMeasurements:
    """Constants used for Resistance measurement."""

    RANGE_AND_FUNCTION = ResistanceRangeAndFunctions.TWO_W_Resistance_Auto_Range


# Resistance measurement-specific range/function setting is defined 
# in ConstantsForDcRmsResistanceMeasurements.
# Default execution type for resistance measurements
DEFAULT_RESISTANCE_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE

# Default measurement function parameter including resistance range/function
# and resolution in digits
DEFAULT_RESISTANCE_MEASUREMENT_PARAMETERS = ResistanceMeasurementFunctionParameters(
    measurement_function=ConstantsForDcRmsResistanceMeasurements.RANGE_AND_FUNCTION,
    resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS,
)

# Default timing parameters including aperture time and settle time
DEFAULT_RESISTANCE_TIMING_PARAMETERS = TimingParameters(
    aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS,
    settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS,
)

# Default trigger parameters including trigger source, trigger delay, and trigger enable setting
DEFAULT_RESISTANCE_TRIGGER_PARAMETERS = TriggerParameters(
    trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE,
    trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY,
    enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER,
    slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE,
)

# Default DC-RMS resistance measurement configuration
DEFAULT_RESISTANCE_MEASUREMENT_CONFIGURATION = ResistanceMeasurementConfiguration(
    execution_type=DEFAULT_RESISTANCE_EXECUTION_TYPE,
    measurement_function_parameters=DEFAULT_RESISTANCE_MEASUREMENT_PARAMETERS,
    trigger_parameters=DEFAULT_RESISTANCE_TRIGGER_PARAMETERS,
    timing_parameters=DEFAULT_RESISTANCE_TIMING_PARAMETERS,
)