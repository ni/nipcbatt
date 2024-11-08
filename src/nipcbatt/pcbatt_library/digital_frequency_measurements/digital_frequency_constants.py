"Constant datatypes for use in digital frequency measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalFrequencyMeasurement:
    "Constants used in digital frequency measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
    DEFAULT_FREQUENCY_COUNTER_METHOD = (
        nidaqmx.constants.CounterFrequencyMethod.LARGE_RANGE_2_COUNTERS
    )
    DEFAULT_FREQUENCY_MEASURE_UNIT = nidaqmx.constants.FrequencyUnits.HZ
    DEFAULT_FREQUENCY_STARTING_EDGE = nidaqmx.constants.Edge.RISING
    DEFAULT_MEAS_TIME = 0.001
    DEFAULT_MIN_VALUE = 1.0
    DEFAULT_MAX_VALUE = 2.0e6
    DEFAULT_TIME_OUT = 10.0
    DEFAULT_INPUT_DIVISOR = 4
