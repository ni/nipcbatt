"""  digital edge count data types """

import nidaqmx.constants
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementOptions,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_constants import (
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DigitalEdgeCountMeasurementCounterChannelParameters(PCBATestToolkitData):
    """Defines the settings counter channel edge for measurement."""

    def __init__(
        self,
        edge_type: nidaqmx.constants.Edge = ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE,
    ) -> None:
        """Used to initialize an instance of `DigitalEdgeCountMeasurementCounterChannelParameters`.

        Args:
            edge_type (nidaqmx.constants.Edge): The `nidaqmx.constants.Edge` value that specifies on which edge
            of a digital pulse the counter increments.

        Raises:
            ValueError:
                if 'active_edge' is None.
        """
        # Input validation
        Guard.is_not_none(edge_type, nameof(edge_type))

        self._edge_type = edge_type

    @property
    def edge_type(self) -> nidaqmx.constants.Edge:
        """Gets the edge type for counter."""
        return self._edge_type


class DigitalEdgeCountMeasurementTimingParameters(PCBATestToolkitData):
    """Defines the timing settings for edge count measurement."""

    def __init__(
        self,
        edge_counting_duration: float = 0.1,
    ) -> None:
        """Used to initialize an instance of `DigitalEdgeCountMeasurementTimingParameters`.

        Args:
            edge_counting_duration (float): The value that specifies the duration of edge count measurement.

        Raises:
            ValueError:
                if 'edge_counting_duration' is less than zero and None.
        """
        # Input validation
        Guard.is_not_none(edge_counting_duration, nameof(edge_counting_duration))
        Guard.is_greater_than_or_equal_to_zero(
            edge_counting_duration, nameof(edge_counting_duration)
        )

        self._edge_counting_duration = edge_counting_duration

    @property
    def edge_counting_duration(self) -> float:
        """Gets the duration for edge count measurement."""
        return self._edge_counting_duration


class DigitalEdgeCountHardwareTimerConfiguration(PCBATestToolkitData):
    """Defines a configuration for hardware timer digital edge count measurement"""

    def __init__(
        self,
        measurement_options: MeasurementOptions,
        counter_channel_parameters: DigitalEdgeCountMeasurementCounterChannelParameters,
        timing_parameters: DigitalEdgeCountMeasurementTimingParameters,
        trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `DigitalEdgeCountHardwareTimerConfiguration`.

        Args:
            measurement_options (MeasurementOptions):
                The type of measurement options selected by user.
            counter_channel_parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
                An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` that represents the settings of edge_type.
            timing_parameters (DigitalEdgeCountMeasurementTimingParameters):
                An instance of 'DigitalEdgeCountMeasurementTimingParameters' that represents the duration of edge count measurement.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            ValueError:
                'measurement_options' is None,
                `counter_channel_parameters` is None,
                'timing_parameters' is None or less than zero,
                `trigger_parameters` is None,
        """
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(counter_channel_parameters, nameof(counter_channel_parameters))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))
        Guard.is_not_none(trigger_parameters, nameof(trigger_parameters))

        self._measurement_options = measurement_options
        self._counter_channel_parameters = counter_channel_parameters
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """
        return self._measurement_options

    @property
    def counter_channel_parameters(self) -> DigitalEdgeCountMeasurementCounterChannelParameters:
        """
        :class:`DigitalEdgeCountMeasurementCounterChannelParameters`:
            Gets a `DigitalEdgeCountMeasurementCounterChannelParameters` instance
            that represents the settings of edge_type to be counted.
        """
        return self._counter_channel_parameters

    @property
    def timing_parameters(self) -> DigitalEdgeCountMeasurementTimingParameters:
        """
        :class:`DigitalEdgeCountMeasurementTimingParameters`:
            Gets a `DigitalEdgeCountMeasurementTimingParameters` instance
            that represents the settings of the time duration in which number of edges to be counted.
        """
        return self._timing_parameters

    @property
    def trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """
        return self._trigger_parameters


class DigitalEdgeCountSoftwareTimerConfiguration(PCBATestToolkitData):
    """Defines a configuration for software timer digital edge count measurement"""

    def __init__(
        self,
        measurement_options: MeasurementOptions,
        counter_channel_parameters: DigitalEdgeCountMeasurementCounterChannelParameters,
        timing_parameters: DigitalEdgeCountMeasurementTimingParameters,
    ) -> None:
        """Initializes an instance of
        `DynamicDigitalPatternMeasurementConfiguration`.

        Args:
            measurement_options (MeasurementOptions):
                The type of measurement options selected by user.
            counter_channel_parameters (DigitalEdgeCountMeasurementCounterChannelParameters):
                An instance of `DigitalEdgeCountMeasurementCounterChannelParameters` that represents the settings of edge_type.
            timing_parameters (DigitalEdgeCountMeasurementTimingParameters):
                An instance of 'DigitalEdgeCountMeasurementTimingParameters' that represents the duration of edge count measurement.

        Raises:
            ValueError:
                'measurement_options' is None,
                `counter_channel_parameters` is None,
                'timing_parameters' is None or less than zero,
        """
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(counter_channel_parameters, nameof(counter_channel_parameters))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))

        self._measurement_options = measurement_options
        self._counter_channel_parameters = counter_channel_parameters
        self._timing_parameters = timing_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """
        return self._measurement_options

    @property
    def counter_channel_parameters(self) -> DigitalEdgeCountMeasurementCounterChannelParameters:
        """
        :class:`DigitalEdgeCountMeasurementCounterChannelParameters`:
            Gets a `DigitalEdgeCountMeasurementCounterChannelParameters` instance
            that represents the settings of edge_type to be counted.
        """
        return self._counter_channel_parameters

    @property
    def timing_parameters(self) -> DigitalEdgeCountMeasurementTimingParameters:
        """
        :class:`DigitalEdgeCountMeasurementTimingParameters`:
            Gets a `DigitalEdgeCountMeasurementTimingParameters` instance
            that represents the settings of the time duration in which number of edges to be counted.
        """
        return self._timing_parameters


class DigitalEdgeCountMeasurementResultData(PCBATestToolkitData):
    """Defines the values returned from the digital edge count measurement"""

    def __init__(self, edge_count: int, edge_type: nidaqmx.constants.Edge) -> None:
        """Initializes an instance of 'DigitalEdgeCountMeasurementResultData'
        with specific values

        Args:
            edge_count: int
           edge_type: nidaqmx.constants.Edge

        Raises: ValueError when,
            1) edge_count is None
            2) edge_count is less than zero
            3) edge_type is None
        """

        # input validation
        Guard.is_not_none(edge_count, nameof(edge_count))
        Guard.is_greater_than_or_equal_to_zero(edge_count, nameof(edge_count))
        Guard.is_not_none(edge_type, nameof(edge_type))

        # assign to member variable
        self._edge_count = edge_count
        self._edge_type = edge_type

    @property
    def edge_count(self) -> int:
        """
        :type:'int': Edge count data captured from the measurement
        """
        return self._edge_count

    @property
    def edge_type(self) -> nidaqmx.constants.Edge:
        """
        :type:'nidaqmx.constants.Edge': Data captured from the measurement
        """
        return self._edge_type
