"""Cleans the dll files present in python src folders"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)

import logging
import os
import sys
from pathlib import Path

from varname import nameof

# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    repository_dir_path = Path(__file__).parent.parent.parent

    logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

    x64_dlls_destination_folder_path = os.path.join(
        repository_dir_path,
        "pcbatt.python",
        "src",
        "nipcbatt",
        "pcbatt_analysis",
        "win_amd64",
    )

    win32_dlls_destination_folder_path = os.path.join(
        repository_dir_path,
        "pcbatt.python",
        "src",
        "nipcbatt",
        "pcbatt_analysis",
        "win32",
    )

    if os.path.exists(x64_dlls_destination_folder_path):
        logging.debug("delete dlls folder: %s", x64_dlls_destination_folder_path)
        x64_dll_files_list = [
            f for f in os.listdir(x64_dlls_destination_folder_path) if f.endswith(".dll")
        ]

        for dll_file in x64_dll_files_list:
            os.remove(os.path.join(x64_dlls_destination_folder_path, dll_file))

    if os.path.exists(win32_dlls_destination_folder_path):
        logging.debug("delete dlls folder: %s", win32_dlls_destination_folder_path)
        win32_dll_files_list = [
            f for f in os.listdir(win32_dlls_destination_folder_path) if f.endswith(".dll")
        ]

        for dll_file in win32_dll_files_list:
            os.remove(os.path.join(win32_dlls_destination_folder_path, dll_file))
