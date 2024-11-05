"Constants used in digital edge count measurement"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)

import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters' imported but unused (auto-generated noqa)
    DigitalStartTriggerParameters,
    StartTriggerType,
)


@dataclasses.dataclass
class ConstantsForDigitalEdgeCountMeasurement:
    """Constants used in digital edge count measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)

    DEFAULT_INITIAL_COUNT = 0
    DEFAULT_COUNT_DIRECTION = nidaqmx.constants.CountDirection.COUNT_UP
    DEFAULT_EDGE = nidaqmx.constants.Edge.RISING

    DEFAULT_LOW_TIME = 0.000001
    DEFAULT_HIGH_TIME = 0.001
    DEFAULT_TIME_UNITS = nidaqmx.constants.TimeUnits.SECONDS
    DEFAULT_IDLE_STATE = nidaqmx.constants.Level.LOW

    DEFAULT_PAUSE_TRIGGER_TYPE = nidaqmx.constants.TriggerType.DIGITAL_LEVEL
    DEFAULT_PAUSE_DIGITAL_LEVEL_STATE = nidaqmx.constants.Level.LOW
    DEFAULT_TRIGGER_TIMEOUT = 10.0

    FINITE_SAMPLES = nidaqmx.constants.AcquisitionType.FINITE
    TIME_OUT = 10.0
