"Constants used in digital pulse generation"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (155 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalPulseGeneration:
    """Constants used in digital pulse generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)

    DEFAULT_GENERATION_IDLE_STATE = nidaqmx.constants.Level.LOW
    DEFAULT_FREQUENCY_GENERATION_UNIT = nidaqmx.constants.TimeUnits.SECONDS
    DEFAULT_LOW_TIME = 0.01
    DEFAULT_HIGH_TIME = 0.01
    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
