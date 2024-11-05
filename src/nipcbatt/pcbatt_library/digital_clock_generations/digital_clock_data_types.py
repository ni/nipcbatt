""" digital clock data types """

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalClockGenerationCounterChannelParameters(PCBATestToolkitData):
    """Defines the values to be used to set on the digital clock counter channel"""

    def __init__(self, frequency_hertz: float, duty_cycle_ratio: float) -> None:
        """Creates an instance of DigitalClockGenerationCounterChannelParameters

        Args:
            frequency_hertz (float): The intended frequency to generate
            duty_cycle_ratio (float): Intended high time % of clock cycle
        """

        # input validation
        Guard.is_not_none(frequency_hertz, nameof(frequency_hertz))
        Guard.is_greater_than_or_equal_to_zero(frequency_hertz, nameof(frequency_hertz))

        Guard.is_not_none(duty_cycle_ratio, nameof(duty_cycle_ratio))
        Guard.is_greater_than_or_equal_to_zero(duty_cycle_ratio, nameof(duty_cycle_ratio))
        Guard.is_less_than_or_equal_to(duty_cycle_ratio, 1.0, nameof(duty_cycle_ratio))

        # assign values
        self._frequency_hertz = frequency_hertz
        self._duty_cycle_ratio = duty_cycle_ratio

    @property
    def frequency_hertz(self) -> float:
        """
        :type:'float': Gets the frequency to generate
        """
        return self._frequency_hertz

    @property
    def duty_cycle_ratio(self) -> float:
        """
        :type:float: Gets the duty cycle to generate
        """
        return self._duty_cycle_ratio


class DigitalClockGenerationTimingParameters(PCBATestToolkitData):
    """Defines the timing values to be used in digital clock generation"""

    def __init__(self, clock_duration_seconds: float) -> None:
        """Creates an instance of DigitalClockGenerationTimingParameters

        Args:
            clock_duration_seconds (float): Clock generation time in seconds
        """

        # input validation
        Guard.is_not_none(clock_duration_seconds, nameof(clock_duration_seconds))
        Guard.is_greater_than_zero(clock_duration_seconds, nameof(clock_duration_seconds))

        # assign values
        self._clock_duration_seconds = clock_duration_seconds

    @property
    def clock_duration_seconds(self) -> float:
        """
        :type:float: Gets the length of the duration of the signal
        """
        return self._clock_duration_seconds


class DigitalClockGenerationConfiguration(PCBATestToolkitData):
    """Defines values to be used in a digital clock generation configuration"""

    def __init__(
        self,
        counter_channel_parameters: DigitalClockGenerationCounterChannelParameters,
        timing_parameters: DigitalClockGenerationTimingParameters,
    ) -> None:
        """Creates an instance of DigitalClockGenerationConfiguration

        Args:
            counter_channel_parameters (DigitalClockGenerationCounterChannelParameters): An
                instance of DigitalClockGenerationCounterChannelParameters
            timing_parameters (DigitalClockGenerationTimingParameters): An instance of
                DigitalClockGenerationTimingParameters
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
    ) -> DigitalClockGenerationCounterChannelParameters:
        """
        :type:DigitalClockGenerationCounterChannelParameters: An instance of
            DigitalClockGenerationCounterChannelParameters
        """
        return self._counter_channel_parameters

    @property
    def timing_parameters(self) -> DigitalClockGenerationTimingParameters:
        """
        :type: DigitalClockGenerationTimingParameters: An instance of
            DigitalClockGenerationTimingParameters
        """
        return self._timing_parameters


class DigitalClockGenerationData(PCBATestToolkitData):
    "Defines the data that was actually used during digital clock generation"

    def __init__(
        self,
        timebase_frequency_hertz: float,
        actual_clock_frequency_hertz: float,
        actual_clock_duty_cycle_ratio: float,
        actual_clock_duration_seconds: float,
    ) -> None:
        """Creates an instance of DigitalClockGenerationData

        Args:
            timebase_frequency_hertz (float): The timebase used during generation
            actual_clock_frequency_hertz (float): Actual clock frequency used during generation
            actual_clock_duty_cycle_ratio (float): Actual duty cycle used during generation
            actual_clock_duration_seconds (float): Actual clock duration implemented in generation
        """

        # input validation
        Guard.is_not_none(timebase_frequency_hertz, nameof(timebase_frequency_hertz))
        Guard.is_greater_than_zero(timebase_frequency_hertz, nameof(timebase_frequency_hertz))

        Guard.is_not_none(actual_clock_frequency_hertz, nameof(actual_clock_frequency_hertz))
        Guard.is_greater_than_zero(
            actual_clock_frequency_hertz, nameof(actual_clock_frequency_hertz)
        )

        Guard.is_not_none(actual_clock_duty_cycle_ratio, nameof(actual_clock_duty_cycle_ratio))
        Guard.is_greater_than_or_equal_to_zero(
            actual_clock_duty_cycle_ratio, nameof(actual_clock_duty_cycle_ratio)
        )

        Guard.is_not_none(actual_clock_duration_seconds, nameof(actual_clock_duration_seconds))
        Guard.is_greater_than_or_equal_to_zero(
            actual_clock_duration_seconds, nameof(actual_clock_duration_seconds)
        )

        # assign values
        self._timebase_frequency_hertz = timebase_frequency_hertz
        self._actual_clock_frequency_hertz = actual_clock_frequency_hertz
        self._actual_clock_duty_cycle_ratio = actual_clock_duty_cycle_ratio
        self._actual_clock_duration_seconds = actual_clock_duration_seconds

    @property
    def timebase_frequency_hertz(self) -> float:
        """
        :type:float:
        """
        return self._timebase_frequency_hertz

    @property
    def actual_clock_frequency_hertz(self) -> float:
        """
        :type:float
        """
        return self._actual_clock_frequency_hertz

    @property
    def actual_clock_duty_cycle_ratio(self) -> float:
        """
        :type:float
        """
        return self._actual_clock_duty_cycle_ratio

    @property
    def actual_clock_duration_seconds(self) -> float:
        """
        :type:float
        """
        return self._actual_clock_duration_seconds
