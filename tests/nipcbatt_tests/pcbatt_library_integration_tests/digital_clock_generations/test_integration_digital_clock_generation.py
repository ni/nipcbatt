"""This module provides test of integration of DigitalClockGeneration."""

import importlib
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_constants import (  # noqa: F401 - 'nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_constants.ConstantsForDigitalClockGeneration' imported but unused (auto-generated noqa)
    ConstantsForDigitalClockGeneration,
)
from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_data_types import (
    DigitalClockGenerationConfiguration,
    DigitalClockGenerationCounterChannelParameters,
    DigitalClockGenerationData,
    DigitalClockGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_generation import (
    DigitalClockGeneration,
)

# constants used across multiple tests
CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
TERMINAL = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestIntegrationDigitalClockGeneration(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DigitalClockGeneration' class

    Args:
        unittest.TestCase: Base class of the unittest framework
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

    def test_integration_digital_clock_generation_counter_channel_expression_is_empty(
        self,
    ):
        """Integration test ensuring that is channel expression
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(counter_channel_expression="", output_terminal_name=TERMINAL)

            gen.close()

    def test_integration_digital_clock_generation_counter_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that is channel expression
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(counter_channel_expression=None, output_terminal_name=TERMINAL)

            gen.close()

    def test_integration_digital_clock_generation_output_terminal_is_empty(
        self,
    ):
        """Integration test ensuring that if terminal
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(counter_channel_expression=CHANNEL, output_terminal_name="")

            gen.close()

    def test_integration_digital_clock_generation_output_terminal_is_none(
        self,
    ):
        """Integration test ensuring that if terminal
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        gen = DigitalClockGeneration()

        with self.assertRaises(ValueError):
            gen.initialize(counter_channel_expression=CHANNEL, output_terminal_name=None)

        gen.close()

    def test_integration_digital_clock_generation_configure_counter_only(self):
        """Integration test of Digital Clock Generation that ensure an instance
        of DigitalClockGeneration is successfully initialized and configured
        when given correct inputs"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (406 > 100 characters) (auto-generated noqa)

        frequency = 1000.0
        duty_cyc = 0.5
        duration = 10.0

        with DigitalClockGeneration() as gen:
            counter_params = DigitalClockGenerationCounterChannelParameters(
                frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
            )

            timing_params = DigitalClockGenerationTimingParameters(clock_duration_seconds=duration)

            gen.initialize(CHANNEL, TERMINAL)
            gen.configure_counter_channel(parameters=counter_params)
            gen.configure_timing(parameters=timing_params)
            gen.close()

    def test_integration_digital_clock_generation_configure_and_measure(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration isntance is successfully returned
        when given the necessary inputs
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        frequency = 1000.0
        duty_cyc = 0.5
        duration = 10.0

        with DigitalClockGeneration() as gen:
            counter_params = DigitalClockGenerationCounterChannelParameters(
                frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
            )

            timing_params = DigitalClockGenerationTimingParameters(clock_duration_seconds=duration)

            config = DigitalClockGenerationConfiguration(
                counter_channel_parameters=counter_params,
                timing_parameters=timing_params,
            )

            gen.initialize(CHANNEL, TERMINAL)
            actual_data = gen.configure_and_generate(configuration=config)
            gen.close()

            self.assertIsInstance(actual_data, DigitalClockGenerationData)

    def test_integration_digital_clock_generation_negative_vales(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration instantiation fails if given a negative
        value for any parameter
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        frequency = -0.1
        duty_cyc = 0.5
        duration = 10.0

        with DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = DigitalClockGenerationCounterChannelParameters(
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = DigitalClockGenerationTimingParameters(
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)

        frequency = 1000.0
        duty_cyc = -0.5
        duration = 10.0

        with DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = DigitalClockGenerationCounterChannelParameters(
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = DigitalClockGenerationTimingParameters(
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)

        frequency = 1000.0
        duty_cyc = 0.5
        duration = -0.1

        with DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = DigitalClockGenerationCounterChannelParameters(  # noqa: F841 - local variable 'counter_params' is assigned to but never used (auto-generated noqa)
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = DigitalClockGenerationTimingParameters(  # noqa: F841 - local variable 'timing_params' is assigned to but never used (auto-generated noqa)
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)

    def test_integration_digital_clock_generation_duty_cycle(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration instantiation fails if given a value
        greater than 1.0 or is provided for duty cycle
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        frequency = 1000
        duty_cyc = 1.1
        duration = 10.0

        with DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = DigitalClockGenerationCounterChannelParameters(  # noqa: F841 - local variable 'counter_params' is assigned to but never used (auto-generated noqa)
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = DigitalClockGenerationTimingParameters(  # noqa: F841 - local variable 'timing_params' is assigned to but never used (auto-generated noqa)
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)

    def test_integration_digital_clock_generation_zero_duration(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalClockGeneration instantiation fails if given a value
        of 0 for duration
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        frequency = 1000
        duty_cyc = 0.5
        duration = 0.0

        with DigitalClockGeneration() as gen:
            with self.assertRaises(ValueError):
                counter_params = DigitalClockGenerationCounterChannelParameters(  # noqa: F841 - local variable 'counter_params' is assigned to but never used (auto-generated noqa)
                    frequency_hertz=frequency, duty_cycle_ratio=duty_cyc
                )

                timing_params = DigitalClockGenerationTimingParameters(  # noqa: F841 - local variable 'timing_params' is assigned to but never used (auto-generated noqa)
                    clock_duration_seconds=duration
                )

                gen.initialize(CHANNEL, TERMINAL)


if __name__ == "__main__":
    unittest.main()
