"""This module provides TemperatureMeasurementUsingThermistor check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestTemperatureMeasurementUsingThermistor(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureMeasurementUsingThermistor` class is ready to use.

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
        _replace_daqmx(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_measurement_using_thermistor(self):
        """Checks if class TemperatureMeasurementUsingThermistor is ready to use"""
        measurement = nipcbatt.TemperatureMeasurementUsingThermistor()
        measurement.initialize(channel_expression="Dev/ai0")

        results = measurement.configure_and_measure(
            configuration=nipcbatt.DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION
        )
        print(results)

        measurement.close()


if __name__ == "__main__":
    unittest.main()
