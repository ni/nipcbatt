"""This module provides test of integration of DcRmsVoltageMeasurement."""

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
    _replace_daqmx_if_not_installed,
)


class TestIntegrationDcRmsVoltageMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `DcRmsVoltageMeasurement` class.

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
        _replace_daqmx_if_not_installed(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_dc_rms_voltage_measurement_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement.DcRmsVoltageMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (425 > 100 characters) (auto-generated noqa)

        with nipcbatt.DcRmsVoltageMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = nipcbatt.DcRmsVoltageMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_dc_rms_voltage_measurement_configure_and_measure(self):
        """Integration test of
        nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement.DcRmsVoltageMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        with nipcbatt.DcRmsVoltageMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            print(f"parameters = {nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION}")
            results = measurement.configure_and_measure(
                configuration=nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION
            )

            print(f"results = {results}")
            self.assertIsInstance(results, nipcbatt.DcRmsVoltageMeasurementResultData)

    def test_integration_dc_rms_voltage_measurement_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement.DcRmsVoltageMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with nipcbatt.DcRmsVoltageMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = nipcbatt.DcRmsVoltageMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.DcRmsVoltageMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.DcRmsVoltageMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
