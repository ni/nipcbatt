"""Defines pcbatt analysis library information elements."""

import logging

from nipcbatt.pcbatt_analysis._pcbatt_analysis_internal import _analysis_library_info
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)


def get_labview_analysis_traces_folder_path() -> str:
    """Gets the path of traces produced by analysis library.

    Returns:
        str: string path.
    """
    return _analysis_library_info.get_labview_analysis_traces_folder_path_impl()


def is_labview_runtime_available() -> bool:
    """Indicates if current machine has labview runtime available.

    Returns:
        bool: True, labview runtime is available elsewhere it returns False.
    """
    return _analysis_library_info.call_interop_api_labview_analysis_lv_runtime_available()


def are_traces_enabled() -> bool:
    """Indicates whether current analysis library traces are enabled or not.

    Returns:
        bool: True, traces are enabled elsewhere it returns False.
    """
    return _analysis_library_info.call_interop_api_labview_analysis_are_traces_enabled()


def enable_traces(traces_status: bool) -> None:
    """Forces current analysis library to produce traces.

    Args:
        trace_status (bool): True, verbose traces are recorded, False, no traces are recorded.
    """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
    _analysis_library_info.call_interop_api_labview_analysis_enable_traces(traces_status)


def get_labview_analysis_available_functions_names_list() -> list[str]:
    """Gets the list of exported labview functions."""
    return ["BasicDcRms"]


def get_labview_analysis_library_version_numbers() -> tuple[int, int, int, int]:
    """Gets the version information elements of labview analysis library."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)

    logging.debug("current script path = %s", __file__)

    call_result_tuple = (
        _analysis_library_info.call_interop_api_labview_analysis_get_library_version()
    )

    # handle status code returned by native code
    if call_result_tuple[0] == 0:
        return (
            call_result_tuple[1],
            call_result_tuple[2],
            call_result_tuple[3],
            call_result_tuple[4],
        )
    else:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}: "
            + _analysis_library_info.NATIVE_FUNCTION_GET_LIBRARY_VERSION
        )
