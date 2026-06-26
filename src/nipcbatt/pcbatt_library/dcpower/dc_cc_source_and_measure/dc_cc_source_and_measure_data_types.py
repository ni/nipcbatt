"""Data types used for DC constant current source and measurement on PCB points."""

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
    "CurrentChannelSettings",
    "DCCurrentSourceAndMeasureParameters",
    "DCCurrentSourceAndMeasureResultData",
]


class CurrentChannelSettings:
    """Defines the current level, voltage limit, sensing, and output enable
    settings for a channel.
    """

    def __init__(
        self,
        current_level: float,
        current_level_range: float,
        voltage_limit: float,
        voltage_limit_range: float,
        sensing: nidcpower.Sense,
        enable_output: bool,
    ) -> None:
        """Initializes the current channel settings.

        Args:
            current_level (float):
                The DC current level to source, in amperes.
            current_level_range (float):
                The current level range setting, in amperes.
            voltage_limit (float):
                The voltage limit for the output, in volts.
            voltage_limit_range (float):
                The voltage limit range setting, in volts.
            sensing (nidcpower.Sense):
                The sensing mode (``LOCAL`` or ``REMOTE``) for voltage measurement.
            enable_output (bool):
                Whether the channel output is enabled.
        """
        self._current_level = current_level
        self._current_level_range = current_level_range
        self._voltage_limit = voltage_limit
        self._voltage_limit_range = voltage_limit_range
        self._sensing = sensing
        self._enable_output = enable_output

    @property
    def current_level(self) -> float:
        """Gets the DC current level to source.

        Returns:
            float: The current level in amperes.
        """
        return self._current_level

    @property
    def current_level_range(self) -> float:
        """Gets the current level range.

        Returns:
            float: The current level range in amperes.
        """
        return self._current_level_range

    @property
    def voltage_limit(self) -> float:
        """Gets the voltage limit for the output.

        Returns:
            float: The voltage limit in volts.
        """
        return self._voltage_limit

    @property
    def voltage_limit_range(self) -> float:
        """Gets the voltage limit range.

        Returns:
            float: The voltage limit range in volts.
        """
        return self._voltage_limit_range

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


class DCCurrentSourceAndMeasureParameters(PCBATestToolkitData):
    """Defines the full configuration for DC constant current source and measure operation."""

    def __init__(
        self,
        current_channel_settings: CurrentChannelSettings,
        execution_settings: ExecutionSettings,
        timing_parameters: TimingParameters,
        trigger_parameters: TriggerParameters,
    ) -> None:
        """Initializes the DC current source and measure parameters.

        Args:
            current_channel_settings (CurrentChannelSettings):
                Current level, voltage limit, sensing mode, and output enable settings.
            execution_settings (ExecutionSettings):
                Execution mode and analysis control settings.
            timing_parameters (TimingParameters):
                Source delay, aperture time, and transient response settings.
            trigger_parameters (TriggerParameters):
                Source trigger input and event signal routing settings.
        """
        self._current_channel_settings = current_channel_settings
        self._execution_settings = execution_settings
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def current_channel_settings(self) -> CurrentChannelSettings:
        """Gets the current channel settings.

        Returns:
            CurrentChannelSettings: Configures the current level, voltage limit,
            sensing, and output enable settings.
        """
        return self._current_channel_settings

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


class DCCurrentSourceAndMeasureResultData(PCBATestToolkitData):
    """Defines the results obtained from a DC constant current source and measure operation."""

    def __init__(
        self,
        execution_settings: dict,
        measurement_results: dict,
    ) -> None:
        """Initializes the DC current source and measure result data.

        Args:
            execution_settings (dict):
                Dictionary containing the applied hardware settings including current level,
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
            dict: Applied hardware settings including current level, ranges, aperture time,
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
