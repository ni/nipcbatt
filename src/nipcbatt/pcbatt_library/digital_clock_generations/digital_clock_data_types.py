""" digital clock data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (143 > 100 characters) (auto-generated noqa)

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalClockGenerationCounterChannelParameters(PCBATestToolkitData):
    """Defines the values to be used to set on the digital clock counter channel"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)

    def __init__(self, frequency_hertz: float, duty_cycle_ratio: float) -> None:
        """Creates an instance of DigitalClockGenerationCounterChannelParameters

        Args:
            frequency_hertz (float): The intended frequency to generate
            duty_cycle_ratio (float): Intended high time % of clock cycle
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._frequency_hertz

    @property
    def duty_cycle_ratio(self) -> float:
        """
        :type:float: Gets the duty cycle to generate
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._duty_cycle_ratio


class DigitalClockGenerationTimingParameters(PCBATestToolkitData):
    """Defines the timing values to be used in digital clock generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (185 > 100 characters) (auto-generated noqa)

    def __init__(self, clock_duration_seconds: float) -> None:
        """Creates an instance of DigitalClockGenerationTimingParameters

        Args:
            clock_duration_seconds (float): Clock generation time in seconds
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(clock_duration_seconds, nameof(clock_duration_seconds))
        Guard.is_greater_than_zero(clock_duration_seconds, nameof(clock_duration_seconds))

        # assign values
        self._clock_duration_seconds = clock_duration_seconds

    @property
    def clock_duration_seconds(self) -> float:
        """
        :type:float: Gets the length of the duration of the signal
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._clock_duration_seconds


class DigitalClockGenerationConfiguration(PCBATestToolkitData):
    """Defines values to be used in a digital clock generation configuration"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (190 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._counter_channel_parameters

    @property
    def timing_parameters(self) -> DigitalClockGenerationTimingParameters:
        """
        :type: DigitalClockGenerationTimingParameters: An instance of
            DigitalClockGenerationTimingParameters
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters


class DigitalClockGenerationData(PCBATestToolkitData):
    "Defines the data that was actually used during digital clock generation"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._timebase_frequency_hertz

    @property
    def actual_clock_frequency_hertz(self) -> float:
        """
        :type:float
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_clock_frequency_hertz

    @property
    def actual_clock_duty_cycle_ratio(self) -> float:
        """
        :type:float
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_clock_duty_cycle_ratio

    @property
    def actual_clock_duration_seconds(self) -> float:
        """
        :type:float
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._actual_clock_duration_seconds
