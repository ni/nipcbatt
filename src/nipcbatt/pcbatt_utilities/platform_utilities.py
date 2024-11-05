"""Defines a set of platform related utilities functions."""

import platform


def is_python_windows_32bits() -> bool:
    """Indicates if current python interpreter is running on windows os
    and if it is 32 bits architecture.

    Returns:
        Boolean: True if python is running 32 bits architecture on windows os
    """
    if platform.system() == "Windows":
        return platform.architecture()[0].endswith("32bit")

    return False


def is_python_windows_64bits() -> bool:
    """Indicates if current python interpreter is running on windows os
    and if it is 64 bits architecture.

    Returns:
        Boolean: True if python is running 64 bits architecture on windows os
    """
    if platform.system() == "Windows":
        return platform.architecture()[0].endswith("64bit")

    return False
