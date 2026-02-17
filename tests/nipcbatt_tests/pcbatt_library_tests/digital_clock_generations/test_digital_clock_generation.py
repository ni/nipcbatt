"""This module provides DigitalClockGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof
from nipcbatt import daq


class TestDigitalClockGeneration(unittest.TestCase):
    """Defines a test fixture that ensures the class 'DigitalClockGeneration' is
       correct and ready to use

    Args:
        unittest.TestCase: Base class for unit tests which is inherited
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

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_clock_generation(self):
        """Checks if class 'DigitalClockGeneration' is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (258 > 100 characters) (auto-generated noqa)

        physical_channel = "Simulated_DAQ/ctr0"
        output_terminal = "/Simulated_DAQ/PFI12"
        timing_parameters = daq.DigitalClockGenerationTimingParameters(1.0)
        counter_parameters = daq.DigitalClockGenerationCounterChannelParameters(1000.0, 0.5)
        config = daq.DigitalClockGenerationConfiguration(counter_parameters, timing_parameters)

        gen = daq.DigitalClockGeneration()
        gen.initialize(physical_channel, output_terminal)
        gen.configure_and_generate(config)
        gen.close()


if __name__ == "__main__":
    unittest.main()
