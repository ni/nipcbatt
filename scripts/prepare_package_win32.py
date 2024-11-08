"""Builds x86 native DLLs then copies them into python src structure"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

import logging
import os
import subprocess
import sys
from pathlib import Path

import filesystem_utils
from varname import nameof

# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    repository_dir_path = Path(__file__).parent.parent.parent

    logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)
    # build native code using x86 scripts
    build_script_path = os.path.join(
        repository_dir_path,
        "pcbatt.native",
        "scripts",
        "build_x86_release.bat",
    )

    if os.path.exists(build_script_path):
        # build cpp source files
        process_result = subprocess.run(
            args=[build_script_path],
            check=True,
        )

        # move x86 release DLLs into python src
        x86_dlls_source_folder_path = os.path.join(
            repository_dir_path,
            "pcbatt.native",
            "PCBATT.Native.Libraries",
            "Release",
        )

        x86_dlls_destination_folder_path = os.path.join(
            repository_dir_path,
            "pcbatt.python",
            "src",
            "nipcbatt",
            "pcbatt_analysis",
            "win32",
        )

        if os.path.exists(x86_dlls_source_folder_path):
            logging.debug("copy dlls folder: %s", x86_dlls_source_folder_path)

            # DLL 1
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.PCBATT.InteropApi.dll",
            )

            # DLL 2
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.PCBATT.Analysis.LabVIEW.dll",
            )

            # DLL 3
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.BasicDcRms.dll",
            )

            # DLL 4
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.AmplitudeAndLevels.dll",
            )

            # DLL 5
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.PulseMeasurements.dll",
            )

            # DLL 6
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.FFTSpectrumAmplitudePhase.dll",
            )

            # DLL 7
            filesystem_utils.safe_copy_dll_file(
                x86_dlls_source_folder_path,
                x86_dlls_destination_folder_path,
                "NI.LabVIEW.ExtractMultipleToneInformation.dll",
            )

        else:
            print(f"x86 dlls folder is not found: {x86_dlls_source_folder_path}")

    else:
        print(f"Script file is not found: {build_script_path}")
