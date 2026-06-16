"""Common data types shared across DC power source and measure operations."""

from enum import Enum

import nidcpower

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData


class MeasurementExecutionType(Enum):
    """Defines the execution type for DC source and measure operations."""

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
    """Defines execution settings for a DC source and measure operation."""

    def __init__(self, execution_type: MeasurementExecutionType, skip_analysis: bool) -> None:
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


class TimingParameters:
    """Defines timing settings for DC source and measure operations."""

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
    """Defines trigger parameters and event signal routing settings for
    a DC source operation.
    """

    def __init__(
        self,
        source_trigger_behavior: SourceTriggerBehavior,
        start_source_name: str,
        export_event: ExportEvent,
        event_signal_to_export: EventSignalToExport,
        output_event_signal_terminal: str,
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
