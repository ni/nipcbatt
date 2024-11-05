"""This module provides Dynamic digital pattern data types check."""

import importlib.metadata
import logging
import sys
import unittest

import numpy as np
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternMeasurementConfiguration,
    DynamicDigitalPatternMeasurementResultData,
)


class TestDynamicDigitalPatternMeasurementDataTypes(unittest.TestCase):
    """Defines a test fixture that checks
    `DynamicDigitalPatternMeasurementDataTypes` class is ready to use.

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

    def test_dynamic_digital_pattern_measurement_configuration(self):
        """Tests if the instance of `DynamicDigitalPatternMeasurementConfiguration`
        is created as expected"""

        # Create test values for the Timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000.0
        expected_number_of_samples_per_channel = 1000
        expected_active_edge = ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE

        expected_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            active_edge=expected_active_edge,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = (
            ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE
        )

        expected_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        # Create test values for measurement options
        expected_measurement_options = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE

        instance = DynamicDigitalPatternMeasurementConfiguration(
            measurement_options=expected_measurement_options,
            timing_parameters=expected_timing_parameters,
            trigger_parameters=expected_trigger_parameters,
        )

        # Log the class name with the values of the instance created for
        # SignalVoltageGenerationSineWaveConfiguration
        logging.debug(
            "%s = %s",
            nameof(DynamicDigitalPatternMeasurementConfiguration),
            instance,
        )

        self.assertEqual(
            expected_measurement_options,
            instance.measurement_options,
        )
        self.assertEqual(expected_trigger_parameters, instance.trigger_parameters)
        self.assertEqual(expected_timing_parameters, instance.timing_parameters)

    def test_dynamic_digital_pattern_measurement_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""
        self.assertRaises(
            ValueError,
            lambda: DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=None,
                timing_parameters=nipcbatt.DynamicDigitalPatternTimingParameters(
                    sample_clock_source=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
                    sampling_rate_hertz=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
                    number_of_samples_per_channel=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
                    active_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
                ),
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                    digital_start_trigger_source=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
                    digital_start_trigger_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                timing_parameters=None,
                trigger_parameters=nipcbatt.DigitalStartTriggerParameters(
                    trigger_select=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                    digital_start_trigger_source=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
                    digital_start_trigger_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
                ),
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                timing_parameters=nipcbatt.DynamicDigitalPatternTimingParameters(
                    sample_clock_source=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
                    sampling_rate_hertz=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
                    number_of_samples_per_channel=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
                    active_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
                ),
                trigger_parameters=None,
            ),
        )

    def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_waveforms_is_none(
        self,
    ):
        """unit test of DynamicDigitalPatternMeasurementResultData."""
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                DynamicDigitalPatternMeasurementResultData(
                    waveforms=None, daq_digital_waveform_from_port=[[1, 2, 3], [4, 5, 6]]
                )
            )

        # Assert
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_waveforms_is_empty(
        self,
    ):
        """unit test of DynamicDigitalPatternMeasurementResultData."""
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                DynamicDigitalPatternMeasurementResultData(
                    waveforms=[], daq_digital_waveform_from_port=[[1, 2, 3], [4, 5, 6]]
                )
            )

        # Assert
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

    def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_daq_digital_waveform_from_port_is_none(
        self,
    ):
        """unit test of DynamicDigitalPatternMeasurementResultData."""
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                DynamicDigitalPatternMeasurementResultData(
                    daq_digital_waveform_from_port=None,
                    waveforms=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]],
                )
            )

        # Assert
        self.assertEqual("The object daq_digital_waveform_from_port is None.", str(ctx.exception))

    def test_dynamic_digital_pattern_measurement_result_data_init_fails_when_daq_digital_waveform_from_port_is_empty(
        self,
    ):
        """unit test of DynamicDigitalPatternMeasurementResultData."""
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                DynamicDigitalPatternMeasurementResultData(
                    daq_digital_waveform_from_port=[], waveforms=[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
                )
            )

        # Assert
        self.assertEqual(
            "The iterable daq_digital_waveform_from_port of type list is empty.", str(ctx.exception)
        )
