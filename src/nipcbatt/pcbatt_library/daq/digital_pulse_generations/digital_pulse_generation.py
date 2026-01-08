# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Implementation of Digital Pulse Generation for TestScale and CompactDAQ"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (188 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import nidaqmx.stream_readers
import nidaqmx.stream_writers
from varname import nameof

from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_constants import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_data_types import (
    DigitalPulseGenerationConfiguration,
    DigitalPulseGenerationCounterChannelParameters,
    DigitalPulseGenerationData,
    DigitalPulseGenerationTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalPulseGeneration(BuildingBlockUsingDAQmx):
    """Use this class for digital pulse generation

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        channel_expression: str,
        output_terminal_name: str,
    ) -> None:
        """_summary_

        Args:
            channel_expression (str): Physical channel
            output_terminal_name (str): Channel to write
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # Here implement initialization of task.
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))

        Guard.is_not_none(output_terminal_name, nameof(output_terminal_name))
        Guard.is_not_empty(output_terminal_name, nameof(output_terminal_name))

        # constants used for instantiation
        t_low = ConstantsForDigitalPulseGeneration.DEFAULT_LOW_TIME
        t_hi = ConstantsForDigitalPulseGeneration.DEFAULT_HIGH_TIME
        def_units = ConstantsForDigitalPulseGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT
        def_idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE

        # check to see if task has only global channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

        else:
            # create virtual channel for pulse generation
            self.task.co_channels.add_co_pulse_chan_time(
                counter=channel_expression,
                units=def_units,
                idle_state=def_idle_state,
                low_time=t_low,
                high_time=t_hi,
            )

        # raise exception if more than one channel is present
        if self.task.number_of_channels and self.task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set output terminal
        self.task.channels.co_pulse_term = output_terminal_name

        # reserve counter and terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_counter_channel(
        self,
        parameters: DigitalPulseGenerationCounterChannelParameters,
    ) -> None:
        """Configuration of the digital channel used for pulse generations

        Args:
            parameters (DigitalPulseGenerationCounterChannelParameters): A valid instance
                of DigitalPulseGenerationCounterChannelParameters
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # stop daq task and return it to previous state
        self.task.stop()

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set channel parameters
        self.task.channels.co_pulse_low_time = parameters.low_time_seconds
        self.task.channels.co_pulse_high_time = parameters.high_time_seconds

    def configure_timing(self, parameters: DigitalPulseGenerationTimingParameters) -> None:
        """Configuration of pulse generation timing

        Args:
            parameters (DigitalPulseGenerationTimingParameters): A valid instance
                of DigitalPulseGenerationTimingParameters
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set timing configuration
        finite_samples = ConstantsForDigitalPulseGeneration.FINITE_SAMPLES
        self.task.timing.cfg_implicit_timing(
            sample_mode=finite_samples, samps_per_chan=parameters.pulses_count
        )

        self.task.start()

    def generate(
        self, parameters: DigitalPulseGenerationTimingParameters
    ) -> DigitalPulseGenerationData:
        """Generate digital pulse(s)

        Returns:
            DigitalPulseGenerationData: A valid instance of DigitalPulseGenerationData
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        # create stream writer
        # writer = nidaqmx.stream_writers.CounterWriter(
        #     task_out_stream=self.task.out_stream,
        #     auto_start=True
        # )

        # # write to hardware
        # writer.write_one_sample_pulse_time(
        #     high_time=self.task.channels.co_pulse_high_time,
        #     low_time=self.task.channels.co_pulse_low_time,
        #     timeout=10
        # )

        # compute generation time
        true_low_time = self.task.channels.co_pulse_low_time
        true_high_time = self.task.channels.co_pulse_high_time
        sum_time = true_low_time + true_high_time
        generation_time = sum_time * parameters.pulses_count

        # return written data
        data_out = DigitalPulseGenerationData(
            timebase_frequency_hertz=self.task.channels.co_ctr_timebase_rate,
            actual_pulse_train_duration_seconds=generation_time,
            actual_pulse_low_time_seconds=true_low_time,
            actual_pulse_high_time_seconds=true_high_time,
        )

        return data_out

    def configure_and_generate(
        self, configuration: DigitalPulseGenerationConfiguration
    ) -> DigitalPulseGenerationData:
        """Configuration of instruments and process to generation

        Args:
            configuration (DigitalPulseGenerationConfiguration): A valid instance
                of DigitalPulseGenerationConfiguration

        Returns:
            DigitalPulseGenerationData: The values written to hardware
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        self.configure_counter_channel(configuration.counter_channel_parameters)
        self.configure_timing(configuration.timing_parameters)

        return self.generate(configuration.timing_parameters)

    def close(self):
        """Stops and closes the DAQ task"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        self.task.wait_until_done()
        self.task.stop()
        self.task.close()
