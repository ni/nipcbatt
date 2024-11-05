"Constant data types used in digital clock generation"

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalClockGeneration:
    """Constants used in digital clock generation"""

    DEFAULT_FREQUENCY_GENERATION_UNIT = nidaqmx.constants.FrequencyUnits.HZ
    DEFAULT_GENERATION_IDLE_STATE = nidaqmx.constants.PowerUpStates.LOW
    DEFAULT_GENERATION_FREQUENCY = 1.0
    DEFAULT_GENERATION_DUTY_CYCLE = 0.5
    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
