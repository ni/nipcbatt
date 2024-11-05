"""Provides a set of function helpers for native interop usage."""

import os
import platform
from ctypes import CDLL
from pathlib import Path

from varname import nameof

from nipcbatt.pcbatt_analysis._pcbatt_analysis_internal import _analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisLoadNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_utilities import platform_utilities


def get_native_libraries_folder_name_for_windows() -> str:
    """Gets the name of folder containing native libraries when running
       on windows operating system.

    Raises:
        RuntimeError: Occurs when executing envrionment is not supported by current
        analysis library.

    Returns:
        str: folder name containing native libraries, win_amd64 or win32.
    """
    if platform_utilities.is_python_windows_64bits():
        return "win_amd64"

    if platform_utilities.is_python_windows_32bits():
        return "win32"

    raise RuntimeError(
        f"{AnalysisLibraryExceptionMessage.NATIVE_INTEROP_IS_NOT_SUPPORTED_ON_CURRENT_PLATFORM}:"
        + f"{platform.architecture()}"
    )


def load_interop_api_library_entries() -> CDLL:
    """Loads content of 'NI.PCBATT.InteropApi.dll' into a CDLL object
       that can be used to perform dynamic function invokation.

    Raises:
        PCBATTAnalysisLoadNativeLibraryFailedException:
        occurs when loading interop api entries fails for some reason.
    """

    native_libraries_folder_name = get_native_libraries_folder_name_for_windows()

    # entry point DLL
    entry_point_dll_path = os.path.join(
        Path(__file__).parent, native_libraries_folder_name, "NI.PCBATT.InteropApi.dll"
    )

    # labview wrapper DLL
    analysis_labview_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.PCBATT.Analysis.LabVIEW.dll",
    )

    # VIs DLL
    analysis_labview_basic_dc_rms_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.BasicDcRms.dll",
    )

    analysis_labview_amplitude_and_levels_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.AmplitudeAndLevels.dll",
    )

    analysis_labview_pulse_measurements_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.PulseMeasurements.dll",
    )

    analysis_labview_fft_spectrum_mag_phase_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.FFTSpectrumAmplitudePhase.dll",
    )

    analysis_labview_multitones_measurements_dll_path = os.path.join(
        Path(__file__).parent,
        native_libraries_folder_name,
        "NI.LabVIEW.ExtractMultipleToneInformation.dll",
    )

    required_dlls_paths = [
        entry_point_dll_path,
        analysis_labview_dll_path,
        analysis_labview_basic_dc_rms_dll_path,
        analysis_labview_amplitude_and_levels_dll_path,
        analysis_labview_pulse_measurements_dll_path,
        analysis_labview_fft_spectrum_mag_phase_dll_path,
        analysis_labview_multitones_measurements_dll_path,
    ]

    required_dlls_files_names = ", ".join(
        map(lambda file_path: f"'{os.path.basename(file_path)}'", required_dlls_paths)
    )

    # Check existence of dll files
    if any(map(lambda dll_path: not os.path.exists(dll_path), required_dlls_paths)):
        raise PCBATTAnalysisLoadNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_IS_MISSING}: "
            + f"{nameof(required_dlls_paths)} = {required_dlls_paths}"
            + os.linesep
            + os.linesep
            + f"{nameof(required_dlls_files_names)} = {required_dlls_files_names}"
        )

    dll_entries = _analysis_library_interop.load_windows_shared_library_entries(
        entry_point_dll_path
    )

    return dll_entries
