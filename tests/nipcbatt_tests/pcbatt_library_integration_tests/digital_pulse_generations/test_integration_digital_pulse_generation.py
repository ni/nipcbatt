"""This module provides test of integration of DigitalPulseGeneration."""

import importlib
import logging
import sys
import unittest

import nidaqmx.constants
import nidaqmx.stream_writers
import numpy as np
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

# constants used across multiple tests
CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
TERMINAL = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestIntegrationDigitalPulseGeneration(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DigitalPulseGeneration' class

    Args:
        unittest (_type_): _description_
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

    def test_integration_digital_pulse_generation_channel_expression_empty(self):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""

        with DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression="", output_terminal_name=TERMINAL)

            gen.close()

    def test_integration_digital_pulse_generation_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""

        with DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=None, output_terminal_name=TERMINAL)

            gen.close()

    def test_integration_digital_pulse_generation_terminal_empty(self):
        """Integration test ensuring that if input terminal
        is empty then initialize() catches the error
        """

        with DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=CHANNEL, output_terminal_name="")

            gen.close()

    def test_integration_digital_pulse_generation_terminal_is_none(self):
        """Integration test ensuring that if input terminal
        is null then initialize() catches the error
        """

        with DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=CHANNEL, output_terminal_name=None)

            gen.close()

    def test_integration_digital_pulse_generation_configure_and_generate(self):
        """Integration test of Digital Pulse Generation that ensures an instance
        of DigitalPulseGeneration is successfully executed when configure
        and measure is performed"""

        t_low = 0.1
        t_high = 0.1
        state_idle = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = 10

        channel_params = DigitalPulseGenerationCounterChannelParameters(state_idle, t_low, t_high)
        timing_params = DigitalPulseGenerationTimingParameters(p_count)
        config = DigitalPulseGenerationConfiguration(channel_params, timing_params)

        with DigitalPulseGeneration() as gen:
            gen.initialize(CHANNEL, TERMINAL)
            gen_data = gen.configure_and_generate(config)
            gen.close()

        self.assertIsInstance(gen_data, DigitalPulseGenerationData)

    def test_integration_digital_pulse_generation_negative_values(self):
        """Integration test of Digital Pulse Generation that ensures
        a DigitalPulseGeneration instantiation fails if given a negative
        value for any parameter
        """

        t_low = -0.1
        t_high = 0.1
        state_idle = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = 10

        with DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                channel_params = DigitalPulseGenerationCounterChannelParameters(
                    state_idle, t_low, t_high
                )

                timing_params = DigitalPulseGenerationTimingParameters(p_count)
                config = DigitalPulseGenerationConfiguration(channel_params, timing_params)

                gen.initialize(CHANNEL, TERMINAL)
                gen.configure_and_generate(config)
                gen.close()

        t_low = 0.1
        t_high = -0.1
        state_idle = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = 10

        with DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                channel_params = DigitalPulseGenerationCounterChannelParameters(
                    state_idle, t_low, t_high
                )

                timing_params = DigitalPulseGenerationTimingParameters(p_count)
                config = DigitalPulseGenerationConfiguration(channel_params, timing_params)

                gen.initialize(CHANNEL, TERMINAL)
                gen.configure_and_generate(config)
                gen.close()

        t_low = 0.1
        t_high = 0.1
        state_idle = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        p_count = -10

        with DigitalPulseGeneration() as gen:
            with self.assertRaises(ValueError):
                channel_params = DigitalPulseGenerationCounterChannelParameters(
                    state_idle, t_low, t_high
                )

                timing_params = DigitalPulseGenerationTimingParameters(p_count)
                config = DigitalPulseGenerationConfiguration(channel_params, timing_params)

                gen.initialize(CHANNEL, TERMINAL)
                gen.configure_and_generate(config)
                gen.close()

    def test_integration_digital_pulse_generation_no_idle_state_defined(self):
        """Integration test of Digital Pulse Generation that ensures an instance
        of DigitalPulseGeneration is successfully executed when the user does not
        define an idle state with otherwise valid data"""

        t_low = 0.1
        t_high = 0.1
        p_count = 10

        with DigitalPulseGeneration() as gen:
            channel_params = DigitalPulseGenerationCounterChannelParameters(
                low_time_seconds=t_low, high_time_seconds=t_high
            )

            timing_params = DigitalPulseGenerationTimingParameters(p_count)
            config = DigitalPulseGenerationConfiguration(channel_params, timing_params)

            gen.initialize(CHANNEL, TERMINAL)
            gen_data = gen.configure_and_generate(config)
            gen.close()

            self.assertIsInstance(gen_data, DigitalPulseGenerationData)


if __name__ == "__main__":
    unittest.main()
