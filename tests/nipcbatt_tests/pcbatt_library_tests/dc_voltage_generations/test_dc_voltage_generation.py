"""This module provides DcVoltageGeneration check."""

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


class TestDcVoltageGeneration(unittest.TestCase):
    """Defines a test fixture that checks
    `DcVoltageGeneration` class is ready to use.

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

    def test_dc_voltage_generation(self):
        """Checks if class `DcVoltageGeneration' is ready for use"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (256 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.DcVoltageGeneration()
        generation.initialize(
            analog_output_channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0"
        )
        generation.configure_and_generate(
            configuration=nipcbatt.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION
        )
        generation.close()


if __name__ == "__main__":
    unittest.main()
