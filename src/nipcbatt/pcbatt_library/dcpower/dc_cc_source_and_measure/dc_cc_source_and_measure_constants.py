"""Constants for DC constant current source and measure operations."""

import dataclasses

import nidcpower

from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure_data_types import (
    CurrentChannelSettings,
    DCCurrentSourceAndMeasureParameters,
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)


@dataclasses.dataclass
class ConstantsForDCCurrentSourceAndMeasure:
    """Default scalar constants for DC current source and measure operations."""

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
    DEFAULT_SKIP_ANALYSIS = False

    DEFAULT_CURRENT_LEVEL_AMPERES = 10e-6         # 10 uA — small value to protect hardware
    DEFAULT_CURRENT_LEVEL_RANGE_AMPERES = 0.1     # Must be >= current level
    DEFAULT_VOLTAGE_LIMIT_VOLTS = 1.0             # Small value to protect hardware
    DEFAULT_VOLTAGE_LIMIT_RANGE_VOLTS = 2.0       # Must be >= voltage limit
    DEFAULT_SENSING = nidcpower.Sense.REMOTE      # Not compatible with all devices; use LOCAL if needed
    DEFAULT_ENABLE_OUTPUT = True                  # Set False to control output manually via enable_output()

    DEFAULT_SOURCE_DELAY_SECONDS = 0.1            # 100 ms; compatible with all PPS/SMU; use <=20 ms for SMUs
    DEFAULT_APERTURE_TIME_SECONDS = 0.02          # 20 ms for 50 Hz noise rejection; use 16.667 ms for 60 Hz
    DEFAULT_TRANSIENT_RESPONSE = nidcpower.TransientResponse.NORMAL  # Adjust based on DUT behavior

    DEFAULT_SOURCE_TRIGGER_BEHAVIOR = SourceTriggerBehavior.Disable_Source_Trigger  # Source trigger disabled by default 
    DEFAULT_START_SOURCE_NAME = ""                                                    # Trigger input terminal, e.g. "/PXI1Slot2/PXI_Trig0"; ignored when trigger is disabled
    DEFAULT_EXPORT_EVENT = ExportEvent.NONE                                           # Use Route_Event to route triggers and events to specified terminals; use None to disable exporting
    DEFAULT_EVENT_SIGNAL_TO_EXPORT = EventSignalToExport.Source_Complete_Event        # Signal to route
    DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL = ""                                         # Output terminal, e.g. "/PXI1Slot2/PXI_Trig1"; Ignored when no export event or when using ExportEvent.NONE

DEFAULT_DC_CC_EXECUTION_SETTINGS = ExecutionSettings(
    execution_type=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_EXECUTION_TYPE,
    skip_analysis=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SKIP_ANALYSIS,
)

DEFAULT_DC_CC_CHANNEL_SETTINGS = CurrentChannelSettings(
    current_level=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_AMPERES,
    current_level_range=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_RANGE_AMPERES,
    voltage_limit=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_VOLTS,
    voltage_limit_range=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_RANGE_VOLTS,
    sensing=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SENSING,
    enable_output=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_ENABLE_OUTPUT,
)

DEFAULT_DC_CC_TIMING_PARAMETERS = TimingParameters(
    source_delay=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
    aperture_time=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
    transient_response=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_TRANSIENT_RESPONSE,
)

DEFAULT_DC_CC_TRIGGER_PARAMETERS = TriggerParameters(
    source_trigger_behavior=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_TRIGGER_BEHAVIOR,
    start_source_name=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_START_SOURCE_NAME,
    export_event=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_EXPORT_EVENT,
    event_signal_to_export=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_EVENT_SIGNAL_TO_EXPORT,
    output_event_signal_terminal=ConstantsForDCCurrentSourceAndMeasure.DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL,
)

DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS = DCCurrentSourceAndMeasureParameters(
    current_channel_settings=DEFAULT_DC_CC_CHANNEL_SETTINGS,
    execution_settings=DEFAULT_DC_CC_EXECUTION_SETTINGS,
    timing_parameters=DEFAULT_DC_CC_TIMING_PARAMETERS,
    trigger_parameters=DEFAULT_DC_CC_TRIGGER_PARAMETERS,
)
