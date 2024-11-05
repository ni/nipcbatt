"""This module provides test of integration of DcRmsCurrentMeasurement."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterDcRmsCurrentMeasurement,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)


class TestIntegrationDcRmsCurrentMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `DcRmsCurrentMeasurement` class.

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
        _replace_daqmx_if_not_installed(_InterpreterDcRmsCurrentMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_dc_rms_current_measurement_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY"""

        with nipcbatt.DcRmsCurrentMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = nipcbatt.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

            measurement.close()

    def test_integration_dc_rms_current_measurement_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""

        with nipcbatt.DcRmsCurrentMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = nipcbatt.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.DcRmsCurrentMeasurementResultData)

            measurement.close()

    def test_integration_dc_rms_current_measurement_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE.
        """

        with nipcbatt.DcRmsCurrentMeasurement() as measurement:
            measurement.initialize(
                analog_input_channel_expression=(
                    "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
                )
            )

            configuration = nipcbatt.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.SKIP_ANALYSIS, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.DcRmsCurrentMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=(nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE),
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.DcRmsCurrentMeasurementResultData)

            measurement.close()

    def test_integration_dc_rms_current_measurement_full_sequence_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement.DcRmsCurrentMeasurement
        to be called in a loop.
        """

        channel_list = [
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai5",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai1,NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai6",
        ]

        for channel in channel_list:
            with nipcbatt.DcRmsCurrentMeasurement() as measurement:
                measurement.initialize(analog_input_channel_expression=channel)

                configuration = nipcbatt.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"With Default configurations for channel string :{channel}, results = {results}"
                )
                self.assertIsInstance(results, nipcbatt.DcRmsCurrentMeasurementResultData)

                measurement.close()


if __name__ == "__main__":
    unittest.main()
