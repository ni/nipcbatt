"""Private module that provides a set of helper functions 
   for `square_waveform` module."""

import math

import numpy
import scipy.signal

from nipcbatt.pcbatt_utilities import numeric_utilities


def create_square_waveform_impl(
    amplitude: float,
    frequency: float,
    duty_cycle: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a square waveform described through its characteristics."""

    sampling_period = numeric_utilities.invert_value(sampling_rate)
    waveform_period = numeric_utilities.invert_value(frequency)

    square_waveform_phase_rounded = phase % (2 * numpy.pi)
    square_wave_delay_from_phase = math.floor(
        sampling_rate * (square_waveform_phase_rounded * waveform_period / (2 * numpy.pi))
    )

    x = numpy.fromiter(
        map(lambda sample_index: sample_index * sampling_period, range(0, samples_count)),
        dtype=numpy.float64,
    )
    y = scipy.signal.square(t=(2 * numpy.pi * frequency) * x, duty=duty_cycle)

    for sample_index in range(0, y.size):
        y[sample_index] = amplitude * y[sample_index] + offset

    return numpy.roll(y, square_wave_delay_from_phase)
