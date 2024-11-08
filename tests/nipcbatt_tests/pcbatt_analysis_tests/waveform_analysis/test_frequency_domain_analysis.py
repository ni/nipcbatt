"""Defines unit tests related to nipcbatt.pcbatt_analysis.frequency_domain_analysis module."""

import argparse
import logging
import math
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
import scipy.signal
from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_analysis import analysis_library_info
from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.frequency_domain_analysis import (
    LabViewFftSpectrumAmplitudePhase,
    LabViewFftSpectrumWindow,
    LabViewFrequencyDomainProcessing,
    LabViewMultipleTonesMeasurement,
    LabViewTonesSortingMode,
    MultipleTonesAmplitudePhaseSpectrumProcessingResult,
    MultipleTonesProcessingResult,
)
from nipcbatt.pcbatt_analysis.waveform_creation import sine_waveform, square_waveform
from nipcbatt.pcbatt_utilities import (
    csv_utilities,
    functional_utilities,
    numeric_utilities,
)


# Input types
class TestLabViewFftSpectrumWindow(unittest.TestCase):
    """Provides unit tests of `FftSpectrumWindow` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @parameterized.expand(
        [
            ("RECTANGLE", LabViewFftSpectrumWindow.RECTANGLE, 0),
            ("HANNING", LabViewFftSpectrumWindow.HANNING, 1),
            ("HAMMING", LabViewFftSpectrumWindow.HAMMING, 2),
            ("BLACKMAN_HARRIS", LabViewFftSpectrumWindow.BLACKMAN_HARRIS, 3),
            ("BLACKMAN_EXACT", LabViewFftSpectrumWindow.BLACKMAN_EXACT, 4),
            ("BLACKMAN", LabViewFftSpectrumWindow.BLACKMAN, 5),
            ("FLAT_TOP", LabViewFftSpectrumWindow.FLAT_TOP, 6),
            ("BHARRIS_4TERMS", LabViewFftSpectrumWindow.BHARRIS_4TERMS, 7),
            ("BHARRIS_7TERMS", LabViewFftSpectrumWindow.BHARRIS_7TERMS, 8),
            ("LOW_LATERAL_LOBE", LabViewFftSpectrumWindow.LOW_LATERAL_LOBE, 9),
            ("BLACKMAN_NUTTALL", LabViewFftSpectrumWindow.BLACKMAN_NUTTALL, 11),
            ("TRIANGLE", LabViewFftSpectrumWindow.TRIANGLE, 30),
            ("BARTLETT_HANNING", LabViewFftSpectrumWindow.BARTLETT_HANNING, 31),
            ("BOHMAN", LabViewFftSpectrumWindow.BOHMAN, 32),
            ("PARZEN", LabViewFftSpectrumWindow.PARZEN, 33),
            ("WELCH", LabViewFftSpectrumWindow.WELCH, 34),
            ("KAISER", LabViewFftSpectrumWindow.KAISER, 60),
            ("DOLPH_TCHEBYCHEV", LabViewFftSpectrumWindow.DOLPH_TCHEBYCHEV, 61),
            ("GAUSSIAN", LabViewFftSpectrumWindow.GAUSSIAN, 62),
        ]
    )
    def test_labview_fft_spectrum_window_integer_values(
        self,
        case_name: str,
        actual_enum_value: LabViewFftSpectrumWindow,
        expected_int_value: int,
    ):
        """Test of `LabViewFftSpectrumWindow` integer values"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (174 > 100 characters) (auto-generated noqa)
        logging.debug("%s = %s", nameof(case_name), case_name)
        self.assertEqual(expected_int_value, actual_enum_value)


# Results types
class TestMultipleTonesProcessingResult(unittest.TestCase):
    """Provides unit tests of `MultipleTonesProcessingResult` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestMultipleTonesProcessingResult),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @parameterized.expand(
        [
            ("PEAK_AMPLITUDE_440Hz_90_Degrees", SpectrumAmplitudeType.PEAK, 1, 440, 90),
            (
                "RMS_AMPLITUDE_440Hz_90_Degrees",
                SpectrumAmplitudeType.RMS,
                0.707,
                440,
                90,
            ),
            (
                "RMS_AMPLITUDE_440Hz_180_Degrees",
                SpectrumAmplitudeType.RMS,
                0.707,
                440,
                180,
            ),
        ]
    )
    def test_multiple_tones_processing_result_single_tone_waveform(
        self,
        case_name: str,
        expected_amplitude_type: SpectrumAmplitudeType,
        expected_amplitude_value: float,
        expected_frequency_value: float,
        expected_phase_degrees: float,
    ):
        """Test of AmplitudePhaseSpectrum class constructor."""
        logging.debug("%s = %s", nameof(case_name), case_name)

        # Act
        multiple_tones_processing_result = MultipleTonesProcessingResult(
            detected_tones=[
                WaveformTone(
                    frequency=expected_frequency_value,
                    amplitude=expected_amplitude_value,
                    phase_radians=math.radians(expected_phase_degrees),
                )
            ],
            amplitude_type=expected_amplitude_type,
        )
        logging.debug(
            "%s = %s",
            nameof(multiple_tones_processing_result),
            repr(multiple_tones_processing_result),
        )

        # Assert
        self.assertEqual(expected_amplitude_type, multiple_tones_processing_result.amplitude_type)

        self.assertEqual(1, len(multiple_tones_processing_result.detected_tones))

        self.assertEqual(expected_amplitude_type, multiple_tones_processing_result.amplitude_type)
        self.assertEqual(
            expected_amplitude_value,
            multiple_tones_processing_result.detected_tones[0].amplitude,
        )

        self.assertEqual(
            expected_frequency_value,
            multiple_tones_processing_result.detected_tones[0].frequency,
        )
        self.assertEqual(
            expected_phase_degrees,
            multiple_tones_processing_result.detected_tones[0].phase_degrees,
        )


# Frequency domain processing tests
class TestMultipleTonesAmplitudePhaseSpectrumProcessingResult(unittest.TestCase):
    """Provides unit tests of `MultipleTonesAmplitudePhaseSpectrumProcessingResult` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # activate debug traces of native dll
        analysis_library_info.enable_traces(True)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestMultipleTonesAmplitudePhaseSpectrumProcessingResult),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    def test_multiple_tones_amplitude_phase_spectrum_processing_result(self):
        """Test of `MultipleTonesAmplitudePhaseSpectrumProcessingResult` class constructor."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)

        # Arrange
        expected_single_tone_amplitude = 4000
        expected_single_tone_frequency = 11
        expected_single_tone_phase_degrees = 90
        expected_phase_unit = SpectrumPhaseUnit.DEGREE
        expected_amplitude_type = SpectrumAmplitudeType.PEAK

        # Act
        multiple_tones_amplitude_phase_spectrum = (
            MultipleTonesAmplitudePhaseSpectrumProcessingResult(
                multiple_tones_result=MultipleTonesProcessingResult(
                    detected_tones=[
                        WaveformTone(
                            frequency=expected_single_tone_frequency,
                            amplitude=expected_single_tone_amplitude,
                            phase_radians=math.radians(expected_single_tone_phase_degrees),
                        )
                    ],
                    amplitude_type=expected_amplitude_type,
                ),
                amplitude_phase_spectrum=AmplitudePhaseSpectrum(
                    f0=10,
                    df=1,
                    frequencies_amplitudes=numpy.array(
                        [5, expected_single_tone_amplitude, 3, 2, 1]
                    ),
                    spectrum_amplitude_type=expected_amplitude_type,
                    spectrum_amplitude_unit_is_db=False,
                    frequencies_phases=numpy.array(
                        [180, expected_single_tone_phase_degrees, 45, 22.5, 0]
                    ),
                    spectrum_phase_unit=expected_phase_unit,
                ),
            )
        )

        logging.debug(
            "%s = %s",
            nameof(multiple_tones_amplitude_phase_spectrum),
            repr(multiple_tones_amplitude_phase_spectrum),
        )

        # Assert
        self.assertIsNotNone(multiple_tones_amplitude_phase_spectrum.multiple_tones_result)
        self.assertIsNotNone(multiple_tones_amplitude_phase_spectrum.amplitude_phase_spectrum)

        self.assertEqual(
            1,
            len(multiple_tones_amplitude_phase_spectrum.multiple_tones_result.detected_tones),
        )

        self.assertEqual(
            expected_single_tone_amplitude,
            multiple_tones_amplitude_phase_spectrum.multiple_tones_result.detected_tones[
                0
            ].amplitude,
        )

        self.assertEqual(
            expected_single_tone_frequency,
            multiple_tones_amplitude_phase_spectrum.multiple_tones_result.detected_tones[
                0
            ].frequency,
        )

        self.assertEqual(
            expected_single_tone_phase_degrees,
            multiple_tones_amplitude_phase_spectrum.multiple_tones_result.detected_tones[
                0
            ].phase_degrees,
        )


# LabVIEW VIs tests


class TestLabViewFrequencyDomainProcessing(unittest.TestCase):
    """Provides unit tests of `FrequencyDomainProcessing` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # activate debug traces of native dll
        analysis_library_info.enable_traces(True)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestLabViewFrequencyDomainProcessing),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_square_waveform(
        self,
    ):
        """Test of `LabViewFrequencyDomainProcessing`
        `process_single_waveform_multiple_tones_and_amplitude_phase_spectrum`
        method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (333 > 100 characters) (auto-generated noqa)
        # Arrange
        waveform_sampling_rate = 44100
        waveform_sampling_period = 1 / waveform_sampling_rate
        waveform_duration_seconds = 0.1
        waveform_samples_count = (int)(waveform_duration_seconds * waveform_sampling_rate)
        waveform_amplitude = 1
        waveform_frequency = 440

        spectrum_view_settings_amplitude_is_db = False
        spectrum_view_settings_phase_unit = SpectrumPhaseUnit.DEGREE
        spectrum_view_settings_amplitude_type = SpectrumAmplitudeType.RMS

        wanted_tones_selection_threshold = 0.15

        expected_spectrum_size = 2205
        expected_tones_count_above_threshold = 4

        square_waveform_samples = square_waveform.create_square_waveform(
            amplitude=waveform_amplitude,
            frequency=waveform_frequency,
            duty_cycle=0.5,
            phase=0,
            offset=0,
            samples_count=waveform_samples_count,
            sampling_rate=waveform_sampling_rate,
        )

        # Act
        fdvm_results = LabViewFrequencyDomainProcessing.process_single_waveform_multiple_tones_and_amplitude_phase_spectrum(
            waveform_samples=square_waveform_samples,
            waveform_sampling_period_seconds=waveform_sampling_period,
            spectrum_amplitude_must_be_db=spectrum_view_settings_amplitude_is_db,
            spectrum_phase_unit=spectrum_view_settings_phase_unit,
            fft_spectrum_window=LabViewFftSpectrumWindow.HANNING,
            tones_sorting_mode=LabViewTonesSortingMode.DECREASING_AMPLITUDES,
            tones_selection_threshold_peak_amplitude=wanted_tones_selection_threshold,
        )

        square_waveform_magnitude_phase_spectrum = fdvm_results.amplitude_phase_spectrum
        square_waveform_multiple_tones = fdvm_results.multiple_tones_result

        csv_file_ouput_path = os.path.join(
            TestLabViewFrequencyDomainProcessing.tests_output_folder_path,
            "test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_square_waveform.csv",
        )

        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=square_waveform_magnitude_phase_spectrum.spectrum_frequencies,
            column2_data=square_waveform_magnitude_phase_spectrum.spectrum_amplitudes,
            column1_name="Frequency (Hz)",
            column2_name="RMS Amplitude",
        )

        logging.debug(
            "%s count = %s",
            nameof(square_waveform_magnitude_phase_spectrum.spectrum_amplitudes),
            len(square_waveform_magnitude_phase_spectrum.spectrum_amplitudes),
        )

        logging.debug(
            "%s count = %s",
            nameof(square_waveform_multiple_tones.detected_tones),
            len(square_waveform_multiple_tones.detected_tones),
        )

        logging.debug(
            "%s repr = %s",
            nameof(square_waveform_multiple_tones.detected_tones),
            repr(square_waveform_multiple_tones.detected_tones),
        )

        # Assert
        self.assertIsNotNone(square_waveform_magnitude_phase_spectrum)
        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_frequencies.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitudes.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_phases.size,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_is_db,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_unit_is_db,
        )

        self.assertEqual(
            spectrum_view_settings_phase_unit,
            square_waveform_magnitude_phase_spectrum.spectrum_phase_unit,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_type,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_type,
        )

        self.assertEqual(
            expected_tones_count_above_threshold,
            len(square_waveform_multiple_tones.detected_tones),
        )

        for detected_tone in square_waveform_multiple_tones.detected_tones:
            self.assertGreaterEqual(detected_tone.amplitude, wanted_tones_selection_threshold)

    def test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_modulated_waveform_amplitude_is_db(
        self,
    ):
        """Test of `LabViewFrequencyDomainProcessing`
        `process_single_waveform_multiple_tones_and_amplitude_phase_spectrum` method when there is no error
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (107 > 100 characters) (auto-generated noqa)
        # Arrange
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        emv_csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "EMV_Waveform_TA123.csv"
        )
        logging.debug("%s = %s", nameof(emv_csv_file_path), emv_csv_file_path)

        (_, column_2_array) = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=emv_csv_file_path, header_is_present=False
        )

        wanted_tones_selection_threshold = 0.02

        # Act
        fdvm_results = LabViewFrequencyDomainProcessing.process_single_waveform_multiple_tones_and_amplitude_phase_spectrum(
            waveform_samples=column_2_array,
            waveform_sampling_period_seconds=1 / 150_000_000,
            spectrum_amplitude_must_be_db=True,
            spectrum_phase_unit=SpectrumPhaseUnit.DEGREE,
            fft_spectrum_window=LabViewFftSpectrumWindow.HANNING,
            tones_sorting_mode=LabViewTonesSortingMode.DECREASING_AMPLITUDES,
            tones_selection_threshold_peak_amplitude=wanted_tones_selection_threshold,
        )

        waveform_magnitude_phase_spectrum = fdvm_results.amplitude_phase_spectrum
        waveform_multiple_tones = fdvm_results.multiple_tones_result

        logging.debug(
            "%s count = %s",
            nameof(waveform_magnitude_phase_spectrum.spectrum_amplitudes),
            len(waveform_magnitude_phase_spectrum.spectrum_amplitudes),
        )

        logging.debug(
            "%s count = %s",
            nameof(waveform_multiple_tones.detected_tones),
            len(waveform_multiple_tones.detected_tones),
        )

        logging.debug(
            "%s repr = %s",
            nameof(waveform_multiple_tones.detected_tones),
            repr(waveform_multiple_tones.detected_tones),
        )

        csv_file_ouput_path = os.path.join(
            TestLabViewFrequencyDomainProcessing.tests_output_folder_path,
            "test_process_single_waveform_multiple_tones_and_amplitude_phase_spectrum_modulated_waveform_amplitude_is_db.csv",
        )

        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=waveform_magnitude_phase_spectrum.spectrum_frequencies,
            column2_data=waveform_magnitude_phase_spectrum.spectrum_amplitudes,
            column1_name="Frequency (Hz)",
            column2_name="RMS Amplitude",
        )

        for detected_tone in waveform_multiple_tones.detected_tones:
            self.assertGreaterEqual(detected_tone.amplitude, wanted_tones_selection_threshold)


class TestLabViewFftSpectrumAmplitudePhase(unittest.TestCase):
    """Provides unit tests of `LabViewFftSpectrumAmplitudePhase` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # activate debug traces of native dll
        analysis_library_info.enable_traces(True)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestLabViewFftSpectrumAmplitudePhase),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of `LabViewFftSpectrumAmplitudePhase`
        get_last_error_message method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (356 > 100 characters) (auto-generated noqa)
        error_message = LabViewFftSpectrumAmplitudePhase.get_last_error_message()
        self.assertEqual("", error_message)

    @parameterized.expand(
        [
            ("PEAK_AMPLITUDE", SpectrumAmplitudeType.PEAK),
            ("RMS_AMPLITUDE", SpectrumAmplitudeType.RMS),
        ]
    )
    def test_process_single_waveform_magnitude_phase_spectrum_single_tone_waveform(
        self, case_name: str, amplitude_type: SpectrumAmplitudeType
    ):
        """Test of `LabViewFftSpectrumAmplitudePhase`
        `process_single_waveform_amplitude_phase_spectrum` method when there is no error
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        waveform_sampling_rate = 44100
        waveform_sampling_period = 1 / waveform_sampling_rate
        waveform_duration_seconds = 0.1
        waveform_samples_count = (int)(waveform_duration_seconds * waveform_sampling_rate)
        waveform_amplitude = 1
        waveform_frequency = 440

        spectrum_view_settings_amplitude_is_db = False
        spectrum_view_settings_phase_unit = SpectrumPhaseUnit.DEGREE
        spectrum_view_settings_amplitude_type = amplitude_type

        expected_spectrum_size = 2205

        square_waveform_samples = sine_waveform.create_sine_waveform(
            amplitude=waveform_amplitude,
            frequency=waveform_frequency,
            phase=math.radians(45),
            offset=0,
            samples_count=waveform_samples_count,
            sampling_rate=waveform_sampling_rate,
        )

        # Act
        square_waveform_magnitude_phase_spectrum = (
            LabViewFftSpectrumAmplitudePhase.process_single_waveform_amplitude_phase_spectrum(
                waveform_samples=square_waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                spectrum_amplitude_must_be_db=spectrum_view_settings_amplitude_is_db,
                spectrum_amplitude_type=spectrum_view_settings_amplitude_type,
                spectrum_phase_unit=spectrum_view_settings_phase_unit,
                fft_spectrum_window=LabViewFftSpectrumWindow.HANNING,
            )
        )

        csv_file_ouput_path = os.path.join(
            TestLabViewFftSpectrumAmplitudePhase.tests_output_folder_path,
            f"test_process_single_waveform_magnitude_phase_spectrum_single_tone_waveform_{str(amplitude_type)}.csv",
        )

        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=square_waveform_magnitude_phase_spectrum.spectrum_frequencies,
            column2_data=square_waveform_magnitude_phase_spectrum.spectrum_amplitudes,
            column1_name="Frequency (Hz)",
            column2_name=f"{str(amplitude_type)} Amplitude",
        )

        # Assert
        self.assertIsNotNone(square_waveform_magnitude_phase_spectrum)
        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_frequencies.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitudes.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_phases.size,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_is_db,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_unit_is_db,
        )

        self.assertEqual(
            spectrum_view_settings_phase_unit,
            square_waveform_magnitude_phase_spectrum.spectrum_phase_unit,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_type,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_type,
        )

        # Assert amplitudes
        max_amplitude = square_waveform_magnitude_phase_spectrum.spectrum_amplitudes.max()

        if spectrum_view_settings_amplitude_type == SpectrumAmplitudeType.PEAK:
            self.assertAlmostEqual(1, max_amplitude, delta=0.001)

        if spectrum_view_settings_amplitude_type == SpectrumAmplitudeType.RMS:
            self.assertAlmostEqual(0.707, max_amplitude, delta=0.001)

    @parameterized.expand(
        [
            ("PEAK_AMPLITUDE", SpectrumAmplitudeType.PEAK),
            ("RMS_AMPLITUDE", SpectrumAmplitudeType.RMS),
        ]
    )
    def test_process_single_waveform_magnitude_phase_spectrum_square_waveform(
        self, case_name: str, amplitude_type: SpectrumAmplitudeType
    ):
        """Test of `LabViewFftSpectrumAmplitudePhase`
        `process_single_waveform_amplitude_phase_spectrum` method when there is no error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        logging.debug("%s = %s", nameof(case_name), case_name)

        # Arrange
        waveform_sampling_rate = 44100
        waveform_sampling_period = 1 / waveform_sampling_rate
        waveform_duration_seconds = 0.1
        waveform_samples_count = (int)(waveform_duration_seconds * waveform_sampling_rate)
        waveform_amplitude = 1
        waveform_frequency = 440

        spectrum_view_settings_amplitude_is_db = False
        spectrum_view_settings_phase_unit = SpectrumPhaseUnit.DEGREE
        spectrum_view_settings_amplitude_type = amplitude_type

        expected_spectrum_size = 2205

        square_waveform_samples = square_waveform.create_square_waveform(
            amplitude=waveform_amplitude,
            frequency=waveform_frequency,
            duty_cycle=0.5,
            phase=0,
            offset=0,
            samples_count=waveform_samples_count,
            sampling_rate=waveform_sampling_rate,
        )

        # Act
        square_waveform_magnitude_phase_spectrum = (
            LabViewFftSpectrumAmplitudePhase.process_single_waveform_amplitude_phase_spectrum(
                waveform_samples=square_waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                spectrum_amplitude_must_be_db=spectrum_view_settings_amplitude_is_db,
                spectrum_amplitude_type=spectrum_view_settings_amplitude_type,
                spectrum_phase_unit=spectrum_view_settings_phase_unit,
                fft_spectrum_window=LabViewFftSpectrumWindow.HANNING,
            )
        )

        csv_file_ouput_path = os.path.join(
            TestLabViewFftSpectrumAmplitudePhase.tests_output_folder_path,
            f"test_process_single_waveform_magnitude_phase_spectrum_square_waveform_{str(amplitude_type)}.csv",
        )

        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=square_waveform_magnitude_phase_spectrum.spectrum_frequencies,
            column2_data=square_waveform_magnitude_phase_spectrum.spectrum_amplitudes,
            column1_name="Frequency (Hz)",
            column2_name=f"{str(amplitude_type)} Amplitude",
        )

        spectrum_peaks = scipy.signal.find_peaks(
            x=square_waveform_magnitude_phase_spectrum.spectrum_amplitudes,
        )

        logging.debug(
            "%s count = %s",
            nameof(square_waveform_magnitude_phase_spectrum.spectrum_amplitudes),
            len(square_waveform_magnitude_phase_spectrum.spectrum_amplitudes),
        )
        logging.debug("%s count = %s", nameof(spectrum_peaks), len(spectrum_peaks[0]))
        logging.debug("%s indexes = %s", nameof(spectrum_peaks), spectrum_peaks[0])

        # Assert
        self.assertIsNotNone(square_waveform_magnitude_phase_spectrum)
        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_frequencies.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitudes.size,
        )

        self.assertEqual(
            expected_spectrum_size,
            square_waveform_magnitude_phase_spectrum.spectrum_phases.size,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_is_db,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_unit_is_db,
        )

        self.assertEqual(
            spectrum_view_settings_phase_unit,
            square_waveform_magnitude_phase_spectrum.spectrum_phase_unit,
        )

        self.assertEqual(
            spectrum_view_settings_amplitude_type,
            square_waveform_magnitude_phase_spectrum.spectrum_amplitude_type,
        )


class TestLabViewMultipleTonesMeasurement(unittest.TestCase):
    """Provides unit tests of `LabViewMultipleTonesMeasurement` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # activate debug traces of native dll
        analysis_library_info.enable_traces(True)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestLabViewMultipleTonesMeasurement),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of `LabViewMultipleTonesMeasurement`
        get_last_error_message method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (356 > 100 characters) (auto-generated noqa)
        error_message = LabViewMultipleTonesMeasurement.get_last_error_message()
        self.assertEqual("", error_message)

    @functional_utilities.repeat(10)
    def test_process_single_waveform_multiple_tones_square_waveform(self):
        """Test of `LabViewMultipleTonesMeasurement`
        process_single_waveform_multiple_tones method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (372 > 100 characters) (auto-generated noqa)
        # Arrange
        waveform_sampling_rate = 44100
        waveform_sampling_period = 1 / waveform_sampling_rate
        waveform_duration_seconds = 0.1
        waveform_samples_count = (int)(waveform_duration_seconds * waveform_sampling_rate)
        waveform_amplitude = 1
        waveform_frequency = 440
        max_tones_count = 10
        tones_selection_threshold = 0.1
        expected_tones_count_above_threshold = 6
        comparison_tolerance_percent = 0.1

        square_waveform_samples = square_waveform.create_square_waveform(
            amplitude=waveform_amplitude,
            frequency=waveform_frequency,
            duty_cycle=0.5,
            phase=0,
            offset=0,
            samples_count=waveform_samples_count,
            sampling_rate=waveform_sampling_rate,
        )

        # Act
        square_waveform_tones = (
            LabViewMultipleTonesMeasurement.process_single_waveform_multiple_tones(
                waveform_samples=square_waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                tones_selection_threshold=tones_selection_threshold,
                tones_max_count=max_tones_count,
                tones_sorting_mode=LabViewTonesSortingMode.DECREASING_AMPLITUDES,
            )
        )

        logging.debug("%s = %s", nameof(square_waveform_tones), repr(square_waveform_tones))

        # Assert
        self.assertEqual(SpectrumAmplitudeType.PEAK, square_waveform_tones.amplitude_type)
        self.assertEqual(
            expected_tones_count_above_threshold,
            len(square_waveform_tones.detected_tones),
        )

        for waveform_tone, waveform_tone_index in zip(
            square_waveform_tones.detected_tones,
            range(0, len(square_waveform_tones.detected_tones)),
        ):
            self.assertGreaterEqual(a=waveform_tone.amplitude, b=tones_selection_threshold)

            k = waveform_tone_index
            expected_tone_frequency = (2 * k + 1) * waveform_frequency

            self.assertAlmostEqual(
                first=expected_tone_frequency,
                second=waveform_tone.frequency,
                delta=numeric_utilities.percent_of(
                    percent=comparison_tolerance_percent, value=expected_tone_frequency
                ),
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repeat", dest="repeat", help="repeat tests")
    (args, unitargs) = parser.parse_known_args()
    unitargs.insert(0, "placeholder")  # unittest ignores first arg

    # add more arguments to unitargs here
    repeat_count = int(vars(args)["repeat"] or 2)
    for iteration in range(repeat_count):
        was_successful = unittest.main(exit=False, argv=unitargs).result.wasSuccessful()
        if not was_successful:
            sys.exit(1)
