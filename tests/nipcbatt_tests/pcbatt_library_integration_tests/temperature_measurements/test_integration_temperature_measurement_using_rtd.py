"""This module provides test of integration of TemperatureMeasurementUsingRtd."""

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


class TestIntegrationTemperatureMeasurementUsingRtd(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `TemperatureMeasurementUsingRtd` class.

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
        _replace_daqmx_if_not_installed(_InterpreterDcRmsVoltageMeasurement)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_temperature_measurement_using_rtd_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd.TemperatureMeasurementUsingRtd
        with MeasurementExecutionType.CONFIGURE_ONLY"""

        with nipcbatt.TemperatureMeasurementUsingRtd() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            configuration = nipcbatt.TemperatureRtdMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_temperature_measurement_using_rtd_configure_and_measure(self):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd.TemperatureMeasurementUsingRtd
        with MeasurementExecutionType.CONFIGURE_AND_MEASURE"""

        with nipcbatt.TemperatureMeasurementUsingRtd() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            print(f"parameters = {nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION}")
            results = measurement.configure_and_measure(
                configuration=nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION
            )

            print(f"results = {results}")
            self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)

    def test_integration_temperature_measurement_using_rtd_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd.TemperatureMeasurementUsingRtd
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""

        with nipcbatt.TemperatureMeasurementUsingRtd() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3"
            )

            configuration = nipcbatt.TemperatureRtdMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.TemperatureRtdMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)

    def test_integration_temperature_measurement_using_rtd_configure_only_and_measure_only_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement.TimeDomainMeasurement
        with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""

        channel_expressions = [
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai6",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0,"
            + " NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai15",
        ]
        for channel_expression in channel_expressions:
            with nipcbatt.TemperatureMeasurementUsingRtd() as measurement:
                measurement.initialize(channel_expression=channel_expression)

                configuration = nipcbatt.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
                print(f"parameters = {configuration}")
                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
                )
                self.assertIs(None, results)

                configuration = nipcbatt.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
                )
                self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
