"""Defines unit tests related to nipcbatt.pcbatt_analysis.pulse_analog_analysis module."""

import argparse
import importlib.metadata
import logging
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
import scipy
from varname import nameof

from nipcbatt.pcbatt_analysis import analysis_library_info
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.pulse_analog_analysis import (
    LabViewPulseAnalogMeasurements,
    PulseAnalogMeasurementPercentLevelsSettings,
    PulseAnalogProcessingExportMode,
    PulseAnalogProcessingPolarity,
    PulseAnalogProcessingReferenceLevels,
    PulseAnalogProcessingReferenceLevelsUnit,
    PulseAnalogProcessingResult,
    WaveformPeriodicityAnalogProcessingResult,
)
from nipcbatt.pcbatt_utilities import (
    csv_utilities,
    functional_utilities,
    numeric_utilities,
)

# Output result tests


class TestPulseAnalogProcessingReferenceLevels(unittest.TestCase):
    """Defines a test fixture that checks class `PulseAnalogProcessingReferenceLevels` of module
    `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

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

    def test_pulse_analog_processing_reference_levels(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.PulseAnalogProcessingReferenceLevels`
        class constructor"""

        # Arrange
        expected_reference_level_high = 5
        expected_reference_level_middle = 4.5
        expected_reference_level_low = 1

        # Act
        pulse_analog_processing_reference_levels = PulseAnalogProcessingReferenceLevels(
            reference_level_high=expected_reference_level_high,
            reference_level_middle=expected_reference_level_middle,
            reference_level_low=expected_reference_level_low,
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_reference_levels),
            repr(pulse_analog_processing_reference_levels),
        )

        # Assert result
        self.assertIsNotNone(pulse_analog_processing_reference_levels)
        self.assertEqual(
            first=expected_reference_level_high,
            second=pulse_analog_processing_reference_levels.reference_level_high,
        )
        self.assertEqual(
            first=expected_reference_level_middle,
            second=pulse_analog_processing_reference_levels.reference_level_middle,
        )
        self.assertEqual(
            first=expected_reference_level_low,
            second=pulse_analog_processing_reference_levels.reference_level_low,
        )


class TestWaveformPeriodicityAnalogProcessingResult(unittest.TestCase):
    """Defines a test fixture that checks class `PulsePeriodicityAnalogProcessingResult` of module
    `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

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

    def test_waveform_periodicity_analog_processing_result(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.WaveformPeriodicityAnalogProcessingResult`
        class constructor"""

        # Arrange + Act
        pulse_periodicty_results = WaveformPeriodicityAnalogProcessingResult(
            period=1, duty_cycle=0.5
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_periodicty_results),
            repr(pulse_periodicty_results),
        )

        # Assert result
        self.assertIsNotNone(pulse_periodicty_results)
        self.assertEqual(first=1, second=pulse_periodicty_results.period)
        self.assertEqual(first=1, second=pulse_periodicty_results.frequency)
        self.assertEqual(first=0.5, second=pulse_periodicty_results.duty_cycle)
        self.assertEqual(first=50, second=pulse_periodicty_results.duty_cycle_percent)

    def test_waveform_periodicity_analog_processing_result_invalid_inputs(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.WaveformPeriodicityAnalogProcessingResult`
        class constructor"""

        # Arrange + Act + Assert
        self.assertRaises(
            ValueError,
            lambda: WaveformPeriodicityAnalogProcessingResult(period=0, duty_cycle=0.5),
        )

        self.assertRaises(
            ValueError,
            lambda: WaveformPeriodicityAnalogProcessingResult(period=1, duty_cycle=-0.5),
        )

        self.assertRaises(
            ValueError,
            lambda: WaveformPeriodicityAnalogProcessingResult(period=-1, duty_cycle=0.5),
        )


class TestPulseAnalogMeasurementPercentLevelsSettings(unittest.TestCase):
    """Defines a test fixture that checks class
        `PulseAnalogMeasurementPercentLevelsSettings` of module
        `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

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

    def test_pulse_analog_measurement_percent_levels_settings_invalid_inputs(self):
        """Test of
        `pcbatt_analysis.pulse_analog_analysis.PulseAnalogMeasurementPercentLevelsSettings`
        class constructor
        """
        self.assertRaises(
            ValueError,
            lambda: PulseAnalogMeasurementPercentLevelsSettings(
                AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                histogram_size=0,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogMeasurementPercentLevelsSettings(
                AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                histogram_size=-0.5,
            ),
        )

    def test_pulse_analog_measurement_percent_levels_settings(self):
        """Test of
        `pcbatt_analysis.pulse_analog_analysis.PulseAnalogMeasurementPercentLevelsSettings`
        class constructor
        """

        # Arrange
        expected_histogram_size = 256
        expected_amplitude_and_levels_processing_method_1 = (
            AmplitudeAndLevelsProcessingMethod.AUTO_SELECT
        )
        expected_amplitude_and_levels_processing_method_2 = (
            AmplitudeAndLevelsProcessingMethod.HISTOGRAM
        )
        expected_amplitude_and_levels_processing_method_3 = AmplitudeAndLevelsProcessingMethod.PEAK

        # Act
        pulse_analog_processing_settings_1 = PulseAnalogMeasurementPercentLevelsSettings(
            expected_amplitude_and_levels_processing_method_1,
            histogram_size=expected_histogram_size,
        )

        pulse_analog_processing_settings_2 = PulseAnalogMeasurementPercentLevelsSettings(
            expected_amplitude_and_levels_processing_method_2,
            histogram_size=expected_histogram_size,
        )

        pulse_analog_processing_settings_3 = PulseAnalogMeasurementPercentLevelsSettings(
            expected_amplitude_and_levels_processing_method_3,
            histogram_size=expected_histogram_size,
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_settings_1),
            repr(pulse_analog_processing_settings_1),
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_settings_2),
            repr(pulse_analog_processing_settings_2),
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_settings_3),
            repr(pulse_analog_processing_settings_3),
        )

        # Assert results
        self.assertIsNotNone(pulse_analog_processing_settings_1)
        self.assertIsNotNone(pulse_analog_processing_settings_2)
        self.assertIsNotNone(pulse_analog_processing_settings_3)

        self.assertEqual(
            first=expected_histogram_size,
            second=pulse_analog_processing_settings_1.histogram_size,
        )
        self.assertEqual(
            first=expected_histogram_size,
            second=pulse_analog_processing_settings_2.histogram_size,
        )
        self.assertEqual(
            first=expected_histogram_size,
            second=pulse_analog_processing_settings_3.histogram_size,
        )

        self.assertEqual(
            first=expected_amplitude_and_levels_processing_method_1,
            second=pulse_analog_processing_settings_1.amplitude_and_levels_processing_method,
        )

        self.assertEqual(
            first=expected_amplitude_and_levels_processing_method_2,
            second=pulse_analog_processing_settings_2.amplitude_and_levels_processing_method,
        )

        self.assertEqual(
            first=expected_amplitude_and_levels_processing_method_3,
            second=pulse_analog_processing_settings_3.amplitude_and_levels_processing_method,
        )


class TestPulseAnalogProcessingResult(unittest.TestCase):
    """Defines a test fixture that checks class PulseAnalogProcessingResult of module
    `pcbatt_analysis.waveform_analysis.pulse_analog_analysis`.

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

    def test_pulse_analog_processing_result(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.PulseAnalogProcessingResult`
        class constructor"""

        # Arrange
        expected_pulse_center = 125
        expected_pulse_duration = 10
        expected_pulse_reference_level_high = 90
        expected_pulse_reference_level_middle = 50
        expected_pulse_reference_level_low = 10
        expected_period = 2
        expected_frequency = 0.5
        expected_duty_cycle = 0.5
        expected_duty_cycle_percent = 50

        # Act
        pulse_analog_processing_results_1 = PulseAnalogProcessingResult(
            pulse_center=expected_pulse_center,
            pulse_duration=expected_pulse_duration,
            pulse_reference_level_high=expected_pulse_reference_level_high,
            pulse_reference_level_middle=expected_pulse_reference_level_middle,
            pulse_reference_level_low=expected_pulse_reference_level_low,
        )

        pulse_analog_processing_results_2 = PulseAnalogProcessingResult(
            pulse_center=expected_pulse_center,
            pulse_duration=expected_pulse_duration,
            pulse_reference_level_high=expected_pulse_reference_level_high,
            pulse_reference_level_middle=expected_pulse_reference_level_middle,
            pulse_reference_level_low=expected_pulse_reference_level_low,
            period=expected_period,
            duty_cycle=expected_duty_cycle,
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_results_1),
            repr(pulse_analog_processing_results_1),
        )

        logging.debug(
            "%s = %s",
            nameof(pulse_analog_processing_results_2),
            repr(pulse_analog_processing_results_2),
        )

        # Assert results 1
        self.assertIsNotNone(pulse_analog_processing_results_1)
        self.assertEqual(
            first=expected_pulse_center,
            second=pulse_analog_processing_results_1.pulse_center,
        )

        self.assertEqual(
            first=expected_pulse_duration,
            second=pulse_analog_processing_results_1.pulse_duration,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_high,
            second=pulse_analog_processing_results_1.pulse_reference_level_high,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_middle,
            second=pulse_analog_processing_results_1.pulse_reference_level_middle,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_low,
            second=pulse_analog_processing_results_1.pulse_reference_level_low,
        )

        self.assertIsNone(pulse_analog_processing_results_1.waveform_periodicity_processing_result)

        # Assert results 2
        self.assertIsNotNone(pulse_analog_processing_results_2)

        self.assertEqual(
            first=expected_pulse_center,
            second=pulse_analog_processing_results_2.pulse_center,
        )

        self.assertEqual(
            first=expected_pulse_duration,
            second=pulse_analog_processing_results_2.pulse_duration,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_high,
            second=pulse_analog_processing_results_2.pulse_reference_level_high,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_middle,
            second=pulse_analog_processing_results_2.pulse_reference_level_middle,
        )

        self.assertEqual(
            first=expected_pulse_reference_level_low,
            second=pulse_analog_processing_results_2.pulse_reference_level_low,
        )

        self.assertIsNotNone(
            pulse_analog_processing_results_2.waveform_periodicity_processing_result
        )

        self.assertEqual(
            first=expected_duty_cycle,
            second=pulse_analog_processing_results_2.waveform_periodicity_processing_result.duty_cycle,
        )

        self.assertEqual(
            first=expected_duty_cycle_percent,
            second=pulse_analog_processing_results_2.waveform_periodicity_processing_result.duty_cycle_percent,
        )

        self.assertEqual(
            first=expected_period,
            second=pulse_analog_processing_results_2.waveform_periodicity_processing_result.period,
        )

        self.assertEqual(
            first=expected_frequency,
            second=pulse_analog_processing_results_2.waveform_periodicity_processing_result.frequency,
        )

    def test_pulse_analog_processing_result_invalid_inputs(self):
        """Test of `pcbatt_analysis.pulse_analog_analysis.PulseAnalogProcessingResult`
        class constructor"""

        # Arrange + Act
        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=0,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=0,
                duty_cycle=1,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=0,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=1,
                duty_cycle=-0.4,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=0,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=-1,
                duty_cycle=1,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=-1,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=1,
                duty_cycle=1,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: PulseAnalogProcessingResult(
                pulse_center=-1,
                pulse_duration=0,
                pulse_reference_level_high=0,
                pulse_reference_level_middle=0,
                pulse_reference_level_low=0,
                period=1,
                duty_cycle=-0.5,
            ),
        )


# LabVIEW VI tests
class TestLabViewPulseAnalogMeasurements(unittest.TestCase):
    """Provides unit tests of
    `pcbatt_analysis.pulse_analog_analysis.LabViewPulseAnalogMeasurements` class.

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

        used_numpy_version = importlib.metadata.version(nameof(numpy))
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)

        used_scipy_version = importlib.metadata.version(nameof(scipy))
        logging.debug("%s = %s", nameof(used_scipy_version), used_scipy_version)

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of ``pcbatt_analysis.pulse_analog_analysis.LabViewPulseAnalogMeasurements
        get_last_error_message`` method when there is no error"""
        last_error_message = LabViewPulseAnalogMeasurements.get_last_error_message()
        self.assertEqual("", last_error_message)

    @functional_utilities.repeat(2)
    def test_process_single_waveform_multiple_pulse_measurements_export_all_relative_percent_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_multiple_pulse_measurements` method.
        """
        # Arrange
        tolerance_percent = 1
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            multiple_pulse_measurements_result = LabViewPulseAnalogMeasurements.process_single_waveform_multiple_pulse_measurements(
                waveform_samples=waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                waveform_t0=waveform_t0,
                export_mode=PulseAnalogProcessingExportMode.ALL,
                processing_polarity=processing_polarity,
                reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT,
                reference_levels=PulseAnalogProcessingReferenceLevels(
                    reference_level_high=95,
                    reference_level_middle=50,
                    reference_level_low=5,
                ),
                percent_levels_settings=PulseAnalogMeasurementPercentLevelsSettings(
                    amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                    histogram_size=512,
                ),
            )

            self.assertIsNotNone(multiple_pulse_measurements_result)

            for pulse_measurement_result in multiple_pulse_measurements_result:
                logging.debug(
                    "%s = %s",
                    nameof(pulse_measurement_result),
                    repr(pulse_measurement_result),
                )

                self.assertIsNotNone(
                    pulse_measurement_result.waveform_periodicity_processing_result
                )

                self.assertAlmostEqual(
                    first=expected_pulse_duration,
                    second=pulse_measurement_result.pulse_duration,
                    delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
                )

                self.assertLess(a=0, b=pulse_measurement_result.pulse_center)

                self.assertAlmostEqual(
                    first=1.0,
                    second=pulse_measurement_result.waveform_periodicity_processing_result.period,
                    delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
                )

                self.assertAlmostEqual(
                    first=1.0,
                    second=pulse_measurement_result.waveform_periodicity_processing_result.frequency,
                    delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
                )

                self.assertAlmostEqual(
                    first=0.5,
                    second=pulse_measurement_result.waveform_periodicity_processing_result.duty_cycle,
                    delta=numeric_utilities.percent_of(tolerance_percent, 0.5),
                )

    @functional_utilities.repeat(2)
    def test_process_single_waveform_pulse_measurements_export_all_relative_percent_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        """
        # Arrange
        tolerance_percent = 1
        expected_pulse_centers_per_polarity = {
            PulseAnalogProcessingPolarity.HIGH: 1.25,
            PulseAnalogProcessingPolarity.LOW: 0.75,
        }
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            pulse_measurements_result = LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                waveform_samples=waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                waveform_t0=waveform_t0,
                export_mode=PulseAnalogProcessingExportMode.ALL,
                processing_polarity=processing_polarity,
                pulse_number=1,
                reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT,
                reference_levels=PulseAnalogProcessingReferenceLevels(
                    reference_level_high=95,
                    reference_level_middle=50,
                    reference_level_low=5,
                ),
                percent_levels_settings=PulseAnalogMeasurementPercentLevelsSettings(
                    amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                    histogram_size=512,
                ),
            )
            logging.debug(
                "%s = %s",
                nameof(pulse_measurements_result),
                repr(pulse_measurements_result),
            )

            self.assertIsNotNone(pulse_measurements_result)
            self.assertIsNotNone(pulse_measurements_result.waveform_periodicity_processing_result)

            self.assertAlmostEqual(
                first=expected_pulse_duration,
                second=pulse_measurements_result.pulse_duration,
                delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
            )

            self.assertAlmostEqual(
                first=expected_pulse_centers_per_polarity[processing_polarity],
                second=pulse_measurements_result.pulse_center,
                delta=numeric_utilities.percent_of(
                    tolerance_percent,
                    expected_pulse_centers_per_polarity[processing_polarity],
                ),
            )

            self.assertAlmostEqual(
                first=1.0,
                second=pulse_measurements_result.waveform_periodicity_processing_result.period,
                delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
            )

            self.assertAlmostEqual(
                first=1.0,
                second=pulse_measurements_result.waveform_periodicity_processing_result.frequency,
                delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
            )

            self.assertAlmostEqual(
                first=0.5,
                second=pulse_measurements_result.waveform_periodicity_processing_result.duty_cycle,
                delta=numeric_utilities.percent_of(tolerance_percent, 0.5),
            )

    @functional_utilities.repeat(2)
    def test_process_single_waveform_pulse_measurements_ignore_periodicity_analysis_relative_percent_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        """
        # Arrange
        tolerance_percent = 1
        expected_pulse_centers_per_polarity = {
            PulseAnalogProcessingPolarity.HIGH: 1.25,
            PulseAnalogProcessingPolarity.LOW: 0.75,
        }
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            pulse_measurements_result = LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                waveform_samples=waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                waveform_t0=waveform_t0,
                export_mode=PulseAnalogProcessingExportMode.IGNORE_WAVEFORM_PERIODICITY_ANALYSIS,
                processing_polarity=processing_polarity,
                pulse_number=1,
                reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT,
                reference_levels=PulseAnalogProcessingReferenceLevels(
                    reference_level_high=95,
                    reference_level_middle=50,
                    reference_level_low=5,
                ),
                percent_levels_settings=PulseAnalogMeasurementPercentLevelsSettings(
                    amplitude_and_levels_processing_method=AmplitudeAndLevelsProcessingMethod.AUTO_SELECT,
                    histogram_size=512,
                ),
            )
            logging.debug(
                "%s = %s",
                nameof(pulse_measurements_result),
                repr(pulse_measurements_result),
            )

            self.assertIsNotNone(pulse_measurements_result)
            self.assertIsNone(pulse_measurements_result.waveform_periodicity_processing_result)

            self.assertAlmostEqual(
                first=expected_pulse_duration,
                second=pulse_measurements_result.pulse_duration,
                delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
            )

            self.assertAlmostEqual(
                first=expected_pulse_centers_per_polarity[processing_polarity],
                second=pulse_measurements_result.pulse_center,
                delta=numeric_utilities.percent_of(
                    tolerance_percent,
                    expected_pulse_centers_per_polarity[processing_polarity],
                ),
            )

    @functional_utilities.repeat(2)
    def test_process_single_waveform_pulse_measurements_ignore_periodicity_analysis_absolute_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        """

        # Arrange
        tolerance_percent = 1
        expected_pulse_centers_per_polarity = {
            PulseAnalogProcessingPolarity.HIGH: 1.25,
            PulseAnalogProcessingPolarity.LOW: 0.75,
        }
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            pulse_measurements_result = LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                waveform_samples=waveform_samples,
                waveform_sampling_period_seconds=waveform_sampling_period,
                waveform_t0=waveform_t0,
                export_mode=PulseAnalogProcessingExportMode.IGNORE_WAVEFORM_PERIODICITY_ANALYSIS,
                processing_polarity=processing_polarity,
                pulse_number=1,
                reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.ABSOLUTE,
                reference_levels=PulseAnalogProcessingReferenceLevels(
                    reference_level_high=0.45,
                    reference_level_middle=0.25,
                    reference_level_low=0.05,
                ),
                percent_levels_settings=None,
            )
            logging.debug(
                "%s = %s",
                nameof(pulse_measurements_result),
                repr(pulse_measurements_result),
            )

            self.assertIsNotNone(pulse_measurements_result)
            self.assertIsNone(pulse_measurements_result.waveform_periodicity_processing_result)

            self.assertAlmostEqual(
                first=expected_pulse_duration,
                second=pulse_measurements_result.pulse_duration,
                delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
            )

            self.assertAlmostEqual(
                first=expected_pulse_centers_per_polarity[processing_polarity],
                second=pulse_measurements_result.pulse_center,
                delta=numeric_utilities.percent_of(
                    tolerance_percent,
                    expected_pulse_centers_per_polarity[processing_polarity],
                ),
            )

    @functional_utilities.repeat(2)
    def test_process_single_waveform_pulse_measurements_export_all_absolute_reference_levels(
        self,
    ):
        """Test of
        `LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements` method.
        """

        # Arrange
        tolerance_percent = 1
        expected_pulse_centers_per_polarity = {
            PulseAnalogProcessingPolarity.HIGH: 1.25,
            PulseAnalogProcessingPolarity.LOW: 0.75,
        }
        expected_pulse_duration = 0.5
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "Ideal_Square_Waveforme.csv"
        )
        logging.debug("%s = %s", nameof(csv_file_path), csv_file_path)

        waveform_2d_array = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=csv_file_path, header_is_present=False
        )

        waveform_samples = waveform_2d_array[1]
        waveform_dates = waveform_2d_array[0]

        waveform_sampling_rate = 1000
        waveform_sampling_period = numeric_utilities.invert_value(waveform_sampling_rate)
        waveform_t0 = waveform_dates[0]

        logging.debug("%s = %s", nameof(waveform_sampling_rate), waveform_sampling_rate)

        logging.debug(
            "%s = %s",
            nameof(waveform_sampling_period),
            waveform_sampling_period,
        )

        logging.debug("%s = %s", nameof(waveform_t0), waveform_t0)
        logging.debug("%s = %s", nameof(waveform_samples), waveform_samples)

        processing_polarities = [
            PulseAnalogProcessingPolarity.HIGH,
            PulseAnalogProcessingPolarity.LOW,
        ]

        for processing_polarity in processing_polarities:
            pulse_measurements_result = (
                LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                    waveform_samples=waveform_samples,
                    waveform_sampling_period_seconds=waveform_sampling_period,
                    waveform_t0=waveform_t0,
                    export_mode=PulseAnalogProcessingExportMode.ALL,
                    processing_polarity=processing_polarity,
                    pulse_number=1,
                    reference_levels_unit=PulseAnalogProcessingReferenceLevelsUnit.ABSOLUTE,
                    reference_levels=PulseAnalogProcessingReferenceLevels(
                        reference_level_high=0.45,
                        reference_level_middle=0.25,
                        reference_level_low=0.05,
                    ),
                    percent_levels_settings=None,
                )
            )
            logging.debug(
                "%s = %s",
                nameof(pulse_measurements_result),
                repr(pulse_measurements_result),
            )

            self.assertIsNotNone(pulse_measurements_result)
            self.assertIsNotNone(pulse_measurements_result.waveform_periodicity_processing_result)

            self.assertAlmostEqual(
                first=expected_pulse_duration,
                second=pulse_measurements_result.pulse_duration,
                delta=numeric_utilities.percent_of(tolerance_percent, expected_pulse_duration),
            )

            self.assertAlmostEqual(
                first=expected_pulse_centers_per_polarity[processing_polarity],
                second=pulse_measurements_result.pulse_center,
                delta=numeric_utilities.percent_of(
                    tolerance_percent,
                    expected_pulse_centers_per_polarity[processing_polarity],
                ),
            )

            self.assertAlmostEqual(
                first=1.0,
                second=pulse_measurements_result.waveform_periodicity_processing_result.period,
                delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
            )

            self.assertAlmostEqual(
                first=1.0,
                second=pulse_measurements_result.waveform_periodicity_processing_result.frequency,
                delta=numeric_utilities.percent_of(tolerance_percent, 1.0),
            )

            self.assertAlmostEqual(
                first=0.5,
                second=pulse_measurements_result.waveform_periodicity_processing_result.duty_cycle,
                delta=numeric_utilities.percent_of(tolerance_percent, 0.5),
            )

        self.assertAlmostEqual(
            first=50,
            second=pulse_measurements_result.waveform_periodicity_processing_result.duty_cycle_percent,
            delta=numeric_utilities.percent_of(tolerance_percent, 50),
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
