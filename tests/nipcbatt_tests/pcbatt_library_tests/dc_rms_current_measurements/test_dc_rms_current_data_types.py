"""This module provides DC-RMS current datatypes check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt


class TestDcRmsCurrentMeasurementTerminalRangeParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurementTerminalRangeParameters` class is ready to use.

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

    def test_dc_rms_current_measurement_terminal_range_parameters(self):
        """Tests if an instance of `DcRmsCurrentMeasurementTerminalRangeParameters`
        is created with the specific values.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.RSE
        expexted_range_min_amperes = -0.01
        expecte_range_max_amperes = 0.01
        expected_shunt_resistor_ohms = 0.02

        instance = nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_amperes=expexted_range_min_amperes,
            range_max_amperes=expecte_range_max_amperes,
            shunt_resistor_ohms=expected_shunt_resistor_ohms,
        )
        actual_terminal_configuration = instance.terminal_configuration
        actual_range_min_amperes = instance.range_min_amperes
        actual_range_max_amperes = instance.range_max_amperes
        actual_shunt_resistor_ohms = instance.shunt_resistor_ohms

        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expexted_range_min_amperes, actual_range_min_amperes)
        self.assertEqual(expecte_range_max_amperes, actual_range_max_amperes)
        self.assertEqual(expected_shunt_resistor_ohms, actual_shunt_resistor_ohms)

    def test_dc_rms_current_measurement_terminal_range_invalid_parameters(self):
        """Tests if the instance creation with invalid parameters throws exception as expected"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (285 > 100 characters) (auto-generated noqa)

        # Test if Valus error is raised when range max = min value
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
                range_min_amperes=0.02,
                range_max_amperes=0.02,
                shunt_resistor_ohms=0.001,
            ),
        )

        # Test if value error is raised when Min is greater than Max
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
                range_min_amperes=0.03,
                range_max_amperes=0.02,
                shunt_resistor_ohms=0.001,
            ),
        )

        # Test if value error is raised when shunt_resistor_ohms value is 0
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
                range_min_amperes=0.03,
                range_max_amperes=0.05,
                shunt_resistor_ohms=0.0,
            ),
        )

        # Test if Valus error is raised when terminal_configuration is None
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=None,
                range_min_amperes=0.02,
                range_max_amperes=0.2,
                shunt_resistor_ohms=100.0,
            ),
        )


class TestDcRmsCurrentMeasurementChannelAndTerminalRangeParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` class is ready to use.

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

    def test_dc_rms_curren_measurement_channel_and_terminal_range_parameters(self):
        """Tests if an instance of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`
        is created with the specific values.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_channel_name = "dev1/ai1"
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expexted_range_min_amperes = 0.02
        expecte_range_max_amperes = 0.05
        expected_shunt_resistor_ohms = 0.1

        expected_channel_parameters = nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_amperes=expexted_range_min_amperes,
            range_max_amperes=expecte_range_max_amperes,
            shunt_resistor_ohms=expected_shunt_resistor_ohms,
        )

        instance = nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
            channel_name=expected_channel_name,
            channel_parameters=expected_channel_parameters,
        )

        actual_channel_name = instance.channel_name
        actual_terminal_configuration = instance.channel_parameters.terminal_configuration
        actual_range_min_amperes = instance.channel_parameters.range_min_amperes
        actual_range_max_amperes = instance.channel_parameters.range_max_amperes
        actual_shunt_resistor_ohms = instance.channel_parameters.shunt_resistor_ohms

        self.assertEqual(expected_channel_name, actual_channel_name)
        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expexted_range_min_amperes, actual_range_min_amperes)
        self.assertEqual(expecte_range_max_amperes, actual_range_max_amperes)
        self.assertEqual(expected_shunt_resistor_ohms, actual_shunt_resistor_ohms)

    def test_dc_rms_curren_measurement_channel_and_terminal_range_parameters_with_invalid_channel_name(
        self,
    ):
        """Tests if the expected value or type error is thrown when creating an instance of
        `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` with invalid values
        for channel_name string.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Check if value error is thrown when channel_name string is empty
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                    channel_name="",
                    channel_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                    ),
                )
            )
        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

        # Check if value error is thrown when channel_name string is None
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                    channel_name=None,
                    channel_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS
                    ),
                )
            )
        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_dc_rms_curren_measurement_channel_and_terminal_range_parameters_when_channel_parameters_is_none(
        self,
    ):
        """Tests if the expected value or type error is thrown when creating an instance of
        `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` when channel_parameters is none.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Check if value error is thrown when channel_name string is empty
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                    channel_name="dev1/ch0",
                    channel_parameters=None,
                )
            )
        # Assert
        self.assertEqual(
            "The object channel_parameters is None.",
            str(ctx.exception),
        )


class TestDcRmsCurrentMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurementConfiguration` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        # Create expected values constants for global_channel_parameters
        # of type DcRmsCurrentMeasurementTerminalRangeParameters
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expexted_range_min_amperes = -0.01
        expected_range_max_amperes = 0.01
        expected_shunt_resistor_ohms = 0.02

        expected_specific_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expexted_specific_range_min_amperes = -0.05
        expecte_specific_range_max_amperes = 0.05
        expected_specific_shunt_resistor_ohms = 0.1

        self._expected_global_channel_parameters = (
            nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=expected_terminal_configuration,
                range_min_amperes=expexted_range_min_amperes,
                range_max_amperes=expected_range_max_amperes,
                shunt_resistor_ohms=expected_shunt_resistor_ohms,
            )
        )
        # Log the class name with the values of the instance created for global_channel_parameters.
        logging.debug(
            "%s = %s",
            nameof(self._expected_global_channel_parameters),
            self._expected_global_channel_parameters,
        )

        # Create constants to test the measurement options
        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        self._expected_measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )
        logging.debug(
            "%s = %s",
            nameof(self._expected_measurement_options),
            self._expected_measurement_options,
        )

        # Craete few constants to test the Specific_channel_parameters list
        self._expected_specific_channel_parameters = []
        self._expected_specific_channel_parameters.append(
            nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai0",
                channel_parameters=nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )
        self._expected_specific_channel_parameters.append(
            nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai1",
                channel_parameters=nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )
        self._expected_specific_channel_parameters.append(
            nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai2",
                channel_parameters=nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )

        # Log the class name with the values of the instance created
        # for specific channel parameters.
        logging.debug(
            "%s = %s",
            nameof(self._expected_specific_channel_parameters),
            self._expected_specific_channel_parameters,
        )

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        self._expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )
        # Log the class name with the values of the instance
        # created for _expected_sample_clock_timing_parameters
        logging.debug(
            "%s = %s",
            nameof(self._expected_sample_clock_timing_parameters),
            self._expected_sample_clock_timing_parameters,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        self._expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )
        logging.debug(
            "%s = %s",
            nameof(self._expected_digital_start_trigger_parameters),
            self._expected_digital_start_trigger_parameters,
        )

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

    def test_dc_rms_current_measurement_configuration(self):
        """Tests if an instance of `DcRmsCurrentMeasurementConfiguration`
        is created with the specific values.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Create expected values constants for global_channel_parameters
        # of type DcRmsCurrentMeasurementTerminalRangeParameters
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expexted_range_min_amperes = -0.01
        expected_range_max_amperes = 0.01
        expected_shunt_resistor_ohms = 0.02

        expected_specific_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expexted_specific_range_min_amperes = -0.05
        expecte_specific_range_max_amperes = 0.05
        expected_specific_shunt_resistor_ohms = 0.1

        expected_global_channel_parameters = (
            nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                terminal_configuration=expected_terminal_configuration,
                range_min_amperes=expexted_range_min_amperes,
                range_max_amperes=expected_range_max_amperes,
                shunt_resistor_ohms=expected_shunt_resistor_ohms,
            )
        )

        # Create constants to test the measurement options
        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        expected_measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        # Craete few constants to test the Specific_channel_parameters list
        expected_specific_channel_parameters = []
        expected_specific_channel_parameters.append(
            nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai0",
                channel_parameters=nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )
        expected_specific_channel_parameters.append(
            nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai1",
                channel_parameters=nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )
        expected_specific_channel_parameters.append(
            nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev0/ai2",
                channel_parameters=nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_amperes=expexted_specific_range_min_amperes,
                    range_max_amperes=expecte_specific_range_max_amperes,
                    shunt_resistor_ohms=expected_specific_shunt_resistor_ohms,
                ),
            )
        )

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        # Create test values for digital trigger parameters
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        # Log the class name with the values of the instance created
        # for specific channel parameters.
        logging.debug(
            "%s = %s",
            nameof(expected_specific_channel_parameters),
            expected_specific_channel_parameters,
        )

        dc_rms_current_configuration_instance = nipcbatt.DcRmsCurrentMeasurementConfiguration(
            global_channel_parameters=expected_global_channel_parameters,
            specific_channels_parameters=expected_specific_channel_parameters,
            measurement_options=expected_measurement_options,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        # Log the class name with the values of the instance
        # created for DcRMSCurentMeasurementConfiguration
        logging.debug(
            "%s = %s",
            nameof(dc_rms_current_configuration_instance),
            dc_rms_current_configuration_instance,
        )

        # Check if all the elements in specific channel parameters list are as expected.
        self.assertListEqual(
            expected_specific_channel_parameters,
            dc_rms_current_configuration_instance.specific_channels_parameters,
        )

        # Get the actual parameters from the instance created
        actual_global_parameters = dc_rms_current_configuration_instance.global_channel_parameters

        actual_measurement_options = dc_rms_current_configuration_instance.measurement_options

        actual_sample_clock_timing_parameters = (
            dc_rms_current_configuration_instance.sample_clock_timing_parameters
        )

        # Test if all the actual parameters of the instance are as expected
        self.assertEqual(expected_global_channel_parameters, actual_global_parameters)

        self.assertEqual(expected_measurement_options, actual_measurement_options)
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            actual_sample_clock_timing_parameters,
        )

    def test_dc_rms_current_measurement_configuration_with_invalid_values_for_specific_channel_parameters(
        self,
    ):
        """Test if expected error is thrown when creating an instance
        of `DcRmsCurrentMeasurementConfiguration`
        with invalid values for specific_channel_parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=None,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

        self._expected_specific_channel_parameters.append("invalid channel parameter")

        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual(
            "Not all elements of the list are of the type (DcRmsCurrentMeasurementChannelAndTerminalRangeParameters).",
            str(ctx.exception),
        )

    def test_dc_rms_current_measurement_configuration_when_global_channel_parameters_is_none(
        self,
    ):
        """Test if expected error is thrown when creating an instance
        of `DcRmsCurrentMeasurementConfiguration`
        with global_channel_parameters is set to None"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (426 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_dc_rms_current_measurement_configuration_when_measurement_options_is_none(
        self,
    ):
        """Test if expected error is thrown
        when creating an instance of `DcRmsCurrentMeasurementConfiguration`
        when measurement_options is None"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (413 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=None,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual("The object measurement_options is None.", str(ctx.exception))

    def test_dc_rms_current_measurement_configuration_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """Test if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementConfiguration`
        when sample_clock_timing_parameters is None"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (424 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        self._expected_digital_start_trigger_parameters
                    ),
                )
            )
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_dc_rms_current_measurement_configuration_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """Test if expected error is thrown
        when creating an instance of `DcRmsCurrentMeasurementConfiguration`
        when digital_start_trigger_parameters is None"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (426 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementConfiguration(
                    global_channel_parameters=self._expected_global_channel_parameters,
                    specific_channels_parameters=self._expected_specific_channel_parameters,
                    measurement_options=self._expected_measurement_options,
                    sample_clock_timing_parameters=self._expected_sample_clock_timing_parameters,
                    digital_start_trigger_parameters=None,
                )
            )
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))


class TestDcRmsCurrentMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsCurrentMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        self._expected_waveforms = []
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai1",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai2",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )

        self._expected_acquisition_duration_seconds = 0.25

        self._expected_dc_values_amperes = [0.12, 0.012, 0.12]
        self._expected_rms_values_amperes = [0.15, 0.14, 0.15]

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

    def test_dc_rms_current_measurement_result_data(self):
        """Tests if an instance of `DcRmsCurrentMeasurementResultData`
        is created with the specific values.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        instance = nipcbatt.DcRmsCurrentMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
            dc_values_amperes=self._expected_dc_values_amperes,
            rms_values_amperes=self._expected_rms_values_amperes,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_waveforms = instance.waveforms
        actual_acquisition_duration_seconds = instance.acquisition_duration_seconds
        actual_dc_values_amperes = instance.dc_values_amperes
        actual_rms_values_amperes = instance.rms_values_amperes

        self.assertListEqual(self._expected_waveforms, actual_waveforms)
        self.assertEqual(
            self._expected_acquisition_duration_seconds,
            actual_acquisition_duration_seconds,
        )
        self.assertListEqual(self._expected_dc_values_amperes, actual_dc_values_amperes)
        self.assertListEqual(self._expected_rms_values_amperes, actual_rms_values_amperes)

    def test_dc_rms_current_measurement_result_data_when_waveforms_is_none(self):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` with waveform as none.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementResultData(
                    waveforms=None,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_dc_rms_current_measurement_result_data_when_waveforms_has_item_not_of_type_analogwaveform(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when waveform has an item
        that is not of type `AnalogWaveform`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_waveforms.append([0.5, 1.2])

        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_dc_rms_current_measurement_result_data_when_dc_values_amperes_has_item_not_of_type_float(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when dc_values_amperes
        has an item that is not of type float.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_dc_values_amperes.append("two")

        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_dc_rms_current_measurement_result_data_when_rms_values_amperes_has_item_not_of_type_float(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when rms_values_amperes
        has an item that is not of type float.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_rms_values_amperes.append([1.0])

        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )
        # "The iterables ({} and {}) do not have same size."

    def test_dc_rms_current_measurement_result_data_when_waveforms_and_rms_values_amperes_have_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when waveforms list and
        rms_values_amperes have list have different lengths
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_rms_values_amperes.append(1.0)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual(
            "The iterables (waveforms and rms_values_amperes) do not have same size.",
            str(ctx.exception),
        )

    def test_dc_rms_current_measurement_result_data_when_waveforms_and_dc_values_amperes_have_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating an instance of
        `DcRmsCurrentMeasurementResultData` when waveforms list and
        dc_values_amperes have list have different lengths
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._expected_dc_values_amperes.append(1.0)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsCurrentMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=self._expected_acquisition_duration_seconds,
                    dc_values_amperes=self._expected_dc_values_amperes,
                    rms_values_amperes=self._expected_rms_values_amperes,
                )
            )
        self.assertEqual(
            "The iterables (waveforms and dc_values_amperes) do not have same size.",
            str(ctx.exception),
        )


if __name__ == "__main__":
    unittest.main()
