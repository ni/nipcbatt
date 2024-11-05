""" Constants data types for Time domain Measurements."""

import dataclasses

from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingWindow,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.pulse_analog_analysis import (
    PulseAnalogProcessingExportMode,
    PulseAnalogProcessingPolarity,
    PulseAnalogProcessingReferenceLevelsUnit,
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
from nipcbatt.pcbatt_library.time_domain_measurements.time_domain_data_types import (
    TimeDomainMeasurementConfiguration,
)


@dataclasses.dataclass
class ConstantsForTimeDomainMeasurement:
    """Constants used for Time Domain measurement"""

    DEFAULT_DC_RMS_PROCESSING_WINDOW = DcRmsProcessingWindow.HANN
    """Default window that will be used to process DC-RMS in time domain measurement class."""

    DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_METHOD = AmplitudeAndLevelsProcessingMethod.AUTO_SELECT
    """Default amplitude and levels processing method that will 
    be used to process peak peak amplitude in time domain measurement class."""

    DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_HISTOGRAM_SIZE = 256
    """Default histogram size that will be used to process peak peak 
    amplitude in time domain measurement class."""

    DEFAULT_PULSE_PROCESSING_POLARITY = PulseAnalogProcessingPolarity.HIGH
    """Default pulse processing polarity that will be used to process periodicity 
    of waveforms."""

    DEFAULT_PULSE_PROCESSING_EXPORT_MODE = PulseAnalogProcessingExportMode.ALL
    """Default pulse processing export mode."""

    DEFAULT_PULSE_PROCESSING_REFERENCE_LEVELS_UNIT = (
        PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT
    )
    """Default pulse processing reference levels unit that will be used to evaluate periodicity 
    of waveforms."""

    DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_HIGH = 95
    """Default pulse processing high reference level that will be used to evaluate periodicity 
    of waveforms."""

    DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_MIDDLE = 50
    """Default pulse processing middle reference level that will be used to evaluate periodicity 
    of waveforms."""

    DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_LOW = 5
    """Default pulse processing low reference level that will be used to evaluate periodicity 
    of waveforms."""


DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS = VoltageRangeAndTerminalParameters(
    terminal_configuration=ConstantsForVoltageMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION,
    range_min_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS,
    range_max_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS,
)

DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForVoltageMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForVoltageMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForVoltageMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForVoltageMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForVoltageMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_TIME_DOMAIN_MEASUREMENT_CONFIGURATION = TimeDomainMeasurementConfiguration(
    global_channel_parameters=DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
    specific_channels_parameters=[],
    measurement_options=DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
)
