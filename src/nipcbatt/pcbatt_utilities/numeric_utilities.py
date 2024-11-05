"""Provides a set of numeric related utilities functions."""

from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def from_percent_to_decimal_ratio(percent: float) -> float:
    """Computes decimal ration of a given percentage value, for example 50%
    returns 0.5.

    Args:
        percent: percentage value to convert to ratio.

    Returns:
        float: for example 10  returns 0.1, 100 returns 1 and  0 returns 0

    Raises:
        ValueError: Occurs when input percent is less than zero.
    """
    Guard.is_greater_than_or_equal_to_zero(percent, nameof(percent))
    return percent / 100


def percent_of(percent: float, value: float) -> float:
    """Computes percent ratio of a given value.

    Args:
        percent (float): Percentage ratio to compute.
        value (float): Value for which percent ration is needed.

    Returns:
        float: for example (10 , 100) -> 10
    Raises:
        ValueError: Occurs when input percent is less than zero.
    """
    Guard.is_greater_than_or_equal_to_zero(percent, nameof(percent))
    return (value * percent) / 100


def absolute_value(value: float) -> float:
    """Computes absolute value of a given value.

    Args:
        value (float): Value for which absolute value is needed.

    Returns:
        float: for example -10 -> 10
    """
    return abs(value)


def invert_value(value: float):
    """Computes invert value of a given value.

    Args:
        value (float): Value for which invert value is needed.

    Returns:
        float: for example 0.5 -> 2
    Raises:
        ValueError: Occurs when input value equals zero.
    """

    Guard.is_greater_than_zero(value, nameof(value))
    return 1 / value
