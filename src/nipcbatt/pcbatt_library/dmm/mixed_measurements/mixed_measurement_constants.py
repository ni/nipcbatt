"""Constants data types for Mixed Measurements."""

import dataclasses

from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.constants import ConstantsForDcRmsMeasurements
from nipcbatt.pcbatt_library.dmm.mixed_measurements.mixed_measurement_data_types import (
    MixedMeasurementConfiguration,
    MixedMeasurementFunctionParameters,
    MixedRangeAndFunctions,
)


@dataclasses.dataclass
class ConstantsForMixedMeasurements:
    """Constants used for Mixed measurement."""

    RANGE_AND_FUNCTION = MixedRangeAndFunctions.DC_Voltage_Auto_Range


"""Mixed measurement-specific range/function setting is defined 
    in ConstantsForMixedMeasurements."""
# Default execution type for Mixed measurements
DEFAULT_MIXED_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE

# Default measurement function parameter including Mixed range/function and resolution in digits
DEFAULT_MIXED_MEASUREMENT_PARAMETERS = MixedMeasurementFunctionParameters(
    measurement_function=ConstantsForMixedMeasurements.RANGE_AND_FUNCTION,
    resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS,
)

# Default timing parameters including aperture time and settle time
DEFAULT_MIXED_TIMING_PARAMETERS = TimingParameters(
    aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS,
    settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS,
)

# Default AC minimum frequency
DEFAULT_MIXED_AC_MIN_FREQUENCY = ConstantsForDcRmsMeasurements.DEFAULT_AC_MIN_FREQUENCY

# Default trigger parameters including trigger source, trigger delay, and trigger enable setting
DEFAULT_MIXED_TRIGGER_PARAMETERS = TriggerParameters(
    trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE,
    trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY,
    slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE,
    enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER,
)

# Default DC-RMS Mixed measurement configuration
DEFAULT_MIXED_MEASUREMENT_CONFIGURATION = MixedMeasurementConfiguration(
    execution_type=DEFAULT_MIXED_EXECUTION_TYPE,
    measurement_function_parameters=DEFAULT_MIXED_MEASUREMENT_PARAMETERS,
    trigger_parameters=DEFAULT_MIXED_TRIGGER_PARAMETERS,
    timing_parameters=DEFAULT_MIXED_TIMING_PARAMETERS,
    ac_min_frequency=DEFAULT_MIXED_AC_MIN_FREQUENCY,
)
