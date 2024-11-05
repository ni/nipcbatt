"Constant datatypes for use in digital frequency measurement"

import dataclasses

import nidaqmx.constants


@dataclasses.dataclass
class ConstantsForDigitalFrequencyMeasurement:
    "Constants used in digital frequency measurement"
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
