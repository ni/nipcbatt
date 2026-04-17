import nidcpower
from enum import Enum

class MeasurementExecutionType(Enum):
    CONFIGURE_SOURCE_AND_MEASURE = "CONFIGURE_SOURCE_AND_MEASURE"
    CONFIGURE_ONLY = "CONFIGURE_ONLY"
    START_SOURCE_ONLY = "START_SOURCE_ONLY"
    MEASURE_ONLY = "MEASURE_ONLY"

class SourceTriggerBehavior(Enum):
    Start_Source_Trigger = "Start_Source_Trigger"
    Disable_Source_Trigger = "Disable_Source_Trigger"

class ExportEvent(Enum):
    NONE = "NONE"
    Route_Event = "Route_Event"

class EventSignalToExport(Enum):
    Source_Complete_Event = "source_complete_event_output_terminal"
    Measure_Complete_Event = "measure_complete_event_output_terminal"
    Sequence_Iteration_Complete_Event = "sequence_iteration_complete_event_output_terminal"
    Sequence_Engine_Done_Event = "sequence_engine_done_event_output_terminal"
    Pulse_Complete_Event = "pulse_complete_event_output_terminal"
    Ready_for_Pulse_Trigger_Event = "ready_for_pulse_trigger_event_output_terminal"
    Start_Trigger = "exported_start_trigger_output_terminal"
    Source_Trigger = "exported_source_trigger_output_terminal"
    Measure_Trigger = "exported_measure_trigger_output_terminal"
    Sequence_Advance_Trigger = "exported_sequence_advance_trigger_output_terminal"
    Pulse_Trigger = "exported_pulse_trigger_output_terminal"

class VoltageChannelSettings:
    def __init__(
        self,
        voltage_level: float,
        voltage_level_range: float,
        current_limit: float,
        current_limit_range: float,
        sensing: nidcpower.Sense,
        enable_output: bool,
    ) -> None:
        self._voltage_level = voltage_level
        self._voltage_level_range = voltage_level_range
        self._current_limit = current_limit
        self._current_limit_range = current_limit_range
        self._sensing = sensing
        self._enable_output = enable_output

    @property
    def voltage_level(self) -> float:
        return self._voltage_level
    
    @property
    def voltage_level_range(self) -> float:
        return self._voltage_level_range    
    
    @property
    def current_limit(self) -> float:   
        return self._current_limit
    
    @property
    def current_limit_range(self) -> float:
        return self._current_limit_range
    
    @property
    def sensing(self) -> nidcpower.Sense:
        return self._sensing
    
    @property
    def enable_output(self) -> bool:
        return self._enable_output

class TimingParameters:
    def __init__(
        self,
        source_delay: float,
        aperture_time: float,
        transient_response: nidcpower.TransientResponse,
    ) -> None:
        self._source_delay = source_delay
        self._aperture_time = aperture_time
        self._transient_response = transient_response

    @property
    def source_delay(self) -> float:
        return self._source_delay
    
    @property
    def aperture_time(self) -> float:
        return self._aperture_time
    
    @property
    def transient_response(self) -> nidcpower.TransientResponse:
        return self._transient_response

class TriggerParameters:
    def __init__(
        self,
        source_trigger_behavior: SourceTriggerBehavior,
        start_source_name: str,
        export_event: ExportEvent,
        event_signal_to_export: EventSignalToExport,
        output_event_signal_terminal: str
    ) -> None:
        self._source_trigger_behavior = source_trigger_behavior
        self._start_source_name = start_source_name
        self._export_event = export_event
        self._event_signal_to_export = event_signal_to_export
        self._output_event_signal_terminal = output_event_signal_terminal

    @property
    def source_trigger_behavior(self) -> SourceTriggerBehavior:
        return self._source_trigger_behavior
    
    @property
    def start_source_name(self) -> str:  
        return self._start_source_name  
    
    @property
    def export_event(self) -> ExportEvent:
        return self._export_event
    
    @property
    def event_signal_to_export(self) -> EventSignalToExport:    
        return self._event_signal_to_export
    
    @property
    def output_event_signal_terminal(self) -> str:
        return self._output_event_signal_terminal   

class DCVoltageSourceAndMeasureParameters:
    def __init__(
        self,
        voltage_channel_settings: VoltageChannelSettings,
        execution_type: MeasurementExecutionType,
        timing_parameters: TimingParameters,
        trigger_parameters:TriggerParameters
    ) -> None:
        self._voltage_channel_settings = voltage_channel_settings
        self._execution_type = execution_type
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def voltage_channel_settings(self) -> VoltageChannelSettings:
        return self._voltage_channel_settings

    @property
    def execution_type(self) -> MeasurementExecutionType:
        return self._execution_type

    @property
    def timing_parameters(self) -> TimingParameters:
        return self._timing_parameters
    
    @property
    def trigger_parameters(self) -> TriggerParameters:
        return self._trigger_parameters