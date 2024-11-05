"""This module provides DigitalEdgeCountMeasurementUsingSoftwareTimer
   and DigitalEdgeCountMeasurementUsingHardwareTimer Datatypes check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx
import nidaqmx.constants
import numpy as np
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_constants import (
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types import (
    DigitalEdgeCountHardwareTimerConfiguration,
    DigitalEdgeCountMeasurementCounterChannelParameters,
    DigitalEdgeCountMeasurementResultData,
    DigitalEdgeCountMeasurementTimingParameters,
    DigitalEdgeCountSoftwareTimerConfiguration,
)


class TestDynamicDigitalEdgeCountMeasuremntDataTypes(unittest.TestCase):
    """Defines a test fixture that checks
    `DigitalEdgeCountMeasuremntDataTypes` class is ready to use.

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

    def test_digital_edge_count_measurement_counter_channel_parameter_init_fails_when_edge_type_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementCounterChannelParameters.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=None,
                )
            )

        self.assertEqual(
            "The object edge_type is None.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_counter_channel_parameter(self):
        """Tests if the instance of `DigitalEdgeCountMeasurementCounterChannelParameters`
        is created as expected"""
        instance = DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=nidaqmx.constants.Edge.FALLING
        )

        actual_edge_type = instance.edge_type

        self.assertEqual(nidaqmx.constants.Edge.FALLING, actual_edge_type)

    def test_digital_edge_count_measurement_timing_parameter_init_fails_when_edge_counting_duration_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementTimingParameters.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=None,
                )
            )

        self.assertEqual(
            "The object edge_counting_duration is None.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_timing_parameter_init_fails_when_edge_counting_duration_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementTimingParameters.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=-0.01,
                )
            )

        self.assertEqual(
            "The value edge_counting_duration must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_timing_parameter(self):
        """Tests if the instance of `DigitalEdgeCountMeasurementTimingParameters`
        is created as expected"""
        instance = DigitalEdgeCountMeasurementTimingParameters(edge_counting_duration=0.005)

        actual_edge_counting_duration = instance._edge_counting_duration

        self.assertEqual(0.005, actual_edge_counting_duration)

    def test__digital_edge_count_hardware_timer_configuration(self):
        """Tests if the instance of `DigitalEdgeCountHardwareTimerConfiguration`
        is created as expected"""

        # Create test values for the Counter Channel Parameter
        expected_edge_type = nidaqmx.constants.Edge.FALLING

        expected_counter_channel_parameter = DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=expected_edge_type,
        )

        # Create test values for the Timing Parameter
        expected_edge_counting_duration = 0.005

        expected_timing_parameters = DigitalEdgeCountMeasurementTimingParameters(
            edge_counting_duration=expected_edge_counting_duration,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.RISING

        expected_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        # Create test values for measurement options
        expected_measurement_options = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE

        instance = DigitalEdgeCountHardwareTimerConfiguration(
            measurement_options=expected_measurement_options,
            counter_channel_parameters=expected_counter_channel_parameter,
            timing_parameters=expected_timing_parameters,
            trigger_parameters=expected_trigger_parameters,
        )

        # Log the class name with the values of the instance created for
        # DigitalEdgeCountHardwareTimerConfiguration
        logging.debug(
            "%s = %s",
            nameof(DigitalEdgeCountHardwareTimerConfiguration),
            instance,
        )

        self.assertEqual(expected_measurement_options, instance.measurement_options)
        self.assertEqual(expected_counter_channel_parameter, instance.counter_channel_parameters)
        self.assertEqual(expected_timing_parameters, instance.timing_parameters)
        self.assertEqual(expected_trigger_parameters, instance.trigger_parameters)

    def test__digital_edge_count_software_timer_configuration(self):
        """Tests if the instance of `DigitalEdgeCountSoftwareTimerConfiguration`
        is created as expected"""

        # Create test values for the Counter Channel Parameter
        expected_edge_type = nidaqmx.constants.Edge.FALLING

        expected_counter_channel_parameter = DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=expected_edge_type,
        )

        # Create test values for the Timing Parameter
        expected_edge_counting_duration = 0.005

        expected_timing_parameters = DigitalEdgeCountMeasurementTimingParameters(
            edge_counting_duration=expected_edge_counting_duration,
        )

        # Create test values for measurement options
        expected_measurement_options = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE

        instance = DigitalEdgeCountSoftwareTimerConfiguration(
            measurement_options=expected_measurement_options,
            counter_channel_parameters=expected_counter_channel_parameter,
            timing_parameters=expected_timing_parameters,
        )

        # Log the class name with the values of the instance created for
        # DigitalEdgeCountSoftwareTimerConfiguration
        logging.debug(
            "%s = %s",
            nameof(DigitalEdgeCountSoftwareTimerConfiguration),
            instance,
        )

        self.assertEqual(expected_measurement_options, instance.measurement_options)
        self.assertEqual(expected_counter_channel_parameter, instance.counter_channel_parameters)
        self.assertEqual(expected_timing_parameters, instance.timing_parameters)

    def test_digital_edge_count_hardware_timer_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""
        self.assertRaises(
            ValueError,
            lambda: DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=None,
                counter_channel_parameters=DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters=DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                    digital_start_trigger_source="triggersource",
                    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=None,
                timing_parameters=DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                    digital_start_trigger_source="triggersource",
                    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters=None,
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
                    digital_start_trigger_source="triggersource",
                    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: DigitalEdgeCountHardwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters=DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
                trigger_parameters=None,
            ),
        )

    def test_digital_edge_count_software_timer_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""
        self.assertRaises(
            ValueError,
            lambda: DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=None,
                counter_channel_parameters=DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters=DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=None,
                timing_parameters=DigitalEdgeCountMeasurementTimingParameters(
                    edge_counting_duration=0.005,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: DigitalEdgeCountSoftwareTimerConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                counter_channel_parameters=DigitalEdgeCountMeasurementCounterChannelParameters(
                    edge_type=nidaqmx.constants.Edge.FALLING,
                ),
                timing_parameters=None,
            ),
        )

    def test_digital_edge_count_measurement_result_data_init_fails_when_edge_count_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                DigitalEdgeCountMeasurementResultData(
                    edge_count=None,
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )

        self.assertEqual(
            "The object edge_count is None.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_result_data_init_fails_when_edge_count_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                DigitalEdgeCountMeasurementResultData(
                    edge_count=-1,
                    edge_type=nidaqmx.constants.Edge.FALLING,
                )
            )

        self.assertEqual(
            "The value edge_count must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_digital_edge_count_measurement_result_data_init_fails_when_edge_type_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                DigitalEdgeCountMeasurementResultData(
                    edge_count=5,
                    edge_type=None,
                )
            )

        self.assertEqual(
            "The object edge_type is None.",
            str(ctx.exception),
        )
