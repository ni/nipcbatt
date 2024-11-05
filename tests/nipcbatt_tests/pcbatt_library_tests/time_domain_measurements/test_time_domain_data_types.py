# pylint: disable=C0301
"""This module provides time domain data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt


class TestTimeDomainMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `TimeDomainMeasurementConfiguration` class is ready to use.

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

    def test_time_domain_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
                    digital_start_trigger_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
                    specific_channels_parameters=None,
                    measurement_options=nipcbatt.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
                    digital_start_trigger_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration_init_fails_when_measurement_options_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
                    specific_channels_parameters=[],
                    measurement_options=None,
                    sample_clock_timing_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
                    digital_start_trigger_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
                )
            )

        # Assert
        self.assertEqual("The object measurement_options is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementConfiguration(
                    global_channel_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=nipcbatt.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_time_domain_measurement_configuration(self):
        """unit test of TimeDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expected_range_min_volts = -9.0
        expected_range_max_volts = 6.3
        expected_specific_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expected_specific_range_min_volts = -5.0
        expected_specific_range_max_volts = 7.5

        global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        specific_channels_parameters = []
        specific_channels_parameters.append(
            nipcbatt.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai0",
                channel_parameters=nipcbatt.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )
        specific_channels_parameters.append(
            nipcbatt.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai1",
                channel_parameters=nipcbatt.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )
        specific_channels_parameters.append(
            nipcbatt.VoltageMeasurementChannelAndTerminalRangeParameters(
                channel_name="Dev/ai2",
                channel_parameters=nipcbatt.VoltageRangeAndTerminalParameters(
                    terminal_configuration=expected_specific_terminal_configuration,
                    range_min_volts=expected_specific_range_min_volts,
                    range_max_volts=expected_specific_range_max_volts,
                ),
            )
        )

        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        logging.debug(
            "%s = %s",
            nameof(specific_channels_parameters),
            specific_channels_parameters,
        )

        # Act
        dc_rms_configuration_instance = nipcbatt.TimeDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=specific_channels_parameters,
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        logging.debug(
            "%s = %s",
            nameof(dc_rms_configuration_instance),
            dc_rms_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            specific_channels_parameters,
            dc_rms_configuration_instance.specific_channels_parameters,
        )

        actual_terminal_configuration = (
            dc_rms_configuration_instance.global_channel_parameters.terminal_configuration
        )
        actual_range_min_volts = (
            dc_rms_configuration_instance.global_channel_parameters.range_min_volts
        )
        actual_range_max_volts = (
            dc_rms_configuration_instance.global_channel_parameters.range_max_volts
        )

        actual_execution_option = dc_rms_configuration_instance.measurement_options.execution_option
        actual_measurement_analysis_requirement = (
            dc_rms_configuration_instance.measurement_options.measurement_analysis_requirement
        )
        actual_sample_clock_source = (
            dc_rms_configuration_instance.sample_clock_timing_parameters.sample_clock_source
        )
        actual_sampling_rate_hertz = (
            dc_rms_configuration_instance.sample_clock_timing_parameters.sampling_rate_hertz
        )
        actual_number_of_samples_per_channel = (
            dc_rms_configuration_instance.sample_clock_timing_parameters.number_of_samples_per_channel
        )
        actual_sample_timing_engine = (
            dc_rms_configuration_instance.sample_clock_timing_parameters.sample_timing_engine
        )

        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expected_range_min_volts, actual_range_min_volts)
        self.assertEqual(expected_range_max_volts, actual_range_max_volts)

        self.assertEqual(expected_execution_option, actual_execution_option)
        self.assertEqual(
            expected_measurement_analysis_requirement,
            actual_measurement_analysis_requirement,
        )
        self.assertEqual(expected_sample_clock_source, actual_sample_clock_source)
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate_hertz)
        self.assertEqual(
            expected_number_of_samples_per_channel, actual_number_of_samples_per_channel
        )
        self.assertEqual(
            expected_sample_timing_engine,
            actual_sample_timing_engine,
        )


class TestTimeDomainMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `TimeDomainMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        methodName: str = "runTest",  # noqa: N803 - argument name 'methodName' should be lowercase (auto-generated noqa)
    ) -> None:
        super().__init__(methodName)
        self._expected_waveforms = None

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

    def test_time_domain_measurement_result_data_init_fails_when_waveforms_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=None,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_time_domain_measurement_result_data_init_fails_when_waveforms_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=[],
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

    def test_time_domain_measurement_result_data_init_fails_when_waveforms_contains_object_that_are_not_of_analog_waveform(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=[2.0],
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_mean_dc_voltage_values_volts_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (238 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=None,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual("The object mean_dc_voltage_values_volts is None.", str(ctx.exception))

    def test_time_domain_measurement_result_data_init_fails_when_mean_dc_voltage_values_volts_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=[],
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "The iterable mean_dc_voltage_values_volts of type list is empty.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_mean_dc_voltage_values_volts_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=["1.0", 1.0, 1.0],
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_vpp_amplitudes_volts_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=None,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual("The object vpp_amplitudes_volts is None.", str(ctx.exception))

    def test_time_domain_measurement_result_data_init_fails_when_vpp_amplitudes_volts_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=[],
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "The iterable vpp_amplitudes_volts of type list is empty.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_vpp_amplitudes_volts_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=["1.0", 1.0, 1.0],
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_frequencies_hertz_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=None,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "The object voltage_waveforms_frequencies_hertz is None.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_does_not_fail_when_voltage_waveforms_frequencies_hertz_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        time_domain_result = nipcbatt.TimeDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=[],
            voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
            voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
        )

        # Assert
        self.assertIsNotNone(time_domain_result.voltage_waveforms_periods_seconds)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_frequencies_hertz)
        self.assertFalse(time_domain_result.voltage_waveforms_frequencies_hertz)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_duty_cycles_percent)

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_frequencies_hertz_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=[1.0, "1.0", 1.0],
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_periods_seconds_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=None,
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "The object voltage_waveforms_periods_seconds is None.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_does_not_fail_when_voltage_waveforms_periods_seconds_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        time_domain_result = nipcbatt.TimeDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
            voltage_waveforms_periods_seconds=[],
            voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
        )

        # Assert
        self.assertIsNotNone(time_domain_result.voltage_waveforms_periods_seconds)
        self.assertFalse(time_domain_result.voltage_waveforms_periods_seconds)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_frequencies_hertz)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_duty_cycles_percent)

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_periods_seconds_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=[0.01, 0.01, "0.01"],
                    voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_duty_cycles_percent_is_none(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=None,
                )
            )

        # Assert
        self.assertEqual(
            "The object voltage_waveforms_duty_cycles_percent is None.",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data_init_does_not_fail_when_voltage_waveforms_duty_cycles_percent_is_empty(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]

        # Act
        time_domain_result = nipcbatt.TimeDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
            voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
            voltage_waveforms_duty_cycles_percent=[],
        )

        # Assert
        self.assertIsNotNone(time_domain_result.voltage_waveforms_periods_seconds)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_frequencies_hertz)
        self.assertIsNotNone(time_domain_result.voltage_waveforms_duty_cycles_percent)
        self.assertFalse(time_domain_result.voltage_waveforms_duty_cycles_percent)

    def test_time_domain_measurement_result_data_init_fails_when_voltage_waveforms_duty_cycles_percent_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.TimeDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
                    vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
                    voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
                    voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
                    voltage_waveforms_duty_cycles_percent=[0.5, "0.5", 0.5],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_time_domain_measurement_result_data(self):
        """unit test of TestTimeDomainMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3

        expected_mean_dc_voltage_values_volts = [1.0, 1.0, 1.0]
        expected_vpp_amplitudes_volts = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_frequencies_hertz = [1.0, 1.0, 1.0]
        expected_voltage_waveforms_periods_seconds = [0.01, 0.01, 0.01]
        expected_voltage_waveforms_duty_cycles_percent = [0.5, 0.5, 0.5]
        instance = nipcbatt.TimeDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            mean_dc_voltage_values_volts=expected_mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=expected_vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=expected_voltage_waveforms_frequencies_hertz,
            voltage_waveforms_periods_seconds=expected_voltage_waveforms_periods_seconds,
            voltage_waveforms_duty_cycles_percent=expected_voltage_waveforms_duty_cycles_percent,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_waveforms = instance.waveforms
        actual_acquisition_duration_seconds = instance.acquisition_duration_seconds
        actual_mean_dc_voltage_values_volts = instance.mean_dc_voltage_values_volts
        actual_vpp_amplitudes_volts = instance.vpp_amplitudes_volts
        actual_voltage_waveforms_frequencies_hertz = instance.voltage_waveforms_frequencies_hertz
        actual_voltage_waveforms_periods_seconds = instance.voltage_waveforms_periods_seconds
        actual_voltage_waveforms_duty_cycles_percent = (
            instance.voltage_waveforms_duty_cycles_percent
        )

        self.assertListEqual(self._expected_waveforms, actual_waveforms)
        self.assertEqual(expected_acquisition_duration_seconds, actual_acquisition_duration_seconds)
        self.assertListEqual(
            expected_mean_dc_voltage_values_volts, actual_mean_dc_voltage_values_volts
        )
        self.assertListEqual(expected_vpp_amplitudes_volts, actual_vpp_amplitudes_volts)
        self.assertListEqual(
            expected_voltage_waveforms_frequencies_hertz,
            actual_voltage_waveforms_frequencies_hertz,
        )
        self.assertListEqual(
            expected_voltage_waveforms_periods_seconds,
            actual_voltage_waveforms_periods_seconds,
        )
        self.assertListEqual(
            expected_voltage_waveforms_duty_cycles_percent,
            actual_voltage_waveforms_duty_cycles_percent,
        )

    def _initialize_waveforms(self):
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


if __name__ == "__main__":
    unittest.main()
