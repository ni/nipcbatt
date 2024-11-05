"""Use this class to measure dynamic digital pattern from a system"""

import re
from typing import List, Union

import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.stream_readers
import nidaqmx.stream_writers
import nidaqmx.system
import nidaqmx.system.storage
import numpy as np
from nidaqmx.constants import LineGrouping
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
    MeasurementAnalysisRequirement,
    MeasurementData,
    MeasurementExecutionType,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternMeasurementConfiguration,
    DynamicDigitalPatternMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DynamicDigitalPatternMeasurement(BuildingBlockUsingDAQmx):
    """class for performing dynamic digital pattern measurement

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    """

    def initialize(
        self,
        channel_expression: str,
    ) -> None:
        """Creates an instance of DynamicDigitalPatternMeasurement class

        Args:
            channel_expression (str): The name of the lines/port where the data will be measured
        """
        if self.is_task_initialized:
            return

        # input validation on channel expression
        Guard.is_not_none_nor_empty_nor_whitespace(channel_expression, nameof(channel_expression))

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
            # create one virtual channel for all Digital In line
            # for channel in channels:
            self.task.di_channels.add_di_chan(
                channel_expression, "", LineGrouping.CHAN_FOR_ALL_LINES
            )

        # reserve lines for the task
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def close(self):
        """Closes the task and returns the hardware resources"""
        if not self.is_task_initialized:
            return

        # stop and close DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(
        self, configuration: DynamicDigitalPatternMeasurementConfiguration
    ) -> Union[None, DynamicDigitalPatternMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DynamicDigitalPatternMeasurementConfiguration):
            A instance of `DynamicDigitalPatternMeasurementConfiguration` used to configure the measurement.

        Returns:
            DynamicDigitalPatternMeasurementResultData | None: An instance of `DynamicDigitalPatternMeasurementResultData`
            or `None` if no measure was performed.
        """

        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_ONLY
        ):
            self.configure_timing(configuration.timing_parameters)
            self.configure_trigger(configuration.trigger_parameters)

        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_options.execution_option
            == MeasurementExecutionType.MEASURE_ONLY
        ):
            data = self.acquire_data_for_measurement_analysis()

            return self.analyze_measurement_data(data)

        else:
            return None

    def configure_timing(self, parameters: DynamicDigitalPatternTimingParameters):
        """Configures the timing parameters for dynamic digital pattern measurement.

        Args:
            parameters (DynamicDigitalPatternTimingParameters):
            An instance of `DynamicDigitalPatternTimingParameters` used to configure the timing.
        """
        self.task.stop()

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            source=parameters.sample_clock_source,
            active_edge=parameters.active_edge,
            sample_mode=ConstantsForDynamicDigitalPatternMeasurement.FINITE_SAMPLES,
            samps_per_chan=parameters.number_of_samples_per_channel,
        )

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for dynamic digital pattern measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters` used to configure the channels.
        """
        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

        self.task.start()

    def acquire_data_for_measurement_analysis(self):
        """Acquires Data from DAQ channel for measurement of dynamic digital pattern

        Returns:
            MeasurementData:
            An instance of `MeasurementData` that specifies the data acquired from DAQ channels.
        """
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan
        data_to_read = np.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=np.uint32,
        )
        reader = nidaqmx.stream_readers.DigitalMultiChannelReader(self.task.in_stream)
        reader.read_many_sample_port_uint32(
            number_of_samples_per_channel=number_of_samples_per_channel,
            timeout=ConstantsForDynamicDigitalPatternMeasurement.TIME_OUT,
            data=data_to_read,
        )

        return data_to_read

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
    ) -> DynamicDigitalPatternMeasurementResultData:
        """Proceeds to the analysis of Digital port data from the measurement.

        Args:
            measurement_data (MeasurementData):
            An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.

        Returns:
            DynamicDigitalPatternMeasurementResultData:
            An instance of `DynamicDigitalPatternMeasurementResultData`
            that specifies the measurement results.
        """
        port_data = measurement_data[0]
        digital_pattern_data = []

        for samples in port_data:
            data_byte = samples
            bit_stream = []
            for _ in range(32):
                bit_stream.append(data_byte % 2)
                data_byte = data_byte // 2
            digital_pattern_data.append(bit_stream)

        number_of_lines = 0
        for d_channel in self.task.di_channels:
            number_of_lines = number_of_lines + d_channel.di_num_lines

        input_string = d_channel.name

        match = re.search(r"line(\d+)", input_string)
        if match:
            result = match.group(1)
            number_int = int(result)
        else:
            number_int = 0

        digital_pattern_data = np.transpose(digital_pattern_data)
        digital_pattern_data = digital_pattern_data[
            (number_int) : (number_int + number_of_lines), 0 : len(port_data)
        ]
        daq_digital_waveform_from_port = port_data[0 : len(port_data)]
        return DynamicDigitalPatternMeasurementResultData(
            daq_digital_waveform_from_port,
            waveforms=np.array(digital_pattern_data, dtype=np.uint32),
        )
