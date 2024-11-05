"""Provides unit tests related to multitones_waveform.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_creation import multitones_waveform
from nipcbatt.pcbatt_utilities import csv_utilities, numeric_utilities


class TestMultitonesWaveform(unittest.TestCase):
    """Defines a test fixture that checks creation functions of module
    `multitones_waveform`.

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
            nameof(TestMultitonesWaveform),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_create_multitones_waveform_single_tone(
        self,
    ):
        """Test of `multitones_waveform.create_multitones_waveform` function"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (267 > 100 characters) (auto-generated noqa)

        # Arrange
        single_tone_frequency = 440
        single_tone_amplitude = 1
        single_tone_phase = 0
        single_tone_sampling_rate = 44100
        single_tone_duration_seconds = 0.2
        single_tone_samples_count = (int)(single_tone_duration_seconds * single_tone_sampling_rate)
        tolerance_percent = 0.5

        # Act
        single_tone_samples = multitones_waveform.create_multitones_waveform(
            multitones_amplitude=1,
            waveform_tones=[
                multitones_waveform.WaveformTone(
                    frequency=single_tone_frequency,
                    amplitude=single_tone_amplitude,
                    phase_radians=single_tone_phase,
                )
            ],
            samples_count=single_tone_samples_count,
            sampling_rate=single_tone_sampling_rate,
        )

        single_tone_samples_max = single_tone_samples.max()
        single_tone_samples_min = single_tone_samples.min()

        csv_file_ouput_path = os.path.join(
            TestMultitonesWaveform.tests_output_folder_path,
            "test_create_multitones_waveform_single_tone.csv",
        )

        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=single_tone_samples,
            signal_sampling_rate=single_tone_sampling_rate,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertEqual(first=single_tone_samples_count, second=single_tone_samples.size)
        self.assertAlmostEqual(
            first=single_tone_amplitude,
            second=single_tone_samples_max,
            delta=numeric_utilities.percent_of(tolerance_percent, single_tone_amplitude),
        )
        self.assertAlmostEqual(
            first=-single_tone_amplitude,
            second=single_tone_samples_min,
            delta=numeric_utilities.percent_of(tolerance_percent, single_tone_amplitude),
        )

    def test_create_multitones_waveform_multiple_harmonics(
        self,
    ):
        """Test of `multitones_waveform.create_multitones_waveform` function"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (267 > 100 characters) (auto-generated noqa)

        # Arrange
        fundamental_tone_frequency = 440
        fundamental_tone_amplitude = 1
        fundamental_tone_phase = 0
        multiple_tones_amplitude = 1
        tones_sampling_rate = 44100
        tones_duration_seconds = 0.2
        tones_samples_count = (int)(tones_duration_seconds * tones_sampling_rate)
        tolerance_percent = 0.5

        # Act
        multiple_tones_samples = multitones_waveform.create_multitones_waveform(
            multitones_amplitude=multiple_tones_amplitude,
            waveform_tones=[
                multitones_waveform.WaveformTone(
                    frequency=fundamental_tone_frequency,
                    amplitude=fundamental_tone_amplitude,
                    phase_radians=fundamental_tone_phase,
                ),
                multitones_waveform.WaveformTone(
                    frequency=2 * fundamental_tone_frequency,
                    amplitude=0.5 * fundamental_tone_amplitude,
                    phase_radians=fundamental_tone_phase,
                ),
                multitones_waveform.WaveformTone(
                    frequency=3 * fundamental_tone_frequency,
                    amplitude=0.25 * fundamental_tone_amplitude,
                    phase_radians=fundamental_tone_phase,
                ),
            ],
            samples_count=tones_samples_count,
            sampling_rate=tones_sampling_rate,
        )

        multiple_tones_samples_max = multiple_tones_samples.max()
        multiple_tones_samples_min = multiple_tones_samples.min()

        csv_file_ouput_path = os.path.join(
            TestMultitonesWaveform.tests_output_folder_path,
            "test_create_multitones_waveform_multiple_harmonics.csv",
        )

        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=multiple_tones_samples,
            signal_sampling_rate=tones_sampling_rate,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertEqual(first=tones_samples_count, second=multiple_tones_samples.size)

        self.assertAlmostEqual(
            first=multiple_tones_amplitude,
            second=multiple_tones_samples_max,
            delta=numeric_utilities.percent_of(tolerance_percent, multiple_tones_amplitude),
        )
        self.assertAlmostEqual(
            first=-multiple_tones_amplitude,
            second=multiple_tones_samples_min,
            delta=numeric_utilities.percent_of(tolerance_percent, multiple_tones_amplitude),
        )


if __name__ == "__main__":
    unittest.main()
