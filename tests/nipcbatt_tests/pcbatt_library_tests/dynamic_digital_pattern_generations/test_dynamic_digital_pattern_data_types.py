"""This module provides Dynamic digital pattern data types check."""

import importlib.metadata  # noqa: F401 - 'importlib.metadata' imported but unused (auto-generated noqa)
import logging  # noqa: F401 - 'logging' imported but unused (auto-generated noqa)
import sys  # noqa: F401 - 'sys' imported but unused (auto-generated noqa)
import unittest

import nidaqmx.constants  # noqa: F401 - 'nidaqmx.constants' imported but unused (auto-generated noqa)
from varname import (  # noqa: F401 - 'varname.nameof' imported but unused (auto-generated noqa)
    nameof,
)

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

CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/port0/line0"
CLOCK_SOURCE = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
TRIGGER_SOURCE = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestDynamicDigitalPatternGenerationDataTypes(unittest.TestCase):
    """Defines a test fixture to test the datatypes used in dynamic digital
       pulse generation

    Args:
        unittest: The unittest class from which all tests inherit
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def test_dynamic_digital_start_trigger_parameters(self):
        """Ensures a valid instance of DynamicDigitalStartTriggerParameters
        is created when given valid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (419 > 100 characters) (auto-generated noqa)

        trig_source = TRIGGER_SOURCE
        trig_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        trig_type = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE

        instance = DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type)

        self.assertIsInstance(instance, DynamicDigitalStartTriggerParameters)
        self.assertEqual(trig_source, instance.digital_start_trigger_source)
        self.assertEqual(trig_edge, instance.digital_start_trigger_edge)
        self.assertEqual(trig_type, instance.trigger_type)

    def test_dynamic_digital_start_trigger_parameters_invalid(self):
        """Ensures an instance of DynamicDigitalStartTriggerParameters is not
        created when given invalid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        trig_source = None
        trig_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        trig_type = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE

        self.assertRaises(
            ValueError,
            lambda: DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type),
        )

        trig_source = TRIGGER_SOURCE
        trig_edge = None
        trig_type = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE

        self.assertRaises(
            ValueError,
            lambda: DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type),
        )

        trig_source = TRIGGER_SOURCE
        trig_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        trig_type = None

        self.assertRaises(
            ValueError,
            lambda: DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type),
        )

    def test_dynamic_digital_pattern_generation_data(self):
        """Ensures that a valid instance of DynamicDigitalPatternGenerationData
        is created when given valid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (419 > 100 characters) (auto-generated noqa)

        gen_time = 1.0
        instance = DynamicDigitalPatternGenerationData(gen_time)
        self.assertIsInstance(instance, DynamicDigitalPatternGenerationData)
        self.assertEqual(gen_time, instance.generation_time_seconds)

    def test_dynamic_digital_pattern_generation_data_invalid(self):
        """Ensures that an instance of DynamicDigitalPatternGenerationData is
        not created when given invalid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        gen_time = None

        self.assertRaises(ValueError, lambda: DynamicDigitalPatternGenerationData(gen_time))

        gen_time = -1.0

        self.assertRaises(ValueError, lambda: DynamicDigitalPatternGenerationData(gen_time))

    def test_dynamic_digital_pattern_generation_configuration(self):
        """Ensures an instance of DynamicDigitalPatternGenerationConfiguration
        is created when given valid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (419 > 100 characters) (auto-generated noqa)

        clock_source = CLOCK_SOURCE
        num_samples = 100
        edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        sample_rate = 10000.0
        trig_source = TRIGGER_SOURCE
        trig_edge = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_EDGE
        trig_type = ConstantsForDynamicDigitalPatternGeneration.DEFAULT_TRIGGER_TYPE

        time_parameters = DynamicDigitalPatternTimingParameters(
            clock_source,
            sample_rate,
            num_samples,
            edge,
        )

        trig_parameters = DynamicDigitalStartTriggerParameters(trig_source, trig_edge, trig_type)

        instance = DynamicDigitalPatternGenerationConfiguration(time_parameters, trig_parameters)

        self.assertIsInstance(instance, DynamicDigitalPatternGenerationConfiguration)

        self.assertEqual(clock_source, instance.timing_parameters.sample_clock_source)
        self.assertEqual(num_samples, instance.timing_parameters.number_of_samples_per_channel)
        self.assertEqual(edge, instance.timing_parameters.active_edge)
        self.assertEqual(sample_rate, instance.timing_parameters.sampling_rate_hertz)

        self.assertEqual(
            trig_source,
            instance.digital_start_trigger_parameters.digital_start_trigger_source,
        )
        self.assertEqual(
            trig_edge,
            instance.digital_start_trigger_parameters.digital_start_trigger_edge,
        )
        self.assertEqual(trig_type, instance.digital_start_trigger_parameters.trigger_type)


if __name__ == "__main__":
    unittest.main()
