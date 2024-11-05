""" Constants data types for Frequency domain Measurements."""

import dataclasses

from nipcbatt.pcbatt_analysis.waveform_analysis.frequency_domain_analysis import (
    LabViewFftSpectrumWindow,
    LabViewTonesSortingMode,
    SpectrumPhaseUnit,
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
from nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_data_types import (
    FrequencyDomainMeasurementConfiguration,
)


@dataclasses.dataclass
class ConstantsForFrequencyDomainMeasurement:
    """Constants used for Frequency Domain measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)

    FILTERING_WINDOW_FOR_FFT = LabViewFftSpectrumWindow.HANNING
    """Specifies the time-domain window to apply to the time signal before performing FFT.
    1- Hanning"""

    VIEW_RESULTS_dB_ON = True
    """Specifies whether the results are expressed in decibels"""

    VIEW_RESULTS_PHASE_UNIT = SpectrumPhaseUnit.RADIAN
    """Specifies whether the phase results are expressed as radians or degrees."""

    DEFAULT_THRESHOLD_FOR_TONE_EXTRACTION = 0.010
    """Specifies the minimum amplitude that each tone must exceed 
    for this VI to extract it from time signal in."""

    DEFAULT_MAX_NUMBER_OF_TONES_TO_BE_EXTRACTED = None
    """Specifies the maximum number of tones that this VI extracts. 
    If you set max num tones to `None`, 
    tones processor will extract all tones whose amplitude exceeds threshold."""

    DEFAULT_SORTING_ORDER_OF_THE_EXTRACTED_TONES = LabViewTonesSortingMode.INCREASING_FREQUENCIES
    """Specifies the sorting order of the tones that this VI extracts, 
    `increasing frequencies` or `decreasing amplitudes`"""


DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS = VoltageRangeAndTerminalParameters(
    terminal_configuration=ConstantsForVoltageMeasurement.DEFAULT_AI_TERMINAL_CONFIGURATION,
    range_min_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS,
    range_max_volts=ConstantsForVoltageMeasurement.DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS,
)

DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForVoltageMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForVoltageMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForVoltageMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForVoltageMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForVoltageMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForVoltageMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForVoltageMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION = FrequencyDomainMeasurementConfiguration(
    global_channel_parameters=DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
    specific_channels_parameters=[],
    measurement_options=DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
)
