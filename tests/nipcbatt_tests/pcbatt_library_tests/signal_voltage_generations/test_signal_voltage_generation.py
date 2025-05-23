"""This module provides SignalVoltageGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestSignalVoltageGeneration(unittest.TestCase):
    """Defines a test fixture that checks
    `SignalVoltageGeneration` class is ready to use.

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_sine_wave(self):
        """Checks if class `SignalVoltageGeneration` is ready for use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (260 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.SignalVoltageGeneration()
        # Test for Sine wave generation
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_and_generate_sine_waveform(
            configuration=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION,
        )
        generation.close()

    def test_signal_voltage_generation_square_wave(self):
        """Checks if class `SignalVoltageGeneration` is ready for use for square wave generation"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.SignalVoltageGeneration()
        # Test for Square wave generation
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_and_generate_square_waveform(
            configuration=nipcbatt.DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION,
        )
        generation.close()

    def test_signal_voltage_generation_multiple_tones_wave(self):
        """Checks if class `SignalVoltageGeneration` is ready for use
        for Multiple-tones generation"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (410 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.SignalVoltageGeneration()
        # Test for multi-tone sine wave generation
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_and_generate_multiple_tones_waveform(
            configuration=nipcbatt.DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION,
        )
        generation.close()


if __name__ == "__main__":
    unittest.main()
