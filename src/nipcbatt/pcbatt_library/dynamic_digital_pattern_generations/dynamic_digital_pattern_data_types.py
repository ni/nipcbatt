""" Dynamic digital pattern data types """

import nidaqmx.constants
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import DynamicDigitalPatternTimingParameters
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DynamicDigitalStartTriggerParameters(PCBATestToolkitData):
    """Defines parameters for dynamic digital pattern trigger start"""

    def __init__(
        self,
        digital_start_trigger_source: str,
        digital_start_trigger_edge: nidaqmx.constants.Edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE,
        trigger_type: nidaqmx.constants.TriggerType = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE,
    ) -> None:
        """Creates an instance of DynamicDigitalStartTriggerParameters

        Args:
            digital_start_trigger_source (str): The phyiscal line to obtain the trigger
            digital_start_trigger_edge (nidaqmx.constants.Edge, optional): The edge on which to trigger.
                Defaults to ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE.
            trigger_type (nidaqmx.constants.TriggerType, optional): The type of trigger being used.
                Defaults to ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE.
        """

        # input validation
        Guard.is_not_none(digital_start_trigger_source, nameof(digital_start_trigger_source))
        Guard.is_not_empty(digital_start_trigger_source, nameof(digital_start_trigger_source))
        Guard.is_not_none(digital_start_trigger_edge, nameof(digital_start_trigger_edge))
        Guard.is_not_none(trigger_type, nameof(trigger_type))

        # assign values
        self._digital_start_trigger_source = digital_start_trigger_source
        self._digital_start_trigger_edge = digital_start_trigger_edge
        self._trigger_type = trigger_type

    @property
    def digital_start_trigger_source(self) -> str:
        """
        :type:str: The source of the digital start trigger
        """
        return self._digital_start_trigger_source

    @property
    def digital_start_trigger_edge(self) -> nidaqmx.constants.Edge:
        """
        :type:nidaqmx.constants.Edge: The edge on which to trigger
        """
        return self._digital_start_trigger_edge

    @property
    def trigger_type(self) -> nidaqmx.constants.TriggerType:
        """
        :type:nidaqmx.constants.TriggerType: The type of trigger used
        """
        return self._trigger_type


class DynamicDigitalPatternGenerationData(PCBATestToolkitData):
    """Contains the data returned from dynamic digital pattern generation"""

    def __init__(self, generation_time_seconds: float) -> None:
        """Creates an instance of DynamicDigitalPatternGenerationData

        Args:
            generation_time_seconds (float): The length of the generation time in seconds
        """

        # input validation
        Guard.is_not_none(generation_time_seconds, nameof(generation_time_seconds))
        Guard.is_float(generation_time_seconds, nameof(generation_time_seconds))
        Guard.is_greater_than_or_equal_to_zero(
            generation_time_seconds, nameof(generation_time_seconds)
        )

        # assign values
        self._generation_time_seconds = generation_time_seconds

    @property
    def generation_time_seconds(self) -> float:
        """
        :type:float: The length of the generation time in seconds
        """
        return self._generation_time_seconds


class DynamicDigitalPatternGenerationConfiguration(PCBATestToolkitData):
    """Contains the parameters for configuration of digital pattern generation"""

    def __init__(
        self,
        timing_parameters: DynamicDigitalPatternTimingParameters,
        digital_start_trigger_parameters: DynamicDigitalStartTriggerParameters,
        pulse_signal: np.ndarray,
    ) -> None:
        """Creates an instance of DynamicDigitalPatternGenerationConfiguration

        Args:
            timing_parameters (DynamicDigitalPatternTimingParameters): A valid instance
                of DynamicDigitalPatternTimingParameters
            digital_start_trigger_parameters (DynamicDigitalStartTriggerParameters): A
                valid instance of DynamicDigitalStartTriggerParameters
        """

        # input validation
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        # assign values
        self._timing_parameters = timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters
        self._pulse_signal = pulse_signal

    @property
    def timing_parameters(self) -> DynamicDigitalPatternTimingParameters:
        """
        :type:DynamicDigitalPatternTimingParameters
        """
        return self._timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DynamicDigitalStartTriggerParameters:
        """
        :type: DynamicDigitalStartTriggerParameters
        """
        return self._digital_start_trigger_parameters

    @property
    def pulse_signal(self) -> np.ndarray:
        """
        :type: Numpy array
        """
        return self._pulse_signal
