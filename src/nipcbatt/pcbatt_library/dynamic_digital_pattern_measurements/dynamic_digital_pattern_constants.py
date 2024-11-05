"Constants used in dynamic digital pattern measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (166 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters' imported but unused (auto-generated noqa)
    DigitalStartTriggerParameters,
    StartTriggerType,
)


@dataclasses.dataclass
class ConstantsForDynamicDigitalPatternMeasurement:
    """Constants used in dynamic didgital pattern measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 1000
    DEFAULT_ACTIVE_EDGE = nidaqmx.constants.Edge.RISING

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING

    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
    TIME_OUT = 10.0
