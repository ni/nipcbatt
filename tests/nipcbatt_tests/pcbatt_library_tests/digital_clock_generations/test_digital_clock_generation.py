"""This module provides DigitalClockGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_data_types import (
    DigitalClockGenerationConfiguration,
    DigitalClockGenerationCounterChannelParameters,
    DigitalClockGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_generation import (
    DigitalClockGeneration,
)


class TestDigitalClockGeneration(unittest.TestCase):
    """Defines a test fixture that ensures the class 'DigitalClockGeneration' is
       correct and ready to use

    Args:
        unittest.TestCase: Base class for unit tests which is inherited
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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_clock_generation(self):
        """Checks if class 'DigitalClockGeneration' is ready to use"""

        physical_channel = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
        output_terminal = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
        timing_parameters = DigitalClockGenerationTimingParameters(1.0)
        counter_parameters = DigitalClockGenerationCounterChannelParameters(1000.0, 0.5)
        config = DigitalClockGenerationConfiguration(counter_parameters, timing_parameters)

        gen = DigitalClockGeneration()
        gen.initialize(physical_channel, output_terminal)
        gen.configure_and_generate(config)
        gen.close()


if __name__ == "__main__":
    unittest.main()
