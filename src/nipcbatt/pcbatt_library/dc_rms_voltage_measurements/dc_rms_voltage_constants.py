""" Constants data types for DC-RMS Voltage  Measurements."""

import dataclasses

from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingWindow,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library.common.voltage_constants import (
    ConstantsForVoltageMeasurement,
)
from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
)


@dataclasses.dataclass
class ConstantsForDcRmsVoltageMeasurement:
    """Constants used for Voltage measurement"""

    DEFAULT_DC_RMS_PROCESSING_WINDOW = DcRmsProcessingWindow.HANN


DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS = VoltageRangeAndTerminalParameters(
    terminal_configuration=ConstantsForVoltageMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION,
    range_min_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS,
    range_max_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS,
)

DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForVoltageMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForVoltageMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForVoltageMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForVoltageMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForVoltageMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION = DcRmsVoltageMeasurementConfiguration(
    global_channel_parameters=DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS,
    specific_channels_parameters=[],
    measurement_options=DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS,
)
