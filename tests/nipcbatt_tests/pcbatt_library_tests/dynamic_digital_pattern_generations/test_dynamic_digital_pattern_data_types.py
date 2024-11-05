"""This module provides Dynamic digital pattern data types check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
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

CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/port0/line0"
CLOCK_SOURCE = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
TRIGGER_SOURCE = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestDynamicDigitalPatternGenerationDataTypes(unittest.TestCase):
    """Defines a test fixture to test the datatypes used in dynamic digital
       pulse generation

    Args:
        unittest: The unittest class from which all tests inherit
    """

    def test_dynamic_digital_start_trigger_parameters(self):
        """Ensures a valid instance of DynamicDigitalStartTriggerParameters
        is created when given valid parameters"""

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
        created when given invalid parameters"""

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
        is created when given valid parameters"""

        gen_time = 1.0
        instance = DynamicDigitalPatternGenerationData(gen_time)
        self.assertIsInstance(instance, DynamicDigitalPatternGenerationData)
        self.assertEqual(gen_time, instance.generation_time_seconds)

    def test_dynamic_digital_pattern_generation_data_invalid(self):
        """Ensures that an instance of DynamicDigitalPatternGenerationData is
        not created when given invalid parameters"""

        gen_time = None

        self.assertRaises(ValueError, lambda: DynamicDigitalPatternGenerationData(gen_time))

        gen_time = -1.0

        self.assertRaises(ValueError, lambda: DynamicDigitalPatternGenerationData(gen_time))

    def test_dynamic_digital_pattern_generation_configuration(self):
        """Ensures an instance of DynamicDigitalPatternGenerationConfiguration
        is created when given valid parameters"""

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
