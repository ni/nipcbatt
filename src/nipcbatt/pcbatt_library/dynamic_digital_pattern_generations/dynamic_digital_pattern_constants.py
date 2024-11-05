"Constants used in dynamic digital pattern generation"

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDynamicDigitalPatternGeneration:
    """Constants used for dynamic digital pattern generation"""

    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
    DEFAULT_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_TRIGGER_TYPE = nidaqmx.constants.TriggerType.NONE
