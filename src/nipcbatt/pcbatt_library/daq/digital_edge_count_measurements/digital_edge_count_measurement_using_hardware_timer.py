"""Use this class to measure digital edge count using hardware timer"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

import re
from typing import Union

import nidaqmx.constants
import nidaqmx.stream_readers
import nidaqmx.stream_writers
import nidaqmx.system
import nidaqmx.system.device
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.MeasurementData' imported but unused (auto-generated noqa)
    DigitalStartTriggerParameters,
    MeasurementData,
    MeasurementExecutionType,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_constants import (
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types import (
    DigitalEdgeCountHardwareTimerConfiguration,
    DigitalEdgeCountMeasurementCounterChannelParameters,
    DigitalEdgeCountMeasurementResultData,
    DigitalEdgeCountMeasurementTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalEdgeCountMeasurementUsingHardwareTimer(BuildingBlockUsingDAQmx):
    """class for performing digital edge count measurement using hardware timer

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    # define class variable as there are two seperate tasks for counter and timer
    counter_task = nidaqmx.Task()
    timer_task = nidaqmx.Task()

    def initialize(
        self,
        measurement_channel_expression: str,
        measurement_input_terminal_name: str,
        timer_channel_expression: str,
    ) -> None:
        """Creates an instance of DigitalEdgeCountMeasurementUsingHardwareTimer class

        Args:
            measurement_channel_expression (str): specifies the counter resource needed for Edge counting operation.
            measurement_input_terminal_name (str): specifies the input terminal on which to look for digital events / edges.
            timer_channel_expression (str): specifies the counter resource needed for Timer task.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (116 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # input validation

        Guard.is_not_none_nor_empty_nor_whitespace(
            measurement_channel_expression, nameof(measurement_channel_expression)
        )
        Guard.is_not_none_nor_empty_nor_whitespace(
            measurement_input_terminal_name, nameof(measurement_input_terminal_name)
        )
        Guard.is_not_none_nor_empty_nor_whitespace(
            timer_channel_expression, nameof(timer_channel_expression)
        )

        # constants used for Initialization of counter
        initial_count = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_INITIAL_COUNT
        count_direction = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_COUNT_DIRECTION
        edge = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE

        # create virtual channel for Edge counting
        self.counter_task.ci_channels.add_ci_count_edges_chan(
            counter=measurement_channel_expression,
            edge=edge,
            initial_count=initial_count,
            count_direction=count_direction,
        )
        # raise exception if more than one channel is present
        if self.counter_task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # set input terminal
        self.counter_task.channels.ci_count_edges_term = measurement_input_terminal_name

        # reserve counter and terminal
        self.counter_task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

        # constatnts used for initializaton of timer
        units = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_TIME_UNITS
        idle_state = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_IDLE_STATE
        min_value = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_LOW_TIME
        max_value = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_HIGH_TIME

        # create virtual channel for timing
        self.timer_task.co_channels.add_co_pulse_chan_time(
            counter=timer_channel_expression,
            units=units,
            idle_state=idle_state,
            low_time=min_value,
            high_time=max_value,
        )

        # add code to get pulse internal treminal

        ctr_channel_number = re.findall(r"[0-9]+$", self.timer_task.channel_names[0])[0]
        daqmx_device_terminals = []

        for i in range(len(self.timer_task.devices)):
            daqmx_device_terminals.extend(self.timer_task.devices[i].terminals)

        for i in range(len(daqmx_device_terminals)):
            if bool(
                re.search("Ctr%sInternalOutput" % (ctr_channel_number), daqmx_device_terminals[i])
            ):
                internal_counter_terminal = daqmx_device_terminals[i]

        # set pulse internal terminal
        self.timer_task.channels.co_pulse_term = internal_counter_terminal

        # reserve timer and terminal
        self.timer_task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_and_measure(
        self, configuration: DigitalEdgeCountHardwareTimerConfiguration
    ) -> Union[None, DigitalEdgeCountMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DigitalEdgeCountHardwareTimerConfiguration):
            A instance of `DigitalEdgeCountHardwareTimerConfiguration` used to configure the measurement.

        Returns:
            DigitalEdgeCountMeasurementResultData | None: An instance of `DigitalEdgeCountMeasurementResultData`
            or `None` if no measure was performed.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (105 > 100 characters) (auto-generated noqa)

        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_ONLY
        ):
            self.configure_counter_channel(
                DigitalEdgeCountMeasurementCounterChannelParameters(
                    configuration.counter_channel_parameters.edge_type
                )
            )
            self.configure_timing(
                DigitalEdgeCountMeasurementTimingParameters(
                    configuration.timing_parameters.edge_counting_duration
                )
            )
            self.configure_trigger(configuration.trigger_parameters)

        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_options.execution_option
            == MeasurementExecutionType.MEASURE_ONLY
        ):
            return self.acquire_data_for_measurement_analysis()

        else:
            return None

    def configure_counter_channel(
        self, parameters: DigitalEdgeCountMeasurementCounterChannelParameters
    ):
        """Configures the counter channel parameter for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
            An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` used to configure the counter channel parameter.
        """  # noqa: D417, W505 - Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (129 > 100 characters) (auto-generated noqa)
        self.counter_task.stop()
        self.counter_task.channels.ci_count_edges_active_edge = parameters.edge_type

    def configure_timing(self, parameters: DigitalEdgeCountMeasurementTimingParameters):
        """Configures the edge counting duration for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementTimingParameters):
            An instance of `DigitalEdgeCountMeasurementTimingParameters` used to configure the edge count duration.
        """  # noqa: D417, W505 - Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (115 > 100 characters) (auto-generated noqa)
        self.timer_task.stop()
        self.counter_task.triggers.pause_trigger.trig_type = (
            ConstantsForDigitalEdgeCountMeasurement.DEFAULT_PAUSE_TRIGGER_TYPE
        )
        self.counter_task.triggers.pause_trigger.dig_lvl_src = (
            self.timer_task.channels.co_pulse_term
        )
        self.counter_task.triggers.pause_trigger.dig_lvl_when = (
            ConstantsForDigitalEdgeCountMeasurement.DEFAULT_PAUSE_DIGITAL_LEVEL_STATE
        )
        self.timer_task.channels.co_pulse_high_time = parameters.edge_counting_duration

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for digital edge count measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters` used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.timer_task.triggers.start_trigger.disable_start_trig()
        else:
            self.timer_task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

        self.counter_task.start()
        self.timer_task.start()

    def acquire_data_for_measurement_analysis(self):
        """Acquires Data from DAQ channel for measurement of digital edge count.

        Returns:
            DigitalEdgeCountMeasurementResultData:
            An instance of `DigitalEdgeCountMeasurementResultData` that specifies the data acquired from DAQ channels.
        """  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
        time_out = (
            self.timer_task.channels.co_pulse_high_time
            + ConstantsForDigitalEdgeCountMeasurement.DEFAULT_TRIGGER_TIMEOUT
        )
        self.timer_task.wait_until_done(time_out)
        reader = nidaqmx.stream_readers.CounterReader(self.counter_task.in_stream)
        edge_count = reader.read_one_sample_uint32(
            timeout=ConstantsForDigitalEdgeCountMeasurement.TIME_OUT
        )
        edge_type = self.counter_task.channels.ci_count_edges_active_edge
        decm_result = DigitalEdgeCountMeasurementResultData(
            edge_count=edge_count, edge_type=edge_type
        )
        return decm_result

    def close(self):
        """Closes the task and returns the hardware resources"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # stop and close DAQmx counter_task
        self.counter_task.stop()
        self.counter_task.close()

        # stop and close DAQmx timer_task
        self.timer_task.wait_until_done()
        self.timer_task.stop()
        self.timer_task.close()
