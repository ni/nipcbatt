"""Provides private module of native interop helper functions"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

import os
from ctypes import CDLL, cdll

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisLoadNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)


def load_windows_shared_library_entries(native_library_path: str) -> CDLL:
    """Load content of DLL file into CDLL object

    Args:
        native_library_path (str): path into window file dll.

    Raises:
        PCBATTAnalysisLoadNativeLibraryFailedException: Occurs when loading
        of shared library fails for some reason.

    Returns:
        CDLL: An object holding windows shared library entries.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    try:
        dll_entries = cdll.LoadLibrary(native_library_path)
        # print(dll_entries)
        return dll_entries
    except Exception as e:
        raise PCBATTAnalysisLoadNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_LOAD_FAILED}"
            + f"{os.path.basename(native_library_path)}: {str(e)}"
        ) from e
