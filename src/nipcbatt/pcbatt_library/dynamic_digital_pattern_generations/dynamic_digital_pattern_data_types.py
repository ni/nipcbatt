""" Dynamic digital pattern data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (153 > 100 characters) (auto-generated noqa)

import nidaqmx.constants
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DynamicDigitalPatternTimingParameters,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DynamicDigitalStartTriggerParameters(PCBATestToolkitData):
    """Defines parameters for dynamic digital pattern trigger start"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_source

    @property
    def digital_start_trigger_edge(self) -> nidaqmx.constants.Edge:
        """
        :type:nidaqmx.constants.Edge: The edge on which to trigger
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_edge

    @property
    def trigger_type(self) -> nidaqmx.constants.TriggerType:
        """
        :type:nidaqmx.constants.TriggerType: The type of trigger used
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._trigger_type


class DynamicDigitalPatternGenerationData(PCBATestToolkitData):
    """Contains the data returned from dynamic digital pattern generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)

    def __init__(self, generation_time_seconds: float) -> None:
        """Creates an instance of DynamicDigitalPatternGenerationData

        Args:
            generation_time_seconds (float): The length of the generation time in seconds
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._generation_time_seconds


class DynamicDigitalPatternGenerationConfiguration(PCBATestToolkitData):
    """Contains the parameters for configuration of digital pattern generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (192 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D202, D415, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (275 > 100 characters) (auto-generated noqa)

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
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DynamicDigitalStartTriggerParameters:
        """
        :type: DynamicDigitalStartTriggerParameters
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters

    @property
    def pulse_signal(self) -> np.ndarray:
        """
        :type: Numpy array
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._pulse_signal
