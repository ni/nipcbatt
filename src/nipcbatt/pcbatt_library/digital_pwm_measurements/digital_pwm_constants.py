"Constant datatypes for use in digital frequency measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalPwmMeasurement:
    "Constants used in digital pwm measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (158 > 100 characters) (auto-generated noqa)
    DEFAULT_PWM_STARTING_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_MIN_SEMIPERIOD = 20e-9
    DEFAULT_MAX_SEMIPERIOD = 42.949672
    DEFAULT_TIME_UNITS = nidaqmx.constants.TimeUnits.SECONDS
    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
