"""This module provides StaticDigitalStateMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.static_digital_state_measurements.static_digital_state_measurement import (
    StaticDigitalStateMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestStaticDigitalStateMeasurement(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'StaticDigitalStateMeasurement' is correct
       and ready to use

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

    def test_static_digital_state_measurement(self):
        """Checks if class 'StaticDigitalStateMeasurement' is ready for use"""
        meas = StaticDigitalStateMeasurement()
        meas.initialize("NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:7")
        meas.configure_and_measure()
        meas.close()


if __name__ == "__main__":
    unittest.main()
