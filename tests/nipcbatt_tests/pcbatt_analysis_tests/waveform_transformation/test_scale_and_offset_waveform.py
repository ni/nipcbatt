"""Provides unit tests related to square_waveform.py module"""

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_transformation import scale_and_offset_waveform


class TestScaleAndOffsetWaveform(unittest.TestCase):
    """Defines a test fixture that checks transformation functions of module
    `scale_and_offset_waveform`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestScaleAndOffsetWaveform),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            (
                "ScaleFactor=1.00_Offset=0.00",  # case_name
                1,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=0.00",  # case_name
                2,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=0.05_Offset=0.00",  # case_name
                0.05,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=1.00",  # case_name
                2,  # expected_scale_factor
                1,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=-1.00",  # case_name
                2,  # expected_scale_factor
                -1,  # expected_offset
            ),
        ]
    )
    def test_scale_and_apply_offset_linear_function(
        self, case_name: str, expected_scale_factor: float, expected_offset: float
    ):
        """Test of `scale_and_offset_waveform.scale_and_apply_offset` function"""

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        input_waveform = numpy.array([1, 2, 3, 4], dtype=numpy.float64)

        # Act
        transformed_waveform = scale_and_offset_waveform.scale_and_apply_offset(
            waveform_samples=input_waveform,
            scale_factor=expected_scale_factor,
            offset=expected_offset,
        )
        # Assert
        self.assertEqual(first=input_waveform.size, second=transformed_waveform.size)
        self.assertNotEqual(first=id(input_waveform), second=id(transformed_waveform))

        for raw_sample, transformed_sample in zip(input_waveform, transformed_waveform):
            self.assertEqual(
                first=expected_scale_factor * raw_sample + expected_offset,
                second=transformed_sample,
            )

    @parameterized.expand(
        [
            (
                "ScaleFactor=1.00_Offset=0.00",  # case_name
                1,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=0.00",  # case_name
                2,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=0.05_Offset=0.00",  # case_name
                0.05,  # expected_scale_factor
                0,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=1.00",  # case_name
                2,  # expected_scale_factor
                1,  # expected_offset
            ),
            (
                "ScaleFactor=2.00_Offset=-1.00",  # case_name
                2,  # expected_scale_factor
                -1,  # expected_offset
            ),
        ]
    )
    def test_scale_and_apply_offset_inplace_linear_function(
        self, case_name: str, expected_scale_factor: float, expected_offset: float
    ):
        """Test of `scale_and_offset_waveform.scale_and_apply_offset_inplace` function"""

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        input_waveform = numpy.array([1, 2, 3, 4], dtype=numpy.float64)
        input_waveform_copy = numpy.array([1, 2, 3, 4], dtype=numpy.float64)

        # Act
        transformed_waveform = scale_and_offset_waveform.scale_and_apply_offset_inplace(
            waveform_samples=input_waveform,
            scale_factor=expected_scale_factor,
            offset=expected_offset,
        )
        # Assert
        self.assertEqual(first=input_waveform_copy.size, second=transformed_waveform.size)
        self.assertEqual(first=id(input_waveform), second=id(transformed_waveform))

        for raw_sample, transformed_sample in zip(input_waveform_copy, transformed_waveform):
            self.assertEqual(
                first=expected_scale_factor * raw_sample + expected_offset,
                second=transformed_sample,
            )


if __name__ == "__main__":
    unittest.main()
