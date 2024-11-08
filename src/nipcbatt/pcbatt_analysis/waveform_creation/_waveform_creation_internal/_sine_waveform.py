"""Private module that provides a set of helper functions
   for `sine_waveform` module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (326 > 100 characters) (auto-generated noqa)

import math

import numpy


def create_cosine_waveform_impl(
    amplitude: float,
    frequency: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a cosine waveform described through its characteristics."""
    phase = phase % (2.0 * numpy.pi)
    samples_array = numpy.zeros(shape=samples_count)

    numerator = 2.0 * numpy.pi * frequency / sampling_rate

    for sample_index in range(0, samples_count):
        samples_array[sample_index] = offset + amplitude * math.cos(
            phase + sample_index * numerator
        )

    return samples_array


def create_sine_waveform_impl(
    amplitude: float,
    frequency: float,
    phase: float,
    offset: float,
    samples_count: int,
    sampling_rate: float,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a sine waveform described through its characteristics."""
    phase = phase % (2.0 * numpy.pi)
    samples_array = numpy.zeros(shape=samples_count)

    numerator = 2.0 * numpy.pi * frequency / sampling_rate

    for sample_index in range(0, samples_count):
        samples_array[sample_index] = offset + amplitude * math.sin(
            phase + sample_index * numerator
        )

    return samples_array
