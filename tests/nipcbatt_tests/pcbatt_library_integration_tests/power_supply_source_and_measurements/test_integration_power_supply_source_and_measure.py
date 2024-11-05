"""This module provides test of integration of PowerSupplySourceAndMeasure check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterPowerSupplySourceAndMeasure,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)


class TestIntegrationPowerSupplySourceAndMeasureMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `PowerSupplySourceAndMeasure` class.

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
        _replace_daqmx_if_not_installed(_InterpreterPowerSupplySourceAndMeasure)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_power_supply_and_source_measurement_configure_only(self):
        """Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
         with MeasurementExecutionType.CONFIGURE_ONLY"""

        with nipcbatt.PowerSupplySourceAndMeasure() as measurement:
            measurement.initialize(
                power_channel_name="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod5/power"
            )

            configuration = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

            measurement.close()

    def test_integration_power_supply_and_source_measurement_configure_only_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
         with MeasurementExecutionType.CONFIGURE_ONLY and MeasurementExecutionType.MEASURE_ONLY
        """

        with nipcbatt.PowerSupplySourceAndMeasure() as measurement:
            measurement.initialize(
                power_channel_name="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod5/power"
            )

            configuration = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(f"results = {results}")
            self.assertIs(None, results)

            configuration = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.PowerSupplySourceAndMeasureResultData)

            measurement.close()

    def test_integration_power_supply_and_source_measurement_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
         with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """

        with nipcbatt.PowerSupplySourceAndMeasure() as measurement:
            measurement.initialize(
                power_channel_name="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod5/power"
            )

            configuration = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            print(f"parameters = {configuration}")
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.SKIP_ANALYSIS, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
                terminal_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                ),
                measurement_options=nipcbatt.MeasurementOptions(
                    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    measurement_analysis_requirement=(
                        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
                    ),
                ),
                sample_clock_timing_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                ),
                digital_start_trigger_parameters=(
                    nipcbatt.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                ),
            )

            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.PowerSupplySourceAndMeasureResultData)

            measurement.close()

    def test_integration_power_supply_and_source_measurement_full_sequence_in_loop(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure.PowerSupplySourceAndMeasure
        for initialize, configure and measure and close to be called in loop with the same context.
        """
        for _ in range(3):
            with nipcbatt.PowerSupplySourceAndMeasure() as measurement:
                measurement.initialize(
                    power_channel_name="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod5/power"
                )

                configuration = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
                    terminal_parameters=(
                        nipcbatt.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS
                    ),
                    measurement_options=nipcbatt.DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )

                results = measurement.configure_and_measure(configuration=configuration)

                print(
                    f"after configuration with MeasurementExecutionType.CONFIGURE_AND_MEASURE and MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS, results = {results}"
                )
                self.assertIsInstance(results, nipcbatt.PowerSupplySourceAndMeasureResultData)

                measurement.close()


if __name__ == "__main__":
    unittest.main()
