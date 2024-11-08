"""Defines unit tests related to nipcbatt.pcbatt_analysis.dc_rms_analysis module."""

import argparse
import logging
import platform
import sys
import unittest

import numpy
from scipy import signal
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingResult,
    DcRmsProcessingWindow,
    LabViewBasicDcRms,
)
from nipcbatt.pcbatt_utilities import functional_utilities, numeric_utilities


# Output result tests
class TestDcRmsProcessingResult(unittest.TestCase):
    """Defines a test fixture that checks class DcRmsProcessingResult of module
    `pcbatt_analysis.dc_rms_analysis`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

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

    def test_dc_rms_processing_result(self):
        """Test of pcbatt_analysis.dc_rms_analysis.DcRmsProcessingResults class constructor"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (282 > 100 characters) (auto-generated noqa)

        # Arrange + Act
        dc_rms_results_1 = DcRmsProcessingResult(0, 0)
        dc_rms_results_2 = DcRmsProcessingResult(1, 0.707)

        logging.debug("%s = %s", nameof(dc_rms_results_1), repr(dc_rms_results_1))
        logging.debug("%s = %s", nameof(dc_rms_results_2), repr(dc_rms_results_2))

        # Assert results 1
        self.assertIsNotNone(dc_rms_results_1)
        self.assertEqual(0, dc_rms_results_1.dc_value)
        self.assertEqual(0, dc_rms_results_1.rms_value)

        # Assert results 2
        self.assertIsNotNone(dc_rms_results_2)
        self.assertEqual(1, dc_rms_results_2.dc_value)
        self.assertEqual(0.707, dc_rms_results_2.rms_value)


# LabVIEW VI tests
class TestLabViewBasicDcRms(unittest.TestCase):
    """Provides unit tests of LabViewBasicDcRms class.

    Args:
        unittest (TestCase): test cases fixture.
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

    @functional_utilities.repeat(10)
    def test_get_last_error_message_returns_empty_string(self):
        """Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        get_last_error_message method when there is no error"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (356 > 100 characters) (auto-generated noqa)
        last_error_message = LabViewBasicDcRms.get_last_error_message()
        self.assertEqual("", last_error_message)

    @functional_utilities.repeat(10)
    def test_process_single_waveform_dc_rms_lsl_window(self):
        """Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        process_single_waveform_dc_rms method using low side lobe window"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (445 > 100 characters) (auto-generated noqa)

        # Arrange
        tolerance_percent = 0.1
        input_50 = signal.unit_impulse(5, 0)
        input_51 = signal.unit_impulse(5, 1)
        input_52 = signal.unit_impulse(5, 2)
        input_53 = signal.unit_impulse(5, 3)
        input_54 = signal.unit_impulse(5, 4)

        # Act
        dc_rms_50 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_50,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_50), repr(dc_rms_50))

        dc_rms_51 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_51,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_51), repr(dc_rms_51))

        dc_rms_52 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_52,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_52), repr(dc_rms_52))

        dc_rms_53 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_53,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_53), repr(dc_rms_53))

        dc_rms_54 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_54,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.LOW_SIDE_LOBE,
        )

        logging.debug("%s = %s", nameof(dc_rms_54), repr(dc_rms_54))

        # Assert
        # input 50
        self.assertAlmostEqual(13.45e-6, dc_rms_50.dc_value)
        self.assertAlmostEqual(20.20e-6, dc_rms_50.rms_value)

        # input 51
        self.assertAlmostEqual(
            0.03648,
            dc_rms_51.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_51.dc_value),
        )

        self.assertAlmostEqual(
            0.0548,
            dc_rms_51.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_51.rms_value
            ),
        )

        # input 52
        self.assertAlmostEqual(
            0.46352,
            dc_rms_52.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_52.dc_value),
        )

        self.assertAlmostEqual(
            0.69635,
            dc_rms_52.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_52.rms_value
            ),
        )

        # input 53
        self.assertAlmostEqual(
            0.46352,
            dc_rms_53.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_53.dc_value),
        )

        self.assertAlmostEqual(
            0.69635,
            dc_rms_53.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_53.rms_value
            ),
        )

        # input 54
        self.assertAlmostEqual(
            0.03648,
            dc_rms_54.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_54.dc_value),
        )

        self.assertAlmostEqual(
            0.05480,
            dc_rms_54.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_54.rms_value
            ),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_dc_rms_hann_window(self):
        """Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        process_single_waveform_dc_rms method using hann window"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (436 > 100 characters) (auto-generated noqa)

        # Arrange
        tolerance_percent = 0.1
        input_50 = signal.unit_impulse(5, 0)
        input_51 = signal.unit_impulse(5, 1)
        input_52 = signal.unit_impulse(5, 2)
        input_53 = signal.unit_impulse(5, 3)
        input_54 = signal.unit_impulse(5, 4)

        # Act
        dc_rms_50 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_50,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        dc_rms_51 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_51,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        dc_rms_52 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_52,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        dc_rms_53 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_53,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        dc_rms_54 = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=input_54,
            waveform_sampling_period_seconds=1,
            dc_rms_processing_window=DcRmsProcessingWindow.HANN,
        )

        logging.debug("%s = %s", nameof(dc_rms_50), repr(dc_rms_50))
        logging.debug("%s = %s", nameof(dc_rms_51), repr(dc_rms_51))
        logging.debug("%s = %s", nameof(dc_rms_52), repr(dc_rms_52))
        logging.debug("%s = %s", nameof(dc_rms_53), repr(dc_rms_53))
        logging.debug("%s = %s", nameof(dc_rms_54), repr(dc_rms_54))

        # Assert
        # input 50
        self.assertAlmostEqual(0, dc_rms_50.dc_value)
        self.assertAlmostEqual(0, dc_rms_50.dc_value)

        # input 51
        self.assertAlmostEqual(
            0.13820,
            dc_rms_51.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_51.dc_value),
        )

        self.assertAlmostEqual(
            0.25231,
            dc_rms_51.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_51.rms_value
            ),
        )

        # input 52
        self.assertAlmostEqual(
            0.36180,
            dc_rms_52.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_52.dc_value),
        )

        self.assertAlmostEqual(
            0.66056,
            dc_rms_52.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_52.rms_value
            ),
        )

        # input 53
        self.assertAlmostEqual(
            0.36180,
            dc_rms_53.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_53.dc_value),
        )

        self.assertAlmostEqual(
            0.66056,
            dc_rms_53.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_53.rms_value
            ),
        )

        # input 54
        self.assertAlmostEqual(
            0.13820,
            dc_rms_54.dc_value,
            delta=numeric_utilities.percent_of(percent=tolerance_percent, value=dc_rms_54.dc_value),
        )

        self.assertAlmostEqual(
            0.25231,
            dc_rms_54.rms_value,
            delta=numeric_utilities.percent_of(
                percent=tolerance_percent, value=dc_rms_54.rms_value
            ),
        )

    @functional_utilities.repeat(10)
    def test_process_single_waveform_dc_rms_rectangular_window(self):
        """Test of pcbatt_analysis.dc_rms_analysis.LabViewDcRms
        process_single_waveform_dc_rms method using rectangular window"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (443 > 100 characters) (auto-generated noqa)

        samples = numpy.array(range(1, 11), dtype=numpy.float64)

        dc_rms_result = LabViewBasicDcRms.process_single_waveform_dc_rms(
            waveform_samples=samples,
            waveform_sampling_period_seconds=1.0,
            dc_rms_processing_window=DcRmsProcessingWindow.RECTANGULAR,
        )

        logging.debug("%s = %s", nameof(dc_rms_result), repr(dc_rms_result))

        self.assertGreaterEqual(dc_rms_result.dc_value, 5.5)
        self.assertGreaterEqual(dc_rms_result.rms_value, 6.2)


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
