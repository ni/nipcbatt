"""This module provides DigitalFrequencyMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_data_types import (  # DigitalFrequencyMeasurementResultData,
    DigitalFrequencyMeasurementConfiguration,
    DigitalFrequencyMeasurementCounterChannelParameters,
    DigitalFrequencyRangeParameters,
)
from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_measurement import (
    DigitalFrequencyMeasurement,
)


class TestDigitalFrequencyMeasurement(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'DigitalFrequencyMeasurement' is correct
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

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_digital_frequency_measurement(self):
        """Checks if class 'DigitalFrequencyMeasurement' is ready to use"""

        min_freq, max_freq, divisor, dur = 1.0, 1000.0, 4, 1.0
        test_params = DigitalFrequencyRangeParameters(min_freq, max_freq)
        test_ccp = DigitalFrequencyMeasurementCounterChannelParameters(test_params, divisor, dur)
        test_config = DigitalFrequencyMeasurementConfiguration(test_ccp)

        meas = DigitalFrequencyMeasurement()
        meas.initialize(
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0",
            "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0",
        )
        meas.configure_and_measure(test_config)
        meas.close()


if __name__ == "__main__":
    unittest.main()
