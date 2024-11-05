# pylint: disable=W0613
# remove it when arguments of initialize are used.
""" Defines class used for generation of DC voltage on PCB points. """

from typing import List

import nidaqmx.constants
import nidaqmx.stream_writers
import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library.dc_voltage_generations.dc_voltage_data_types import (
    DcVoltageGenerationConfiguration,
)
from nipcbatt.pcbatt_library.dc_voltage_generations.dc_voltage_generation_constants import (
    ConstantsForDcVoltageGeneration,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcVoltageGeneration(BuildingBlockUsingDAQmx):
    """Defines a way for the user to configure the Analog Output pins for DC voltage generation."""

    def initialize(self, analog_output_channel_expression: str):
        """Initializes the DC voltage generation with the specific channels.

        Args:
            analog_output_channel_expression (str):
                Expression representing the name of an analog output physical channel,
                or a global channel in DAQ System.
        """
        if self.is_task_initialized:
            return

        # If the input analog_output_channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for analog output voltage.
        if self.contains_only_global_virtual_channels(
            channel_expression=analog_output_channel_expression
        ):
            self.add_global_channels(global_channel_expression=analog_output_channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_generation_type(nidaqmx.constants.UsageTypeAO.VOLTAGE)
        else:
            # Add the analog_output_channel_expression to analog output channel of the Daqmx task
            self.task.ao_channels.add_ao_voltage_chan(
                physical_channel=analog_output_channel_expression,
                min_val=ConstantsForDcVoltageGeneration.INITIAL_RANGE_MIN_VOLTS,
                max_val=ConstantsForDcVoltageGeneration.INITIAL_RANGE_MAX_VOLTS,
                units=ConstantsForDcVoltageGeneration.INITIAL_AO_VOLTAGE_UNITS,
            )

    def configure_all_channels(
        self,
        parameters: VoltageGenerationChannelParameters,
    ) -> None:
        """Configures all analog output channels for DC Voltage generation.

        Args:
            parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
        """
        self.task.stop()
        for channel in self.task.ao_channels:
            channel.ao_min = parameters.range_min_volts
            channel.ao_max = parameters.range_max_volts

    def generate_voltage(
        self,
        output_voltages: List[float],
    ) -> None:
        """Generates voltage at the DAQ channel.

        Args:
            output_voltages (List[float]):
                specifies the actual output voltage to generate on the selected channel(s).
                Each element of the array corresponds to a channel in the task.
                The order of the channels in the array corresponds to the order
                in which the channels have been added to the task in the initialize method.

        Raises:
            ValueError:
                If the `output_voltages` is an ampty array.
                If the size of `output_voltages` does not match with the number of channels in the Task.
        """
        # Check if the output_voltages array is not empty and if it has same number of elements as the number of channels in the task.
        Guard.is_not_empty(output_voltages, nameof(output_voltages))
        Guard.have_same_size(
            first_iterable_instance=output_voltages,
            first_iterable_name=nameof(output_voltages),
            second_iterable_instance=self.task.ao_channels.channel_names,
            second_iterable_name=nameof(self.task.ao_channels.count),
        )
        writer = nidaqmx.stream_writers.AnalogMultiChannelWriter(
            task_out_stream=self.task.out_stream,
            auto_start=True,
        )
        writer.write_one_sample(data=numpy.array(output_voltages))

    def configure_and_generate(
        self,
        configuration: DcVoltageGenerationConfiguration,
    ) -> None:
        """Configures and generates the DC Voltages according to the specific configuration.

        Args:
            configuration (DcVoltageGenerationConfiguration):
                An instance of 'DcVoltageGenerationConfiguration` used to configure the generation of DC voltage.

        Returns:
            None.
        """
        self.configure_all_channels(parameters=configuration.voltage_generation_range_parameters)
        self.generate_voltage(
            output_voltages=configuration.output_voltages,
        )

    def close(self):
        """Stops and closes the generation task and releases the internal resources."""
        if not self.is_task_initialized:
            return

        # Stop and close the Daqmx task
        self.task.stop()
        self.task.close()
