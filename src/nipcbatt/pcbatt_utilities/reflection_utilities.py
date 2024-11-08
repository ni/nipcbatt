""" Provides a set of reflection utilities functions."""

from enum import Enum
from typing import Callable, Iterable, Tuple, Type, Union

import numpy as np


def substitute_method(cls: Type, method: Callable, method_name: str):
    """Replaces the specific method of a class by a specific function (Callable).
       This function must have self as first argument.
    Args:
        cls (Type): The class on which the method is replaced.
        method (Callable): the function to substitute.
        method_name (str): the name of the method to replace.
    """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)
    setattr(
        cls,
        method_name,
        method,
    )


def enumerate_properties(instance: object) -> Iterable[Tuple]:
    """Enumerates properties defined in instance

    Args:
        instance (object): the object on which properties are enumerated.

    Returns:
        iterator with a sequence of tuples containing the name of property and its value.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    members = [item for item in vars(type(instance)).items() if isinstance(item[1], property)]

    for property_name, property_object in members:
        yield property_name, property_object.fget(instance)


def convert_for_json_serialization(
    value: object,
) -> Union[int, float, bool, str, list, dict]:
    """Converts an instance for JSON serialization.

    Args:
        value (object): the value to convert.

    Returns:
        Union[int, float, bool, str, dict]:
            if value is an Enum, returns a string with its name and its value;
            if value is str, int, float or bool, returns the value itself;
            if value is a list, return a list of JSON representation of each item;
            if value is a class containing properties,
            returns a dictionary with property names and values.
    """
    if isinstance(value, Enum):
        return f"{value.name} ({value.value})"

    if isinstance(value, (int, float, bool, str)):
        return value

    if isinstance(value, dict):
        if np.bool_(False) in value.values() or np.bool_(True) in value.values():
            return str(value)
        return value

    if isinstance(value, list):
        return [convert_for_json_serialization(item) for item in value]

    if len(list(enumerate_properties(value))) != 0:
        return {
            property_name: convert_for_json_serialization(property_value)
            for property_name, property_value in enumerate_properties(value)
        }

    return repr(value)
