"""Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.frequency_domain_analysis module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (361 > 100 characters) (auto-generated noqa)

import math
from ctypes import (
    POINTER,
    byref,
    c_bool,
    c_char_p,
    c_double,
    c_int,
    c_size_t,
    create_string_buffer,
)

import numpy
import scipy.signal

from nipcbatt.pcbatt_analysis import analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)
from nipcbatt.pcbatt_analysis.waveform_transformation import scale_and_offset_waveform


def labview_multiple_tones_measurement_get_last_error_message_impl() -> str:
    """Gets LabVIEW VI last error message."""
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement_GetLastErrorMessage"
        ) from e


def labview_fft_spectrum_amplitude_phase_get_last_error_message_impl() -> str:
    """Gets LabVIEW VI last error message."""
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement_GetLastErrorMessage"
        ) from e


def labview_process_single_waveform_amplitude_phase_spectrum_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    spectrum_amplitude_must_be_db: bool,
    spectrum_amplitude_type: SpectrumAmplitudeType,
    spectrum_phase_unit: SpectrumPhaseUnit,
    fft_spectrum_window: int,
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
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement(
    # FftSpectrumWindowEnum inputFftWindow,
    # bool inputViewSettingsAmplitudeUnitIsdDb,
    # bool inputViewSettingsPhaseMustUnwrap,
    # bool inputViewSettingsPhaseUnitIsDegree,
    # double inputAdvancedFftWindowParameter,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # const double* inputWaveformSamplesArray,
    # double* outputSpectrumResolution,
    # double* outputSpectrumStartFrequency,
    # double* outputSpectrumEndFrequency,
    # double* outputSpectrumMagnitudesArray,
    # double* outputSpectrumPhasesArray);
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement.argtypes = [
            # FftSpectrumWindowEnum inputFftWindow
            c_int,
            # bool inputViewSettingsAmplitudeUnitIsdDb
            c_bool,
            # inputViewSettingsPhaseMustUnwrap
            c_bool,
            # bool inputViewSettingsPhaseUnitIsDegree
            c_bool,
            # double inputAdvancedFftWindowParameter
            c_double,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double* outputSpectrumResolution,
            POINTER(c_double),
            # double* outputSpectrumStartFrequency,
            POINTER(c_double),
            # double* outputSpectrumEndFrequency,
            POINTER(c_double),
            # double* outputSpectrumMagnitudesArray,
            POINTER(c_double),
            # double* outputSpectrumPhasesArray
            POINTER(c_double),
        ]

        # fill function arguements
        input_fft_window = c_int(fft_spectrum_window)
        input_view_settings_amplitude_unit_isd_db = c_bool(spectrum_amplitude_must_be_db)

        input_view_settings_phase_must_unwrap = c_bool(False)
        input_view_settings_phase_unit_is_degree = c_bool(
            spectrum_phase_unit == SpectrumPhaseUnit.DEGREE
        )

        input_advanced_fft_window_parameter = c_double(fft_spectrum_window_advanced_parameter or 0)

        waveform_sampling_period_in = c_double(waveform_sampling_period_seconds)
        waveform_length_in = c_size_t(waveform_samples.size)
        waveform_samples_array_in = waveform_samples.ctypes.data_as(POINTER(c_double))

        output_spectrum_resolution = c_double(0)
        output_spectrum_start_frequency = c_double(0)
        output_spectrum_end_frequency = c_double(0)

        fft_spectrum_size = math.ceil(waveform_samples.size / 2)
        output_spectrum_magnitudes_array = numpy.zeros(
            fft_spectrum_size, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        output_spectrum_phases_array = numpy.zeros(
            fft_spectrum_size, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement(
            input_fft_window,
            input_view_settings_amplitude_unit_isd_db,
            input_view_settings_phase_must_unwrap,
            input_view_settings_phase_unit_is_degree,
            input_advanced_fft_window_parameter,
            waveform_sampling_period_in,
            waveform_length_in,
            waveform_samples_array_in,
            byref(output_spectrum_resolution),
            byref(output_spectrum_start_frequency),
            byref(output_spectrum_end_frequency),
            output_spectrum_magnitudes_array,
            output_spectrum_phases_array,
        )

        if res_status != 0:
            error_message = labview_fft_spectrum_amplitude_phase_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement"
                + f" status = {res_status}, error = {error_message}"
            )

        frequencies_amplitudes_result = numpy.ctypeslib.as_array(
            obj=output_spectrum_magnitudes_array, shape=(fft_spectrum_size,)
        )

        if spectrum_amplitude_type == SpectrumAmplitudeType.PEAK:
            scale_and_offset_waveform.scale_inplace(
                waveform_samples=frequencies_amplitudes_result,
                scale_factor=math.sqrt(2),
            )

        spectrum_final_result = AmplitudePhaseSpectrum(
            f0=output_spectrum_start_frequency.value,
            df=output_spectrum_resolution.value,
            frequencies_amplitudes=frequencies_amplitudes_result,
            spectrum_amplitude_type=spectrum_amplitude_type,
            spectrum_amplitude_unit_is_db=spectrum_amplitude_must_be_db,
            frequencies_phases=numpy.ctypeslib.as_array(
                obj=output_spectrum_phases_array, shape=(fft_spectrum_size,)
            ),
            spectrum_phase_unit=spectrum_phase_unit,
        )

        return spectrum_final_result
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudePhaseSpectrumMeasurement"
        ) from e


def labview_process_single_waveform_multiple_tones_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    tones_selection_threshold: float,
    tones_max_count: int,
    tones_sorting_mode: int,
) -> tuple[list[WaveformTone], SpectrumAmplitudeType]:
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
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement(
    # TonesSortingModeEnum inputTonesSortingMode,
    # size_t inputTonesResultsMaxCount,
    # double inputTonesSelectionAmplitudeThreshold,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # const double* inputWaveformSamplesArray,
    # double* outputTonesResultActualCount,
    # double* outputTonesFrequenciesArray,
    # double* outputTonesPeakAmplitudesArray,
    # double* outputTonesPhasesDegreeArray);
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement.argtypes = [
            # TonesSortingModeEnum inputTonesSortingMode
            c_int,
            # size_t inputTonesResultsMaxCount
            c_size_t,
            # double inputTonesSelectionAmplitudeThreshold
            c_double,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # size_t* outputTonesResultActualCount
            POINTER(c_size_t),
            # double* outputTonesFrequenciesArray
            POINTER(c_double),
            # outputTonesPeakAmplitudesArray
            POINTER(c_double),
            # outputTonesPhasesDegreeArray
            POINTER(c_double),
        ]

        # call native code
        input_tones_sorting_mode = c_int(tones_sorting_mode)
        input_tones_results_max_count = c_size_t(tones_max_count)
        input_tones_selection_amplitude_threshold = c_double(tones_selection_threshold)

        waveform_sampling_period_in = c_double(waveform_sampling_period_seconds)
        waveform_length_in = c_size_t(waveform_samples.size)
        waveform_samples_array_in = waveform_samples.ctypes.data_as(POINTER(c_double))

        output_tones_result_actual_count = c_size_t(0)
        output_tones_frequencies_array = numpy.zeros(
            tones_max_count, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        output_tones_peak_amplitudes_array = numpy.zeros(
            tones_max_count, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        output_tones_phases_degree_array = numpy.zeros(
            tones_max_count, dtype=numpy.float64
        ).ctypes.data_as(POINTER(c_double))

        # labview returns phases in degree, amplitudes are peak amplitudes
        res_status = (
            dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement(
                input_tones_sorting_mode,
                input_tones_results_max_count,
                input_tones_selection_amplitude_threshold,
                waveform_sampling_period_in,
                waveform_length_in,
                waveform_samples_array_in,
                byref(output_tones_result_actual_count),
                output_tones_frequencies_array,
                output_tones_peak_amplitudes_array,
                output_tones_phases_degree_array,
            )
        )

        if res_status != 0:
            error_message = labview_multiple_tones_measurement_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement"
                + f" status = {res_status}, error = {error_message}"
            )

        output_tones_result_actual_count_value = min(
            tones_max_count, output_tones_result_actual_count.value
        )
        tones_final_result_list: list[WaveformTone] = []

        for tone_index in range(0, output_tones_result_actual_count_value):
            if output_tones_peak_amplitudes_array[tone_index] >= tones_selection_threshold:
                tones_final_result_list.append(
                    WaveformTone(
                        frequency=output_tones_frequencies_array[tone_index],
                        amplitude=output_tones_peak_amplitudes_array[tone_index],
                        phase_radians=math.radians(output_tones_phases_degree_array[tone_index]),
                    )
                )

        return (tones_final_result_list, SpectrumAmplitudeType.PEAK)

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformTonesMeasurement"
        ) from e


def labview_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    spectrum_amplitude_must_be_db: bool,
    spectrum_phase_unit: SpectrumPhaseUnit,
    fft_spectrum_window: int,
    tones_sorting_mode: int,
    tones_selection_threshold_peak_amplitude: float,
    tones_max_count: int = None,
    fft_spectrum_window_advanced_parameter: float = None,
):
    """Processes amplitude phase spectrum of a given waveform samples using LabVIEW VI

    Args:
        waveform_samples (`numpy.ndarray[numpy.float64]`): samples of the waveform to process.
        waveform_sampling_period_seconds (`float`): sampling period of the waveform to process.
        spectrum_amplitude_must_be_db (`bool`): amplitudes of the spectrum should
        be expressed as db gain, instead of nominal unit.
        spectrum_phase_unit (`FftSpectrumPhaseUnit`): can be `RADIAN` or `DEGREE`.
        fft_spectrum_window (`FftSpectrumWindow`): fft processing window.
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
    """  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (106 > 100 characters) (auto-generated noqa)

    # process spectrum magnitude and phase
    rms_spectrum_result = labview_process_single_waveform_amplitude_phase_spectrum_impl(
        waveform_samples,
        waveform_sampling_period_seconds,
        spectrum_amplitude_must_be_db,
        SpectrumAmplitudeType.RMS,
        spectrum_phase_unit,
        fft_spectrum_window,
        fft_spectrum_window_advanced_parameter,
    )

    # if tones_max_count is not provided,
    # we will resolve automatic value for it, using peak detection algorithm
    if tones_max_count is None:
        rms_to_peak_sale_factor = math.sqrt(2)
        spectrum_rms_amplitudes = rms_spectrum_result.spectrum_amplitudes
        amplitude_spectrum_peaks_indices = scipy.signal.find_peaks(x=spectrum_rms_amplitudes)[0]

        tones_selection_threshold_rms_amplitude = 0
        if spectrum_amplitude_must_be_db:
            tones_selection_threshold_rms_amplitude = 20 * numpy.log10(
                tones_selection_threshold_peak_amplitude / rms_to_peak_sale_factor
            )
        else:
            tones_selection_threshold_rms_amplitude = (
                tones_selection_threshold_peak_amplitude / rms_to_peak_sale_factor
            )

        amplitude_spectrum_peaks_values_above_threhold = list(
            filter(
                lambda rms_amplitude_value: rms_amplitude_value
                >= tones_selection_threshold_rms_amplitude,
                map(
                    lambda indice: spectrum_rms_amplitudes[indice],
                    amplitude_spectrum_peaks_indices,
                ),
            )
        )
        tones_max_count = len(amplitude_spectrum_peaks_values_above_threhold)

    # process multiple tones
    multiple_tones_result: tuple[list[WaveformTone], SpectrumAmplitudeType] = None

    if tones_max_count > 0:
        multiple_tones_result = labview_process_single_waveform_multiple_tones_impl(
            waveform_samples,
            waveform_sampling_period_seconds,
            tones_selection_threshold_peak_amplitude,
            tones_max_count,
            tones_sorting_mode,
        )
    else:
        multiple_tones_result = [], SpectrumAmplitudeType.PEAK

    return rms_spectrum_result, multiple_tones_result[0], multiple_tones_result[1]
