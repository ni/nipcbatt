# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Defines class used for digital frequency measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import nidaqmx.stream_readers
from varname import nameof

from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_constants import (
    ConstantsForDigitalFrequencyMeasurement,
)
from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_data_types import (
    DigitalFrequencyMeasurementConfiguration,
    DigitalFrequencyMeasurementCounterChannelParameters,
    DigitalFrequencyMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalFrequencyMeasurement(BuildingBlockUsingDAQmx):
    """This class is used to perform digital frequency meausrements
    Args:
        BuildingBlockUsingDAQmx: Parent class for all modules
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        channel_expression: str,
        input_terminal_name: str,
    ):
        """Creates a DigitalFrequencyMeasurement object with the
           given arguments

        Args:
            channel_expression (str): Channels to acquire
            input_terminal_name (str): Terminal to acquire
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # input validation on channel expression and terminal
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))
        Guard.is_not_none(input_terminal_name, nameof(input_terminal_name))
        Guard.is_not_empty(input_terminal_name, nameof(input_terminal_name))

        # check to see if task has only global virtual channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

        else:
            # create virtual channel for counter input

            self.task.ci_channels.add_ci_freq_chan(
                counter=channel_expression,
                name_to_assign_to_channel="",
                min_val=ConstantsForDigitalFrequencyMeasurement.DEFAULT_MIN_VALUE,
                max_val=ConstantsForDigitalFrequencyMeasurement.DEFAULT_MAX_VALUE,
                units=ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_MEASURE_UNIT,
                edge=ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_STARTING_EDGE,
                meas_method=ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_COUNTER_METHOD,
                meas_time=ConstantsForDigitalFrequencyMeasurement.DEFAULT_MEAS_TIME,
                divisor=ConstantsForDigitalFrequencyMeasurement.DEFAULT_INPUT_DIVISOR,
            )

        # raise exception if more than one channel is present
        if self.task.channel_names and len(self.task.channel_names) > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set input terminal for frequency counter
        self.task.channels.ci_freq_term = input_terminal_name

        # reserve counter and input terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def close(self):
        """Ends measurement process and releases internal resources"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(self, configuration: DigitalFrequencyMeasurementConfiguration):
        """Configures and/or performs a digital frequency measurement
           according to specific configuration parameters.

        Args:
            configuration (DigitalFrequencyMeasurementConfiguration): An instance of
            `DigitalFrequencyMeasurementConfiguration` used to configure the measurement.

        Returns:
            DigitalFrequencyMeasurementResultData: An instance of
            `DigitalFrequencyMeasurementResultData`or `None` if no measure was performed.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self.configure_counter_channel(configuration.counter_channel_configuration_parameters)

        # extract frequency data
        digital_frequency = self.acquire_data_for_measurement_analysis()

        # return frequency data in DigitalFrequencyMeasurementResultData object
        # or implicitly return None if no measurement was performed
        if digital_frequency is not None:
            return DigitalFrequencyMeasurementResultData(digital_frequency)

    def configure_counter_channel(
        self, parameters: DigitalFrequencyMeasurementCounterChannelParameters
    ) -> None:
        """Configures a counter channel according to specific configuration parameters.

        Args:
        parameters (DigitalFrequencyMeasurementCounterChannelParameters): An instance of
            `DigitalFrequencyMeasurementCounterChannelParameters` used to configure the
             counter channel.
        """
        self.task.stop()

        # set parameters for measurement
        self.task.channels.ci_freq_meas_meth = (
            ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_COUNTER_METHOD
        )
        self.task.channels.ci_max = parameters.range_parameters.frequency_maximum_value_hertz
        self.task.channels.ci_min = parameters.range_parameters.frequency_minimum_value_hertz

        self.task.channels.ci_freq_div = parameters.input_divisor_for_frequency_measurement

        self.task.channels.ci_freq_units = (
            ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_MEASURE_UNIT
        )
        self.task.channels.ci_freq_starting_edge = (
            ConstantsForDigitalFrequencyMeasurement.DEFAULT_FREQUENCY_STARTING_EDGE
        )

        self.task.start()

    def acquire_data_for_measurement_analysis(self) -> float:
        """Acquires Data from DAQ channel for measurement of digital frequency.

        Args: None

        Returns:
            float: A digital frequency measurement result
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        # create reader
        counter_reader = nidaqmx.stream_readers.CounterReader(self.task.in_stream)

        # read the data
        time_out = ConstantsForDigitalFrequencyMeasurement.DEFAULT_TIME_OUT
        digital_frequency = counter_reader.read_one_sample_double(time_out)

        return digital_frequency
