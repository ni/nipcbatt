"""This module provides DcRmsCurrentMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_analysis import analysis_library_info
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsCurrentMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestDcRmsCurrentMeasurement(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurement` class is ready to use.

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
        _replace_daqmx(_InterpreterDcRmsCurrentMeasurement)

        # active debug traces of native dll
        analysis_library_info.enable_traces(True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

        # active debug traces of native dll
        analysis_library_info.enable_traces(False)

    def test_dc_rms_current_measurement(self):
        """Tests for the proper flow of DC-RMS Current Measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)
        measurement = nipcbatt.DcRmsCurrentMeasurement()
        measurement.initialize(analog_input_channel_expression="TS1Mod2_ai/ai0:2")
        measurement.configure_and_measure(
            configuration=nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION
        )
        measurement.close()

    def test_dc_rms_current_measurement_analysis_with_empty_data(self):
        """Tests if calling analyze_measurement_data
        with None as measure_data input raises Attribute error as expected."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (371 > 100 characters) (auto-generated noqa)
        measurement = nipcbatt.DcRmsCurrentMeasurement()
        self.assertRaises(
            AttributeError,
            lambda: measurement.analyze_measurement_data(measurement_data=None),
        )


if __name__ == "__main__":
    unittest.main()
