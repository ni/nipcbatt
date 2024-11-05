"""This module provides DigitalPwmMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_data_types import (
    DigitalPwmMeasurementConfiguration,
    DigitalPwmMeasurementCounterChannelParameters,
    DigitalPwmMeasurementData,
    DigitalPwmMeasurementResultData,
    DigitalPwmMeasurementTimingParameters,
)
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_measurement import (
    DigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestDigitalPwmMeasurement(unittest.TestCase):
    """Defines a test fixutre that ensure the class 'DigitalPwmMeasurement'
       is correct and ready to use

    Args:
        unittest.TestCase: Base class of the Python unittest framework
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

    def test_digital_pwm_measurement(self):
        """Checks if class 'DigitalPwmMeasurement' is ready to use"""

        channel = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
        terminal = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
        range_params = DigitalPwmMeasurementCounterChannelParameters(1.0, 10.0, 42)
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        cfg = DigitalPwmMeasurementConfiguration(range_params, edge)

        meas = DigitalPwmMeasurement()
        meas.initialize(channel_expression=channel, input_terminal_name=terminal)
        meas.configure_and_measure(cfg)
        meas.close()


if __name__ == "__main__":
    unittest.main()
