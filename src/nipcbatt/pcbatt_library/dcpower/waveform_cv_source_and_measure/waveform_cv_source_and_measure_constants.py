"""Constants for waveform DC voltage source and measure operations."""

import dataclasses

import nidcpower

from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure_data_types import (
    EventSignalToExport,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TriggerParameters,
    WaveformExecutionSettings,
    WaveformTimingParameters,
    WaveformVoltageChannelSettings,
    WaveformVoltageSourceAndMeasureParameters,
)


@dataclasses.dataclass
class ConstantsForWaveformVoltageSourceAndMeasure:
    """Default scalar constants for waveform voltage source and measure operations."""

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE

    # WaveformVoltageChannelSettings
    DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS = 6.0
    DEFAULT_CURRENT_LIMIT_AMPERES = 0.020
    DEFAULT_CURRENT_LIMIT_RANGE_AMPERES = 0.020
    DEFAULT_STEP_TIME_SECONDS = 0.1
    DEFAULT_SENSING = nidcpower.Sense.REMOTE
    DEFAULT_ENABLE_OUTPUT = True

    # Voltage setpoints applied as a sequence
    DEFAULT_VOLTAGE_SETPOINTS = [0.0, 1.0, 0.0]

    # WaveformTimingParameters
    DEFAULT_SOURCE_DELAY_SECONDS = 0.0  # Source Delay = 0 s
    DEFAULT_APERTURE_TIME_SECONDS = 0.001
    DEFAULT_TRANSIENT_RESPONSE = nidcpower.TransientResponse.NORMAL
    DEFAULT_VOLTAGE_GAIN_BANDWIDTH = 5000.0  # Hz
    DEFAULT_VOLTAGE_COMPENSATION_FREQUENCY = 50000.0  # Hz
    DEFAULT_VOLTAGE_POLE_ZERO_RATIO = 0.16
    DEFAULT_CURRENT_GAIN_BANDWIDTH = 50000.0  # Hz
    DEFAULT_CURRENT_COMPENSATION_FREQUENCY = 250000.0  # Hz
    DEFAULT_CURRENT_POLE_ZERO_RATIO = 5.0

    # TriggerParameters
    DEFAULT_SOURCE_TRIGGER_BEHAVIOR = (
        SourceTriggerBehavior.Disable_Source_Trigger
    )  # Source trigger disabled by default
    DEFAULT_START_SOURCE_NAME = (
        ""  # Trigger input terminal, e.g. "/PXI1Slot2/PXI_Trig0"; ignored when trigger is disabled
    )
    DEFAULT_EXPORT_EVENT = (
        ExportEvent.NONE
    )  # Use Route_Event to route triggers and events to specified terminals; use None to disable exporting
    DEFAULT_EVENT_SIGNAL_TO_EXPORT = EventSignalToExport.Source_Complete_Event  # Signal to route
    DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL = (
        ""  # Output terminal, e.g. "/PXI1Slot2/PXI_Trig1"; Ignored when using ExportEvent.NONE
    )


DEFAULT_WAVEFORM_CV_EXECUTION_SETTINGS = WaveformExecutionSettings(
    execution_type=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_EXECUTION_TYPE,
)

DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS = WaveformVoltageChannelSettings(
    voltage_level_range=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS,
    current_limit_range=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_RANGE_AMPERES,
    current_limit=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_AMPERES,
    step_time=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_STEP_TIME_SECONDS,
    sensing=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_SENSING,
    enable_output=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_ENABLE_OUTPUT,
    voltage_setpoints=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_SETPOINTS,
)

DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS = WaveformTimingParameters(
    source_delay=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
    aperture_time=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
    transient_response=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_TRANSIENT_RESPONSE,
    voltage_gain_bandwidth=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_GAIN_BANDWIDTH,
    voltage_compensation_frequency=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_COMPENSATION_FREQUENCY,
    voltage_pole_zero_ratio=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_POLE_ZERO_RATIO,
    current_gain_bandwidth=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_GAIN_BANDWIDTH,
    current_compensation_frequency=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_COMPENSATION_FREQUENCY,
    current_pole_zero_ratio=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_POLE_ZERO_RATIO,
)

DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS = TriggerParameters(
    source_trigger_behavior=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_SOURCE_TRIGGER_BEHAVIOR,
    start_source_name=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_START_SOURCE_NAME,
    export_event=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_EXPORT_EVENT,
    event_signal_to_export=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_EVENT_SIGNAL_TO_EXPORT,
    output_event_signal_terminal=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL,
)

DEFAULT_WAVEFORM_CV_SOURCE_AND_MEASURE_PARAMETERS = WaveformVoltageSourceAndMeasureParameters(
    voltage_channel_settings=DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS,
    execution_settings=DEFAULT_WAVEFORM_CV_EXECUTION_SETTINGS,
    timing_parameters=DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS,
    trigger_parameters=DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS,
)
