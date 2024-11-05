"""Private module that provides a set of helper functions 
   for `square_waveform` module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (328 > 100 characters) (auto-generated noqa)

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
    """Creates samples of a square waveform described through its characteristics."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)

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
