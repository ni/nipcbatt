"""This module provides DigitalPulseGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_constants import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_data_types import (
    DigitalPulseGenerationConfiguration,
    DigitalPulseGenerationCounterChannelParameters,
    DigitalPulseGenerationData,
    DigitalPulseGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_generation import (
    DigitalPulseGeneration,
)

CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
TERMINAL = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestDigitalPulseGeneration(unittest.TestCase):
    """Defines a test fixture that ensures the class 'DigitalPulseGeneration' is
       correct and readhy to use

    Args:
        unittest.TestCase: Base class from which this class inherits
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

    def test_digital_pulse_generation(self):
        """Checks if class DigitalPulseGneration is ready to use"""

        t_low = 1.0
        t_high = 1.0
        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = 10
        cc_params = DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high)
        t_params = DigitalPulseGenerationTimingParameters(p_count)
        config = DigitalPulseGenerationConfiguration(cc_params, t_params)

        gen = DigitalPulseGeneration()
        gen.initialize(CHANNEL, TERMINAL)
        gen.configure_and_generate(config)
        gen.close()


if __name__ == "__main__":
    unittest.main()
