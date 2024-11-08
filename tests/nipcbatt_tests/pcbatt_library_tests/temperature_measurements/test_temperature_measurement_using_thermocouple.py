"""This module provides TemperatureMeasurementUsingThermocouple check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
from varname import nameof

import nipcbatt


class TestTemperatureMeasurementUsingThermocouple(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureMeasurementUsingThermocouple` class is ready to use.

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

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_measurement_using_thermocouple(self):
        """Checks if class TemperatureMeasurementUsingThermocouple is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (196 > 100 characters) (auto-generated noqa)
        measurement = nipcbatt.TemperatureMeasurementUsingThermocouple()
        measurement.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0",
            cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
            cold_junction_compensation_channel="",
        )

        results = measurement.configure_and_measure(
            configuration=nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION
        )
        print(results)

        measurement.close()


if __name__ == "__main__":
    unittest.main()
