"""Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.dc_rms_analysis module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (351 > 100 characters) (auto-generated noqa)

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
    """Gets last error message hold by labview DC-RMS VI.

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: occurs when native call fails for some reason.

    Returns:
        str: last error message
    """  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement_GetLastErrorMessage"
        ) from e


def labview_process_single_waveform_dc_rms_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    dc_rms_processing_window: int,
) -> tuple[float, float]:
    """Invokes native library DC-RMS processing LabVIEW VI.

    Args:
        dc_rms_processing_window (int): 0 for Rectangular, 1 for Hann or 2 for LowSideLobe.
        waveform_samples (numpy.ndarray[float]): An array of 64bites floating points
        that will be passed to native code library.
        waveform_sampling_period_seconds (float): Sampling period of the input array of samples.

    Returns:
        tuple[float, float]: DC value and RMS value gathered in a tuple.
    """
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement(
    # DcRmsProcessingWindowEnum inputDcRmsProcessingWindow,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # const double* inputWaveformSamplesArray,
    # double* outputProcessedDcValue,
    # double* outputProcessedRmsValue)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement.argtypes = [
            # DcRmsProcessingWindowEnum inputDcRmsProcessingWindow
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double* outputProcessedDcValue
            POINTER(c_double),
            # double* outputProcessedRmsValue
            POINTER(c_double),
        ]

        # call native code
        dc_value_out = c_double()
        rms_value_out = c_double()

        dc_rms_processing_window_in = c_int(dc_rms_processing_window)
        waveform_sampling_period_in = c_double(waveform_sampling_period_seconds)
        waveform_length_in = c_size_t(waveform_samples.size)
        waveform_samples_array_in = waveform_samples.ctypes.data_as(POINTER(c_double))

        res_status = (
            dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement(
                dc_rms_processing_window_in,
                waveform_sampling_period_in,
                waveform_length_in,
                waveform_samples_array_in,
                byref(dc_value_out),
                byref(rms_value_out),
            )
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement"
                + f" status = {res_status}, error = {error_message}"
            )

        return (dc_value_out.value, rms_value_out.value)
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformDcRmsMeasurement"
        ) from e
