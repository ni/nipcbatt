"""Constants for waveform DC voltage source and measure operations."""

import dataclasses

import nidcpower

from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure_data_types import (
    ExecutionSettings,
    EventSignalToExport,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    VoltageChannelSettings,
    WaveformVoltageSourceAndMeasureParameters,
)


@dataclasses.dataclass
class ConstantsForWaveformVoltageSourceAndMeasure:
    """Default scalar constants for waveform voltage source and measure operations."""

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
    DEFAULT_SKIP_ANALYSIS = False

    # VoltageChannelSettings
    DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS = 6.0         # Voltage Level Range
    DEFAULT_CURRENT_LIMIT_AMPERES = 0.020            # Current Limit = 20 mA
    DEFAULT_CURRENT_LIMIT_RANGE_AMPERES = 0.020      # Current Limit Range = 20 mA

    # Voltage setpoints applied as a sequence
    DEFAULT_VOLTAGE_SETPOINTS = [0.1, 1.0, 0.1]     # [100 mV, 1 V, 100 mV]

    # TimingParameters
    DEFAULT_SOURCE_DELAY_SECONDS = 0.1               # Step Time = 100 ms
    DEFAULT_APERTURE_TIME_SECONDS = 0.001            # Aperture Time = 1 ms
    DEFAULT_STEP_SIZE_SECONDS = 0.00001              # Step size = 10 µs (aperture_time / step_record_length)
    DEFAULT_MEASURE_RECORD_LENGTH = 100              # Step Record Length
    DEFAULT_MEASURE_WHEN = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
    DEFAULT_TRANSIENT_RESPONSE = nidcpower.TransientResponse.NORMAL
    DEFAULT_VOLTAGE_GAIN_BANDWIDTH = 5000.0          # Hz
    DEFAULT_VOLTAGE_COMPENSATION_FREQUENCY = 50000.0 # Hz
    DEFAULT_VOLTAGE_POLE_ZERO_RATIO = 0.16
    DEFAULT_CURRENT_GAIN_BANDWIDTH = 50000.0         # Hz
    DEFAULT_CURRENT_COMPENSATION_FREQUENCY = 250000.0 # Hz
    DEFAULT_CURRENT_POLE_ZERO_RATIO = 5.0

    # TriggerParameters
    DEFAULT_SOURCE_TRIGGER_BEHAVIOR = SourceTriggerBehavior.No_Synchronization_Events
    DEFAULT_SOURCE_TRIGGER_EDGE = nidcpower.TriggerEdge.RISING
    DEFAULT_START_SOURCE_NAME = ""
    DEFAULT_START_MEASURE_NAME = ""
    DEFAULT_EXPORT_EVENT = ExportEvent.NONE
    DEFAULT_EVENT_SIGNAL_TO_EXPORT = EventSignalToExport.Source_Complete_Event
    DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL = ""


DEFAULT_WAVEFORM_CV_EXECUTION_SETTINGS = ExecutionSettings(
    execution_type=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_EXECUTION_TYPE,
    skip_analysis=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_SKIP_ANALYSIS,
)

DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS = VoltageChannelSettings(
    voltage_level_range=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS,
    current_limit=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_AMPERES,
    current_limit_range=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_RANGE_AMPERES,
)

DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS = TimingParameters(
    source_delay=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
    aperture_time=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
    step_size=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_STEP_SIZE_SECONDS,
    measure_record_length=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_MEASURE_RECORD_LENGTH,
    measure_when=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_MEASURE_WHEN,
    transient_response=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_TRANSIENT_RESPONSE,
    voltage_gain_bandwidth=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_GAIN_BANDWIDTH,
    voltage_compensation_frequency=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_COMPENSATION_FREQUENCY,
    voltage_pole_zero_ratio=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_POLE_ZERO_RATIO,
    current_gain_bandwidth=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_GAIN_BANDWIDTH,
    current_compensation_frequency=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_COMPENSATION_FREQUENCY,
    current_pole_zero_ratio=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_POLE_ZERO_RATIO,
)

# DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS = TriggerParameters(
#     source_trigger_behavior=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_SOURCE_TRIGGER_BEHAVIOR,
#     source_trigger_edge=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_SOURCE_TRIGGER_EDGE,
#     start_source_name=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_START_SOURCE_NAME,
#     start_measure_name=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_START_MEASURE_NAME,
#     export_event=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_EXPORT_EVENT,
#     event_signal_to_export=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_EVENT_SIGNAL_TO_EXPORT,
#     output_event_signal_terminal=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL,
# )

DEFAULT_WAVEFORM_CV_SOURCE_AND_MEASURE_PARAMETERS = WaveformVoltageSourceAndMeasureParameters(
    voltage_channel_settings=DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS,
    execution_settings=DEFAULT_WAVEFORM_CV_EXECUTION_SETTINGS,
    timing_parameters=DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS,
    voltage_setpoints=ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_SETPOINTS,
)
