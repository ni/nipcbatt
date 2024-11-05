"Constant datatypes for use in digital frequency measurement"

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalPwmMeasurement:
    "Constants used in digital pwm measurement"
    DEFAULT_PWM_STARTING_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_MIN_SEMIPERIOD = 20e-9
    DEFAULT_MAX_SEMIPERIOD = 42.949672
    DEFAULT_TIME_UNITS = nidaqmx.constants.TimeUnits.SECONDS
    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
