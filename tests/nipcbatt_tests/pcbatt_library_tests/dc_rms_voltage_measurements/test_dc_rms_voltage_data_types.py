"""This module provides DC-RMS voltage datatypes check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt


class TestDcRmsVoltageMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsVoltageMeasurementConfiguration` class is ready to use.

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

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_options=nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_specific_channels_parameters_contains_invalid_objects(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[1.2, "4"],
                    measurement_options=nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (VoltageMeasurementChannelAndTerminalRangeParameters).",
            str(ctx.exception),
        )

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_measurement_options_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=None,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object measurement_options is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_configuration(self):
        """unit test of DcRmsVoltageMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expected_range_min_volts = -9.0
        expected_range_max_volts = 6.3
        expected_specific_terminal_configuration = nidaqmx.constants.TerminalConfiguration.DIFF
        expected_specific_range_min_volts = -5.0
        expected_specific_range_max_volts = 7.5

        expected_global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        expected_measurement_options = nipcbatt.MeasurementOptions(
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

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
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

        dc_rms_configuration_instance = nipcbatt.DcRmsVoltageMeasurementConfiguration(
            global_channel_parameters=expected_global_channel_parameters,
            specific_channels_parameters=specific_channels_parameters,
            measurement_options=expected_measurement_options,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        logging.debug(
            "%s = %s",
            nameof(dc_rms_configuration_instance),
            dc_rms_configuration_instance,
        )

        self.assertListEqual(
            specific_channels_parameters,
            dc_rms_configuration_instance.specific_channels_parameters,
        )

        actual_global_channel_parameters = dc_rms_configuration_instance.global_channel_parameters
        actual_measurement_options = dc_rms_configuration_instance.measurement_options
        actual_sample_clock_timing_parameters = (
            dc_rms_configuration_instance.sample_clock_timing_parameters
        )

        self.assertEqual(expected_global_channel_parameters, actual_global_channel_parameters)
        self.assertEqual(expected_measurement_options, actual_measurement_options)
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            actual_sample_clock_timing_parameters,
        )


class TestDcRmsVoltageMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `DcRmsVoltageMeasurementResultData` class is ready to use.

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

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_waveforms_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementResultData(
                    waveforms=None,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_waveforms_is_empty(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementResultData(
                    waveforms=[],
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_waveforms_contains_invalid_objects(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementResultData(
                    waveforms=[0.0, "2"],
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_dc_values_volts_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=None,
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual("The object dc_values_volts is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_dc_values_volts_is_empty(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual("The iterable dc_values_volts of type list is empty.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_dc_values_volts_contains_invalid_objects(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=["0.0", 2.0],
                    rms_values_volts=[0.0],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_rms_values_volts_is_none(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=None,
                )
            )

        # Assert
        self.assertEqual("The object rms_values_volts is None.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_rms_values_volts_is_empty(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=[],
                )
            )

        # Assert
        self.assertEqual("The iterable rms_values_volts of type list is empty.", str(ctx.exception))

    def test_dc_rms_voltage_measurement_result_data_init_fails_when_rms_values_volts_contains_invalid_objects(
        self,
    ):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_waveforms = [
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        ]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.DcRmsVoltageMeasurementResultData(
                    waveforms=expected_waveforms,
                    acquisition_duration_seconds=0.0,
                    dc_values_volts=[0.0],
                    rms_values_volts=["0.0", 2.0],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_dc_rms_voltage_measurement_result_data(self):
        """unit test of DcRmsVoltageMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)
        expected_waveforms = []
        expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.ones(shape=(1000), dtype=numpy.float64),
            )
        )
        expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai1",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )
        expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai2",
                delta_time_seconds=1.0 / 10000,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 1000)],
                    dtype=numpy.float64,
                ),
            )
        )

        expected_acquisition_duration_seconds = 0.3

        expected_dc_values_volts = [1.0, 1.0, 1.0]
        expected_rms_values_volts = [2.0, 2.0, 0.0]
        instance = nipcbatt.DcRmsVoltageMeasurementResultData(
            waveforms=expected_waveforms,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
            dc_values_volts=expected_dc_values_volts,
            rms_values_volts=expected_rms_values_volts,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_waveforms = instance.waveforms
        actual_acquisition_duration_seconds = instance.acquisition_duration_seconds
        actual_dc_values_volts = instance.dc_values_volts
        actual_rms_values_volts = instance.rms_values_volts

        self.assertListEqual(expected_waveforms, actual_waveforms)
        self.assertEqual(expected_acquisition_duration_seconds, actual_acquisition_duration_seconds)
        self.assertListEqual(expected_dc_values_volts, actual_dc_values_volts)
        self.assertListEqual(expected_rms_values_volts, actual_rms_values_volts)


if __name__ == "__main__":
    unittest.main()
