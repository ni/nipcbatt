"""Provides frequency domain analysis tools"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (157 > 100 characters) (auto-generated noqa)

from enum import IntEnum

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)
from nipcbatt.pcbatt_analysis.waveform_analysis._waveform_analysis_internal import (
    _frequency_domain_analysis,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class LabViewTonesSortingMode(IntEnum):
    """Defines how should be sorted tone analysis results."""

    INCREASING_FREQUENCIES = 0
    """Tone analysis results are sorted according to frequency (X axis)."""
    DECREASING_AMPLITUDES = 1
    """Tone analysis results are sorted according to amplitude (Y axis)."""


class LabViewFftSpectrumWindow(IntEnum):
    """Defines all supported signal `fft processing` time windows."""

    RECTANGLE = (0,)
    """`Rectangle` window."""

    HANNING = (1,)
    """`Hanning` window, for more details please see: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/hanning_window.html"""

    HAMMING = (2,)
    """`Hamming` window, for more details please see: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/hamming_window.html"""

    BLACKMAN_HARRIS = (3,)
    """`Blackman-Harris` window, for more details please see: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/blackman_harris_window.html"""

    BLACKMAN_EXACT = (4,)
    """`Blackman exact window`, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/exact_blackman_window.html"""

    BLACKMAN = (5,)
    """`Blackman` window; for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/blackman_window.html"""

    FLAT_TOP = (6,)
    """`Flat top profile` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/flat_top_window.html"""

    BHARRIS_4TERMS = (7,)
    """See: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/scaled_time_domain_window.html"""

    BHARRIS_7TERMS = (8,)
    """See: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/scaled_time_domain_window.html"""

    LOW_LATERAL_LOBE = (9,)
    """See: 
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/scaled_time_domain_window.html"""

    BLACKMAN_NUTTALL = (11,)
    """`Blackman-Nuttall` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/blackman_nuttall_window.html"""

    TRIANGLE = (30,)
    """`Triangle` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/triangle_window.html"""

    BARTLETT_HANNING = (31,)
    """`Bartlett-Hanning` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/modbhw.html"""

    BOHMAN = (32,)
    """`Bohman` window, For more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/bohman.html"""

    PARZEN = (33,)
    """`Parzen` window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/parzen.html"""

    WELCH = (34,)
    """Welch window, for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/welch.html"""

    KAISER = (60,)
    """`Kaiser` (requires to provide beta parameter):
    The Kaiser window function allows you to control the stop band
    attenuation via the β parameter, the higher the value of β, the more the attenuation is.
    The more attenuation you have the wider the main lobe and hence the wider the transition band,
    for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/rfmx-waveform-creator/page/rfwfmcreator/kaiserwindow.html"""  # noqa: W505 - doc line too long (101 > 100 characters) (auto-generated noqa)

    DOLPH_TCHEBYCHEV = (61,)
    """`DolphTchebychev` (requires to provider lobes ratio parameter), for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/chebyshev_window.html"""

    GAUSSIAN = 62
    """Gaussian (requires to provide standard deviation parameter), for more details please see:
    https://www.ni.com/docs/fr-FR/bundle/labview/page/lvanls/gaussian_window.html"""


class MultipleTonesProcessingResult(AnalysisLibraryElement):
    """Defines multiple tones processing results"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        detected_tones: list[WaveformTone],
        amplitude_type: SpectrumAmplitudeType,
    ) -> None:
        """Initializes an instance of `MultipleTonesProcessingResult`

        Args:
            detected_tones (`list[WaveformTone]`): list of waveform tones.
            amplitude_type (`SpectrumAmplitudeType`): amplitude type of the waveform tones.

        Raises:
            ValueError: Occurs when input `detected_tones` list is none.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(instance=detected_tones, instance_name=nameof(detected_tones))
        self._detected_tones = detected_tones
        self._amplitude_type = amplitude_type

    @property
    def detected_tones(self) -> list[WaveformTone]:
        """Gets the list of the tones detected in analyzed waveform.

        Returns:
            list[WaveformTone]: list of waveform tones.
        """
        return self._detected_tones

    @property
    def amplitude_type(self) -> SpectrumAmplitudeType:
        """Gets the kind amplitudes of the tones detected in analyzed waveform.

        Returns:
            SpectrumAmplitudeType: amplitude type `RMS` or `PEAK`.
        """
        return self._amplitude_type


class MultipleTonesAmplitudePhaseSpectrumProcessingResult(AnalysisLibraryElement):
    """Defines multiple tones and spectrum processing results"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        multiple_tones_result: MultipleTonesProcessingResult,
        amplitude_phase_spectrum: AmplitudePhaseSpectrum,
    ) -> None:
        """Initialize an instance of `MultipleTonesAmplitudePhaseSpectrumProcessingResult`.

        Args:
            multiple_tones_result (`MultipleTonesProcessingResult`):
                holds multiple tones processing results.
            amplitude_phase_spectrum (`AmplitudePhaseSpectrum`):
                holds fft spectrum processing results.

        Raises:
            ValueError: Occurs when input `multiple_tones_result` or
            `amplitude_phase_spectrum` are none.
        """
        Guard.is_not_none(
            instance=multiple_tones_result, instance_name=nameof(multiple_tones_result)
        )

        Guard.is_not_none(
            instance=amplitude_phase_spectrum,
            instance_name=nameof(amplitude_phase_spectrum),
        )

        self._multiple_tones_result = multiple_tones_result
        self._amplitude_phase_spectrum = amplitude_phase_spectrum

    @property
    def multiple_tones_result(self) -> MultipleTonesProcessingResult:
        """Gets multiple tones processing results of analyzed waveform.

        Returns:
            MultipleTonesProcessingResult: multiple tones processing result.
        """
        return self._multiple_tones_result

    @property
    def amplitude_phase_spectrum(self) -> AmplitudePhaseSpectrum:
        """Gets fft spectrum processing results of analyzed waveform.

        Returns:
            AmplitudePhaseSpectrum: fft spectrum processing result.
        """
        return self._amplitude_phase_spectrum


class LabViewFrequencyDomainProcessing(AnalysisLibraryElement):
    """Defines frequency domain analysis functions such
    fft spectrum and multiple tones processing."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (343 > 100 characters) (auto-generated noqa)

    @staticmethod
    def process_single_waveform_multiple_tones_and_amplitude_phase_spectrum(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        spectrum_amplitude_must_be_db: bool,
        spectrum_phase_unit: SpectrumPhaseUnit,
        fft_spectrum_window: LabViewFftSpectrumWindow,
        tones_sorting_mode: LabViewTonesSortingMode,
        tones_selection_threshold_peak_amplitude: float,
        tones_max_count: int = None,
        fft_spectrum_window_advanced_parameter: float = None,
    ) -> MultipleTonesAmplitudePhaseSpectrumProcessingResult:
        """Processes `RMS` amplitude phase spectrum of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
            waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
            spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
            be expressed as db gain, instead of nominal unit.
            spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
            fft_spectrum_window (`LabViewFftSpectrumWindow`): fft processing window.
            fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
            only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.
            tones_selection_threshold_peak_amplitude (`float`): minimum amplitude peak of tone to be selected.
            tones_max_count (`int`): maximum tones count to extract from analyzed waveform,
            when not set, all tones will be extracted.

        Raises:
            PCBATTAnalysisException:
                Occurs when frequency domain processing fails for some reason.

        Returns:
            FrequencyDomainProcessingResult: An object that holds result of fft spectrum
            processing result and multiple tones processing result using LabVIEW VIs.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        try:
            results_tuple = _frequency_domain_analysis.labview_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_impl(
                waveform_samples,
                waveform_sampling_period_seconds,
                spectrum_amplitude_must_be_db,
                spectrum_phase_unit,
                fft_spectrum_window,
                tones_sorting_mode,
                tones_selection_threshold_peak_amplitude,
                tones_max_count,
                fft_spectrum_window_advanced_parameter,
            )

            return MultipleTonesAmplitudePhaseSpectrumProcessingResult(
                multiple_tones_result=MultipleTonesProcessingResult(
                    detected_tones=results_tuple[1], amplitude_type=results_tuple[2]
                ),
                amplitude_phase_spectrum=results_tuple[0],
            )
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.FREQUENCY_DOMAIN_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e


class LabViewFftSpectrumAmplitudePhase(AnalysisLibraryElement):
    """Provides Amplitude/Phase spectrum processing based on
    `LabVIEW FFT Spectrum Magnitude Phase VI`"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (341 > 100 characters) (auto-generated noqa)

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occurred error of
        ``FFT Spectrum Magnitude and Phase`` labview VI.

        Returns:
            str: Empty string when no error occurred, elsewhere not empty string.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        return (
            _frequency_domain_analysis.labview_fft_spectrum_amplitude_phase_get_last_error_message_impl()
        )

    @staticmethod
    def process_single_waveform_amplitude_phase_spectrum(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        spectrum_amplitude_must_be_db: bool,
        spectrum_amplitude_type: SpectrumAmplitudeType,
        spectrum_phase_unit: SpectrumPhaseUnit,
        fft_spectrum_window: LabViewFftSpectrumWindow,
        fft_spectrum_window_advanced_parameter: float = None,
    ) -> AmplitudePhaseSpectrum:
        """Processes amplitude phase spectrum of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
            waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
            spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
            be expressed as db gain, instead of nominal unit.
            spectrum_amplitude_type (`FftSpectrumAmplitudeType`): can be `RMS` or `PEAK`.
            spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
            fft_spectrum_window (`FftSpectrumWindow`): fft processing window.
            fft_spectrum_window_advanced_parameter (`float`): advanced parameter value,
            only used when selected window is `KAISER`, `DOLPH_TCHEBYCHEV` or `GAUSSIAN`.

        Raises:
            PCBATTAnalysisException:
                Occurs when multiple tones processing fails for some reason.

        Returns:
            AmplitudePhaseSpectrum: An object that holds result of fft spectrum
            processing result using LabVIEW VI.
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        try:
            return _frequency_domain_analysis.labview_process_single_waveform_amplitude_phase_spectrum_impl(
                waveform_samples,
                waveform_sampling_period_seconds,
                spectrum_amplitude_must_be_db,
                spectrum_amplitude_type,
                spectrum_phase_unit,
                fft_spectrum_window,
                fft_spectrum_window_advanced_parameter,
            )
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.AMPLITUDE_AND_PHASE_SPECTRUM_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e


class LabViewMultipleTonesMeasurement(AnalysisLibraryElement):
    """Provides multiple tones processing based on
    `LabVIEW Multiple Tone Information VI`"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (338 > 100 characters) (auto-generated noqa)

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occurred error of
        ``Multiple Tones Measurements`` labview VI.

        Returns:
            str: Empty string when no error occurred, elsewhere not empty string.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        return (
            _frequency_domain_analysis.labview_multiple_tones_measurement_get_last_error_message_impl()
        )

    @staticmethod
    def process_single_waveform_multiple_tones(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        tones_selection_threshold: float,
        tones_max_count: int,
        tones_sorting_mode: LabViewTonesSortingMode,
    ) -> MultipleTonesProcessingResult:
        """Processes multiple tones of a given waveform samples using LabVIEW VI

        Args:
            waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
            waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
            tones_selection_threshold (`float`): minimum amplitude peak of tone to be selected.
            tones_max_count (`int`): maximum tones count to extract from analyzed waveform.
            tones_sorting_mode (`TonesSortingMode`): sorting of the output tones list.

        Raises:
            PCBATTAnalysisException:
                Occurs when multiple tones processing fails for some reason.

        Returns:
            MultipleTonesMeasurementResult: An object that holds result of multiple tones
            processing result using LabVIEW VI.
        """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        Guard.is_greater_than_zero(tones_selection_threshold, nameof(tones_selection_threshold))

        if tones_max_count is not None:
            Guard.is_greater_than_zero(tones_max_count, nameof(tones_max_count))

        try:
            tuple_result = (
                _frequency_domain_analysis.labview_process_single_waveform_multiple_tones_impl(
                    waveform_samples,
                    waveform_sampling_period_seconds,
                    tones_selection_threshold,
                    tones_max_count,
                    tones_sorting_mode,
                )
            )

            return MultipleTonesProcessingResult(
                detected_tones=tuple_result[0], amplitude_type=tuple_result[1]
            )
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.MULTIPLE_TONES_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e
