"""This module provides DynamicDigitalPatternGeneration check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants  # noqa: F401 - 'nidaqmx.constants' imported but unused (auto-generated noqa)
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DynamicDigitalPatternTimingParameters,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_data_types.DynamicDigitalPatternGenerationData' imported but unused (auto-generated noqa)
    DynamicDigitalPatternGenerationConfiguration,
    DynamicDigitalPatternGenerationData,
    DynamicDigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_generation import (
    DynamicDigitalPatternGeneration,
)

CHANNEL = "TS1_DIO/port0/line0:7"
CLOCK_SOURCE = "OnboardClock"
TRIGGER_SOURCE = "/TS1_Core/PFI0"


class TestDynamicDigitalPatternGeneration(unittest.TestCase):
    """Defines a test fixture that ensures the class 'DynamicDigitalPatternGeneration' is
       correct and ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits
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

    def test_dynamic_digital_pattern_generation(self):
        """Checks if class DynamicDigitalPatternGeneration is ready to use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (265 > 100 characters) (auto-generated noqa)

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

        config = DynamicDigitalPatternGenerationConfiguration(time_parameters, trig_parameters)

        gen = DynamicDigitalPatternGeneration()

        gen.initialize(CHANNEL)
        gen.task.stop()

        if gen.task.channel_names:
            n = len(gen.task.channel_names)
        else:
            n = 1
        pattern = np.zeros((n, 1), dtype="uint32")

        gen.configure_and_generate(config, pattern)
        gen.close()


if __name__ == "__main__":
    unittest.main()
