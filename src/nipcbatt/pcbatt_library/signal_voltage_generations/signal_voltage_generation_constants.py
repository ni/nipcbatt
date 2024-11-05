""" Constants data types for Signal Voltage Generation Data types."""

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library.signal_voltage_generations.signal_voltage_data_types import (
    SignalVoltageGenerationMultipleTonesConfiguration,
    SignalVoltageGenerationMultipleTonesWaveParameters,
    SignalVoltageGenerationSineWaveConfiguration,
    SignalVoltageGenerationSineWaveParameters,
    SignalVoltageGenerationSquareWaveConfiguration,
    SignalVoltageGenerationSquareWaveParameters,
    SignalVoltageGenerationTimingParameters,
    ToneParameters,
)


@dataclasses.dataclass
class ConstantsForSignalVoltageGeneration:
    """Constants used for signal voltage generation."""

    INITIAL_AO_OUTPUT_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    INITIAL_RANGE_MIN_VOLTS = -10.0
    INITIAL_RANGE_MAX_VOLTS = 10.0
    INITIAL_AO_VOLTAGE_UNITS = nidaqmx.constants.VoltageUnits.VOLTS

    DEFAULT_AO_OUTPUT_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_RANGE_MIN_VOLTS = -10.0
    DEFAULT_RANGE_MAX_VOLTS = 10.0

    DEFAULT_SIGNAL_DURATION_SECONDS = 0.1
    DEFAULT_SIGNAL_OFFSET_VOLTS = 0
    DEFAULT_SIGNAL_FREQUENCY_HERTZ = 100
    DEFAULT_SIGNAL_AMPLITUDE_VOLTS = 1.0
    DEFAULT_SIGNAL_PHASE_RADIANS = 0
    DEFAULT_SIGNAL_DUTY_CYCLE_PERCENT = 50.0

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = int(
        DEFAULT_SIGNAL_DURATION_SECONDS * DEFAULT_SAMPLING_RATE_HERTZ
    )

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING


DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS = VoltageGenerationChannelParameters(
    range_min_volts=ConstantsForSignalVoltageGeneration.DEFAULT_RANGE_MIN_VOLTS,
    range_max_volts=ConstantsForSignalVoltageGeneration.DEFAULT_RANGE_MAX_VOLTS,
)

DEFAULT_TONE_PARAMETERS = ToneParameters(
    tone_frequency_hertz=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_FREQUENCY_HERTZ,
    tone_amplitude_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_AMPLITUDE_VOLTS,
    tone_phase_radians=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_PHASE_RADIANS,
)

DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS = SignalVoltageGenerationSineWaveParameters(
    generated_signal_offset_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_OFFSET_VOLTS,
    generated_signal_tone_parameters=DEFAULT_TONE_PARAMETERS,
)

DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS = SignalVoltageGenerationTimingParameters(
    sample_clock_source=ConstantsForSignalVoltageGeneration.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForSignalVoltageGeneration.DEFAULT_SAMPLING_RATE_HERTZ,
    generated_signal_duration_seconds=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_DURATION_SECONDS,
)

DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForSignalVoltageGeneration.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForSignalVoltageGeneration.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForSignalVoltageGeneration.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION = (
    SignalVoltageGenerationSineWaveConfiguration(
        voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS,
        waveform_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
        timing_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        digital_start_trigger_parameters=DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
    )
)

DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS = SignalVoltageGenerationSquareWaveParameters(
    generated_signal_amplitude_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_AMPLITUDE_VOLTS,
    generated_signal_offset_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_OFFSET_VOLTS,
    generated_signal_frequency_hertz=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_FREQUENCY_HERTZ,
    generated_signal_duty_cycle_percent=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_DUTY_CYCLE_PERCENT,
    generated_signal_phase_radians=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_PHASE_RADIANS,
)

DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION = SignalVoltageGenerationSquareWaveConfiguration(
    voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS,
    waveform_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS,
    timing_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
)

DEFAULT_MULTI_TONE_GENERATION_PARAMETERS = SignalVoltageGenerationMultipleTonesWaveParameters(
    generated_signal_offset_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_OFFSET_VOLTS,
    generated_signal_amplitude_volts=ConstantsForSignalVoltageGeneration.DEFAULT_SIGNAL_AMPLITUDE_VOLTS,
    multiple_tones_parameters=[
        ToneParameters(tone_frequency_hertz=100, tone_amplitude_volts=1.0, tone_phase_radians=0),
        ToneParameters(tone_frequency_hertz=200, tone_amplitude_volts=0.5, tone_phase_radians=0.1),
    ],
)

DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION = SignalVoltageGenerationMultipleTonesConfiguration(
    voltage_generation_range_parameters=DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS,
    waveform_parameters=DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
    timing_parameters=DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
)
