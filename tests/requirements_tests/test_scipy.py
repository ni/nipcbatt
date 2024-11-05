"""This module provides scipy framework check."""

import importlib.metadata
import logging
import sys
import unittest

import scipy
import scipy.signal
from varname import nameof


class TestSignal(unittest.TestCase):
    """Defines a test fixture that checks scipy package is ready to use.

    Args:
        unittest (TestCase): test case type
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_numpy_version = importlib.metadata.version("numpy")
        used_scypi_version = importlib.metadata.version("scipy")

        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)
        logging.debug("%s = %s", nameof(used_scypi_version), used_scypi_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def setUp(self):
        print("Setup method")

    def tearDown(self):
        print("Teardown method")

    def test_signal_windows_hann(self):
        """Checks method scipy.signal.windows.hann is ready to use"""
        window_length = 51
        hann_window = scipy.signal.windows.hann(M=window_length)
        self.assertIsNotNone(hann_window)
        self.assertEqual(first=window_length, second=len(hann_window.data))

        hann_window_first_element = hann_window[0]
        hann_window_last_element = hann_window[-1]

        self.assertEqual(first=hann_window_first_element, second=hann_window_last_element)

        self.assertAlmostEqual(first=hann_window[1], second=hann_window[-2], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[2], second=hann_window[-3], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[3], second=hann_window[-4], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[4], second=hann_window[-5], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[5], second=hann_window[-6], delta=0.0001)

    def test_signal_windows_hamming(self):
        """Checks method scipy.signal.windows.hamming is ready to use"""
        window_length = 51
        hann_window = scipy.signal.windows.hamming(M=window_length)
        self.assertIsNotNone(hann_window)
        self.assertEqual(first=window_length, second=len(hann_window.data))

        hann_window_first_element = hann_window[0]
        hann_window_last_element = hann_window[-1]

        self.assertEqual(first=hann_window_first_element, second=hann_window_last_element)

        self.assertAlmostEqual(first=hann_window[1], second=hann_window[-2], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[2], second=hann_window[-3], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[3], second=hann_window[-4], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[4], second=hann_window[-5], delta=0.0001)
        self.assertAlmostEqual(first=hann_window[5], second=hann_window[-6], delta=0.0001)

    def test_signal_find_peaks(self):
        """Checks method scipy.signal.find_peaks is ready to use"""

        sawtooth_width_eq1 = scipy.signal.sawtooth(t=range(0, 16), width=1)
        found_peaks = scipy.signal.find_peaks(x=sawtooth_width_eq1, threshold=0.01)

        logging.debug("%s = %s", nameof(sawtooth_width_eq1), sawtooth_width_eq1)
        logging.debug("%s = %s", nameof(found_peaks), found_peaks)

        self.assertIsNotNone(found_peaks)
        self.assertEqual(first=2, second=len(found_peaks[1]))

    def test_signal_square(self):
        """Checks method scipy.signal.square is ready to use"""
        square_05_duty_cycle = scipy.signal.square(t=[1, 2, 3, 4], duty=0.5)
        self.assertIsNotNone(square_05_duty_cycle)
        self.assertEqual(first=4, second=len(square_05_duty_cycle.data))

    def test_signal_sawtooth(self):
        """Checks method scipy.signal.sawtooth is ready to use"""
        sawtooth_width_eq1 = scipy.signal.sawtooth(t=[1, 2, 3, 4], width=1)
        self.assertIsNotNone(sawtooth_width_eq1)
        self.assertEqual(first=4, second=len(sawtooth_width_eq1.data))


if __name__ == "__main__":
    unittest.main()
