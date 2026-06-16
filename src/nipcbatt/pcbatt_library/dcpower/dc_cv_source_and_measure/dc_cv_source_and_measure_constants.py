"""Constants for DC constant voltage source and measure operations."""

import dataclasses

import nidcpower

from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)


@dataclasses.dataclass
class ConstantsForDCVoltageSourceAndMeasure:
    """Default scalar constants for DC voltage source and measure operations."""

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
    DEFAULT_SKIP_ANALYSIS = False

    DEFAULT_VOLTAGE_LEVEL_VOLTS = 1.0  # Small value to protect hardware
    DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS = 1.0  # Must be >= voltage level
    DEFAULT_CURRENT_LIMIT_AMPERES = 0.01  # 10 mA — small value to protect hardware
    DEFAULT_CURRENT_LIMIT_RANGE_AMPERES = 0.1  # Must be >= current limit
    DEFAULT_SENSING = nidcpower.Sense.REMOTE  # Not compatible with all devices; use LOCAL if needed
    DEFAULT_ENABLE_OUTPUT = True  # Set False to control output manually via enable_output()

    DEFAULT_SOURCE_DELAY_SECONDS = 0.1  # 100 ms; compatible with all PPS/SMU; use <=20 ms for SMUs
    DEFAULT_APERTURE_TIME_SECONDS = 0.02  # 20 ms for 50 Hz noise rejection; use 16.667 ms for 60 Hz
    DEFAULT_TRANSIENT_RESPONSE = nidcpower.TransientResponse.NORMAL  # Adjust based on DUT behavior

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
