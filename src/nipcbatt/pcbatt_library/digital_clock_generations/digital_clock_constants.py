"Constant data types used in digital clock generation"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalClockGeneration:
    """Constants used in digital clock generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)

    DEFAULT_FREQUENCY_GENERATION_UNIT = nidaqmx.constants.FrequencyUnits.HZ
    DEFAULT_GENERATION_IDLE_STATE = nidaqmx.constants.PowerUpStates.LOW
    DEFAULT_GENERATION_FREQUENCY = 1.0
    DEFAULT_GENERATION_DUTY_CYCLE = 0.5
    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
