"""This module provides numpy framework check."""

import importlib.metadata
import inspect
import logging
import sys
import unittest

import numpy
import numpy.matlib
from varname import nameof


class TestNDArray(unittest.TestCase):
    """Defines a test fixture that provides sample usage of ndarray datastructure.

    Args:
        unittest (TestCase): test case using unittest framework
    """

    def setUp(self):
        print("Setup test method")

    def tearDown(self):
        print("Teardown test method")

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_ndarray_zeros_array(self):
        """Checks method numpy.zeros is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (243 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.zeros(shape=(4, 1), dtype=numpy.int16)
        self.assertIsNotNone(ndarray_instance)
        self.assertEqual(first=4, second=ndarray_instance.size)

        array_shape = ndarray_instance.shape
        array_shape_item1 = array_shape[0]

        logging.debug("%s = %s", nameof(array_shape), array_shape)

        self.assertEqual(first=4, second=array_shape_item1)
        self.assertEqual(first=0, second=ndarray_instance[0])
        self.assertEqual(first=0, second=ndarray_instance[1])
        self.assertEqual(first=0, second=ndarray_instance[2])
        self.assertEqual(first=0, second=ndarray_instance[3])

    def test_ndarray_create_single_dimension_array(self):
        """Checks method numpy.array is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (243 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.array([1, 2, 3, 4], dtype=numpy.int16)
        self.assertIsNotNone(ndarray_instance)
        self.assertEqual(first=4, second=ndarray_instance.size)

        array_shape = ndarray_instance.shape
        array_shape_item1 = array_shape[0]

        logging.debug("%s = %s", nameof(array_shape), array_shape)

        self.assertEqual(first=4, second=array_shape_item1)

    def test_ndarray_create_two_dimensions_array(self):
        """Checks method numpy.ndarray is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (245 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.ndarray(shape=(2, 2), dtype=numpy.int16)
        logging.debug("%s = %s", nameof(ndarray_instance), ndarray_instance)

        self.assertIsNotNone(ndarray_instance)
        self.assertEqual(first=4, second=ndarray_instance.size)

        array_shape = ndarray_instance.shape
        array_shape_item1 = array_shape[0]
        array_shape_item2 = array_shape[1]

        logging.debug("%s = %s", nameof(array_shape), array_shape)

        self.assertEqual(first=2, second=array_shape_item1)
        self.assertEqual(first=2, second=array_shape_item2)

        ndarray_instance[0][0] = 2
        ndarray_instance[0][1] = 2
        ndarray_instance[1][0] = 2
        ndarray_instance[1][1] = 2

        self.assertEqual(first=ndarray_instance[0][0], second=2)
        self.assertEqual(first=ndarray_instance[0][1], second=2)
        self.assertEqual(first=ndarray_instance[1][0], second=2)
        self.assertEqual(first=ndarray_instance[1][0], second=2)

    def test_ndarray_sum_single_dimension_array(self):
        """Checks method numpy.sum is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (241 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.array([1, 2, 3, 4], dtype=numpy.int16)

        ndarray_instance_sum = ndarray_instance.sum()
        self.assertEqual(first=10, second=ndarray_instance_sum)

    def test_ndarray_mean_single_dimension_array(self):
        """Checks method numpy.mean is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (242 > 100 characters) (auto-generated noqa)

        logging.debug("=> %s", inspect.currentframe().f_code.co_name)
        ndarray_instance = numpy.array([1, 2, 3, 4], dtype=numpy.int16)

        ndarray_instance_sum = ndarray_instance.mean()
        self.assertEqual(first=10 / 4, second=ndarray_instance_sum)


class TestMatlib(unittest.TestCase):
    """Defines a test fixture that checks numpy package is ready to use.

    Args:
        unittest (_type_): test case type
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_mathlib_average(self):
        """Checks method numpy.matlib.average is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
        average_result = numpy.matlib.average(a=[1, -1, -2, 2])
        self.assertIsNotNone(average_result)
        self.assertEqual(first=0, second=average_result)

    def test_mathlib_amax(self):
        """Checks method numpy.matlib.amax is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
        amax_result = numpy.matlib.amax(a=[1, -1, -2, 2])
        self.assertIsNotNone(amax_result)
        self.assertEqual(first=2, second=amax_result)

    def test_mathlib_amin(self):
        """Checks method numpy.matlib.amin is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
        amin_result = numpy.matlib.amin(a=[1, -1, -2, 2])
        self.assertIsNotNone(amin_result)
        self.assertEqual(first=-2, second=amin_result)

    def test_mathlib_all(self):
        """Checks method numpy.matlib.all is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        all_result = numpy.matlib.all(a=[-1, -1, -2, -2], axis=0, where=lambda x: x < 0)
        self.assertIsNotNone(all_result)
        self.assertEqual(first=True, second=all_result)


if __name__ == "__main__":
    unittest.main()
