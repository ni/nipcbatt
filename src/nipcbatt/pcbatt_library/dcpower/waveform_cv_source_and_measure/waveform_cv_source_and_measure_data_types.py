"""Data types used for waveform constant voltage source and measurement on PCB points."""

from enum import Enum
from typing import List

import nidcpower

from nipcbatt.pcbatt_library.common.common_data_types import AnalogWaveform
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData

from nipcbatt.pcbatt_library.dcpower.common.common_data_types import (
    MeasurementExecutionType,
    EventSignalToExport,
    ExportEvent,
    TriggerParameters,
    SourceTriggerBehavior,
)

class WaveformExecutionSettings:
    def __init__(self, execution_type: MeasurementExecutionType, skip_analysis: bool) -> None:
            """Initializes the execution settings.
    
            Args:
                execution_type (MeasurementExecutionType):
                    The execution type having values:
                    - ``CONFIGURE_SOURCE_AND_MEASURE``,
                    - ``CONFIGURE_ONLY``,
                    - ``START_SOURCE_ONLY``, or
                    - ``MEASURE_ONLY``.
            """
            self._execution_type = execution_type
    
    @property
    def execution_type(self) -> MeasurementExecutionType:
        """Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The configured execution type.
        """
        return self._execution_type

class WaveformVoltageChannelSettings:
    """Defines the voltage level, current limit, sensing, and output enable
    settings for a channel.
    """

    def __init__(
        self,
        voltage_level_range: float,
        current_limit_range: float,
        current_limit: float,
        step_time: float,
        sensing: nidcpower.Sense,
        enable_output: bool,
        voltage_setpoints: list,
    ) -> None:
        """Initializes the voltage channel settings.

        Args:
            voltage_level_range (float):
                The voltage level range setting, in volts.
            current_limit (float):
                The current limit for the output, in amperes.
            current_limit_range (float):
                The current limit range setting, in amperes.
            step_time (float):
                The duration of each voltage setpoint step, in seconds.
            sensing (nidcpower.Sense):
                The sensing mode (``LOCAL`` or ``REMOTE``) for voltage measurement.
            enable_output (bool):
                Whether the channel output is enabled.
            voltage_setpoints (list):
                List of voltage setpoints, in volts, to be applied as a sequence during
                the source and measure operation.
        """
        self._voltage_level_range = voltage_level_range
        self._current_limit_range = current_limit_range
        self._current_limit = current_limit
        self._step_time = step_time
        self._sensing = sensing
        self._enable_output = enable_output
        self._voltage_setpoints = voltage_setpoints

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

        Returns:i
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
    def step_time(self) -> float:
        """Gets the duration of each voltage setpoint step.

        Returns:
            float: The step time in seconds.
        """
        return self._step_time

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

    @property
    def voltage_setpoints(self) -> list:
        """Gets the voltage setpoints.

        Returns:
            list: Voltage setpoints, in volts, to apply as a sequence.
        """
        return self._voltage_setpoints


class WaveformTimingParameters:
    """Defines timing settings for waveform constant voltage source and measure."""

    def __init__(
        self,
        source_delay: float,
        aperture_time: float,
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

class WaveformVoltageSourceAndMeasureParameters(PCBATestToolkitData):
    """Defines the full configuration for DC constant voltage source and measure operation."""

    def __init__(
        self,
        voltage_channel_settings: WaveformVoltageChannelSettings,
        execution_settings: WaveformExecutionSettings,
        timing_parameters: WaveformTimingParameters,
        trigger_parameters: TriggerParameters,
    ) -> None:
        """Initializes the DC voltage source and measure parameters.

        Args:
            voltage_channel_settings (WaveformVoltageChannelSettings):
                Voltage level, current limit, sensing mode, output enable, step time,
                and voltage setpoints settings.
            execution_settings (WaveformExecutionSettings):
                Execution mode and analysis control settings.
            timing_parameters (WaveformTimingParameters):
                Source delay, aperture time, and transient response settings.
            trigger_parameters (TriggerParameters):
                Source trigger input and event signal routing settings.
        """
        self._voltage_channel_settings = voltage_channel_settings
        self._execution_settings = execution_settings
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def voltage_channel_settings(self) -> WaveformVoltageChannelSettings:
        """Gets the voltage channel settings.

        Returns:
            WaveformVoltageChannelSettings: Configures the voltage level, current limit,
            sensing, output enable, step time, and voltage setpoints settings.
        """
        return self._voltage_channel_settings

    @property
    def execution_settings(self) -> WaveformExecutionSettings:
        """Gets the execution settings.

        Returns:
            WaveformExecutionSettings: Configures the execution mode and skip analysis settings.
        """
        return self._execution_settings

    @property
    def timing_parameters(self) -> WaveformTimingParameters:
        """Gets the timing parameters.

        Returns:
            WaveformTimingParameters: Configures the source delay, aperture time, and transient
            response settings.
        """
        return self._timing_parameters

    @property
    def trigger_parameters(self) -> TriggerParameters:
        """Gets the trigger parameters.

        Returns:
            TriggerParameters: Configures the source trigger input and event signal routing settings.
        """
        return self._trigger_parameters
    
class WaveformVoltageSourceAndMeasureResultData(PCBATestToolkitData):
    """Defines the results obtained from a waveform DC voltage source and measure operation."""

    def __init__(
        self,
        execution_settings: dict,
        voltage_waveform: List[AnalogWaveform],
        current_waveform: List[AnalogWaveform],
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
        self._voltage_waveform = voltage_waveform
        self._current_waveform = current_waveform

    @property
    def execution_settings(self) -> dict:
        """Gets the applied hardware execution settings.

        Returns:
            dict: Applied hardware settings including voltage level, ranges, aperture time,
                device model, and output function.
        """
        return self._execution_settings

    @property
    def voltage_waveform(self) -> List[AnalogWaveform]:
        """Gets the measured voltage waveform.

        Returns:
            List[AnalogWaveform]: Measured voltage waveform data.
        """
        return self._voltage_waveform   

    @property
    def current_waveform(self) -> List[AnalogWaveform]:     
        """Gets the measured current waveform.

        Returns:
            List[AnalogWaveform]: Measured current waveform data.
        """
        return self._current_waveform

