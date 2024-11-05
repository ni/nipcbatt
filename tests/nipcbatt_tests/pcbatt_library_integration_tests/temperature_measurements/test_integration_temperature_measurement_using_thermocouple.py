"""This module provides test of integration of TemperatureMeasurementUsingThermocouple."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
import nidaqmx.errors
from varname import nameof

import nipcbatt


class TestIntegrationTemperatureMeasurementUsingThermocouple(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `TemperatureMeasurementUsingThermocouple` class.

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

    def test_integration_temperature_measurement_using_thermocouple_channel_expression_empty(
        self,
    ):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            with self.assertRaises(nidaqmx.errors.DaqError):
                measurement.initialize(
                    channel_expression="",
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                    cold_junction_compensation_channel="",
                )

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            with self.assertRaises(AttributeError):
                measurement.initialize(
                    channel_expression=None,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                    cold_junction_compensation_channel="",
                )

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_cjc_source_is_none(
        self,
    ):
        """Integration test ensuring that if cjc source
        is None then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            with self.assertRaises(AttributeError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                    cold_junction_compensation_source=None,
                    cold_junction_compensation_channel="",
                )

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_cjc_channel_is_none(
        self,
    ):
        """Integration test ensuring that if cjc_channel is null when cjc_source is set to SCANNABLE_CHANNEL,
        then initialize() catches the error
        """  # noqa: W505, D202, D205, D415 - doc line too long (109 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")

            with self.assertRaises(nidaqmx.errors.DaqError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL,
                    cold_junction_compensation_channel=None,
                )
                results = measurement.configure_and_measure(configuration=configuration)
                print(f"results = {results}")

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_cjc_channel_is_empty(
        self,
    ):
        """Integration test ensuring that if cjc_channel is empty when cjc_source is set to SCANNABLE_CHANNEL,
        then configure_and_measure() catches the error
        """  # noqa: W505, D202, D205, D415 - doc line too long (110 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                ),
                specific_channels_parameters=[],
                measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )
            print(f"parameters = {configuration}")

            with self.assertRaises(nidaqmx.errors.DaqError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL,
                    cold_junction_compensation_channel="",
                )
                results = measurement.configure_and_measure(configuration=configuration)
                print(f"results = {results}")

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_cjc_value_is_none(
        self,
    ):
        """Integration test ensuring that if cjc_value is None when cjc_source is set to CONSTANT_USER_VALUE,
        then configure_and_measure() catches the error
        """  # noqa: W505, D202, D205, D415 - doc line too long (109 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            with self.assertRaises(ValueError):
                channel_parameters = nipcbatt.TemperatureThermocoupleMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=0.0,
                    temperature_maximum_value_celsius_degrees=100.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_temperature=None,  # cjc_value is None
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )

                configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=channel_parameters,
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
                print(f"parameters = {configuration}")

                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                    cold_junction_compensation_channel="",
                )
                results = measurement.configure_and_measure(configuration=configuration)
                print(f"results = {results}")

            measurement.close()

    def test_integration_temperature_measurement_using_thermocouple_configure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_ONLY
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                cold_junction_compensation_channel="",
            )

            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
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

    def test_integration_temperature_measurement_using_thermocouple_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                cold_junction_compensation_channel="",
            )

            print(
                f"parameters = {nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION}"
            )
            results = measurement.configure_and_measure(
                configuration=nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION
            )

            print(f"results = {results}")
            self.assertIsInstance(results, nipcbatt.TemperatureMeasurementResultData)

    def test_integration_temperature_measurement_using_thermocouple_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
                cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                cold_junction_compensation_channel="",
            )

            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
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

            configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=(
                    nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
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

    def test_integration_temperature_measurement_using_thermocouple_configure_only_and_measure_only_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple.
        TemperatureMeasurementUsingthermocouple with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        channel_expressions = [
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0:3",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai6",
            "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai0,"
            + " NI_PCBA_Measurement_Simulated_TestScale_TS1Mod2/ai15",
        ]
        for channel_expression in channel_expressions:
            with nipcbatt.TemperatureMeasurementUsingThermocouple() as measurement:
                measurement.initialize(
                    channel_expression=channel_expression,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
                    cold_junction_compensation_channel="",
                )

                configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
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

                configuration = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
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
