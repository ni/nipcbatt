# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Use this class to generate digital states to output on system"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)

from typing import List

import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.stream_writers
import nidaqmx.system
import numpy as np
from nidaqmx.constants import LineGrouping
from varname import nameof

from nipcbatt.pcbatt_library.static_digital_state_generations.static_digital_state_data_types import (
    StaticDigitalStateGenerationConfiguration,
    StaticDigitalStateGenerationData,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateGeneration(BuildingBlockUsingDAQmx):
    """This class represents the set of static digital states
       the user wishes to write to digital output lines

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def initialize(self, channel_expression: str):
        """Initializes the task to prepare for generation

        Args:
            channel_expression (str): The name of the lines/port
            where the data will be written
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        self.task.stop()

        if self.is_task_initialized:
            return

        # input validation
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))

        # check to seee if task has only global virtual channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

            # check for presence of global channel ports
            for do_channel in self.task.do_channels:
                if do_channel.do_num_lines != 1:
                    raise PCBATTLibraryException(
                        PCBATTLibraryExceptionMessages.GLOBAL_CHANNEL_PORT_NOT_SUPPORTED_ARGS_3.format(
                            do_channel.name, do_channel.di_num_lines, do_channel.name
                        )
                    )

        else:
            # create virtual channel for each Digital Out line
            self.task.do_channels.add_do_chan(channel_expression, "", LineGrouping.CHAN_PER_LINE)

    def close(self):
        """Closes the task and returns the hardware resource"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # stop and close DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_generate(
        self, configuration: StaticDigitalStateGenerationConfiguration
    ) -> StaticDigitalStateGenerationData:
        """Uses the configuration provided to generate the digital
           states on the hardware

        Args:
            configuration (StaticDigitalStateGenerationConfiguration): An
            instance of an object that contains the states to generate

        Returns:
            StaticDigitalStateGenerationData: Contains an array of strings
            describing the lines that were written to
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self.generate_digital_states(configuration.data_to_write)

    def generate_digital_states(
        self, output_states: List[bool]
    ) -> StaticDigitalStateGenerationData:
        """This method takes the states the user wishes to generate
           and creates a StaticDigitalStateGenerationData object

        Args:
            output_states (List[bool]): The list of digital states
            to be generated

        Returns:
            StaticDigitalStateGenerationData: An array of strings
            describing the lines that were written to
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self.task.stop()

        # create values for memory declaration
        num_channels = len(self.task.do_channels.channel_names)
        num_samples_per_channel = 1

        # declare memory for write
        numpy_array_of_booleans = np.zeros(
            shape=(num_channels, num_samples_per_channel), dtype=bool
        )

        # populate boolean array with values
        for index, state in enumerate(output_states):
            numpy_array_of_booleans[index] = np.array([state])

        # write to the digital lines
        writer = nidaqmx.stream_writers.DigitalMultiChannelWriter(self.task.out_stream)
        writer.write_one_sample_multi_line(data=numpy_array_of_booleans)

        # get the channel names that have been used
        channel_names = self.task.channel_names

        # create the returned object
        return StaticDigitalStateGenerationData(channel_names)
