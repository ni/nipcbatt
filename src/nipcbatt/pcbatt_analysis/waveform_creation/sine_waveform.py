"""Provides sine waveform creation API."""

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.waveform_creation._waveform_creation_internal import (
    _sine_waveform,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def create_cosine_waveform(
    amplitude: float,
    frequency: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a sine waveform described through its characteristics, using math.cos.

    Args:
        amplitude (float): amplitude of the sinusoid, must be greater than zero.
        frequency (float): frequency of the sinusoid, must be greater than zero.
        phase (float): phase of the sinusoid, will be rounded modulo 2*PI.
        offset (float): vertical offset of the sinusoid, will be used to translated y-axis values.
        samples_count (int): number of samples that will be created for the sinusoid.
        sampling_rate (float): sampling rate of the sinusoid.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when amplitude is less or equal zero,
            occurs when frequency is less or equal zero,
            occurs when samples_count is less or equal zero,
            occurs when sampling_rate is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created sine waveform.
    """
    Guard.is_greater_than_zero(value=amplitude, value_name=nameof(amplitude))
    Guard.is_greater_than_zero(value=frequency, value_name=nameof(frequency))
    Guard.is_greater_than_zero(value=samples_count, value_name=nameof(samples_count))
    Guard.is_greater_than_zero(value=sampling_rate, value_name=nameof(sampling_rate))

    try:
        return _sine_waveform.create_cosine_waveform_impl(
            amplitude, frequency, phase, offset, samples_count, sampling_rate
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SINE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON
        ) from e


def create_sine_waveform(
    amplitude: float,
    frequency: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a sine waveform described through its characteristics, using math.sin.

    Args:
        amplitude (float): amplitude of the sinusoid, must be greater than zero.
        frequency (float): frequency of the sinusoid, must be greater than zero.
        phase (float): phase of the sinusoid, will be rounded modulo 2*PI.
        offset (float): vertical offset of the sinusoid, will be used to translated y-axis values.
        samples_count (int): number of samples that will be created for the sinusoid.
        sampling_rate (float): sampling rate of the sinusoid.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when amplitude is less or equal zero,
            occurs when frequency is less or equal zero,
            occurs when samples_count is less or equal zero,
            and occurs when sampling_rate is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created sine waveform.
    """
    Guard.is_greater_than_zero(value=amplitude, value_name=nameof(amplitude))
    Guard.is_greater_than_zero(value=frequency, value_name=nameof(frequency))
    Guard.is_greater_than_zero(value=samples_count, value_name=nameof(samples_count))
    Guard.is_greater_than_zero(value=sampling_rate, value_name=nameof(sampling_rate))

    try:
        return _sine_waveform.create_sine_waveform_impl(
            amplitude, frequency, phase, offset, samples_count, sampling_rate
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SINE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON
        ) from e
