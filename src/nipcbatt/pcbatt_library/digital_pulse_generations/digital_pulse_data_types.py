""" Digital pulse data types """

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_constants import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalPulseGenerationCounterChannelParameters(PCBATestToolkitData):
    """Defines the counter channel parameters used for digital pulse generation"""

    def __init__(
        self,
        pulse_idle_state: nidaqmx.constants.Level = ConstantsForDigitalPulseGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT,
        low_time_seconds: float = 0.01,
        high_time_seconds: float = 0.01,
    ) -> None:
        """Creates an instance of DigitalPulseGenerationCounterChannelParameters

        Args:
            pulse_idle_state (Constant state): The intended idle state of the generation
            low_time_seconds (float): The intended duration of the low time of the pulse
            high_time_seconds (float): The intended duration of the high time of the pulse
        """

        # input validation
        Guard.is_not_none(pulse_idle_state, nameof(pulse_idle_state))

        Guard.is_not_none(low_time_seconds, nameof(low_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(low_time_seconds, nameof(low_time_seconds))
        Guard.is_float(low_time_seconds, nameof(low_time_seconds))

        Guard.is_not_none(high_time_seconds, nameof(high_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(high_time_seconds, nameof(high_time_seconds))
        Guard.is_float(high_time_seconds, nameof(high_time_seconds))

        # assign values
        self._pulse_idle_state = pulse_idle_state
        self._low_time_seconds = low_time_seconds
        self._high_time_seconds = high_time_seconds

    @property
    def pulse_idle_state(self) -> nidaqmx.constants.Level:
        """
        :type:'nidaqmx.constants.Level': The idle state of the pulse generation
        """
        return self._pulse_idle_state

    @property
    def low_time_seconds(self) -> float:
        """
        :type:float: The low time of the pulse
        """
        return self._low_time_seconds

    @property
    def high_time_seconds(self) -> float:
        """
        :type:float: The high time of the pulse
        """
        return self._high_time_seconds


class DigitalPulseGenerationTimingParameters(PCBATestToolkitData):
    """Defines the pulses count used in digital pulse generation"""

    def __init__(self, pulses_count: int) -> None:
        """Creates an instance of DigitalPulseGenerationTimingParameters

        Args: pulses_count (int): The number of pulses to generate
        """

        # input validation
        Guard.is_not_none(pulses_count, nameof(pulses_count))
        Guard.is_greater_than_or_equal_to_zero(pulses_count, nameof(pulses_count))
        Guard.is_int(pulses_count, nameof(pulses_count))

        # assign values
        self._pulses_count = pulses_count

    @property
    def pulses_count(self) -> int:
        """
        :type:int: Gets the number of pulses to generate
        """
        return self._pulses_count


class DigitalPulseGenerationConfiguration(PCBATestToolkitData):
    """Defines a configuration for digital pulse generation"""

    def __init__(
        self,
        counter_channel_parameters: DigitalPulseGenerationCounterChannelParameters,
        timing_parameters: DigitalPulseGenerationTimingParameters,
    ) -> None:
        """Creates an instance of DigitalPulseGenerationConfiguration

        Args:
            counter_channel_parameters:
                An valid instance of DigitalPulseGenerationCounterChannelParameters
            timing_parameters:
                An valid instance of DigitalPulseGenerationTimingParameters
        """

        # input validation
        Guard.is_not_none(counter_channel_parameters, nameof(counter_channel_parameters))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))

        # assign values
        self._counter_channel_parameters = counter_channel_parameters
        self._timing_parameters = timing_parameters

    @property
    def counter_channel_parameters(
        self,
    ) -> DigitalPulseGenerationCounterChannelParameters:
        """
        :type:DigitalPulseGenerationCounterChannelParameters: The instance of
            DigitalPulseGenerationCounterChannelParameters used for digital pulse generation
        """
        return self._counter_channel_parameters

    @property
    def timing_parameters(self) -> DigitalPulseGenerationTimingParameters:
        """
        :type:DigitalPulseGenerationTimingParameters: The instance of
            DigitalPulseGenerationTimingParameters used for digital pulse generation
        """
        return self._timing_parameters


class DigitalPulseGenerationData(PCBATestToolkitData):
    """Returns the values actually written to the hardware"""

    def __init__(
        self,
        timebase_frequency_hertz: float,
        actual_pulse_train_duration_seconds: float,
        actual_pulse_low_time_seconds: float,
        actual_pulse_high_time_seconds: float,
    ) -> None:
        """Creates an instance of DigitalPulseGenerationData"""

        # input validation
        Guard.is_not_none(timebase_frequency_hertz, nameof(timebase_frequency_hertz))
        Guard.is_greater_than_or_equal_to_zero(
            timebase_frequency_hertz, nameof(timebase_frequency_hertz)
        )
        Guard.is_float(timebase_frequency_hertz, nameof(timebase_frequency_hertz))

        Guard.is_not_none(
            actual_pulse_train_duration_seconds,
            nameof(actual_pulse_train_duration_seconds),
        )
        Guard.is_greater_than_or_equal_to_zero(
            actual_pulse_train_duration_seconds,
            nameof(actual_pulse_train_duration_seconds),
        )
        Guard.is_float(
            actual_pulse_train_duration_seconds,
            nameof(actual_pulse_train_duration_seconds),
        )

        Guard.is_not_none(actual_pulse_low_time_seconds, nameof(actual_pulse_low_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(
            actual_pulse_low_time_seconds, nameof(actual_pulse_low_time_seconds)
        )
        Guard.is_float(actual_pulse_low_time_seconds, nameof(actual_pulse_low_time_seconds))

        Guard.is_not_none(actual_pulse_high_time_seconds, nameof(actual_pulse_high_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(
            actual_pulse_high_time_seconds, nameof(actual_pulse_high_time_seconds)
        )
        Guard.is_float(actual_pulse_high_time_seconds, nameof(actual_pulse_high_time_seconds))

        # assign values
        self._timebase_frequency_hertz = timebase_frequency_hertz
        self._actual_pulse_train_duration_seconds = actual_pulse_train_duration_seconds
        self._actual_pulse_low_time_seconds = actual_pulse_low_time_seconds
        self._actual_pulse_high_time_seconds = actual_pulse_high_time_seconds

    @property
    def timebase_frequency_hertz(self) -> float:
        """
        :type:float: The timebase frequecy used to generate the pulse(s)
        """
        return self._timebase_frequency_hertz

    @property
    def actual_pulse_train_duration_seconds(self) -> float:
        """
        :type:float: The actual pulse train duration written to the hardware
        """
        return self._actual_pulse_train_duration_seconds

    @property
    def actual_pulse_low_time_seconds(self) -> float:
        """
        :type:float: The actual pulse low time written to the hardware
        """
        return self._actual_pulse_low_time_seconds

    @property
    def actual_pulse_high_time_seconds(self) -> float:
        """
        :type:float: The actual pulse high time written to the hardware
        """
        return self._actual_pulse_high_time_seconds
