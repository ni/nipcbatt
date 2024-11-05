"Constants used in dynamic digital pattern measurement"

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    StartTriggerType,
)


@dataclasses.dataclass
class ConstantsForDynamicDigitalPatternMeasurement:
    """Constants used in dynamic didgital pattern measurement"""

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 1000
    DEFAULT_ACTIVE_EDGE = nidaqmx.constants.Edge.RISING

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING

    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
    TIME_OUT = 10.0
