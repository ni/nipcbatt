"""Private module that provides a set of helper functions 
   for `multitones_waveform` module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (332 > 100 characters) (auto-generated noqa)

import math

import numpy

from nipcbatt.pcbatt_analysis.common.common_types import WaveformTone
from nipcbatt.pcbatt_analysis.waveform_transformation import (  # noqa: F401 - 'nipcbatt.pcbatt_analysis.waveform_transformation.scale_and_offset_waveform' imported but unused (auto-generated noqa)
    scale_and_offset_waveform,
)
from nipcbatt.pcbatt_utilities import (  # noqa: F401 - 'nipcbatt.pcbatt_utilities.numeric_utilities' imported but unused (auto-generated noqa)
    numeric_utilities,
)


def create_multitones_waveform_impl(
    amplitude: float,
    waveform_tones: list[WaveformTone],
    samples_count: int,
    sampling_rate: float,
    amplitude_normalization_threshold: float = 0.000001,
) -> numpy.ndarray[numpy.float64]:
    """Creates samples of a multitones waveform described through its characteristics."""
    result_waveform: numpy.ndarray[numpy.float64] = numpy.zeros(shape=samples_count)

    # fill sum of sine waves
    for waveform_tone in waveform_tones:
        for sample_index in range(0, samples_count):
            numerator = 2.0 * numpy.pi * waveform_tone.frequency / sampling_rate
            result_waveform[sample_index] = result_waveform[sample_index] + (
                waveform_tone.amplitude
                * math.sin(waveform_tone.phase_radians + sample_index * numerator)
            )

    # normalize resulting sum waveform
    # samples_max: numpy.float64 = result_waveform.max()

    # if samples_max > amplitude_normalization_threshold:
    #     wanted_samples_max = amplitude
    #     actual_samples_max = samples_max
    #     normalization_factor = numeric_utilities.absolute_value(
    #         wanted_samples_max
    #     ) / numeric_utilities.absolute_value(actual_samples_max)

    #     scale_and_offset_waveform.scale_inplace(
    #         waveform_samples=result_waveform, scale_factor=normalization_factor
    #     )

    return result_waveform
