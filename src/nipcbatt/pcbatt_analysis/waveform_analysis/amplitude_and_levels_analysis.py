"""Provides Amplitude And Levels analysis tools"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)

from enum import IntEnum
from typing import Iterable

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.waveform_analysis._waveform_analysis_internal import (
    _amplitude_and_levels_analysis,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class AmplitudeAndLevelsProcessingResult(AnalysisLibraryElement):
    """Defines Amplitude and Levels processing results"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)

    def __init__(self, amplitude: float, high_state_level: float, low_state_level: float) -> None:
        """Initialize an instance of Amplitude and Levels processing result.

        Args:
            amplitude (float): Amplitude value obtained after processing waveform.
            high_state_level (float): High state level obtained after processing waveform.
            low_state_level (float): Low state level obtained after processing waveform.
        """
        self._amplitude = amplitude
        self._high_state_level = high_state_level
        self._low_state_level = low_state_level

    @property
    def amplitude(self) -> float:
        """Gets amplitude value obtained after processing waveform.

        Returns:
            float: amplitude is the difference between high state level and low state level.
        """
        return self._amplitude

    @property
    def high_state_level(self) -> float:
        """Gets high state level value obtained after processing waveform.

        Returns:
            float: High state level value.
        """
        return self._high_state_level

    @property
    def low_state_level(self) -> float:
        """Gets low state level value obtained after processing waveform.

        Returns:
            float: Low state level value.
        """
        return self._low_state_level


class AmplitudeAndLevelsProcessingMethod(IntEnum):
    """Defines Amplitude and levels processing method"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)

    HISTOGRAM = 0
    """Strategy is based on histogram analysis to estimate waveform states."""

    PEAK = 1
    """Strategy is based on maximum/minimum analysis to estimate waveform states."""

    AUTO_SELECT = 2
    """Strategy is automatically selected by labview, 
    it is a combination of histogram and peak strategies."""


class LabViewAmplitudeAndLevels(AnalysisLibraryElement):
    """Provides Amplitude and Levels processing based on LabVIEW Amplitude and Levels VI"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (202 > 100 characters) (auto-generated noqa)

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occurred error of
        `Amplitude and levels` processing labview VI.

        Returns:
            str: Empty string when no error occured, elsewhere not empty string.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return _amplitude_and_levels_analysis.labview_get_last_error_message_impl()

    @staticmethod
    def process_single_waveform_amplitude_and_levels(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        amplitude_and_levels_processing_method: AmplitudeAndLevelsProcessingMethod,
        histogram_size: int,
    ) -> AmplitudeAndLevelsProcessingResult:
        """Processes amplitude and levels of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): samples of the waveform to process.
            waveform_sampling_period_seconds (float): sampling period of the waveform to process.
            amplitude_and_levels_processing_method (AmplitudeAndLevelsProcessingMethod):
                amplitude and levels processing method.
            histogram_size (int):
                histogram bins count that will be used when labview decides to use histogram method.

        Raises:
            PCBATTAnalysisException:
                Occurs when amplitude and levels processing fails for some reason.

        Returns:
            AmplitudeAndLevelsProcessingResult: An object that holds result of amplitude and levels
            processing result using LabVIEW VI.
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )
        Guard.is_greater_than_zero(histogram_size, nameof(histogram_size))
        try:
            tuple_result = _amplitude_and_levels_analysis.labview_process_single_waveform_amplitude_and_levels_impl(
                waveform_samples,
                waveform_sampling_period_seconds,
                amplitude_and_levels_processing_method,
                histogram_size,
            )

            # Build object from tuple
            return AmplitudeAndLevelsProcessingResult(
                tuple_result[0], tuple_result[1], tuple_result[2]
            )
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.AMPLITUDE_AND_LEVELS_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e

    @staticmethod
    def process_multiple_waveforms_amplitude_and_levels(
        waveforms_samples: Iterable[numpy.ndarray[numpy.float64]],
        waveforms_sampling_period_seconds: float,
        amplitude_and_levels_processing_method: AmplitudeAndLevelsProcessingMethod,
        histogram_size: int,
    ) -> Iterable[AmplitudeAndLevelsProcessingResult]:
        """Processes amplitude and levels of given waveforms samples provided as iterable object using LabVIEW VI

        Args:
            waveforms_samples (Iterable[numpy.ndarray[numpy.float64]]): iterable of single waveforms.
            waveforms_sampling_period_seconds (float): common sampling rate of all waveforms.
            amplitude_and_levels_processing_method (AmplitudeAndLevelsProcessingMethod): amplitude and levels processing method.
            histogram_size (int): histogram bins count that will be used when labview decides to use histogram method.

        Raises:
            PCBATTAnalysisException:
                Occurs when amplitude and levels processing fails for some reason.

        Returns:
            Iterable[AmplitudeAndLevelsProcessingResult]: An iterable of objects that hold result of
            amplitude and levels processing of each input waveform using LabVIEW VI.

        Yields:
            Iterator[Iterable[AmplitudeAndLevelsProcessingResult]]: objects that hold result of
            amplitude and levels processing of each input waveform using LabVIEW VI.
        """  # noqa: W505, D415 - doc line too long (113 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)
        Guard.is_not_none(waveforms_samples, nameof(waveforms_samples))
        Guard.is_greater_than_zero(
            waveforms_sampling_period_seconds, nameof(waveforms_sampling_period_seconds)
        )
        Guard.is_greater_than_zero(histogram_size, nameof(histogram_size))

        for waveform_samples in waveforms_samples:
            yield LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
                waveform_samples,
                waveforms_sampling_period_seconds,
                amplitude_and_levels_processing_method,
                histogram_size,
            )
