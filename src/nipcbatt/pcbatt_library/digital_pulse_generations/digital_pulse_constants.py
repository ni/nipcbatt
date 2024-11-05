"Constants used in digital pulse generation"

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalPulseGeneration:
    """Constants used in digital pulse generation"""

    DEFAULT_GENERATION_IDLE_STATE = nidaqmx.constants.Level.LOW
    DEFAULT_FREQUENCY_GENERATION_UNIT = nidaqmx.constants.TimeUnits.SECONDS
    DEFAULT_LOW_TIME = 0.01
    DEFAULT_HIGH_TIME = 0.01
    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
