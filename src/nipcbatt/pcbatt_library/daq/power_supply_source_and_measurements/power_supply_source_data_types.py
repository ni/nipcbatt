""" Power supply source data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (149 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class PowerSupplySourceAndMeasureTerminalParameters(PCBATestToolkitData):
    """Defines parameters used for configuration of Power source and measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (195 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_setpoint_volts: float,
        current_setpoint_amperes: float,
        power_sense: nidaqmx.constants.Sense,
        idle_output_behaviour: nidaqmx.constants.PowerIdleOutputBehavior,
        enable_output: bool,
    ) -> None:
        """Initializes an instance of `PowerSupplySourceAndMeasureTerminalParameters'
        with specific values

        Args:
            voltage_setpoint_volts (float):
                The constant output voltage, in volts, to be set for the terminal.
            current_setpoint_amperes (float):
                The constant output current, in amperes, to be set for the terminal.
            power_sense (nidaqmx.constants.Sense):
                Specifies whether to use local or remote sense to sense the output voltage.
            idle_output_behaviour (nidaqmx.constants.PowerIdleOutputBehavior):
                Specifies whether to disable the output or
                maintain the existing value after the task is uncommitted.
            enable_output (bool):
                Specifies whether to enable or disable power module output.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._voltage_setpoint_volts = voltage_setpoint_volts
        self._current_setpoint_amperes = current_setpoint_amperes
        self._power_sense = power_sense
        self._idle_output_behaviour = idle_output_behaviour
        self._enable_output = enable_output

    @property
    def voltage_setpoint_volts(self) -> float:
        """
        :type:`float`:Gets the output voltage setpoint in volts for the terminal
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._voltage_setpoint_volts

    @property
    def current_setpoint_amperes(self) -> float:
        """
        :type:`float`:Gets the output current setpoint in amperes for the terminal
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._current_setpoint_amperes

    @property
    def power_sense(self) -> nidaqmx.constants.Sense:
        """
        :class:`nidaqmx.constants.Sense`:
            Gets the remote sense value configured for the power measurement
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._power_sense

    @property
    def idle_output_behaviour(self) -> nidaqmx.constants.PowerIdleOutputBehavior:
        """
        :class:`nidaqmx.constants.PowerIdleOutputBehavior`:
            Gets the idle output behaviour value configured for the power channels
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._idle_output_behaviour

    @property
    def enable_output(self) -> bool:
        """
        :type:`bool`:Gets if the output is enabled or disabled
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._enable_output


class PowerSupplySourceAndMeasureConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Power measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        terminal_parameters: PowerSupplySourceAndMeasureTerminalParameters,
        measurement_options: MeasurementOptions,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `PowerSupplySourceAndMeasureConfiguration` with specific values.

        Args:
            terminal_parameters (PowerSupplySourceAndMeasureTerminalParameters)
                The settings of terminal for all Power channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents
                the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters`
                that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.
        """  # noqa: D205, D415, D417, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (286 > 100 characters) (auto-generated noqa)
        self._measurement_options = measurement_options
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters
        self._terminal_parameters = terminal_parameters

    @property
    def terminal_parameters(self) -> PowerSupplySourceAndMeasureTerminalParameters:
        """
        :class: `PowerSupplySourceAndMeasureTerminalParameters`:
            Gets the settings of Power terminal for all the channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._terminal_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class PowerSupplySourceAndMeasureResultData(PCBATestToolkitData):
    """Defines the result values computed after analysing
    voltage and current waveforms from Power Supply Source."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (355 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_waveform: AnalogWaveform,
        current_waveform: AnalogWaveform,
        max_voltage_level_volts: float,
        max_current_level_amperes: float,
        max_power_level_watts: float,
        average_power_value_watts: float,
        acquisition_duration_seconds: float,
    ) -> None:
        """Constructor that initializes
        a new object of PowerSupplySourceAndMeasureResultData with specific values.

        Args:
            voltage_waveform (AnalogWaveform):
                A collection of samples representing the voltage values captured in the waveform.
            current_waveform (AnalogWaveform):
                A collection of samples representing the current values captured in the waveform.
            max_voltage_level_volts (float):
                The maximum voltage level value (in Volts).
            max_current_level_amperes (float):
                The maximum current level value (in Amperes).
            max_power_level_watts (float):
                The maximum power level value (in Watts).
            average_power_value_watts (float):
                The average power value (in Watts).
            acquisition_duration_seconds (float):
                The total acquisition time by the instrument in seconds.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(voltage_waveform, nameof(voltage_waveform))
        Guard.is_not_none(current_waveform, nameof(current_waveform))

        self._voltage_waveform = voltage_waveform
        self._current_waveform = current_waveform
        self._max_voltage_level_volts = max_voltage_level_volts
        self._max_current_level_amperes = max_current_level_amperes
        self._max_power_level_watts = max_power_level_watts
        self._average_power_value_watts = average_power_value_watts
        self._acquisition_duration_seconds = acquisition_duration_seconds

    @property
    def voltage_waveform(self) -> AnalogWaveform:
        """
        :class:`AnalogWaveform`:
            Gets the voltage waveforms acquired from channels defined
            for measurement and used to compute power measurements.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_waveform

    @property
    def current_waveform(self) -> AnalogWaveform:
        """
        :class:`AnalogWaveform`:
            Gets the current waveforms acquired from channels defined
            for measurement and used to compute power measurements.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._current_waveform

    @property
    def max_voltage_level_volts(self) -> float:
        """
        :type:`float`:
            Gets the maximum voltage level value (in Volts).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._max_voltage_level_volts

    @property
    def max_current_level_amperes(self) -> float:
        """
        :type:`float`:
            Gets the maximum current level value (in Amperes).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._max_current_level_amperes

    @property
    def max_power_level_watts(self) -> float:
        """
        :type:`float`:
            Gets the maximum power level value (in Watts).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._max_power_level_watts

    @property
    def average_power_value_watts(self) -> float:
        """
        :type:`float`:
            Gets the average power value (in Watts).
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._average_power_value_watts

    @property
    def acquisition_duration_seconds(self) -> float:
        """
        :type:`float`:
            Gets the duration of acquisition of samples for each of the power channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._acquisition_duration_seconds


class PowerSupplySourceAndMeasureData(PCBATestToolkitData):
    """
    Defines the voltage and current waveform acquired from power channels.
    """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        source_name: str,
        voltage_samples: numpy.ndarray,
        current_samples: numpy.ndarray,
        sampling_rate_hertz: int,
    ):
        """Initializes an instance of `PowerSupplySourceAndMeasureData`
           with specific values.

        Args:
            source_name (str): The name of channel on which waveform was captured.
            voltage_samples (numpy.ndarray): A collection of samples
            representing the voltage values captured in the waveform.
            Note: argument cannot be None or an empty array.

            current_samples (numpy.ndarray): A collection of samples
            representing the current values captured in the waveform.
            Note: argument cannot be None or an empty array.

            sampling_rate_hertz (int): The sampling rate (in Hz).
            Note: argument cannot be None or zero.

            voltage_samples, current_samples, and sampling_rate_hertz ca
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._source_name = source_name

        Guard.is_greater_than_zero(
            sampling_rate_hertz,
            nameof(sampling_rate_hertz),
        )
        self._sampling_rate_hertz = sampling_rate_hertz

        Guard.is_not_none(voltage_samples, nameof(voltage_samples))
        Guard.is_not_none(current_samples, nameof(current_samples))

        if numpy.size(voltage_samples) > 0:
            self._voltage_samples = voltage_samples
        else:
            raise ValueError("voltage_samples cannot be empty")

        if numpy.size(current_samples) > 0:
            self._current_samples = current_samples
        else:
            raise ValueError("current_samples cannot be empty")

    @property
    def source_name(self) -> str:
        """
        :type:`str`: Gets the name of channel on which waveform was captured.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._source_name

    @property
    def voltage_samples(self) -> numpy.ndarray:
        """
        :class:`numpy.ndarray`:
            Gets the array of samples from the voltage waveform.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_samples

    @property
    def current_samples(self) -> numpy.ndarray:
        """
        :class:`numpy.ndarray`:
            Gets the array of samples from the current waveform.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._current_samples

    @property
    def sampling_rate_hertz(self) -> int:
        """Gets the sampling rate (in Hz)."""
        return self._sampling_rate_hertz
