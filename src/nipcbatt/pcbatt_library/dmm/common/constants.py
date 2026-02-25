"""Constants for DMM measurements."""

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    Slope,
)


class ConstantsForDcRmsMeasurements:
    """Encapsulates the constants for DMM measurements."""

    DEFAULT_POWERLINE_FREQUENCY = 50.0

    DEFAULT_RESOLUTION_IN_DIGITS = ResolutionInDigits.DIGITS_5_5

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_AND_MEASURE

    DEFAULT_APERTURE_TIME_SECONDS = -1.0
    DEFAULT_SETTLE_TIME_SECONDS = -1.0
    DEFAULT_AC_MIN_FREQUENCY = 40.0

    DEFAULT_TRIGGER_SOURCE = nidmm.TriggerSource.IMMEDIATE
    DEFAULT_TRIGGER_DELAY = -1.0
    DEFAULT_ENABLE_TRIGGER = False
    DEFAULT_TRIGGER_SLOPE = Slope.RISING_EDGE
