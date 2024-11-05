""" digital PWM data types """

import nidaqmx.constants
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalPwmMeasurementRangeParameters(PCBATestToolkitData):
    """Defines the range between minimum and maximum pulse width"""

    def __init__(
        self,
        semi_period_minimum_value_seconds: float = 20e-9,
        semi_period_maximum_value_seconds: float = 42.949672,
    ) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementRangeParameters'
           with the values provided in the arguments

        Args:
            semi_period_minimum_value_seconds (float):
                Minimum length of pwm semi-period
            semi_period_maximum_value_seconds (float):
                Maximum length of pwm semi-period

        Raises: ValueError when,
            1) The value of semi_period_minimum_value_seconds is less than or equal to zero
            2) The value of semi_period_maximum_value_seconds is less than or eqaul to zero
            3) semi_period_maximum_value_seconds < semi_period_minimum_value_seconds
        """

        # input validation
        Guard.is_not_none(
            semi_period_minimum_value_seconds, nameof(semi_period_minimum_value_seconds)
        )

        Guard.is_not_none(
            semi_period_maximum_value_seconds, nameof(semi_period_maximum_value_seconds)
        )

        Guard.is_less_than_or_equal_to(
            semi_period_minimum_value_seconds,
            semi_period_maximum_value_seconds,
            nameof(semi_period_minimum_value_seconds),
        )

        Guard.is_greater_than_or_equal_to_zero(
            semi_period_minimum_value_seconds, nameof(semi_period_minimum_value_seconds)
        )

        Guard.is_greater_than_or_equal_to_zero(
            semi_period_maximum_value_seconds, nameof(semi_period_maximum_value_seconds)
        )

        # assign member variables
        self._semi_period_minimum_value_seconds = semi_period_minimum_value_seconds
        self._semi_period_maximum_value_seconds = semi_period_maximum_value_seconds

    @property
    def semi_period_minimum_value_seconds(self) -> float:
        """
        :type:'float': Gets the minimum semi period value in seconds
        """
        return self._semi_period_minimum_value_seconds

    @property
    def semi_period_maximum_value_seconds(self) -> float:
        """
        :type:'float': Gets the minimum semi period value in seconds
        """
        return self._semi_period_maximum_value_seconds


class DigitalPwmMeasurementTimingParameters(PCBATestToolkitData):
    """Defines the desired number of cycles to capture"""

    def __init__(self, semi_period_counter_wanted_cycles_count: int = 2) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementTimingParameters'
           with the values provided in the arguments

        Args:
            semi_period_counter_wanted_cycles_count(int):
                The desired number of cycles to capture

        Raises: ValueError when,
            1) The value of semi_period_counter_wanted_cycles_count is less than zero
            2) The value of semi_period_maximum_value_seconds is more than 2147483647
            3) The value of semi_period_counter_wanted_cycles_count does not exist (null)
        """

        # input validation
        Guard.is_not_none(
            semi_period_counter_wanted_cycles_count,
            nameof(semi_period_counter_wanted_cycles_count),
        )

        Guard.is_greater_than_or_equal_to_zero(
            semi_period_counter_wanted_cycles_count,
            nameof(semi_period_counter_wanted_cycles_count),
        )

        Guard.is_less_than_or_equal_to(
            semi_period_counter_wanted_cycles_count,
            2147483647,
            nameof(semi_period_counter_wanted_cycles_count),
        )

        # assign member variable
        self._semi_period_counter_wanted_cycles_count = semi_period_counter_wanted_cycles_count

    @property
    def semi_period_counter_wanted_cycles_count(self) -> int:
        """
        :type:'int': Gets the desired number of cycles to capture
        """
        return self._semi_period_counter_wanted_cycles_count


class DigitalPwmMeasurementCounterChannelParameters(PCBATestToolkitData):
    """Holds all of the parameters for creating a PWM measurement"""

    def __init__(
        self,
        range_parameters: DigitalPwmMeasurementRangeParameters,
        timing_parameters: DigitalPwmMeasurementTimingParameters,
        semi_period_counter_starting_edge: nidaqmx.constants.Edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE,
    ) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementCounterChannelParameters'
           with the values provided in the arguments

        Args:
            range_parameters(DigitalPwmMeasurementRangeParameters):
                An instance of DigitalPwmMeasurementRangeParameters
            timing_parameters(DigitalPwmMeasurementTimingParameters):
                An instance of DigitalPwmMeasurementTimingParameters
            semi_period_counter_starting_edge:
                Constant value representing the starting edge

        Raises: ValueError when,
            1) The value of range_parameters is None
            2) The value of timing_parameters is None
            3) The value of semi_period_counter_starting_edge is None"""

        # input validation
        Guard.is_not_none(range_parameters, nameof(range_parameters))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))
        Guard.is_not_none(
            semi_period_counter_starting_edge, nameof(semi_period_counter_starting_edge)
        )

        # assign member variables
        self._range_parameters = range_parameters
        self._timing_parameters = timing_parameters
        self._semi_period_counter_starting_edge = semi_period_counter_starting_edge

    @property
    def range_parameters(self) -> DigitalPwmMeasurementRangeParameters:
        """
        :type:DigitalPwmMeasurementRangeParamters: The range parameters of the measurement
        """
        return self._range_parameters

    @property
    def timing_parameters(self) -> DigitalPwmMeasurementTimingParameters:
        """
        :type:DigitalPwmMeasurementTimingParameters: The timing parameters of the measurement
        """
        return self._timing_parameters

    @property
    def semi_period_counter_starting_edge(self) -> int:
        """
        :type:Constant int:The starting edge for the measurement
        """
        return self._semi_period_counter_starting_edge


class DigitalPwmMeasurementConfiguration(PCBATestToolkitData):
    """Defines values for the configuration of a digital pwm measurement"""

    def __init__(
        self,
        parameters: DigitalPwmMeasurementCounterChannelParameters,
        measurement_option: MeasurementExecutionType = MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    ) -> None:
        """Creates an instance of DigitalPwmMeasurementConfiguration

        Args:
            parameters (DigitalPwmMeasurementCounterChannelParameters):
                A valid instance of DigitalPwmMeasurementCounterChannelParameters
            measurement_options (MeasurementExecutionType):
                A valid instance of MeasurementExecutionType
        """

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))
        Guard.is_not_none(measurement_option, nameof(measurement_option))

        # assign to member properties
        self._parameters = parameters
        self._measurement_option = measurement_option

    @property
    def parameters(self) -> DigitalPwmMeasurementCounterChannelParameters:
        """
        :type:DigitalPwmMeasurementCounterChannelParameters: Contains data
        range and timing parameters
        """
        return self._parameters

    @property
    def measurement_option(self) -> MeasurementExecutionType:
        """
        :type:MeasurmentExecutionType: Contains the type of execution
        """
        return self._measurement_option


class DigitalPwmMeasurementData(PCBATestToolkitData):
    """Defines the values returned from the capture"""

    def __init__(self, data: np.ndarray) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementData'
        with specific values

        Args:
            data: Numpy ndarray

        Raises: ValueError when,
            1) data is empty
            2) data is None
        """

        # input validation
        Guard.is_not_none(data, nameof(data))
        Guard.is_not_empty(data, nameof(data))

        # assign to member variable
        self._data = data

    @property
    def data(self) -> np.ndarray:
        """
        :type:'numpy.ndarray': Data captured from the measurement
        """
        return self._data


class DigitalPwmMeasurementResultData(PCBATestToolkitData):
    """Defines the values returned by a digital PWM measurement"""

    def __init__(
        self,
        actual_cycles_count: int,
        duty_cycle: float,
        period_duration: float,
        frequency: float,
        high_state_duration: float,
        low_state_duration: float,
    ) -> None:
        """Initializes an instance of 'DigitalPwmMeasurementResultData'
           with specific values

        Args:
            actual_cycles_count (int):
                The actual number of cycles measured
            duty_cycle (float):
                The measured duty cycle within the pwm measurement
            period_duration(float):
                The length of each period
            frequency(float):
                The measured frequency
            high_state_duration(float):
                The length of the high state
            low_state_duration(float):
                The length of the low state

        Raises: ValueError when,
            1) The value of actual_cycles_count is None or is < 0
            2) The value of duty_cycle is None or is < 0
            3) The value of period duration is None or is < 0
            4) The value of frequency is None or is < 0
            5) The value of high_state_duration is None or is < 0
            6) THe value of low_state_duration is None or is < 0
        """

        # input validation
        Guard.is_not_none(actual_cycles_count, nameof(actual_cycles_count))
        Guard.is_greater_than_or_equal_to_zero(actual_cycles_count, nameof(actual_cycles_count))

        Guard.is_not_none(duty_cycle, nameof(duty_cycle))
        Guard.is_greater_than_or_equal_to_zero(duty_cycle, nameof(duty_cycle))
        Guard.is_less_than_or_equal_to(duty_cycle, 1.0, nameof(duty_cycle))

        Guard.is_not_none(period_duration, nameof(period_duration))
        Guard.is_greater_than_or_equal_to_zero(period_duration, nameof(period_duration))

        Guard.is_not_none(frequency, nameof(frequency))
        Guard.is_greater_than_or_equal_to_zero(frequency, nameof(frequency))

        Guard.is_not_none(high_state_duration, nameof(high_state_duration))
        Guard.is_greater_than_or_equal_to_zero(high_state_duration, nameof(high_state_duration))

        Guard.is_not_none(low_state_duration, nameof(low_state_duration))
        Guard.is_greater_than_or_equal_to_zero(low_state_duration, nameof(low_state_duration))

        # assign to member variables
        self._actual_cycles_count = actual_cycles_count
        self._duty_cycle = duty_cycle
        self._period_duration = period_duration
        self._frequency = frequency
        self._high_state_duration = high_state_duration
        self._low_state_duration = low_state_duration

    @property
    def actual_cycles_count(self) -> int:
        """
        :type:'int': Gets the number of cycles
        """
        return self._actual_cycles_count

    @property
    def duty_cycle(self) -> float:
        """
        :type:'float': Gets the measured duty cycle
        """
        return self._duty_cycle

    @property
    def period_duration(self) -> float:
        """
        :type:'float': Gets the length of the period
        """
        return self._period_duration

    @property
    def frequency(self) -> float:
        """
        :type:'float': Gets the measured frequency
        """
        return self._frequency

    @property
    def high_state_duration(self) -> float:
        """
        :type:'float': Gets the length of the high state
        """
        return self._high_state_duration

    @property
    def low_state_duration(self) -> float:
        """
        :type:'float': Gets the length of the low state
        """
        return self._low_state_duration
