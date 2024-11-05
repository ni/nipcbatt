# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Use this class to generate a digital clock"""

import nidaqmx.constants
import nidaqmx.stream_writers
from varname import nameof

from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_constants import (
    ConstantsForDigitalClockGeneration,
)
from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_data_types import (
    DigitalClockGenerationConfiguration,
    DigitalClockGenerationCounterChannelParameters,
    DigitalClockGenerationData,
    DigitalClockGenerationTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

# when class are defined in module change to
# from digital_clock_data_types import ...
# import digital_clock_data_types


class DigitalClockGeneration(BuildingBlockUsingDAQmx):
    """Used to output a digital clock to the hardware

    Args:
        BuildingBlockUsingDAQmx: Base class for all testscale modules
    """

    def initialize(
        self,
        counter_channel_expression: str,
        output_terminal_name: str,
    ):
        """_summary_

        Args:
            counter_channel_expression (str): Physical channel of counter to use
            output_terminal_name (str): Terminal on which the signal is measured
        """
        if self.is_task_initialized:
            return

        # input validation on channel expression and output terminal
        Guard.is_not_none(counter_channel_expression, nameof(counter_channel_expression))
        Guard.is_not_empty(counter_channel_expression, nameof(counter_channel_expression))
        Guard.is_not_none(output_terminal_name, nameof(output_terminal_name))
        Guard.is_not_empty(output_terminal_name, nameof(output_terminal_name))

        # constant used for initialization
        frequency_initial = ConstantsForDigitalClockGeneration.DEFAULT_GENERATION_FREQUENCY
        duty_cycle_initial = ConstantsForDigitalClockGeneration.DEFAULT_GENERATION_DUTY_CYCLE
        idle_state_initial = ConstantsForDigitalClockGeneration.DEFAULT_GENERATION_IDLE_STATE
        units_initial = ConstantsForDigitalClockGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT

        # check to see if task has only global channels
        if self.contains_only_global_virtual_channels(counter_channel_expression):
            # add global channels to task
            self.add_global_channels(counter_channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

        else:
            # create virtual channel for clock generation
            self.task.co_channels.add_co_pulse_chan_freq(
                counter=counter_channel_expression,
                units=units_initial,
                idle_state=idle_state_initial,
                freq=frequency_initial,
                duty_cycle=duty_cycle_initial,
            )

        # raise execption if more than one channel is present
        if self.task.number_of_channels and self.task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set output terminal
        self.task.channels.co_pulse_term = output_terminal_name

        # reserve counter and terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    # submethods -- not visible to end users
    def configure_counter_channel(
        self, parameters: DigitalClockGenerationCounterChannelParameters
    ) -> None:
        """Configures the counter channel used for digital clock generation

        Args:
            parameters (DigitalClockGenerationCounterChannelParameters): An instance
            of DigitalClockGenerationCounterChannelParameters containg frequency
            and duty cycle data
        """

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        self.task.stop()
        # set channel parameters
        self.task.channels.co_pulse_freq = parameters.frequency_hertz
        self.task.channels.co_pulse_duty_cyc = parameters.duty_cycle_ratio

    # sets the timing property of the task
    def configure_timing(self, parameters: DigitalClockGenerationTimingParameters) -> None:
        """Defines timing settings used in digital clock generation

        Args:
            parameters (DigitalClockGenerationTimingParameters): Contains
            duration settings used for generation
        """
        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # calculate samples per channel -- step 1: extract frequency
        frequency = self.task.channels.co_pulse_freq

        # step 2 -- calculate number of samples
        num_samples = int(frequency * parameters.clock_duration_seconds)

        # set timing property
        finite_samples = ConstantsForDigitalClockGeneration.FINITE_SAMPLES
        self.task.timing.cfg_implicit_timing(sample_mode=finite_samples, samps_per_chan=num_samples)

    # writes the signal to hardware
    def generate(
        self, timing: DigitalClockGenerationTimingParameters
    ) -> DigitalClockGenerationData:
        """Starts the clock signal generation

        Returns:
            DigitalClockGenerationData: Contains the settings that
            were actually written to the instrument
        """
        self.task.start()
        # return written data
        data_out = DigitalClockGenerationData(
            timebase_frequency_hertz=self.task.channels.co_ctr_timebase_rate,
            actual_clock_frequency_hertz=self.task.channels.co_pulse_freq,
            actual_clock_duty_cycle_ratio=self.task.channels.co_pulse_duty_cyc,
            actual_clock_duration_seconds=timing.clock_duration_seconds,
        )

        return data_out

    def configure_and_generate(self, configuration: DigitalClockGenerationConfiguration):
        """Generates a digital clock to the hardware based on the configuration provided

        Args:
            configuration (DigitalClockGenerationConfiguration): A instance of
            DigitalClockGenerationConfiguration containing the settings to be used
        """

        # configure channel
        self.configure_counter_channel(configuration.counter_channel_parameters)

        # configure timing
        self.configure_timing(configuration.timing_parameters)

        # generate clock signal
        data = self.generate(configuration.timing_parameters)

        return data

    def close(self):
        """_summary_"""
        if not self.is_task_initialized:
            return

        self.task.wait_until_done()
        self.task.stop()
        self.task.close()
