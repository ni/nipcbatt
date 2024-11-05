""" Provides a set of operating system utilities routines."""

import os
from typing import List


def get_env_variable_paths() -> List[str]:
    """Enumerates paths described in the 'Path' environment variable."""
    path_env = set(os.getenv("Path").split(";"))
    return list(path_env)


def is_path_absolute(path: str) -> bool:
    """Checks is a path is absolute (containing root path).

    Args:
        path (str): the path of file or folder.

    Returns:
        bool: `True` if the path is absolute.
    """
    return os.path.isabs(path)


def combine_path_components(path: str, *path_components: str) -> str:
    """Appends path components to a specific path.

    Args:
        path (str): the path on which path are appended.
        *path_components (str): contains path components to add.
    Returns:
        str: the conbined path.
    """  # noqa: D411 - Missing blank line before section (auto-generated noqa)
    return os.path.join(path, *path_components)
