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

from nipcbatt.pcbatt_analysis.waveform_creation import square_waveform
from nipcbatt.pcbatt_utilities import csv_utilities


class TestSquareWaveform(unittest.TestCase):
    """Defines a test fixture that checks creation functions of module
    `square_waveform`.

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
            nameof(TestSquareWaveform),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            (
                "60_Hz_Duty=0.00_Offset=1.00_Phase=0.0_PI",  # case_name
                1,  # expected_amplitude
                60,  # expected_frequency
                0.0,  # expected_duty_cycle
                0,  # expected_phase
                1,  # expected_offset
                6000,  # expected_sampling_rate
                2,  # expected_waveform_duration_seconds
                0,  # expected_waveform_max
                0,  # expected_waveform_max
            ),
            ("60_Hz_Duty=0.25_Phase=0.0_PI", 1, 60, 0.25, 0, 0, 6000, 2, +1, -1),
            ("60_Hz_Duty=0.50_Phase=0.0_PI", 1, 60, 0.50, 0, 0, 6000, 2, +1, -1),
            ("60_Hz_Duty=0.75_Phase=0.0_PI", 1, 60, 0.75, 0, 0, 6000, 2, +1, -1),
            (
                "60_Hz_Duty=1.00_Phase=0.0_PI",  # case_name
                1,  # expected_amplitude
                60,  # expected_frequency
                1.00,  # expected_duty_cycle
                0,  # expected_phase
                1,  # expected_offset
                6000,  # expected_sampling_rate
                2,  # expected_waveform_duration_seconds
                2,  # expected_waveform_max
                2,  # expected_waveform_max
            ),
            (
                "60_Hz_Duty=0.50_Offset=1.00_Amplitude=0.5",
                0.5,
                60,
                0.50,
                0,
                1.00,
                6000,
                2,
                +1.5,
                +0.5,
            ),
            (
                "60_Hz_Duty=0.50_Phase=1.0_PI",
                1,
                60,
                0.50,
                3.1415927,
                0,
                6000,
                2,
                +1,
                -1,
            ),
            (
                "60_Hz_Duty=0.50_Phase=2.0_PI",
                1,
                60,
                0.50,
                2 * 3.1415927,
                0,
                6000,
                2,
                +1,
                -1,
            ),
            (
                "60_Hz_Duty=0.50_Phase=0.5_PI",
                1,
                60,
                0.50,
                0.5 * 3.1415927,
                0,
                6000,
                2,
                +1,
                -1,
            ),
        ]
    )
    def test_create_square_waveform(
        self,
        case_name: str,
        expected_amplitude: float,
        expected_frequency: float,
        expected_duty_cycle: float,
        expected_phase: float,
        expected_offset: float,
        expected_sampling_rate: float,
        expected_waveform_duration_seconds: float,
        expected_waveform_max: float,
        expected_waveform_min: float,
    ):
        """Test of `square_waveform.create_square_waveform` function"""

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        expected_samples_count = expected_waveform_duration_seconds * expected_sampling_rate

        # Act
        waveform_samples = square_waveform.create_square_waveform(
            amplitude=expected_amplitude,
            frequency=expected_frequency,
            duty_cycle=expected_duty_cycle,
            phase=expected_phase,
            offset=expected_offset,
            samples_count=expected_samples_count,
            sampling_rate=expected_sampling_rate,
        )

        actual_waveform_max = numpy.max(waveform_samples)
        actual_waveform_min = numpy.min(waveform_samples)

        csv_file_ouput_path = os.path.join(
            TestSquareWaveform.tests_output_folder_path,
            f"test_create_square_waveform{case_name}.csv",
        )

        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=waveform_samples,
            signal_sampling_rate=expected_sampling_rate,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertEqual(first=expected_samples_count, second=waveform_samples.size)
        self.assertEqual(first=expected_waveform_max, second=actual_waveform_max)
        self.assertEqual(first=expected_waveform_min, second=actual_waveform_min)


if __name__ == "__main__":
    unittest.main()
