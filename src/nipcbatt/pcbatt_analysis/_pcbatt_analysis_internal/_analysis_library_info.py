"""Provides private functions of analysis_library_info module."""

from ctypes import POINTER, byref, c_char_p, c_int, c_size_t, create_string_buffer

from nipcbatt.pcbatt_analysis import analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)

NATIVE_FUNCTION_GET_LIBRARY_VERSION = "NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion"

NATIVE_FUNCTION_IS_LABVIEW_RUNTIME_AVAILABLE = (
    "NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable"
)

NATIVE_FUNCTION_ARE_TRACES_ENABLED = "NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled"

NATIVE_FUNCTION_ENABLE_TRACES = "NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces"


def get_labview_analysis_traces_folder_path_impl() -> str:
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath' fails for some reason.
    """
    # Create native code DLL call
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath.argtypes = [
            # char* path output
            c_char_p,
            # size_t path length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_GetTracesFolderPath"
        ) from e


def call_interop_api_labview_analysis_enable_traces(traces_status: bool) -> None:
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces' fails for some reason.
    """
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces.argtypes = [c_int]

        # call native code
        traces_status_in = c_int()

        if traces_status is True:
            traces_status_in = c_int(1)
        else:
            traces_status_in = c_int(0)

        return_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_EnableTraces(
            traces_status_in
        )

        if return_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + f"{NATIVE_FUNCTION_ENABLE_TRACES}, status code = {return_status}"
            )

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + f"{NATIVE_FUNCTION_ENABLE_TRACES}"
        ) from e


def call_interop_api_labview_analysis_are_traces_enabled() -> bool:
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled' fails for some reason.
    """
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled.argtypes = [
            POINTER(c_int)
        ]

        # call native code
        traces_status_out = c_int()

        return_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_AreTracesEnabled(
            byref(traces_status_out)
        )

        if return_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + f"{NATIVE_FUNCTION_ARE_TRACES_ENABLED}, status code = {return_status}"
            )

        return traces_status_out.value > 0
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + f"{NATIVE_FUNCTION_ARE_TRACES_ENABLED}"
        ) from e


def call_interop_api_labview_analysis_lv_runtime_available():
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable' located in DLL
    'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable' fails for some reason.
    """

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable.argtypes = []

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_IsLvRuntimeAvailable()

        return res_status == 0
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + f"{NATIVE_FUNCTION_IS_LABVIEW_RUNTIME_AVAILABLE}"
        ) from e


def call_interop_api_labview_analysis_get_library_version():
    """Calls function 'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion' located in DLL
       'NI.PCBATT.InteropApi.dll'

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when function call to
        'NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion' fails for some reason.

    Returns:
        tuple[Any, int, int, int, int]: status code and library version numbers.
    """
    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()

        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion.restype = c_int
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion.argtypes = [
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
            POINTER(c_int),
        ]

        # call native code
        major_number_out = c_int()
        minor_number_out = c_int()
        patch_number_out = c_int()
        build_number_out = c_int()

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_GetLibraryVersion(
            byref(major_number_out),
            byref(minor_number_out),
            byref(patch_number_out),
            byref(build_number_out),
        )

        return (
            res_status,
            major_number_out.value,
            minor_number_out.value,
            patch_number_out.value,
            build_number_out.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + f"{NATIVE_FUNCTION_GET_LIBRARY_VERSION}"
        ) from e
