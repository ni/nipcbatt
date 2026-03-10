"""Constants data types for DC-RMS Current Measurements."""

import dataclasses

from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.constants import ConstantsForDcRmsMeasurements
from nipcbatt.pcbatt_library.dmm.dc_rms_current_measurements.dc_rms_current_data_types import (
    CurrentRangeAndFunctions,
    DcRmsCurrentMeasurementFunctionParameters,
    DcRmsCurrentMeasurementConfiguration,
)


@dataclasses.dataclass
class ConstantsForDcRmsCurrentMeasurements:
    """Constants used for Current measurement."""

    RANGE_AND_FUNCTION = CurrentRangeAndFunctions.DC_Current_Auto_Range


# Current measurement-specific range/function setting is defined
# in ConstantsForDcRmsCurrentMeasurements.
# Default execution type for current measurements
DEFAULT_DC_RMS_CURRENT_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE

# Default measurement function parameters including current range/function and resolution in digits
DEFAULT_DC_RMS_CURRENT_MEASUREMENT_PARAMETERS = DcRmsCurrentMeasurementFunctionParameters(
    measurement_function=ConstantsForDcRmsCurrentMeasurements.RANGE_AND_FUNCTION,
    resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS,
)

# Default timing parameters including aperture time and settle time
DEFAULT_DC_RMS_CURRENT_TIMING_PARAMETERS = TimingParameters(
    aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS,
    settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS,
)

# Default AC minimum frequency
DEFAULT_DC_RMS_CURRENT_AC_MIN_FREQUENCY = ConstantsForDcRmsMeasurements.DEFAULT_AC_MIN_FREQUENCY

# Default trigger parameters including trigger source, trigger delay, and trigger enable setting
DEFAULT_DC_RMS_CURRENT_TRIGGER_PARAMETERS = TriggerParameters(
    trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE,
    trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY,
    slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE,
    enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER,
)

# Default DC-RMS current measurement configuration
DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION = DcRmsCurrentMeasurementConfiguration(
    execution_type=DEFAULT_DC_RMS_CURRENT_EXECUTION_TYPE,
    measurement_function_parameters=DEFAULT_DC_RMS_CURRENT_MEASUREMENT_PARAMETERS,
    trigger_parameters=DEFAULT_DC_RMS_CURRENT_TRIGGER_PARAMETERS,
    timing_parameters=DEFAULT_DC_RMS_CURRENT_TIMING_PARAMETERS,
    ac_min_frequency=DEFAULT_DC_RMS_CURRENT_AC_MIN_FREQUENCY,
)
