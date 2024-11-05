"""Provides multiple tones waveform creation API."""

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.common_types import WaveformTone
from nipcbatt.pcbatt_analysis.waveform_creation._waveform_creation_internal import (
    _multitones_waveform,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def create_multitones_waveform(
    multitones_amplitude: float,
    waveform_tones: list[WaveformTone],
    samples_count: int,
    sampling_rate: float,
    amplitude_normalization_threshold: float = 0.000001,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a multi-tones waveform described through its characteristics.

    Args:
        multitones_amplitude (float): amplitude of the multi-tones waveform,
        must be greater than zero.
        waveform_tones (list[WaveformTone]): describes the distribution of tones
        that will be contained in the created waveform.
        samples_count (int): number of samples that will be created for the multi-tones waveform.
        sampling_rate (float): sampling rate of the multi-tones waveform.
        amplitude_normalization_threshold(float): when waveform maximum is greater than it,
            normalization of the amplitude is applied to match input `multitones_amplitude`.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when samples_count is less or equal zero,
            when sampling_rate is less or equal zero,
            and when amplitude_normalization_threshold is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created multi-tones waveform.
    """
    Guard.is_greater_than_zero(multitones_amplitude, nameof(multitones_amplitude))
    Guard.is_greater_than_zero(samples_count, nameof(samples_count))
    Guard.is_greater_than_zero(sampling_rate, nameof(sampling_rate))
    Guard.is_greater_than_zero(
        amplitude_normalization_threshold, nameof(amplitude_normalization_threshold)
    )

    try:
        return _multitones_waveform.create_multitones_waveform_impl(
            multitones_amplitude,
            waveform_tones,
            samples_count,
            sampling_rate,
            amplitude_normalization_threshold,
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.MULTIPLE_TONES_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON
        ) from e
