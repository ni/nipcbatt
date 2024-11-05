"""Provides square waveform creation API."""

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.waveform_creation._waveform_creation_internal import (
    _square_waveform,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def create_square_waveform(
    amplitude: float,
    frequency: float,
    duty_cycle: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a square waveform described through its characteristics.

    Args:
        amplitude (float): amplitude of the square wave, must be greater than zero.
        frequency (float): frequency of the square wave, must be greater than zero.
        duty_cycle (float): duty cycle of the square wave, must be in [0,1].
        phase (float): phase of the square wave, will be rounded modulo 2*PI.
        offset (float): vertical offset of the square wave,
        will be used to translated y-axis values.
        samples_count (int): number of samples that will be created for the square wave.
        sampling_rate (float): sampling rate of the square wave.

    Raises:
        PCBATTAnalysisException: occurs when waveform creation fails for some reason.
        ValueError: occurs when amplitude is less or equal zero,
            occurs when `frequency` is less or equal zero,
            occurs when `samples_count` is less or equal zero,
            and occurs when `sampling_rate` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: samples constituting created square waveform.
    """
    Guard.is_greater_than_zero(value=amplitude, value_name=nameof(amplitude))
    Guard.is_greater_than_zero(value=frequency, value_name=nameof(frequency))
    Guard.is_within_limits_included(
        value=duty_cycle, lower_limit=0, upper_limit=1, value_name=nameof(duty_cycle)
    )
    Guard.is_greater_than_zero(value=samples_count, value_name=nameof(samples_count))
    Guard.is_greater_than_zero(value=sampling_rate, value_name=nameof(sampling_rate))

    try:
        return _square_waveform.create_square_waveform_impl(
            amplitude,
            frequency,
            duty_cycle,
            phase,
            offset,
            samples_count,
            sampling_rate,
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SQUARE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON
        ) from e
