"""Private module that provides a set of helper functions
   for `scale_and_offset_waveform` module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (338 > 100 characters) (auto-generated noqa)

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
