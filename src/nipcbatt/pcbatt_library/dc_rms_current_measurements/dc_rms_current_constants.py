""" Constants data types for DC-RMS Current  Measurements."""

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingWindow,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementExecutionType,
    MeasurementOptions,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_data_types import (
    DcRmsCurrentMeasurementConfiguration,
    DcRmsCurrentMeasurementTerminalRangeParameters,
)


@dataclasses.dataclass
class ConstantsForDcRmsCurrentMeasurement:
    """Constants used for Current measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)

    INITIAL_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.DEFAULT
    INITIAL_CURRENT_RANGE_MINIMUM_AMPERES = -0.01
    INITIAL_CURRENT_RANGE_MAXIMUM_AMPERES = 0.01
    INITIAL_AI_CURRENT_UNITS = nidaqmx.constants.CurrentUnits.AMPS
    INITIAL_SHUNT_RESISTOR_LOCATION = nidaqmx.constants.CurrentShuntResistorLocation.EXTERNAL
    INITIAL_EXTERNAL_SHUNT_RESISTOR_VALUE_OHMS = 0.001

    DEFAULT_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_CURRENT_RANGE_MINIMUM_AMPERES = -0.01
    DEFAULT_CURRENT_RANGE_MAXIMUM_AMPERES = 0.01
    DEFAULT_EXTERNAL_SHUNT_RESISTOR_VALUE_OHMS = 0.001

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_AND_MEASURE
    DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT = MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 1000
    DEFAULT_SAMPLE_TIMING_ENGINE = SampleTimingEngine.AUTO

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_DC_RMS_PROCESSING_WINDOW = DcRmsProcessingWindow.HANN


DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS = DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=ConstantsForDcRmsCurrentMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION,
    range_min_amperes=ConstantsForDcRmsCurrentMeasurement.DEFAULT_CURRENT_RANGE_MINIMUM_AMPERES,
    range_max_amperes=ConstantsForDcRmsCurrentMeasurement.DEFAULT_CURRENT_RANGE_MAXIMUM_AMPERES,
    shunt_resistor_ohms=ConstantsForDcRmsCurrentMeasurement.DEFAULT_EXTERNAL_SHUNT_RESISTOR_VALUE_OHMS,
)

DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForDcRmsCurrentMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForDcRmsCurrentMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForDcRmsCurrentMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForDcRmsCurrentMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForDcRmsCurrentMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForDcRmsCurrentMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForDcRmsCurrentMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForDcRmsCurrentMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForDcRmsCurrentMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION = DcRmsCurrentMeasurementConfiguration(
    global_channel_parameters=DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS,
    specific_channels_parameters=[],
    measurement_options=DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS,
)
