# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Use this class for digital pulse width modulation measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)
import nidaqmx.constants
import nidaqmx.stream_readers
import nidaqmx.stream_writers
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_data_types import (
    DigitalPwmMeasurementConfiguration,
    DigitalPwmMeasurementCounterChannelParameters,
    DigitalPwmMeasurementData,
    DigitalPwmMeasurementResultData,
    DigitalPwmMeasurementTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

# when class are defined in module change to
# from digital_pwm_data_types import ...


class DigitalPwmMeasurement(BuildingBlockUsingDAQmx):
    """Class for performing a digital pulse width modulation measurement

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        channel_expression: str,
        input_terminal_name: str,
    ) -> None:
        """Creates an instance of the DigitalPwmMeasurement class

        Args:
            channel_expression (str): The physical channel being measured
            input_terminal_name (str): The name of the paticular input terminal
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # Here implement initialization of task.
        # input validation on channel expression and terminal
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))
        Guard.is_not_none(input_terminal_name, nameof(input_terminal_name))
        Guard.is_not_empty(input_terminal_name, nameof(input_terminal_name))

        # constants used for initialization
        min_semiperiod = ConstantsForDigitalPwmMeasurement.DEFAULT_MIN_SEMIPERIOD
        max_semiperiod = ConstantsForDigitalPwmMeasurement.DEFAULT_MAX_SEMIPERIOD
        default_units = ConstantsForDigitalPwmMeasurement.DEFAULT_TIME_UNITS

        # check to see if task has only global channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

        else:
            # create virtual channel for clock generation
            self.task.ci_channels.add_ci_semi_period_chan(
                counter=channel_expression,
                name_to_assign_to_channel="",
                min_val=min_semiperiod,
                max_val=max_semiperiod,
                units=default_units,
            )

        # raise execption if more than one channel is present
        if self.task.number_of_channels and self.task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set input terminal
        self.task.channels.ci_semi_period_term = input_terminal_name

        # reserve counter and terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_counter_channel(
        self, parameters: DigitalPwmMeasurementCounterChannelParameters
    ) -> None:
        """This method uses the semi_period values within the
            DigitalPwmMeasurementCounterChannelParameters argument provided to set
            the configuration for the counter channel

        Args:
            parameters (DigitalPwmMeasurementCounterChannelParameters):
                An instance of DigitalPwmMeasurementCounterChannelParameters
                with correct values
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # stop daq task and return it to previous state
        self.task.stop()

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set channel parameters
        self.task.channels.ci_semi_period_starting_edge = (
            parameters.semi_period_counter_starting_edge
        )
        self.task.channels.ci_max = parameters.range_parameters.semi_period_maximum_value_seconds
        self.task.channels.ci_min = parameters.range_parameters.semi_period_minimum_value_seconds

    def configure_timing(self, parameters: DigitalPwmMeasurementTimingParameters) -> None:
        """This method uses the cycles count within the DigitalPwmMeasurementTimingParameters
            argument to set the value in the task

        Args:
            parameters (DigitalPwmMeasurementTimingParameters):
                An instance of DigitalPwmMeasurementTimingParameters containing
                a valid value for semi_period_wounter_wanted_cycles_count
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # calculate # of semiperiods to read
        # Always last cycles will be ignored for the calculations as it does not have complete cycle info  # noqa: W505 - doc line too long (105 > 100 characters) (auto-generated noqa)
        semiperiods_to_read = 2 * parameters.semi_period_counter_wanted_cycles_count - 1

        # set timing task
        finite_samples = ConstantsForDigitalPwmMeasurement.FINITE_SAMPLES
        self.task.timing.cfg_implicit_timing(
            sample_mode=finite_samples, samps_per_chan=semiperiods_to_read
        )

        self.task.start()

    def acquire_data_for_measurement_analysis(self) -> DigitalPwmMeasurementData:
        """Acquires data from the hardware and prepares it for analysis

        Returns:
            DigitalPwmMeasurementData: Numpy array of data to be processed"""  # noqa: D202, D209, D414, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Section has no content (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        num_samples_per_channel = self.task.timing.samp_quant_samp_per_chan

        # preallocate memory for samples
        double_nparray = np.zeros(shape=(num_samples_per_channel,), dtype=np.double)

        # read the counter line and populate memory
        reader = nidaqmx.stream_readers.CounterReader(self.task.in_stream)
        reader.read_many_sample_double(
            data=double_nparray, number_of_samples_per_channel=num_samples_per_channel
        )

        # create DigitalPwmMeasurementData object out of read data and return
        pwm_data = DigitalPwmMeasurementData(double_nparray)
        return pwm_data

    def analyze_measurement_data(
        self, measurement_data: DigitalPwmMeasurementData
    ) -> DigitalPwmMeasurementResultData:
        """This method analyzes the input data and prepares a
           DigitalPwmMeasurementResultData object which contains
           all of the measurements of interest

        Args:
            measurement_data (DigitalPwmMeasurementData): An instance of
            DigitalPwmMeasurementData with valid data

        Returns:
            DigitalPwmMeasurementResultData: Contains the data of interest
            from the PWM measurement
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        meas_data = measurement_data.data
        half_data_length = len(meas_data) // 2

        # create arrays to hold high & low time data -- each w/ half the total samples
        low_time_data = np.zeros(
            shape=max(1, half_data_length),
        )
        high_time_data = np.zeros(
            shape=max(1, half_data_length),
        )

        # decimate original array
        for n in range(2 * half_data_length):
            sample = meas_data[n]
            if n % 2 == 0:
                high_time_data[n // 2] = sample
            else:
                low_time_data[n // 2] = sample

        # derive the average low time
        low_time = np.mean(low_time_data)

        # derive the average high time
        high_time = np.mean(high_time_data)

        # derive the average period from the sum of high time and low time
        sum_array = np.add(low_time_data, high_time_data)
        time_period = np.mean(sum_array)

        # guard time period to avoid divide by zero
        if time_period < ConstantsForDigitalPwmMeasurement.DEFAULT_MIN_SEMIPERIOD:
            time_period = ConstantsForDigitalPwmMeasurement.DEFAULT_MIN_SEMIPERIOD

        # calculate duty cycle
        duty_cyc = high_time / time_period

        # calculate frequency
        freq = 1 / time_period

        # create output object
        result_data = DigitalPwmMeasurementResultData(
            actual_cycles_count=half_data_length + 1,
            duty_cycle=duty_cyc,
            period_duration=time_period,
            frequency=freq,
            high_state_duration=high_time,
            low_state_duration=low_time,
        )

        return result_data

    def configure_and_measure(
        self, configuration: DigitalPwmMeasurementConfiguration
    ) -> DigitalPwmMeasurementResultData:
        """Main method to create and execute a digital pwm measurement

        Args:
            configuration (DigitalPwmMeasurementConfiguration): An instance
            of DigitalPwmMeasurementConfiguration

        Returns:
            DigitalPwmMeasurementResultData:
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        if (
            configuration.measurement_option == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_option == MeasurementExecutionType.CONFIGURE_ONLY
        ):
            self.configure_counter_channel(
                DigitalPwmMeasurementCounterChannelParameters(
                    range_parameters=configuration.parameters.range_parameters,
                    timing_parameters=configuration.parameters.timing_parameters,
                    semi_period_counter_starting_edge=configuration.parameters.semi_period_counter_starting_edge,
                )
            )

            self.configure_timing(configuration.parameters.timing_parameters)

        if (
            configuration.measurement_option == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_option == MeasurementExecutionType.MEASURE_ONLY
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(data)
        else:
            return None

    def close(self):
        """_summary_"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (134 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        self.task.stop()
        self.task.close()
