""" Provides a set of guard function utilities routines."""

from typing import Iterable, Type

from varname import nameof


class Guard:
    """Defines some methods used to validate arguments of functions."""

    NOT_ALL_ELEMENTS_OF_LIST_ARE_OF_TYPE_ARGS_1 = (
        "Not all elements of the list are of the type ({})."
    )

    ITERABLE_IS_EMPTY_ARGS_2 = "The iterable {} of type {} is empty."

    ITERABLES_HAVE_NOT_SAME_SIZE_ARGS_2 = "The iterables ({} and {}) do not have same size."

    ITERABLE_MUST_HAVE_ENOUGH_ELEMENTS_ARGS_2 = "The iterable {} must have at least {} elements."

    ITERABLE_MUST_CONTAIN_LESS_THAN_SPECIFIC_NUMBER_OF_ELEMENTS_ARGS_2 = (
        "The size of {} must less than or equal to {}."
    )

    VALUE_IS_NOT_INTEGER = "The value {} is not an integer."

    VALUE_IS_NOT_FLOAT = "The value {} is not a float."

    OBJECT_IS_NONE_ARGS_1 = "The object {} is None."

    VALUE_MUST_BE_LESS_THAN_ARGS_2 = "The value {} must be less than {}."

    VALUE_MUST_BE_LESS_THAN_OR_EQUAL_TO_ARGS_2 = "The value {} must be less than or equal to {}."

    VALUE_MUST_BE_GREATER_THAN_ARGS_2 = "The value {} must be greater than {}."

    VALUE_MUST_BE_GREATER_THAN_OR_EQUAL_TO_ARGS_2 = (
        "The value {} must be greater than or equal to {}."
    )

    VALUE_MUST_BE_WITHIN_LIMITS_INCLUDED = (
        "The value of {} must be greater than or equal to {} and less than or equal to {}."
    )

    VALUE_MUST_BE_WITHIN_LIMITS_EXCLUDED = (
        "The value of {} must be greater than {} and less than {}."
    )

    STRING_IS_NONE_OR_EMPTY_OR_WHITESPACE_ARGS_1 = (
        "The string value {} is None, empty or whitespace."
    )

    VALUE_IS_NOT_NUMERIC_ARGS_1 = "The object {} is not a numeric value."

    @staticmethod
    def all_elements_are_of_same_type(input_list: list, expected_type: Type):
        """Asserts that all elements of the the list are of same type.

        Args:
            input_list (List): The list to validate.
            expected_type (Type): The expected type.

        Raises:
            TypeError: Raised when some elements in the list are not of the expected type.
        """
        if all(isinstance(item, expected_type) for item in input_list):
            return

        raise TypeError(
            Guard.NOT_ALL_ELEMENTS_OF_LIST_ARE_OF_TYPE_ARGS_1.format(expected_type.__name__)
        )

    @staticmethod
    def is_not_none(instance: object, instance_name: str):
        """Asserts that the object is not None."""
        if not instance is None:
            return

        raise ValueError(Guard.OBJECT_IS_NONE_ARGS_1.format(instance_name))

    @staticmethod
    def is_not_int(value, value_name: str):
        """Ensures value is not an integer"""
        if isinstance(value, int):
            raise ValueError(Guard.VALUE_IS_NOT_INTEGER.format(value_name))

    @staticmethod
    def is_float(value, value_name: str):
        "Ensures value is a float"
        if isinstance(value, float):
            return

        raise ValueError(Guard.VALUE_IS_NOT_FLOAT.format(value_name))

    @staticmethod
    def is_int(value, value_name: str):
        "Ensures value is an integer"
        if isinstance(value, int):
            return

        raise ValueError(Guard.VALUE_IS_NOT_INTEGER.format(value_name))

    @staticmethod
    def is_not_float(value, value_name: str):
        """Ensures value is not a float"""
        if isinstance(value, float):
            raise ValueError(Guard.VALUE_IS_NOT_FLOAT.format(value_name))

    @staticmethod
    def is_greater_than_zero(value, value_name: str):
        """Asserts that the value is greater than zero."""
        Guard.is_greater_than(value=value, expected_smaller_value=0, value_name=value_name)

    @staticmethod
    def is_greater_than_or_equal_to_zero(value, value_name: str):
        """Asserts that the value is greater than or equal to zero."""
        Guard.is_greater_than_or_equal_to(
            value=value, expected_smaller_value=0, value_name=value_name
        )

    @staticmethod
    def is_less_than_zero(value, value_name: str):
        """Asserts that the value is less than to zero."""
        Guard.is_less_than(value=value, expected_greater_value=0, value_name=value_name)

    @staticmethod
    def is_less_than_or_equal_to_zero(value, value_name: str):
        """Asserts that the value is less than or equal to zero."""
        Guard.is_less_than_or_equal_to(value=value, expected_greater_value=0, value_name=value_name)

    @staticmethod
    def is_less_than(value, expected_greater_value, value_name: str):
        """Asserts that the value is less than expected greater value."""
        if not isinstance(value, (int, float)):
            raise TypeError(Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(value_name))

        if not isinstance(expected_greater_value, (int, float)):
            raise TypeError(
                Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(nameof(expected_greater_value))
            )

        if value < expected_greater_value:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_LESS_THAN_ARGS_2.format(value_name, expected_greater_value)
        )

    @staticmethod
    def is_less_than_or_equal_to(value, expected_greater_value, value_name: str):
        """Asserts that the value is less than expected greater value."""
        if not isinstance(value, (int, float)):
            raise TypeError(Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(value_name))

        if not isinstance(expected_greater_value, (int, float)):
            raise TypeError(
                Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(nameof(expected_greater_value))
            )

        if value <= expected_greater_value:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_LESS_THAN_OR_EQUAL_TO_ARGS_2.format(
                value_name, expected_greater_value
            )
        )

    @staticmethod
    def is_greater_than(value, expected_smaller_value, value_name: str):
        """Asserts that the value is greater than expected smaller value."""
        if not isinstance(value, (int, float)):
            raise TypeError(Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(value_name))

        if not isinstance(expected_smaller_value, (int, float)):
            raise TypeError(
                Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(nameof(expected_smaller_value))
            )

        if value > expected_smaller_value:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_GREATER_THAN_ARGS_2.format(value_name, expected_smaller_value)
        )

    @staticmethod
    def is_greater_than_or_equal_to(value, expected_smaller_value, value_name: str):
        """Asserts that the value is greater than or equal to expected smaller value."""
        if not isinstance(value, (int, float)):
            raise TypeError(Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(value_name))

        if not isinstance(expected_smaller_value, (int, float)):
            raise TypeError(
                Guard.VALUE_IS_NOT_NUMERIC_ARGS_1.format(nameof(expected_smaller_value))
            )

        if value >= expected_smaller_value:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_GREATER_THAN_OR_EQUAL_TO_ARGS_2.format(
                value_name, expected_smaller_value
            )
        )

    @staticmethod
    def is_not_empty(iterable_instance: Iterable, instance_name: str):
        """Asserts that the iterable object is not empty."""
        if len(iterable_instance) > 0:
            return
        raise ValueError(
            Guard.ITERABLE_IS_EMPTY_ARGS_2.format(instance_name, type(iterable_instance).__name__)
        )

    @staticmethod
    def is_not_none_nor_empty_nor_whitespace(value: str, value_name: str):
        """Asserts that the str object is empty."""
        if not value is None and value and value.strip():
            return

        raise ValueError(Guard.STRING_IS_NONE_OR_EMPTY_OR_WHITESPACE_ARGS_1.format(value_name))

    @staticmethod
    def size_is_greater_or_equal_than(iterable_instance: Iterable, size: int, iterable_name: str):
        """Asserts that the iterable object has enough elements."""
        if len(iterable_instance) >= size:
            return
        raise ValueError(
            Guard.ITERABLE_MUST_HAVE_ENOUGH_ELEMENTS_ARGS_2.format(iterable_name, size)
        )

    @staticmethod
    def size_is_less_than_or_equal(iterable_instance: Iterable, size: int, iterable_name: str):
        """Asserts that the iterable object does contains
        less than the specific size."""
        if len(iterable_instance) <= size:
            return
        raise ValueError(
            Guard.ITERABLE_MUST_CONTAIN_LESS_THAN_SPECIFIC_NUMBER_OF_ELEMENTS_ARGS_2.format(
                iterable_name, size
            )
        )

    @staticmethod
    def have_same_size(
        first_iterable_instance: Iterable,
        first_iterable_name: str,
        second_iterable_instance: Iterable,
        second_iterable_name: str,
    ):
        """Asserts that both iterable objects have same size."""
        if len(first_iterable_instance) == len(second_iterable_instance):
            return

        raise ValueError(
            Guard.ITERABLES_HAVE_NOT_SAME_SIZE_ARGS_2.format(
                first_iterable_name, second_iterable_name
            )
        )

    @staticmethod
    def is_within_limits_included(value, lower_limit, upper_limit, value_name: str):
        """Asserts that the value is not within the specified limits including the limit values"""

        if value >= lower_limit and value <= upper_limit:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_WITHIN_LIMITS_INCLUDED.format(value_name, lower_limit, upper_limit)
        )

    @staticmethod
    def is_within_limits_excluded(value, lower_limit, upper_limit, value_name: str):
        """Asserts that the value is not within the specified limits excluding the limit values"""

        if value > lower_limit and value < upper_limit:
            return

        raise ValueError(
            Guard.VALUE_MUST_BE_WITHIN_LIMITS_EXCLUDED.format(value_name, lower_limit, upper_limit)
        )
