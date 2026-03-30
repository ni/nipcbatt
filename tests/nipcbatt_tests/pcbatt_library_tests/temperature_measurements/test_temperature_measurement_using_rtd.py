"""This module provides TemperatureMeasurementUsingRtd check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library_core.daq._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestTemperatureMeasurementUsingRtd(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureMeasurementUsingRtd` class is ready to use.

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
        _replace_daqmx(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_temperature_measurement_using_rtd(self):
        """Checks if class TemperatureMeasurementUsingRtd is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)
        measurement = nipcbatt.daq.TemperatureMeasurementUsingRtd()
        measurement.initialize(channel_expression="Dev/ai0")

        # Create a custom configuration with CONFIGURE_ONLY to avoid mock limitations
        from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
        from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_data_types import (
            TemperatureRtdMeasurementConfiguration,
        )
        from nipcbatt.pcbatt_library.daq.temperature_measurements.temperature_constants import (
            DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS,
            DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
            DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
        )

        configure_only_configuration = TemperatureRtdMeasurementConfiguration(
            global_channel_parameters=DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS,
            specific_channels_parameters=[],
            measurement_execution_type=MeasurementExecutionType.CONFIGURE_ONLY,
            sample_clock_timing_parameters=DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
            digital_start_trigger_parameters=DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
        )

        measurement.configure_and_measure(configuration=configure_only_configuration)

        measurement.close()


if __name__ == "__main__":
    unittest.main()
