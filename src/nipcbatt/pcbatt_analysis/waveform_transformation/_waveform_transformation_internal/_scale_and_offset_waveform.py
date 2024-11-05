"""Private module that provides a set of helper functions
   for `scale_and_offset_waveform` module."""

import numpy


def scale_and_apply_offset_impl(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float
) -> numpy.ndarray[numpy.float64]:
    """Implementation of scale and offset waveform."""
    result_array = numpy.fromiter(
        iter=map(
            lambda waveform_sample: scale_factor * waveform_sample + offset,
            waveform_samples,
        ),
        dtype=numpy.float64,
    )

    return result_array


def scale_and_apply_offset_inplace_impl(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float
) -> numpy.ndarray[numpy.float64]:
    """Implementation of scale and offset waveform in place."""
    for sample_index in range(0, waveform_samples.size):
        waveform_samples[sample_index] = scale_factor * waveform_samples[sample_index] + offset
    return waveform_samples
