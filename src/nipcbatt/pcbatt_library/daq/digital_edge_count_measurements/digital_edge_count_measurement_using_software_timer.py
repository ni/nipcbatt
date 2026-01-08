"""Use this class to measure digital edge count using software timer"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

import time
from typing import Union

import nidaqmx.constants
import nidaqmx.stream_readers
import nidaqmx.system
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.MeasurementData' imported but unused (auto-generated noqa)
    MeasurementData,
    MeasurementExecutionType,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_constants import (
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types import (
    DigitalEdgeCountMeasurementCounterChannelParameters,
    DigitalEdgeCountMeasurementResultData,
    DigitalEdgeCountMeasurementTimingParameters,
    DigitalEdgeCountSoftwareTimerConfiguration,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryException,
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalEdgeCountMeasurementUsingSoftwareTimer(BuildingBlockUsingDAQmx):
    """class for performing digital edge count measurement using software timer

    Args:
        BuildingBlockUsingDAQmx (_type_): Parent class for all PCBATT classes
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)

    def initialize(
        self,
        measurement_channel_expression: str,
        measurement_input_terminal_name: str,
    ) -> None:
        """Creates an instance of DigitalEdgeCountMeasurementUsingSoftwareTimer class

        Args:
            measurement_channel_expression (str): specifies the counter resource needed for Edge counting operation.
            measurement_input_terminal_name (str): specifies the input terminal on which to look for digital events/edges.
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

        # Constants used for Initialization of counter
        initial_count = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_INITIAL_COUNT
        count_direction = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_COUNT_DIRECTION
        edge = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE

        # Create virtual channel for Edge counting
        self.task.ci_channels.add_ci_count_edges_chan(
            counter=measurement_channel_expression,
            edge=edge,
            initial_count=initial_count,
            count_direction=count_direction,
        )
        # Raise exception if more than one channel is present
        if self.task.number_of_channels > 1:
            raise PCBATTLibraryException(
                PCBATTLibraryExceptionMessages.MORE_THAN_ONE_CHANNEL_INVALID
            )

        # Set input terminal
        self.task.channels.ci_count_edges_term = measurement_input_terminal_name

        # Reserve counter and terminal
        self.task.control(nidaqmx.constants.TaskMode.TASK_RESERVE)

    def configure_and_measure(
        self, configuration: DigitalEdgeCountSoftwareTimerConfiguration
    ) -> Union[None, DigitalEdgeCountMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DigitalEdgeCountSoftwareTimerConfiguration):
            A instance of `DigitalEdgeCountSoftwareTimerConfiguration` used to configure the measurement.

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
                    configuration.counter_channel_parameters.edge_type,
                )
            )
            self.configure_timing(
                DigitalEdgeCountMeasurementTimingParameters(
                    configuration.timing_parameters.edge_counting_duration,
                )
            )

        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
            or configuration.measurement_options.execution_option
            == MeasurementExecutionType.MEASURE_ONLY
        ):
            self.meas_option = configuration.measurement_options
            return self.acquire_data_for_measurement_analysis(configuration)

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
        self.task.stop()
        self.task.channels.ci_count_edges_active_edge = parameters.edge_type
        self.task.start()

    def configure_timing(self, parameters: DigitalEdgeCountMeasurementTimingParameters):
        """Configures the edge counting duration for digital edge count measurement.

        Args:
            parameters (DigitalEdgeCountMeasurementTimingParameters):
            An instance of `DigitalEdgeCountMeasurementTimingParameters` used to configure the edge count duration.
        """  # noqa: D417, W505 - Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (115 > 100 characters) (auto-generated noqa)
        wait_delay = (  # noqa: F841 - local variable 'wait_delay' is assigned to but never used (auto-generated noqa)
            parameters.edge_counting_duration
        )

    def acquire_data_for_measurement_analysis(
        self, configuration: DigitalEdgeCountSoftwareTimerConfiguration
    ):
        """Acquires Data from DAQ channel for measurement of digital edge count.

        Returns:
            DigitalEdgeCountMeasurementResultData:
            An instance of `DigitalEdgeCountMeasurementResultData` that specifies the data acquired from DAQ channels.
        """  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
        if (
            configuration.measurement_options.execution_option
            == MeasurementExecutionType.CONFIGURE_AND_MEASURE
        ):
            time.sleep(configuration.timing_parameters.edge_counting_duration)

        reader = nidaqmx.stream_readers.CounterReader(self.task.in_stream)
        edge_count = reader.read_one_sample_uint32(
            timeout=ConstantsForDigitalEdgeCountMeasurement.TIME_OUT
        )
        edge_type = self.task.channels.ci_count_edges_active_edge
        decm_result = DigitalEdgeCountMeasurementResultData(
            edge_count=edge_count, edge_type=edge_type
        )
        return decm_result

    def close(self):
        """Closes the task and returns the hardware resources"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
        if not self.is_task_initialized:
            return

        # stop and close DAQmx task
        self.task.stop()
        self.task.close()
