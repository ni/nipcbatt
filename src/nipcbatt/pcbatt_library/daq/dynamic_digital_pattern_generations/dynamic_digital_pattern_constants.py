"Constants used in dynamic digital pattern generation"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDynamicDigitalPatternGeneration:
    """Constants used for dynamic digital pattern generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)

    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
    DEFAULT_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_TRIGGER_TYPE = nidaqmx.constants.TriggerType.NONE
