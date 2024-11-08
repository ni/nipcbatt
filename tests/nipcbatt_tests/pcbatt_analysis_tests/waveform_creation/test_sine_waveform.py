"""Provides unit tests related to sine_waveform.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_creation import sine_waveform
from nipcbatt.pcbatt_utilities import csv_utilities


class TestSineWaveform(unittest.TestCase):
    """Defines a test fixture that checks creation functions of module
    `sine_waveform`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

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
            nameof(TestSineWaveform),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @parameterized.expand(
        [
            ("60_Hz_Phase=0", 1, 60, 0, 0, 6000, 1),
            ("60_Hz_Phase=0.5_PI", 1, 60, 1.5707963, 0, 6000, 1),
            ("60_Hz_Phase=1.0_PI", 1, 60, 3.1415927, 0, 6000, 1),
            ("60_Hz_Phase=1.0_PI_Offset=1.0", 1, 60, 3.1415927, 1, 6000, 1),
        ]
    )
    def test_create_cosine_waveform(
        self,
        case_name: str,
        expected_amplitude: float,
        expected_frequency: float,
        expected_phase: float,
        expected_offset: float,
        expected_sampling_rate: float,
        expected_waveform_duration_seconds: float,
    ):
        """Test of `sin_waveform.create_cosine_waveform` function"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (256 > 100 characters) (auto-generated noqa)

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        expected_samples_count = expected_waveform_duration_seconds * expected_sampling_rate

        # Act
        waveform_samples = sine_waveform.create_cosine_waveform(
            amplitude=expected_amplitude,
            frequency=expected_frequency,
            phase=expected_phase,
            offset=expected_offset,
            samples_count=expected_samples_count,
            sampling_rate=expected_sampling_rate,
        )

        csv_file_ouput_path = os.path.join(
            TestSineWaveform.tests_output_folder_path,
            f"test_create_cosine_waveform_{case_name}.csv",
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

    @parameterized.expand(
        [
            ("60_Hz_Phase=0", 1, 60, 0, 0, 6000, 1),
            ("60_Hz_Phase=0.5_PI", 1, 60, 1.5707963, 0, 6000, 1),
            ("60_Hz_Phase=1.0_PI", 1, 60, 3.1415927, 0, 6000, 1),
            ("60_Hz_Phase=1.0_PI_Offset=1.0", 1, 60, 3.1415927, 1, 6000, 1),
        ]
    )
    def test_create_sine_waveform(
        self,
        case_name: str,
        expected_amplitude: float,
        expected_frequency: float,
        expected_phase: float,
        expected_offset: float,
        expected_sampling_rate: float,
        expected_waveform_duration_seconds: float,
    ):
        """Test of `sin_waveform.create_sine_waveform` function"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)
        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        expected_samples_count = expected_waveform_duration_seconds * expected_sampling_rate

        # Act
        waveform_samples = sine_waveform.create_sine_waveform(
            amplitude=expected_amplitude,
            frequency=expected_frequency,
            phase=expected_phase,
            offset=expected_offset,
            samples_count=expected_samples_count,
            sampling_rate=expected_sampling_rate,
        )

        csv_file_ouput_path = os.path.join(
            TestSineWaveform.tests_output_folder_path,
            f"test_create_sine_waveform_{case_name}.csv",
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


if __name__ == "__main__":
    unittest.main()
