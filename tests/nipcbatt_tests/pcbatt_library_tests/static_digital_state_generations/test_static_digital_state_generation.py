"""This module provides StaticDigitalStateGeneration check."""

import importlib.metadata
import logging
import random
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


class TestStaticDigitalStateGeneration(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'StaticDigitalStateGeneration' is correct and
       ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits.
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
        _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_static_digital_state_generation(self):
        """Checks if class 'StaticDigitalStateGeneration' is ready to use"""

        num_channels = 3
        test_data_to_write = [random.choice([True, False]) for item in range(num_channels)]
        test_cfg = nipcbatt.StaticDigitalStateGenerationConfiguration(
            data_to_write=test_data_to_write
        )

        gen = nipcbatt.StaticDigitalStateGeneration()
        gen.initialize("NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:2")
        gen.configure_and_generate(configuration=test_cfg)
        gen.close()


if __name__ == "__main__":
    unittest.main()
