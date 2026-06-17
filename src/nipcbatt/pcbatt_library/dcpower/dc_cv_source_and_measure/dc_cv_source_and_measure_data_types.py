"""Data types used for DC constant voltage source and measurement on PCB points."""

import nidcpower

from nipcbatt.pcbatt_library.dcpower.common.common_data_types import (
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData

__all__ = [
    "EventSignalToExport",
    "ExecutionSettings",
    "ExportEvent",
    "MeasurementExecutionType",
    "SourceTriggerBehavior",
    "TimingParameters",
    "TriggerParameters",
    "VoltageChannelSettings",
    "DCVoltageSourceAndMeasureParameters",
    "DCVoltageSourceAndMeasureResultData",
]


class VoltageChannelSettings:
    """Defines the voltage level, current limit, sensing, and output enable
    settings for a channel.
    """

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


class DCVoltageSourceAndMeasureParameters(PCBATestToolkitData):
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
            VoltageChannelSettings: Configures the voltage level, current limit,
            sensing, and output enable settings.
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


class DCVoltageSourceAndMeasureResultData(PCBATestToolkitData):
    """Defines the results obtained from a DC constant voltage source and measure operation."""

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
