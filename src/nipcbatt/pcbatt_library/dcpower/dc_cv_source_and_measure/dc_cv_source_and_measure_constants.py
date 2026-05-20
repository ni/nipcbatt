"""Constants for DC constant voltage source and measure operations."""

import dataclasses

import nidcpower

from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    ExecutionSettings,
    EventSignalToExport,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)


@dataclasses.dataclass
class ConstantsForDCVoltageSourceAndMeasure:
    """Default scalar constants used for DC voltage source and measure operations."""

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
    DEFAULT_SKIP_ANALYSIS = False

    DEFAULT_VOLTAGE_LEVEL_VOLTS = 1.0
    DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS = 1.0
    DEFAULT_CURRENT_LIMIT_AMPERES = 0.01
    DEFAULT_CURRENT_LIMIT_RANGE_AMPERES = 0.1
    DEFAULT_SENSING = nidcpower.Sense.REMOTE
    DEFAULT_ENABLE_OUTPUT = True

    DEFAULT_SOURCE_DELAY_SECONDS = 0.1
    DEFAULT_APERTURE_TIME_SECONDS = 0.02
    DEFAULT_TRANSIENT_RESPONSE = nidcpower.TransientResponse.NORMAL

    DEFAULT_SOURCE_TRIGGER_BEHAVIOR = SourceTriggerBehavior.Disable_Source_Trigger
    DEFAULT_START_SOURCE_NAME = ""
    DEFAULT_EXPORT_EVENT = ExportEvent.NONE
    DEFAULT_EVENT_SIGNAL_TO_EXPORT = EventSignalToExport.Source_Complete_Event
    DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL = ""


DEFAULT_DC_CV_EXECUTION_SETTINGS = ExecutionSettings(
    execution_type=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_EXECUTION_TYPE,
    skip_analysis=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SKIP_ANALYSIS,
)

DEFAULT_DC_CV_CHANNEL_SETTINGS = VoltageChannelSettings(
    voltage_level=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_VOLTS,
    voltage_level_range=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS,
    current_limit=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_AMPERES,
    current_limit_range=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_RANGE_AMPERES,
    sensing=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SENSING,
    enable_output=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_ENABLE_OUTPUT,
)

DEFAULT_DC_CV_TIMING_PARAMETERS = TimingParameters(
    source_delay=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
    aperture_time=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
    transient_response=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_TRANSIENT_RESPONSE,
)

DEFAULT_DC_CV_TRIGGER_PARAMETERS = TriggerParameters(
    source_trigger_behavior=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_SOURCE_TRIGGER_BEHAVIOR,
    start_source_name=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_START_SOURCE_NAME,
    export_event=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_EXPORT_EVENT,
    event_signal_to_export=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_EVENT_SIGNAL_TO_EXPORT,
    output_event_signal_terminal=ConstantsForDCVoltageSourceAndMeasure.DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL,
)

DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS = DCVoltageSourceAndMeasureParameters(
    voltage_channel_settings=DEFAULT_DC_CV_CHANNEL_SETTINGS,
    execution_settings=DEFAULT_DC_CV_EXECUTION_SETTINGS,
    timing_parameters=DEFAULT_DC_CV_TIMING_PARAMETERS,
    trigger_parameters=DEFAULT_DC_CV_TRIGGER_PARAMETERS,
)
