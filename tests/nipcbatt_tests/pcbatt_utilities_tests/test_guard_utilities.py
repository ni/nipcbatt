"""Provides unit tests related to guard_utilities.py module"""

import logging
import platform
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class TestGuard(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `nipcbatt.pcbatt_utilities.guard_utilities.Guard`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_is_not_empty_fails_if_iterable_empty(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_empty"""
        empty_tuple = ()

        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_empty(empty_tuple, nameof(empty_tuple))

        self.assertEqual("The iterable empty_tuple of type tuple is empty.", str(ctx.exception))

    def test_is_not_empty_should_not_fail_if_iterable_not_empty(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_empty"""
        tuple_instance = (1, 3)

        Guard.is_not_empty(tuple_instance, nameof(tuple_instance))

    @unittest.skip("known to fail!")
    def test_size_of_iterable_breaks_iterator(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.size_is_greater_or_equal_than"""
        iterable_instance = map(lambda x: x, range(0, 10))

        Guard.size_is_greater_or_equal_than(iterable_instance, 3, nameof(iterable_instance))

        iterable_instance_to_list = list(iterable_instance)
        self.assertEqual(first=10, second=len(iterable_instance_to_list))

    def test_size_is_greater_or_equal_than_fails_if_iterable_has_not_enough_elements(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.size_is_greater_or_equal_than"""
        tuple_instance = (2, 4)

        with self.assertRaises(ValueError) as ctx:
            Guard.size_is_greater_or_equal_than(tuple_instance, 3, nameof(tuple_instance))

        self.assertEqual(
            "The iterable tuple_instance must have at least 3 elements.",
            str(ctx.exception),
        )

    def test_size_is_greater_or_equal_than_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.size_is_greater_or_equal_than"""
        tuple_instance = (1.0, 2, 3, 4)

        Guard.size_is_greater_or_equal_than(tuple_instance, 3, nameof(tuple_instance))

    def test_size_is_less_than_or_equal_fails_if_iterable_is_too_large(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.Guard.size_is_less_than_or_equal"""
        tuple_instance = (2, 4, 5, 6)

        with self.assertRaises(ValueError) as ctx:
            Guard.size_is_less_than_or_equal(tuple_instance, 3, nameof(tuple_instance))

        self.assertEqual(
            "The size of tuple_instance must less than or equal to 3.",
            str(ctx.exception),
        )

    def test_size_is_less_than_or_equal_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.Guard.size_is_less_than_or_equal"""
        tuple_instance = (1.0, 2)

        Guard.size_is_less_than_or_equal(tuple_instance, 3, nameof(tuple_instance))

    def test_all_elements_are_of_same_type_fails_if_list_contains_invalid_objects(self):
        """Unit test
        of nipcbatt.pcbatt_utilities.guard_utilities.Guard.all_elements_are_of_same_type
        """
        input_list = [1.0, 3.0, "string_not_allowed"]

        with self.assertRaises(TypeError) as ctx:
            Guard.all_elements_are_of_same_type(input_list=input_list, expected_type=float)

        self.assertEqual(
            "Not all elements of the list are of the type (float).", str(ctx.exception)
        )

    def test_all_elements_are_of_same_type_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.all_elements_are_of_same_type"""
        input_list = [1.0, 3.0, 10.0]

        Guard.all_elements_are_of_same_type(input_list=input_list, expected_type=float)

    def test_have_same_size_fails_if_lists_have_not_same_size(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.have_same_size"""
        first_input_list = [1.0, 3.0, 4.0]
        second_input_list = ["item_1", "item_2", "item_3", "item_4"]

        with self.assertRaises(ValueError) as ctx:
            Guard.have_same_size(
                first_iterable_instance=first_input_list,
                first_iterable_name=nameof(first_input_list),
                second_iterable_instance=second_input_list,
                second_iterable_name=nameof(second_input_list),
            )

        self.assertEqual(
            "The iterables (first_input_list and second_input_list) do not have same size.",
            str(ctx.exception),
        )

    def test_have_same_size_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.have_same_size"""
        first_input_list = [1.0, 3.0, 4.0]
        second_input_list = ["item_1", "item_2", "item_3"]

        Guard.have_same_size(
            first_iterable_instance=first_input_list,
            first_iterable_name=nameof(first_input_list),
            second_iterable_instance=second_input_list,
            second_iterable_name=nameof(second_input_list),
        )

    def test_is_not_none_fails_if_object_is_none(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none"""
        instance = None
        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_none(instance, nameof(instance))

        self.assertEqual("The object instance is None.", str(ctx.exception))

    def test_is_not_none_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none"""
        instance = 3.0
        Guard.is_not_none(instance, nameof(instance))

    def test_is_greater_than_zero_fails_if_object_is_string(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_zero"""
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than_zero(instance, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_greater_than_zero_fails_if_object_is_less_than_or_equal_to_zero(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_zero"""
        instance = -6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_greater_than_zero(instance, nameof(instance))

        self.assertEqual("The value instance must be greater than 0.", str(ctx.exception))

    def test_is_greater_than_zero_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_zero"""
        instance = 3.0
        Guard.is_greater_than_zero(instance, nameof(instance))

    def test_is_greater_than_or_equal_to_zero_fails_if_object_is_string(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to_zero
        """
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than_or_equal_to_zero(instance, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_greater_than_or_equal_to_zero_fails_if_object_is_negative(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to_zero
        """
        instance = -6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_greater_than_or_equal_to_zero(instance, nameof(instance))

        self.assertEqual(
            "The value instance must be greater than or equal to 0.", str(ctx.exception)
        )

    def test_is_greater_than_or_equal_to_zero_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to_zero
        """
        instance = 3.0
        Guard.is_greater_than_or_equal_to_zero(instance, nameof(instance))
        instance = 0.0
        Guard.is_greater_than_or_equal_to_zero(instance, nameof(instance))

    def test_is_less_than_zero_fails_if_object_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_zero"""
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than_zero(instance, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_less_than_zero_fails_if_object_is_positive_or_equal_to_zero(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_zero"""
        instance = 6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_less_than_zero(instance, nameof(instance))

        self.assertEqual("The value instance must be less than 0.", str(ctx.exception))

    def test_is_less_than_zero_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_zero"""
        instance = -3.0
        Guard.is_less_than_zero(instance, nameof(instance))

    def test_is_less_than_or_equal_to_zero_fails_if_object_is_string(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to_zero"""
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than_or_equal_to_zero(instance, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_less_than_or_equal_to_zero_fails_if_object_is_greater_than_zero(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to_zero"""
        instance = 6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_less_than_or_equal_to_zero(instance, nameof(instance))

        self.assertEqual("The value instance must be less than or equal to 0.", str(ctx.exception))

    def test_is_less_than_or_equal_to_zero_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to_zero"""
        instance = -3.0
        Guard.is_less_than_or_equal_to_zero(instance, nameof(instance))
        instance = 0.0
        Guard.is_less_than_or_equal_to_zero(instance, nameof(instance))

    def test_is_less_than_fails_if_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than"""
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than(instance, -3, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_less_than_fails_if_expected_greater_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than"""
        instance = -6

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than(instance, "-3", nameof(instance))

        self.assertEqual(
            "The object expected_greater_value is not a numeric value.",
            str(ctx.exception),
        )

    def test_is_less_than_fails_if_value_is_greater_or_equal(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than"""
        instance = -6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_less_than(instance, -8, nameof(instance))

        self.assertEqual("The value instance must be less than -8.", str(ctx.exception))

    def test_is_less_than_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than"""
        instance = 3.0
        Guard.is_less_than(instance, 4.0, nameof(instance))

    def test_is_less_than_or_equal_to_fails_if_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to"""
        instance = "-6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than_or_equal_to(instance, -3, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_less_than_or_equal_to_fails_if_expected_greater_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to"""
        instance = -6

        with self.assertRaises(TypeError) as ctx:
            Guard.is_less_than_or_equal_to(instance, "-3", nameof(instance))

        self.assertEqual(
            "The object expected_greater_value is not a numeric value.",
            str(ctx.exception),
        )

    def test_is_less_than_or_equal_to_fails_if_value_is_greater(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to"""
        instance = -6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_less_than_or_equal_to(instance, -8, nameof(instance))

        self.assertEqual("The value instance must be less than or equal to -8.", str(ctx.exception))

    def test_is_less_than_or_equal_to_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_less_than_or_equal_to"""
        instance = 3.0
        Guard.is_less_than_or_equal_to(instance, 4.0, nameof(instance))
        instance = 4.0
        Guard.is_less_than_or_equal_to(instance, 4.0, nameof(instance))

    def test_is_greater_than_fails_if_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than"""
        instance = "6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than(instance, 3, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_greater_than_fails_if_expected_smaller_value_is_string(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than"""
        instance = 6

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than(
                value=instance, expected_smaller_value="3", value_name=nameof(instance)
            )

        self.assertEqual(
            "The object expected_smaller_value is not a numeric value.",
            str(ctx.exception),
        )

    def test_is_greater_than_fails_if_value_is_less_than_or_equal_to(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than"""
        instance = 6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_greater_than(instance, 8, nameof(instance))

        self.assertEqual("The value instance must be greater than 8.", str(ctx.exception))

    def test_is_greater_than_should_not_fail(self):
        """Unit test of nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than"""
        instance = 6.0
        Guard.is_greater_than(instance, 4.0, nameof(instance))

    def test_is_greater_or_equal_to_fails_if_value_is_string(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to"""
        instance = "6"

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than_or_equal_to(instance, 3, nameof(instance))

        self.assertEqual("The object instance is not a numeric value.", str(ctx.exception))

    def test_is_greater_than_or_equal_to_fails_if_expected_smaller_value_is_string(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to"""
        instance = 6

        with self.assertRaises(TypeError) as ctx:
            Guard.is_greater_than_or_equal_to(
                value=instance, expected_smaller_value="3", value_name=nameof(instance)
            )

        self.assertEqual(
            "The object expected_smaller_value is not a numeric value.",
            str(ctx.exception),
        )

    def test_is_greater_than_or_equal_to_fails_if_value_is_less_than(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to"""
        instance = 6
        with self.assertRaises(ValueError) as ctx:
            Guard.is_greater_than_or_equal_to(instance, 8, nameof(instance))

        self.assertEqual(
            "The value instance must be greater than or equal to 8.", str(ctx.exception)
        )

    def test_is_greater_than_or_equal_to_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_greater_than_or_equal_to"""
        instance = 6.0
        Guard.is_greater_than_or_equal_to(instance, 4.0, nameof(instance))
        instance = 4.0
        Guard.is_greater_than_or_equal_to(instance, 4.0, nameof(instance))

    def test_is_not_none_nor_empty_nor_whitespace_fails_if_string_value_is_none(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        """
        instance = None
        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_none_nor_empty_nor_whitespace(value=instance, value_name=nameof(instance))

        self.assertEqual(
            "The string value instance is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_is_not_none_nor_empty_nor_whitespace_fails_if_string_value_is_empty(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        """
        instance = ""
        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_none_nor_empty_nor_whitespace(value=instance, value_name=nameof(instance))

        self.assertEqual(
            "The string value instance is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_is_not_none_nor_empty_nor_whitespace_fails_if_string_value_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        """
        instance = " "
        with self.assertRaises(ValueError) as ctx:
            Guard.is_not_none_nor_empty_nor_whitespace(value=instance, value_name=nameof(instance))

        self.assertEqual(
            "The string value instance is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_is_not_none_nor_empty_nor_whitespace_should_not_fail(self):
        """Unit test of
        nipcbatt.pcbatt_utilities.guard_utilities.Guard.is_not_none_nor_empty_nor_whitespace
        """
        instance = "3.0"
        Guard.is_not_none_nor_empty_nor_whitespace(value=instance, value_name=nameof(instance))


if __name__ == "__main__":
    unittest.main()
