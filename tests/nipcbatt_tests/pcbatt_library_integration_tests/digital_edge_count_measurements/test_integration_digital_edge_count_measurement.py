"""This module provides test of integration of DigitalEdgeCountMeasurementUsingSoftwareTimer
   and DigitalEdgeCountMeasurementUsingHardwareTimer."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx
import nidaqmx.constants
from varname import nameof

import nipcbatt


class TestIntegrationDigitalEdgeCountMeasurement(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `DigitalEdgeCountMeasurementUsingHardwareTimer` and
    'DigitalEdgeCountMeasurementUsingSoftwareTimer' classes.

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

    # Hardware timer
    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_channel_expression_empty(
        self,
    ):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="",
                    measurement_input_terminal_name="/TS1_Core/PFI6",
                    timer_channel_expression="TS1_Core/ctr2",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression=None,
                    measurement_input_terminal_name="/TS1_Core/PFI6",
                    timer_channel_expression="TS1_Core/ctr2",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_input_terminal_empty(
        self,
    ):
        """Integration test ensuring that if measurement_input_terminal_name is empty then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS1_Core/ctr1",
                    measurement_input_terminal_name="",
                    timer_channel_expression="TS1_Core/ctr2",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_input_terminal_is_none(
        self,
    ):
        """Integration test ensuring that if measurement_input_terminal_name is None then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS1_Core/ctr1",
                    measurement_input_terminal_name=None,
                    timer_channel_expression="TS1_Core/ctr2",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_timer_channel_expression_empty(
        self,
    ):
        """Integration test ensuring that if timer channel expression is empty then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS1_Core/ctr1",
                    measurement_input_terminal_name="/TS1_Core/PFI6",
                    timer_channel_expression="",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_timer_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS1_Core/ctr1",
                    measurement_input_terminal_name="/TS1_Core/PFI6",
                    timer_channel_expression=None,
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_configure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_hardware_timer.
        DigitalEdgeCountMeasurementUsingHardwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        """

        with nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS1_Core/ctr0",
                measurement_input_terminal_name="/TS1_Core/PFI0",
                timer_channel_expression="TS1_Core/ctr2",
            )

            counter_channel_parameters = (
                nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                digital_start_trigger_source="/TS1_Core/PFI6",
                digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
            )
            configuration = nipcbatt.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_hardware_timer.
        DigitalEdgeCountMeasurementUsingHardwareTimer with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """

        with nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS1_Core/ctr1",
                measurement_input_terminal_name="/TS1_Core/PFI6",
                timer_channel_expression="TS1_Core/ctr2",
            )

            counter_channel_parameters = (
                nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
            )
            configuration = nipcbatt.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIsInstance(results, nipcbatt.DigitalEdgeCountMeasurementResultData)

    def test_integration_test_digital_edge_count_measurement_using_hardware_timer_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_hardware_timer.
        DigitalEdgeCountMeasurementUsingHardwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS1_Core/ctr1",
                measurement_input_terminal_name="/TS1_Core/PFI6",
                timer_channel_expression="TS1_Core/ctr2",
            )

            counter_channel_parameters = (
                nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
            )
            configuration = nipcbatt.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.DigitalEdgeCountMeasurementResultData)

    # Software timer
    def test_integration_test_digital_edge_count_measurement_using_software_timer_channel_expression_empty(
        self,
    ):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="",
                    measurement_input_terminal_name="/TS3_Core/PFI6",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_software_timer_channel_expression_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression=None,
                    measurement_input_terminal_name="/TS3_Core/PFI6",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_software_timer_input_terminal_empty(
        self,
    ):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS3_Core/ctr1",
                    measurement_input_terminal_name="",
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_software_timer_input_terminal_is_none(
        self,
    ):
        """Integration test ensuring that if channel expression is None then
        initialize() catches the error"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(
                    measurement_channel_expression="TS3_Core/ctr1",
                    measurement_input_terminal_name=None,
                )

            measurement.close()

    def test_integration_test_digital_edge_count_measurement_using_software_timer_configure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_software_timer.
        DigitalEdgeCountMeasurementUsingSoftwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        """

        with nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS3_Core/ctr1",
                measurement_input_terminal_name="/TS3_Core/PFI6",
            )

            counter_channel_parameters = (
                nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            configuration = nipcbatt.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
            )
            results = measurement.configure_and_measure(
                configuration=configuration,
            )
            measurement.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_test_digital_edge_count_measurement_using_software_timer_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_software_timer.
        DigitalEdgeCountMeasurementUsingSoftwareTimer with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """

        with nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS3_Core/ctr1",
                measurement_input_terminal_name="/TS3_Core/PFI6",
            )

            counter_channel_parameters = (
                nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            configuration = nipcbatt.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIsInstance(results, nipcbatt.DigitalEdgeCountMeasurementResultData)

    def test_integration_test_digital_edge_count_measurement_using_software_timer_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.digital_edge_count_measurements.test_digital_edge_count_measurement_using_software_timer.
        DigitalEdgeCountMeasurementUsingSoftwareTimer with MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""

        with nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer() as measurement:
            measurement.initialize(
                measurement_channel_expression="TS3_Core/ctr1",
                measurement_input_terminal_name="/TS3_Core/PFI6",
            )
            counter_channel_parameters = (
                nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )
            timing_parameters = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(
                edge_counting_duration=0.005,
            )
            configuration = nipcbatt.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                counter_channel_parameters=counter_channel_parameters,
                timing_parameters=timing_parameters,
            )
            results = measurement.configure_and_measure(configuration=configuration)
            measurement.close()

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, nipcbatt.DigitalEdgeCountMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
