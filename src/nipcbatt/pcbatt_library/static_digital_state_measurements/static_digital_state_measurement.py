# pylint: disable=W0613
# pylint: disable=W0612
# remove it when arguments of initialize are used.
""" _summary_ """

from typing import List

# when class are defined in module change to
# from static_digital_state_data_types import ...
import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.stream_readers
import nidaqmx.system
import numpy as np
from nidaqmx.constants import LineGrouping
from nidaqmx.utils import unflatten_channel_string
from varname import nameof

from nipcbatt.pcbatt_library.static_digital_state_measurements.static_digital_state_data_types import (
    StaticDigitalStateMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateMeasurement(BuildingBlockUsingDAQmx):
    """Defines the means for creating, configuring, and measuring
    the static digital state of a series of digital lines

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    """

    def initialize(self, channel_expression: str):
        """Initializes Digital input channels for static digital measurements for
        a DAQmx Task

        Args:
            channel_expression (str): Digital input channels to read off of the
            DAQmx task
        """
        if self.is_task_initialized:
            return

        # input validation on channel expression
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))

        # check to see if task has only global virtual channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

            # check for the presence of global channel ports
            for d_channel in self.task.di_channels:
                # presence of global channel port with # of lines > 1
                if d_channel.di_num_lines > 1:
                    raise PCBATTLibraryException(
                        PCBATTLibraryExceptionMessages.GLOBAL_CHANNEL_PORT_NOT_SUPPORTED_ARGS_3.format(
                            d_channel.name, d_channel.di_num_lines, d_channel.name
                        )
                    )

        else:
            # create virtual channel for each Digital In line
            # for channel in channels:
            self.task.di_channels.add_di_chan(channel_expression, "", LineGrouping.CHAN_PER_LINE)

    def close(self):
        """Closes the measurement process and releases the internal resources"""
        if not self.is_task_initialized:
            return

        # Stop and close DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(self) -> StaticDigitalStateMeasurementResultData:
        """Configures and executes a measurement according to the current configuration parameters.

        Args:

        Returns:
            An instance of `StaticDigitalStateMeasurementResultData
            ` or `None` if no measure was performed.
        """
        return self.acquire_data_for_measurement_analysis()

    def acquire_data_for_measurement_analysis(
        self,
    ) -> StaticDigitalStateMeasurementResultData:
        """Processes digital data acquistion for measurement analysis

        Args:

        Returns:
            An instance of StaticDigitalStateMeasurementResultData"""

        # set values for memory declaration
        num_channels = len(self.task.in_stream.channels_to_read.channel_names)
        num_samples_per_channel = 1

        # declare memory for read
        booleans_nparray = np.zeros(
            shape=(num_channels, num_samples_per_channel),
            dtype=bool,
        )
        channel_ids: List[str] = []

        # populate channel IDs
        for d_channel in self.task.di_channels:
            channel_ids.append(d_channel.name)

        # read the digital lines
        reader = nidaqmx.stream_readers.DigitalMultiChannelReader(self.task.in_stream)
        reader.read_one_sample_multi_line(data=booleans_nparray)

        # extract list of booleans from read data
        digital_states: List[bool] = []
        for boolean_sample in booleans_nparray:
            digital_states.append(boolean_sample[0])

        # create the returned object
        return StaticDigitalStateMeasurementResultData(digital_states, channel_ids)
