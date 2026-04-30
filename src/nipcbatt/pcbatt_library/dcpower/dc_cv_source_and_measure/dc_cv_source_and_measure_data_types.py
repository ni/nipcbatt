"""Data types used for DC constant voltage source and measurement on PCB points."""

import nidcpower
from enum import Enum


class MeasurementExecutionType(Enum):
    """Defines the execution type for DC constant voltage source and measure."""

    CONFIGURE_SOURCE_AND_MEASURE = "CONFIGURE_SOURCE_AND_MEASURE"
    CONFIGURE_ONLY = "CONFIGURE_ONLY"
    START_SOURCE_ONLY = "START_SOURCE_ONLY"
    MEASURE_ONLY = "MEASURE_ONLY"

class SourceTriggerBehavior(Enum):
    """Defines the source trigger behavior enum."""

    Start_Source_Trigger = "Start_Source_Trigger"
    Disable_Source_Trigger = "Disable_Source_Trigger"

class ExportEvent(Enum):
    """Defines the export event enum."""

    NONE = "NONE"
    Route_Event = "Route_Event"

class EventSignalToExport(Enum):
    """Defines the NI-DCPower event or trigger signal to route to an output terminal enum.

    Each member's value is the corresponding NI-DCPower channel attribute name,
    used with ``setattr`` to configure the output terminal for that signal.
    """

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

class ExecutionSettings:
    """Defines execution settings for a DC constant voltage source and measure operation."""

    def __init__(
            self,
            execution_type: MeasurementExecutionType,
            skip_analysis: bool
        ) -> None:  
        """Initializes the execution settings.

        Args:
            execution_type (MeasurementExecutionType):
                The execution type having values:
                - ``CONFIGURE_SOURCE_AND_MEASURE``,
                - ``CONFIGURE_ONLY``,
                - ``START_SOURCE_ONLY``, or
                - ``MEASURE_ONLY``.
            skip_analysis (bool):
                When ``True``, post-measurement analysis is skipped.
        """
        self._execution_type = execution_type
        self._skip_analysis = skip_analysis

    @property
    def execution_type(self) -> MeasurementExecutionType:
        """Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The configured execution type.
        """
        return self._execution_type

    @property
    def skip_analysis(self) -> bool:
        """Gets whether post-measurement analysis is skipped.

        Returns:
            bool: ``True`` if analysis is skipped;
            ``False`` if full analysis is performed.
        """
        return self._skip_analysis

class VoltageChannelSettings:
    """Defines the voltage level, current limit, sensing, and output enable settings for a channel."""

    def __init__(
        self,
        voltage_level: float,
        voltage_level_range: float,
        current_limit: float,
        current_limit_range: float,
        sensing: nidcpower.Sense,
        enable_output: bool,
    ) -> None:
        """Initializes the voltage channel settings.

        Args:
            voltage_level (float):
                The DC voltage level to source, in volts.
            voltage_level_range (float):
                The voltage level range setting, in volts.
            current_limit (float):
                The current limit for the output, in amperes.
            current_limit_range (float):
                The current limit range setting, in amperes.
            sensing (nidcpower.Sense):
                The sensing mode (``LOCAL`` or ``REMOTE``) for voltage measurement.
            enable_output (bool):
                Whether the channel output is enabled.
        """
        self._voltage_level = voltage_level
        self._voltage_level_range = voltage_level_range
        self._current_limit = current_limit
        self._current_limit_range = current_limit_range
        self._sensing = sensing
        self._enable_output = enable_output

    @property
    def voltage_level(self) -> float:
        """Gets the DC voltage level to source.

        Returns:
            float: The voltage level in volts.
        """
        return self._voltage_level

    @property
    def voltage_level_range(self) -> float:
        """Gets the voltage level range.

        Returns:
            float: The voltage level range in volts.
        """
        return self._voltage_level_range

    @property
    def current_limit(self) -> float:
        """Gets the current limit for the output.

        Returns:
            float: The current limit in amperes.
        """
        return self._current_limit

    @property
    def current_limit_range(self) -> float:
        """Gets the current limit range.

        Returns:
            float: The current limit range in amperes.
        """
        return self._current_limit_range

    @property
    def sensing(self) -> nidcpower.Sense:
        """Gets the sensing mode.

        Returns:
            nidcpower.Sense: The sensing mode (``LOCAL`` or ``REMOTE``).
        """
        return self._sensing

    @property
    def enable_output(self) -> bool:
        """Gets whether output is enabled.

        Returns:
            bool: ``True`` if the output is enabled, ``False`` otherwise.
        """
        return self._enable_output

class TimingParameters:
    """Defines timing settings for DC constant voltage source and measure."""

    def __init__(
        self,
        source_delay: float,
        aperture_time: float,
        transient_response: nidcpower.TransientResponse,
    ) -> None:
        """Initializes the timing parameters.

        Args:
            source_delay (float):
                Defines source delay in seconds.
            aperture_time (float):
                Defines aperture time in seconds.
            transient_response (nidcpower.TransientResponse):
                Defines the transient response.
        """
        self._source_delay = source_delay
        self._aperture_time = aperture_time
        self._transient_response = transient_response

    @property
    def source_delay(self) -> float:
        """Gets the source delay.

        Returns:
            float: The source delay in seconds.
        """
        return self._source_delay

    @property
    def aperture_time(self) -> float:
        """Gets the aperture time.

        Returns:
            float: The aperture time in seconds.
        """
        return self._aperture_time

    @property
    def transient_response(self) -> nidcpower.TransientResponse:
        """Gets the transient response setting.

        Returns:
            nidcpower.TransientResponse: The transient response mode.
        """
        return self._transient_response

class TriggerParameters:
    """Defines trigger parameters and event signal routing settings for a DC voltage source operation."""

    def __init__(
        self,
        source_trigger_behavior: SourceTriggerBehavior,
        start_source_name: str,
        export_event: ExportEvent,
        event_signal_to_export: EventSignalToExport,
        output_event_signal_terminal: str
    ) -> None:
        """Initializes the trigger parameters.

        Args:
            source_trigger_behavior (SourceTriggerBehavior):
                Configures source trigger behavior.
            start_source_name (str):
                Configures the start source name.
                Ignored when ``source_trigger_behavior`` is ``Disable_Source_Trigger``.
            export_event (ExportEvent):
                Configures export event.
            event_signal_to_export (EventSignalToExport):
                Configures the event signal to export.
                Ignored when ``export_event`` is ``NONE``.
            output_event_signal_terminal (str):
                The output terminal name to which the event signal is routed. 
                Ignored when ``export_event`` is ``NONE``.
        """
        self._source_trigger_behavior = source_trigger_behavior
        self._start_source_name = start_source_name
        self._export_event = export_event
        self._event_signal_to_export = event_signal_to_export
        self._output_event_signal_terminal = output_event_signal_terminal

    @property
    def source_trigger_behavior(self) -> SourceTriggerBehavior:
        """Gets the source trigger behavior.

        Returns:
            SourceTriggerBehavior: Configures source trigger behavior.
        """
        return self._source_trigger_behavior

    @property
    def start_source_name(self) -> str:
        """Gets the start source name.

        Returns:
            str: The start source name.
        """
        return self._start_source_name

    @property
    def export_event(self) -> ExportEvent:
        """Gets the export event setting.

        Returns:
            ExportEvent: Configures export event.
        """
        return self._export_event

    @property
    def event_signal_to_export(self) -> EventSignalToExport:
        """Gets the event signal to export.

        Returns:
            EventSignalToExport: Configures the event signal to export.
        """
        return self._event_signal_to_export

    @property
    def output_event_signal_terminal(self) -> str:
        """Gets the output event signal terminal.

        Returns:
            str: Configures the output event signal terminal.
        """
        return self._output_event_signal_terminal   

class DCVoltageSourceAndMeasureParameters:
    """Defines the full configuration for DC constant voltage source and measure operation."""

    def __init__(
        self,
        voltage_channel_settings: VoltageChannelSettings,
        execution_settings: ExecutionSettings,
        timing_parameters: TimingParameters,
        trigger_parameters: TriggerParameters,
    ) -> None:
        """Initializes the DC voltage source and measure parameters.

        Args:
            voltage_channel_settings (VoltageChannelSettings):
                Voltage level, current limit, sensing mode, and output enable settings.
            execution_settings (ExecutionSettings):
                Execution mode and analysis control settings.
            timing_parameters (TimingParameters):
                Source delay, aperture time, and transient response settings.
            trigger_parameters (TriggerParameters):
                Source trigger input and event signal routing settings.
        """
        self._voltage_channel_settings = voltage_channel_settings
        self._execution_settings = execution_settings
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def voltage_channel_settings(self) -> VoltageChannelSettings:
        """Gets the voltage channel settings.

        Returns:
            VoltageChannelSettings: Configures the voltage level, current limit, sensing, and output enable settings.
        """
        return self._voltage_channel_settings

    @property
    def execution_settings(self) -> ExecutionSettings:
        """Gets the execution settings.

        Returns:
            ExecutionSettings: Configures the execution mode and skip analysis settings.
        """
        return self._execution_settings

    @property
    def timing_parameters(self) -> TimingParameters:
        """Gets the timing parameters.

        Returns:
            TimingParameters: Configures the source delay, aperture time, and transient
            response settings.
        """
        return self._timing_parameters

    @property
    def trigger_parameters(self) -> TriggerParameters:
        """Gets the trigger parameters.

        Returns:
            TriggerParameters: Configures the source trigger input and event signal
            routing settings.
        """
        return self._trigger_parameters