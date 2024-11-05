"""This module provides test of integration of DynamicDigitalPatternGeneration."""

import importlib
import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
import nidaqmx.stream_writers
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DynamicDigitalPatternTimingParameters,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternGenerationConfiguration,
    DynamicDigitalPatternGenerationData,
    DynamicDigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_generation import (
    DynamicDigitalPatternGeneration,
)

# constants used across tests
CHANNEL = "TS1_DIO/port0/line0:7"
CLOCK_SOURCE = "OnboardClock"
TRIGGER_SOURCE = "/TS1_Core/PFI0"


class TestIntegrationDynamicDigitalPatternGeneration(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DynamicDigitalPatternGeneration' class

    Args:
        unittest: Base class for all tests
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

    def test_integration_dynamic_digital_pattern_gen_channel_expression_empty(self):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""

        with DynamicDigitalPatternGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression="")

            gen.close()

    def test_integration_dynamic_digital_pattern_gen_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression
        is null then initialize() catches the error
        """

        with DynamicDigitalPatternGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=None)

            gen.close()

    def test_integration_dynamic_digital_pattern_gen_configure_and_measure(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is successfully executed when configure
        and measure is performed"""

        test_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000.0

        timing_params = DynamicDigitalPatternTimingParameters(
            sample_clock_source=CLOCK_SOURCE,
            number_of_samples_per_channel=100,
            active_edge=test_edge,
            sampling_rate_hertz=test_sample_rate,
        )

        trigger_params = DynamicDigitalStartTriggerParameters(
            digital_start_trigger_source=TRIGGER_SOURCE,
            digital_start_trigger_edge=test_edge,
            trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
        )

        test_config = DynamicDigitalPatternGenerationConfiguration(
            timing_parameters=timing_params,
            digital_start_trigger_parameters=trigger_params,
        )

        gen = DynamicDigitalPatternGeneration()
        gen.initialize(CHANNEL)

        if gen.task.name is not None and gen.task.channel_names is not None:
            n = len(gen.task.channel_names)
        else:
            n = 11

        pattern = np.zeros((n, 10), dtype="uint32")

        gen.configure_and_generate(test_config, pattern)
        gen.close()

    def test_integration_dynamic_digital_pattern_rate_not_float(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given sample
        rate is not a float"""

        test_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000

        with self.assertRaises(ValueError):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = DynamicDigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = DynamicDigitalPatternGenerationConfiguration(
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
            )

            gen = DynamicDigitalPatternGeneration()

    def test_integration_dynamic_digital_pattern_rate_negative(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given sample
        rate is a negative number"""

        test_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = -1000.0

        with self.assertRaises(ValueError):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = DynamicDigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = DynamicDigitalPatternGenerationConfiguration(
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
            )

            gen = DynamicDigitalPatternGeneration()

    def test_integration_dynamic_digital_pattern_signal_empty(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given signal is an empty
        array"""

        test_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000.0

        signal = np.array([])

        gen = DynamicDigitalPatternGeneration()

        with self.assertRaises(ValueError):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = DynamicDigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = DynamicDigitalPatternGenerationConfiguration(
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
            )

            gen.initialize(channel_expression=CHANNEL)
            gen.configure_and_generate(configuration=test_config, pulse_signal=signal)

        gen.close()

    def test_integration_dynamic_digital_pattern_signal_none(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given signal is an empty
        array"""

        test_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000.0

        signal = None

        with self.assertRaises(ValueError):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = DynamicDigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = DynamicDigitalPatternGenerationConfiguration(
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
            )

            gen = DynamicDigitalPatternGeneration()
            gen.initialize(channel_expression=CHANNEL)
            gen.configure_and_generate(configuration=test_config, pulse_signal=signal)
            gen.close()

    def test_integration_dynamic_digital_pattern_signal_wrong_shape(self):
        """Integration test of Dynamic Digital Pattern Generation that ensures an instance
        of DynamicDigitalPatternGeneration is not created if the given signal is the
        wrong shape"""

        test_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        test_sample_rate = 1000.0

        # wrong shape of data array
        signal = np.zeros((10, 10))

        with self.assertRaises(Exception):
            timing_params = DynamicDigitalPatternTimingParameters(
                sample_clock_source=CLOCK_SOURCE,
                number_of_samples_per_channel=100,
                active_edge=test_edge,
                sampling_rate_hertz=test_sample_rate,
            )

            trigger_params = DynamicDigitalStartTriggerParameters(
                digital_start_trigger_source=TRIGGER_SOURCE,
                digital_start_trigger_edge=test_edge,
                trigger_type=nidaqmx.constants.TriggerType.DIGITAL_EDGE,
            )

            test_config = DynamicDigitalPatternGenerationConfiguration(
                timing_parameters=timing_params,
                digital_start_trigger_parameters=trigger_params,
            )

            gen = DynamicDigitalPatternGeneration()
            gen.initialize(channel_expression=CHANNEL)
            gen.configure_and_generate(configuration=test_config, pulse_signal=signal)
            gen.close()


if __name__ == "__main__":
    unittest.main()
