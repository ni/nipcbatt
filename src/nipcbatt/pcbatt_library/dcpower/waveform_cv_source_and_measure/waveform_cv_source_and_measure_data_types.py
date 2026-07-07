"""Data types used for waveform constant voltage source and measurement on PCB points."""

from enum import Enum

import nidcpower

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData

from nipcbatt.pcbatt_library.dcpower.common.common_data_types import (
    ExecutionSettings,
    MeasurementExecutionType,
    EventSignalToExport,
)


class VoltageChannelSettings:
    """Defines the voltage level, current limit, sensing, and output enable
    settings for a channel.
    """

    def __init__(
        self,
        voltage_level_range: float,
        current_limit_range: float,
        current_limit: float,
        
    ) -> None:
        """Initializes the voltage channel settings.

        Args:
            voltage_level_range (float):
                The voltage level range setting, in volts.
            current_limit (float):
                The current limit for the output, in amperes.
            current_limit_range (float):
                The current limit range setting, in amperes.
            
        """
        self._voltage_level_range = voltage_level_range
        self._current_limit_range = current_limit_range
        self._current_limit = current_limit

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


class WaveformTimingParameters:
    """Defines timing settings for waveform constant voltage source and measure."""

    def __init__(
        self,
        source_delay: float,
        aperture_time: float,
        step_size: float,
        measure_record_length: int,
        measure_when: nidcpower.MeasureWhen,
        transient_response: nidcpower.TransientResponse,
        voltage_gain_bandwidth: float,
        voltage_compensation_frequency: float,
        voltage_pole_zero_ratio: float,
        current_gain_bandwidth: float,
        current_compensation_frequency: float,
        current_pole_zero_ratio: float,
    ) -> None:
        """Initializes the timing parameters.

        Args:
            source_delay (float):
                Defines source delay in seconds.
            aperture_time (float):
                Defines aperture time in seconds.
            step_size (float):
                Defines the time interval between consecutive measurement samples, in seconds.
                Used to calculate step_record_length = aperture_time / step_size.
            measure_record_length (int):
                Defines how many samples constitute a record. If this is set to value greater than 1,
                then the measure_when parameter must be set to MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE, 
                or MeasureWhen.ON_MEASURE_TRIGGER.
            measure_when (nidcpower.MeasureWhen):
                Specifies when the measure unit should take measurements. Unless this property is set to MeasureWhen.ON_MEASURE_TRIGGER, 
                the measure_trigger propery will be ignored.
            transient_response (nidcpower.TransientResponse):
                Defines the transient response.
            voltage_gain_bandwidth (float):
                The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. 
                This property takes effect when the channel is in Constant Voltage mode. 
            voltage_compensation_frequency (float):
                The frequency at which a pole-zero pair is added to the system when the channel is in Constant Voltage mode. 
            voltage_pole_zero_ratio (float):
                The ratio of the pole frequency to the zero frequency when the channel is in Constant Voltage mode. 
            current_gain_bandwidth (float):
                The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. 
                This property takes effect when the channel is in Constant Current mode. 
            current_compensation_frequency (float):
                The frequency at which a pole-zero pair is added to the system when the channel is in Constant Current mode. 
            current_pole_zero_ratio (float):
                The ratio of the pole frequency to the zero frequency when the channel is in Constant Current mode. 


        """
        self._source_delay = source_delay
        self._aperture_time = aperture_time
        self._step_size = step_size
        self._measure_record_length = measure_record_length
        self._measure_when = measure_when
        self._transient_response = transient_response
        self._voltage_gain_bandwidth = voltage_gain_bandwidth
        self._voltage_compensation_frequency = voltage_compensation_frequency
        self._voltage_pole_zero_ratio = voltage_pole_zero_ratio
        self._current_gain_bandwidth = current_gain_bandwidth
        self._current_compensation_frequency = current_compensation_frequency
        self._current_pole_zero_ratio = current_pole_zero_ratio


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
    def step_size(self) -> float:
        """Gets the step size (time interval between samples).

        Returns:
            float: The step size in seconds.
        """
        return self._step_size

    @property
    def measure_record_length(self) -> int:
        """Gets the measure record length.

        Returns:
            int: Number of samples per record.
        """
        return self._measure_record_length

    @property
    def measure_when(self) -> nidcpower.MeasureWhen:
        """Gets the measure when setting.

        Returns:
            nidcpower.MeasureWhen: When measurements are taken.
        """
        return self._measure_when

    @property
    def transient_response(self) -> nidcpower.TransientResponse:
        """Gets the transient response setting.

        Returns:
            nidcpower.TransientResponse: The transient response mode.
        """
        return self._transient_response

    @property
    def voltage_gain_bandwidth(self) -> float:
        """Gets the voltage gain bandwidth.

        Returns:
            float: The voltage gain bandwidth in Hz.
        """
        return self._voltage_gain_bandwidth

    @property
    def voltage_compensation_frequency(self) -> float:
        """Gets the voltage compensation frequency.

        Returns:
            float: The voltage compensation frequency in Hz.
        """
        return self._voltage_compensation_frequency

    @property
    def voltage_pole_zero_ratio(self) -> float:
        """Gets the voltage pole-zero ratio.

        Returns:
            float: The voltage pole-zero ratio.
        """
        return self._voltage_pole_zero_ratio

    @property
    def current_gain_bandwidth(self) -> float:
        """Gets the current gain bandwidth.

        Returns:
            float: The current gain bandwidth in Hz.
        """
        return self._current_gain_bandwidth

    @property
    def current_compensation_frequency(self) -> float:
        """Gets the current compensation frequency.

        Returns:
            float: The current compensation frequency in Hz.
        """
        return self._current_compensation_frequency

    @property
    def current_pole_zero_ratio(self) -> float:
        """Gets the current pole-zero ratio.

        Returns:
            float: The current pole-zero ratio.
        """
        return self._current_pole_zero_ratio


class TriggerParameters:
    """Defines trigger parameters and event signal routing settings for
    a DC voltage source operation.
    """

    def __init__(
        self,
        source_trigger_behavior: SourceTriggerBehavior,
        source_trigger_edge: nidcpower.TriggerEdge,
        start_source_name: str,
        start_measure_name: str,
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
        self._source_trigger_edge = source_trigger_edge
        self._start_source_name = start_source_name
        self._start_measure_name = start_measure_name
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


class WaveformVoltageSourceAndMeasureParameters(PCBATestToolkitData):
    """Defines the full configuration for DC constant voltage source and measure operation."""

    def __init__(
        self,
        voltage_channel_settings: VoltageChannelSettings,
        execution_settings: ExecutionSettings,
        timing_parameters: TimingParameters,
        voltage_setpoints: list,
        # trigger_parameters: TriggerParameters,
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
            voltage_setpoints (list):
                List of voltage setpoints to be applied during the source and measure operation.
        """
        self._voltage_channel_settings = voltage_channel_settings
        self._execution_settings = execution_settings
        self._timing_parameters = timing_parameters
        self._voltage_setpoints = voltage_setpoints
        # self._trigger_parameters = trigger_parameters

    @property
    def voltage_channel_settings(self) -> VoltageChannelSettings:
        """Gets the voltage channel settings.

        Returns:
            VoltageChannelSettings: Configures the voltage level, current limit,
            sensing, and output enable settings.
        """
        return self._voltage_channel_settings

    @property
    def voltage_setpoints(self) -> list:
        """Gets the voltage setpoints.

        Returns:
            list: Voltage setpoints to apply as a sequence.
        """
        return self._voltage_setpoints

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


class WaveformVoltageSourceAndMeasureResultData(PCBATestToolkitData):
    """Defines the results obtained from a waveform DC voltage source and measure operation."""

    def __init__(
        self,
        execution_settings: dict,
        measurement_results: dict,
    ) -> None:
        """Initializes the DC voltage source and measure result data.

        Args:
            execution_settings (dict):
                Dictionary containing the applied hardware settings including voltage level,
                ranges, aperture time, device model, and output function.
                Fields are ``math.nan`` when configuration is not performed.
            measurement_results (dict):
                Dictionary containing the measured values including voltage, current,
                compliance state, power, and resistance.
                Fields are ``math.nan``/``False`` when measurement is not performed.
        """
        self._execution_settings = execution_settings
        self._measurement_results = measurement_results

    @property
    def execution_settings(self) -> dict:
        """Gets the applied hardware execution settings.

        Returns:
            dict: Applied hardware settings including voltage level, ranges, aperture time,
                device model, and output function.
        """
        return self._execution_settings

    @property
    def measurement_results(self) -> dict:
        """Gets the measurement results.

        Returns:
            dict: Measured values including voltage, current, compliance state, power,
                and resistance.
        """
        return self._measurement_results
