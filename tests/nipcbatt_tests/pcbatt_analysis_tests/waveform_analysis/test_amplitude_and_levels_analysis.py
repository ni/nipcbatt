"""Defines unit tests related to nipcbatt.pcbatt_analysis.amplitude_and_levels_analysis module."""

import argparse
import logging
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
from scipy import signal
from varname import nameof

from nipcbatt.pcbatt_analysis import analysis_library_info
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
    AmplitudeAndLevelsProcessingResult,
    LabViewAmplitudeAndLevels,
)
from nipcbatt.pcbatt_utilities import (
    csv_utilities,
    functional_utilities,
    numeric_utilities,
)


# Output result tests
class TestAmplitudeAndLevelsProcessingResult(unittest.TestCase):
    """Defines a test fixture that checks class AmplitudeAndLevelsProcessingResult of module
    `pcbatt_analysis.amplitude_and_levels_analysis`.

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

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    def test_amplitude_and_levels_processing_result(self):
        """Test of pcbatt_analysis.amplitude_and_levels_analysis.AmplitudeAndLevelsProcessingResult
        class constructor"""

        # Arrange + Act
        amplitude_and_levels_results_1 = AmplitudeAndLevelsProcessingResult(0, 0, 0)
        amplitude_and_levels_results_2 = AmplitudeAndLevelsProcessingResult(1, 1, -1)

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_results_1),
            str(amplitude_and_levels_results_1),
        )
        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_results_2),
            str(amplitude_and_levels_results_2),
        )

        logging.debug(
            "repr(%s) = %s",
            nameof(amplitude_and_levels_results_1),
            repr(amplitude_and_levels_results_1),
        )
        logging.debug(
            "repr(%s) = %s",
            nameof(amplitude_and_levels_results_2),
            repr(amplitude_and_levels_results_2),
        )

        # Assert results 1
        self.assertIsNotNone(amplitude_and_levels_results_1)
        self.assertEqual(0, amplitude_and_levels_results_1.amplitude)
        self.assertEqual(0, amplitude_and_levels_results_1.high_state_level)
        self.assertEqual(0, amplitude_and_levels_results_1.low_state_level)

        # Assert results 2
        self.assertIsNotNone(amplitude_and_levels_results_2)
        self.assertEqual(1, amplitude_and_levels_results_2.amplitude)
        self.assertEqual(1, amplitude_and_levels_results_2.high_state_level)
        self.assertEqual(-1, amplitude_and_levels_results_2.low_state_level)


# LabVIEW VI tests
class TestLabViewAmplitudeAndLevels(unittest.TestCase):
    """Provides unit tests of LabViewAmplitudeAndLevels class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    def setUp(self):
        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    def tearDown(self):
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of pcbatt_analysis.amplitude_and_levels_analysis.LabViewAmplitudeAndLevels
        get_last_error_message method when there is no error"""
        last_error_message = LabViewAmplitudeAndLevels.get_last_error_message()
        self.assertEqual("", last_error_message)

    @functional_utilities.repeat(2)
    def test_process_single_waveform_amplitude_and_levels_auto_select_method_emv_trace(
        self,
    ):
        """Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using auto select analysis strategy
        using emv 106 Khz waveform.
        """
        # Arrange
        expected_amplitude = 0.474
        expected_high_state = 0.476000212085181
        expected_low_state = 0.0018392165666242
        tolerance_percent = 0.1
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        emv_csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "EMV_Waveform_TA121.csv"
        )
        logging.debug("%s = %s", nameof(emv_csv_file_path), emv_csv_file_path)

        # Act
        (column_1_array, column_2_array) = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=emv_csv_file_path, header_is_present=False
        )
        logging.debug(
            "%s[%s] = %s",
            nameof(column_1_array),
            "Time (s)",
            column_1_array,
        )

        logging.debug(
            "%s[%s] = %s",
            nameof(column_2_array),
            "Ampltiude (V)",
            column_2_array,
        )
        # Act
        amplitude_and_levels_result = LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
            waveform_samples=column_2_array,
            waveform_sampling_period_seconds=150_000_000,
            amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
            histogram_size=512,
        )

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_result),
            repr(amplitude_and_levels_result),
        )

        # Assert
        self.assertAlmostEqual(
            first=expected_amplitude,
            second=amplitude_and_levels_result.amplitude,
            delta=numeric_utilities.percent_of(tolerance_percent, expected_amplitude),
        )
        self.assertAlmostEqual(
            first=expected_high_state,
            second=amplitude_and_levels_result.high_state_level,
            delta=numeric_utilities.percent_of(tolerance_percent, expected_high_state),
        )
        self.assertAlmostEqual(
            first=expected_low_state,
            second=amplitude_and_levels_result.low_state_level,
            delta=numeric_utilities.percent_of(tolerance_percent, expected_low_state),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_amplitude_and_levels_auto_select_method(self):
        """Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using auto select analysis strategy.
        """
        # Arrange
        t = numpy.linspace(0, 1, 500, endpoint=False)
        y = signal.square(2 * numpy.pi * 5 * t)

        logging.debug("%s = %s", nameof(t), t)
        logging.debug("%s = %s", nameof(y), y)

        # Act
        amplitude_and_levels_result = LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
            waveform_samples=y,
            waveform_sampling_period_seconds=1,
            amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
            histogram_size=256,
        )

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_result),
            repr(amplitude_and_levels_result),
        )

        # Assert
        self.assertAlmostEqual(
            2,
            amplitude_and_levels_result.amplitude,
            delta=numeric_utilities.percent_of(0.8, 2),
        )
        self.assertAlmostEqual(
            1,
            amplitude_and_levels_result.high_state_level,
            delta=numeric_utilities.percent_of(0.8, 1),
        )
        self.assertAlmostEqual(
            -1,
            amplitude_and_levels_result.low_state_level,
            delta=numeric_utilities.percent_of(0.8, 1),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_amplitude_and_levels_histogram_method(self):
        """Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using histogram analysis strategy.
        """
        # Arrange
        t = numpy.linspace(0, 1, 500, endpoint=False)
        y = signal.square(2 * numpy.pi * 5 * t)

        logging.debug("%s = %s", nameof(t), t)
        logging.debug("%s = %s", nameof(y), y)

        # Act
        amplitude_and_levels_result = (
            LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
                waveform_samples=y,
                waveform_sampling_period_seconds=1,
                amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.HISTOGRAM,
                histogram_size=1024,
            )
        )

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_result),
            repr(amplitude_and_levels_result),
        )

        # Assert
        self.assertAlmostEqual(
            2,
            amplitude_and_levels_result.amplitude,
            delta=numeric_utilities.percent_of(0.1, 2),
        )

        self.assertAlmostEqual(
            1,
            amplitude_and_levels_result.high_state_level,
            delta=numeric_utilities.percent_of(0.1, 1),
        )

        self.assertAlmostEqual(
            -1,
            amplitude_and_levels_result.low_state_level,
            delta=numeric_utilities.percent_of(0.1, 1),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_amplitude_and_levels_peak_method(self):
        """Test of pcbatt_analysis.amplitude_and_levels.LabViewAmplitudeAndLevels
        process_single_waveform_amplitude_and_levels method using peak analysis strategy.
        """
        # Arrange
        t = numpy.linspace(0, 1, 500, endpoint=False)
        y = signal.sawtooth(2 * numpy.pi * 5 * t, 0.5)

        logging.debug("%s = %s", nameof(t), t)
        logging.debug("%s = %s", nameof(y), y)

        # Act
        amplitude_and_levels_result = (
            LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
                waveform_samples=y,
                waveform_sampling_period_seconds=1,
                amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.PEAK,
                histogram_size=1024,
            )
        )

        logging.debug(
            "%s = %s",
            nameof(amplitude_and_levels_result),
            repr(amplitude_and_levels_result),
        )

        # Assert
        self.assertEqual(
            2,
            amplitude_and_levels_result.amplitude,
        )

        self.assertEqual(
            1,
            amplitude_and_levels_result.high_state_level,
        )

        self.assertEqual(
            -1,
            amplitude_and_levels_result.low_state_level,
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
