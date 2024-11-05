"""Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.amplitude_and_levels_analysis module."""

from ctypes import (
    POINTER,
    byref,
    c_char_p,
    c_double,
    c_int,
    c_size_t,
    create_string_buffer,
)

import numpy

from nipcbatt.pcbatt_analysis import analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)


def labview_get_last_error_message_impl() -> str:
    """Gets last error message hold by labview Amplitude and Levels VI.

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when native function call fails
        for some reason.

    Returns:
        str: empty string when no error occured, elsewhere not empty string.
    """
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement_GetLastErrorMessage"
        ) from e


def labview_process_single_waveform_amplitude_and_levels_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    amplitude_and_levels_processing_method: int,
    histogram_size: int,
) -> tuple[float, float, float]:
    """Invokes native library Amplitude and Levels processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when native dll call fails for some reason.

    Returns:
        tuple[float, float, float]: Tuple gathering, amplitude, high state and low state levels.
    """
    # Create native code DLL call
    # int NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement(
    # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int histogramSize,
    # const double* inputWaveformSamplesArray,
    # double* outputProcessedAmplitudeValue,
    # double* outputProcessedHighStateLevelValue,
    # double* outputProcessedLowStateLevelValue)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement.argtypes = [
            # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int histogramSize
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double* outputProcessedAmplitudeValue
            POINTER(c_double),
            # double* outputProcessedHighStateLevelValue
            POINTER(c_double),
            # double* outputProcessedLowStateLevelValue
            POINTER(c_double),
        ]

        # call native code
        amplitude_value_out = c_double()
        high_state_level_value_out = c_double()
        low_state_level_value_out = c_double()

        amplitude_and_levels_processing_method_in = c_int(amplitude_and_levels_processing_method)

        waveform_sampling_period_in = c_double(waveform_sampling_period_seconds)
        waveform_length_in = c_size_t(waveform_samples.size)
        waveform_samples_array_in = waveform_samples.ctypes.data_as(POINTER(c_double))
        histogram_size_in = c_int(histogram_size)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement(
            amplitude_and_levels_processing_method_in,
            waveform_sampling_period_in,
            waveform_length_in,
            histogram_size_in,
            waveform_samples_array_in,
            byref(amplitude_value_out),
            byref(high_state_level_value_out),
            byref(low_state_level_value_out),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement"
                + f" status = {res_status}, error = {error_message}"
            )

        return (
            amplitude_value_out.value,
            high_state_level_value_out.value,
            low_state_level_value_out.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformAmplitudeAndLevelsMeasurement"
        ) from e
