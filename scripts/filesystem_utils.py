"""Defines a set of filesystem utility functions"""

import os
import shutil


def safe_copy_dll_file(
    dlls_source_folder_path: str,
    dlls_destination_folder_path: str,
    dll_file_name: str,
):
    """Copies dll file from a given source folder into a destination folder.

    Args:
        dlls_source_folder_path (str): source folder from where dll file should be copied.
        dlls_destination_folder_path (str): destination folder where dll files
        should be copied into.
        dll_file_name (str): name of the dll file
    """
    destination_file_path = os.path.join(dlls_destination_folder_path, dll_file_name)

    if os.path.exists(destination_file_path):
        os.remove(destination_file_path)

    shutil.copy(
        src=os.path.join(dlls_source_folder_path, dll_file_name),
        dst=destination_file_path,
    )
