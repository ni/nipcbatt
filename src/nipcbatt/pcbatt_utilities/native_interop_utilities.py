"""Provides a set of utilities functions related to native functions."""

from ctypes import CDLL, WinDLL, c_int, cdll, windll
from typing import List, Type

from _ctypes import (
    FUNCFLAG_CDECL as _FUNCFLAG_CDECL,
    FUNCFLAG_STDCALL as _FUNCFLAG_STDCALL,
    FUNCFLAG_USE_ERRNO as _FUNCFLAG_USE_ERRNO,
    CFuncPtr as _CFunctPtr,
)
from varname import nameof

from nipcbatt.pcbatt_utilities import os_utilities
from nipcbatt.pcbatt_utilities.file_utilities import file_exists
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

FUNCTION_CALL_FAILED_ARGS_2 = "Call of function '{}' failed ({})"
FILE_NOT_FOUND_ARGS_1 = "file '{}' not found"


class _StdCallFuncPtr(_CFunctPtr):
    """Defines a pointer to a callable that supports standard calling convention."""

    _flags_ = _FUNCFLAG_STDCALL | _FUNCFLAG_USE_ERRNO
    _restype_ = c_int


class _CdeclFuncPtr(_CFunctPtr):
    """Defines a pointer to a callable that supports C calling convention (Cdecl)."""

    _flags_ = _FUNCFLAG_CDECL | _FUNCFLAG_USE_ERRNO
    _restype_ = c_int


def load_stcall_win_dll(dll_path: str) -> WinDLL:
    """Loads a windows dll library with standard calling convention.

    Args:
        dll_path (str): the path of the dll.

    Raises:
        FileNotFoundError:
            Raised when an error occured while loading the dll.
        OSError:
            Raised when dll has invalid format.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(dll_path, nameof(dll_path))

    return windll.LoadLibrary(dll_path)


def load_cdecl_dll(dll_path: str) -> CDLL:
    """Loads a dll with cdecl convention.

    Args:
        dll_path (str): The path of the dll.

    Raises:
        FileNotFoundError:
            Raised when an error occured while loading the dll.
        OSError:
            Raised when dll has invalid format.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(dll_path, nameof(dll_path))

    return cdll.LoadLibrary(dll_path)


def create_native_stdcall_win_function(
    dll_path: str,
    function_name: str,
    return_value_type: Type,
    arguments_types: List[Type],
) -> _StdCallFuncPtr:
    """Creates a pointer on a native function from a win stdcall dll.

    Args:
        dll_path (str): The path of the dll.
        function_name (str): The name of the function.
        return_value_type (Type): The type of the object the function should return.
        arguments_types (List[Type]): A list of types for arguments.

    Raises:
        AttributeError:
            Raised the function is not defined in the library.
        FileNotFoundError:
            Raised when dll was not found.

    Returns:
        StdCallFuncPtr: the pointer to a callable object function retrieved from the library.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(dll_path, nameof(dll_path))
    Guard.is_not_none_nor_empty_nor_whitespace(function_name, nameof(function_name))

    check_dll_availability(dll_path)

    library_entries = load_stcall_win_dll(dll_path)

    function_to_call = _StdCallFuncPtr()

    function_to_call = getattr(library_entries, function_name)

    function_to_call.restype = return_value_type
    function_to_call.argtypes = arguments_types

    return function_to_call


def create_native_cdecl_function(
    dll_path: str,
    function_name: str,
    return_value_type: Type,
    arguments_types: List[Type],
) -> _CdeclFuncPtr:
    """Creates a pointer on a native function from a dll with cdecl convention.

    Args:
        dll_path (str): The path of the dll.
        function_name (str): The name of the function.
        return_value_type (Type): The type of the object the function should return.
        arguments_types (List[Type]): A list of types for arguments.

    Raises:
        AttributeError:
            Raised the function is not defined in the library.
        FileNotFoundError:
            Raised when dll was not found.

    Returns:
        _CdeclFuncPtr: the pointer to a callable object function retrieved from the library.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(dll_path, nameof(dll_path))
    Guard.is_not_none_nor_empty_nor_whitespace(function_name, nameof(function_name))

    check_dll_availability(dll_path)

    library_entries = load_cdecl_dll(dll_path)

    function_to_call = _CdeclFuncPtr()

    function_to_call = getattr(library_entries, function_name)

    function_to_call.restype = return_value_type
    function_to_call.argtypes = arguments_types

    return function_to_call


def check_dll_availability(relative_or_absolute_dll_path: str):
    """Checks a dll file exist when path is absolute,
    elsewhere, the function resolves an absolute path by looking up system path variables
    then it checks the existence of resolved path.

    Args:
        relative_or_absolute_dll_path (str): The path of the dll (absolute or relative).

    Raises:
        FileNotFoundError:
            Raised the dll is not found.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
    if os_utilities.is_path_absolute(relative_or_absolute_dll_path):
        if file_exists(relative_or_absolute_dll_path):
            return
    else:
        env_variable_paths = os_utilities.get_env_variable_paths()

        for env_variable_path in env_variable_paths:
            absolute_dll_path = os_utilities.combine_path_components(
                env_variable_path, relative_or_absolute_dll_path
            )
            if file_exists(absolute_dll_path):
                return

    raise FileNotFoundError(FILE_NOT_FOUND_ARGS_1.format(relative_or_absolute_dll_path))
