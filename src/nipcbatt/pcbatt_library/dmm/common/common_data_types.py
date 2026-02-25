"""Common data types for DMM measurements."""

from enum import Enum

import nidmm


class ResolutionInDigits(Enum):
    """Defines the resolution settings for DMM measurements."""

    DIGITS_3_5 = 3.5
    DIGITS_4_5 = 4.5
    DIGITS_5_5 = 5.5
    DIGITS_6_5 = 6.5
    DIGITS_7_5 = 7.5


class Slope(Enum):
    """Defines the slope settings for DMM measurements."""

    RISING_EDGE = 0
    FALLING_EDGE = 1


class TriggerParameters:
    """Parameters for configuring trigger settings in DMM measurements."""

    def __init__(
        self,
        trigger_source: nidmm.TriggerSource,
        trigger_delay: float,
        slope: Slope,
        enable_trigger: bool,
    ) -> None:
        """Initializes the trigger parameters.

        Args:
            trigger_source (nidmm.TriggerSource):
                The trigger source for the measurement.
            trigger_delay (float):
                The delay in seconds between the trigger and the start of measurement.
            slope (Slope):
                The trigger slope (rising or falling edge).
            enable_trigger (bool):
                Whether triggering is enabled for the measurement.
        """
        self._trigger_source = trigger_source
        self._trigger_delay = trigger_delay
        self._slope = slope
        self._enable_trigger = enable_trigger

    @property
    def trigger_source(self) -> nidmm.TriggerSource:
        """Gets the trigger source.

        Returns:
            nidmm.TriggerSource: The trigger source for the measurement.
        """
        return self._trigger_source

    @property
    def trigger_delay(self) -> float:
        """Gets the trigger delay.

        Returns:
            float: The delay in seconds between trigger and measurement start.
        """
        return self._trigger_delay

    @property
    def trigger_slope(self) -> Slope:
        """Gets the trigger slope.

        Returns:
            Slope: The trigger slope (rising or falling edge).
        """
        return self._slope

    @property
    def enable_trigger(self) -> bool:
        """Gets whether triggering is enabled.

        Returns:
            bool: True if triggering is enabled, False otherwise.
        """
        return self._enable_trigger


class TimingParameters:
    """Parameters for configuring timing settings in DMM measurements."""

    def __init__(
        self,
        aperture_time_seconds: float,
        settle_time_seconds: float,
    ) -> None:
        """Initializes the timing parameters.

        Args:
            aperture_time_seconds (float):
                The aperture time in seconds for the measurement.
            settle_time_seconds (float):
                The settle time in seconds before taking a measurement.
        """
        self._aperture_time_seconds = aperture_time_seconds
        self._settle_time_seconds = settle_time_seconds

    @property
    def aperture_time_seconds(self) -> float:
        """Gets the aperture time.

        Returns:
            float: The aperture time in seconds.
        """
        return self._aperture_time_seconds

    @property
    def settle_time_seconds(self) -> float:
        """Gets the settle time.

        Returns:
            float: The settle time in seconds.
        """
        return self._settle_time_seconds
