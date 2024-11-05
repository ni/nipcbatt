# pylint: disable=W0613
# remove it when arguments of initialize are used.
""" _summary_ """

import nidaqmx.constants
import nidaqmx.stream_writers
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
    SampleClockTimingParameters,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_data_types import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternGenerationConfiguration,
    DynamicDigitalPatternGenerationData,
    DynamicDigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.synchronizations.synchronization_signal_routing import (
    SynchronizationSignalRouting,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

# when class are defined in module change to
# from dynamic_digital_pattern_data_types import ...


class DynamicDigitalPatternGeneration(SynchronizationSignalRouting):
    """Use this class to generate dynamic digital patterns"""

    def initialize(self, channel_expression: str):
        """Initializes a dynamic digital pattern generation sequence

        Args:
            channel_expression (str): The channel to generate on
        """
        # self.task.stop()

        if self.is_task_initialized:
            return

        # input validation
        Guard.is_not_none(channel_expression, nameof(channel_expression))
        Guard.is_not_empty(channel_expression, nameof(channel_expression))

        # check to see if task has only global virtual channels
        if self.contains_only_global_virtual_channels(channel_expression):
            # add global channels to task
            self.add_global_channels(channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)

            # check task for number of devices
            # device count > 2 indicates multiple modules are present
            if self.task.number_of_devices > 2:
                # notify user of error and modules listed
                raise PCBATTLibraryException(
                    PCBATTLibraryExceptionMessages.GLOBAL_CHANNEL_TOO_MANY_MODULES_ARGS_1.format(
                        self.task.devices
                    )
                )

        else:
            # create digital output task
            self.task.do_channels.add_do_chan(channel_expression)

            # reserve resources for task
            self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_timing(self, parameters: DynamicDigitalPatternTimingParameters) -> None:
        """This method configures the timing of the generation

        Args:
            parameters (DynamicDigitalPatternTimingParameters): A valid instance
                of DynamicDigitalPatternTimingParameters
        """

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set timing for task
        finite_samples = ConstantsForDynamicDigitalPatternGeneration.FINITE_SAMPLES
        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            source=parameters.sample_clock_source,
            active_edge=parameters.active_edge,
            sample_mode=finite_samples,
            samps_per_chan=parameters.number_of_samples_per_channel,
        )

    def configure_trigger(self, parameters: DynamicDigitalStartTriggerParameters) -> None:
        """This method configures the trigger of the generation

        Args:
            parameters (DynamicDigitalStartTriggerParameters): A valid instance of
                DynamicDigitalStartTriggerParameters
        """

        # input validation
        Guard.is_not_none(parameters, nameof(parameters))

        # set trigger settings

        if parameters.trigger_type is not StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def generate(self, pulse_signal: np.ndarray) -> float:
        """Generates the dynamic digital pattern

        Args:
            pulse_signal (np.ndarray): Numpy array of (shape=(number_of_channels), dtype=numpy.uint32)

        Returns:
            float: The total generation time
        """

        # input validation
        Guard.is_not_none(pulse_signal, nameof(pulse_signal))
        Guard.is_not_empty(pulse_signal, nameof(pulse_signal))

        # write data
        writer = nidaqmx.stream_writers.DigitalMultiChannelWriter(self.task.out_stream)
        writer.write_many_sample_port_uint32(pulse_signal)

        # calculate generation time
        sample_rate = self.task.timing.samp_clk_rate

        if len(pulse_signal.shape) == 1:
            num_samples = pulse_signal.shape[0]
        else:
            num_samples = pulse_signal.shape[1]

        generation_time = num_samples / sample_rate

        return generation_time

    def configure_and_generate(
        self,
        configuration: DynamicDigitalPatternGenerationConfiguration,
    ) -> DynamicDigitalPatternGenerationData:
        """_summary_

        Args:
            configuration (DynamicDigitalPatternGenerationConfiguration): An
                instance of DynamicDigitalPatternGenerationConfiguration

        Returns:
            An instance of DynamicDigitalPatternGenerationData
        """

        self.task.stop()
        self.configure_timing(configuration.timing_parameters)
        self.configure_trigger(configuration.digital_start_trigger_parameters)

        generation_time = self.generate(configuration.pulse_signal)
        data_out = DynamicDigitalPatternGenerationData(generation_time)
        self.task.start()

        return data_out

    def close(self):
        """_summary_"""
        if not self.is_task_initialized:
            return
        self.task.wait_until_done()
        self.task.stop()
        self.task.close()
