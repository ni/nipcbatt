"""Constants data types for DC-RMS Voltage Measurements."""

import dataclasses

from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.constants import ConstantsForDcRmsMeasurements
from nipcbatt.pcbatt_library.dmm.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
    DcRmsVoltageMeasurementFunctionParameters,
    VoltageRangeAndFunctions,
)


@dataclasses.dataclass
class ConstantsForDcRmsVoltageMeasurements:
    """Constants used for Voltage measurement."""

    RANGE_AND_FUNCTION = VoltageRangeAndFunctions.DC_Voltage_Auto_Range


# Voltage measurement-specific range/function setting is defined
# in ConstantsForDcRmsVoltageMeasurements.
# Default execution type for voltage measurements
DEFAULT_DC_RMS_VOLTAGE_EXECUTION_TYPE = ConstantsForDcRmsMeasurements.DEFAULT_EXECUTION_TYPE

# Default measurement function parameter including voltage range/function and resolution in digits
DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_PARAMETERS = DcRmsVoltageMeasurementFunctionParameters(
    measurement_function=ConstantsForDcRmsVoltageMeasurements.RANGE_AND_FUNCTION,
    resolution_in_digits=ConstantsForDcRmsMeasurements.DEFAULT_RESOLUTION_IN_DIGITS,
)

# Default timing parameters including aperture time and settle time
DEFAULT_DC_RMS_VOLTAGE_TIMING_PARAMETERS = TimingParameters(
    aperture_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_APERTURE_TIME_SECONDS,
    settle_time_seconds=ConstantsForDcRmsMeasurements.DEFAULT_SETTLE_TIME_SECONDS,
)

# Default AC minimum frequency
DEFAULT_DC_RMS_VOLTAGE_AC_MIN_FREQUENCY = ConstantsForDcRmsMeasurements.DEFAULT_AC_MIN_FREQUENCY

# Default trigger parameters including trigger source, trigger delay, and trigger enable setting
DEFAULT_DC_RMS_VOLTAGE_TRIGGER_PARAMETERS = TriggerParameters(
    trigger_source=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SOURCE,
    trigger_delay=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_DELAY,
    slope=ConstantsForDcRmsMeasurements.DEFAULT_TRIGGER_SLOPE,
    enable_trigger=ConstantsForDcRmsMeasurements.DEFAULT_ENABLE_TRIGGER,
)

# Default DC-RMS voltage measurement configuration
DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION = DcRmsVoltageMeasurementConfiguration(
    execution_type=DEFAULT_DC_RMS_VOLTAGE_EXECUTION_TYPE,
    measurement_function_parameters=DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_PARAMETERS,
    trigger_parameters=DEFAULT_DC_RMS_VOLTAGE_TRIGGER_PARAMETERS,
    timing_parameters=DEFAULT_DC_RMS_VOLTAGE_TIMING_PARAMETERS,
    ac_min_frequency=DEFAULT_DC_RMS_VOLTAGE_AC_MIN_FREQUENCY,
)
