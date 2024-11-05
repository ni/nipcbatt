# pylint: disable=C0301
"""This module provides temperature data types check."""
import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt


class TestTemperatureRtdMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureRtdMeasurementConfiguration` class is ready to use.

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

    def test_temperature_rtd_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_temperature_rtd_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_temperature_rtd_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_temperature_rtd_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureRtdMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_temperature_rtd_measurement_configuration(self):
        """unit test of TemperatureRtdMeasurementConfiguration."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (241 > 100 characters) (auto-generated noqa)

        # Arrange

        expected_global_channel_parameters = nipcbatt.TemperatureRtdMeasurementTerminalParameters(
            temperature_minimum_value_celsius_degrees=1.0,
            temperature_maximum_value_celsius_degrees=99.0,
            current_excitation_value_amperes=1.0,
            sensor_resistance_ohms=10.0,
            rtd_type=nidaqmx.constants.RTDType.PT_3916,
            excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
            resistance_configuration=nidaqmx.constants.ResistanceConfiguration.TWO_WIRE,
            adc_timing_mode=nidaqmx.constants.ADCTimingMode.BEST_60_HZ_REJECTION,
        )

        expected_specific_channels_parameters = []
        expected_specific_channels_parameters.append(
            nipcbatt.TemperatureRtdMeasurementChannelParameters(
                channel_name="Dev/ai0",
                sensor_resistance_ohms=8.0,
                current_excitation_value_amperes=2.0,
                rtd_type=nidaqmx.constants.RTDType.PT_3851,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                excitation_source=nidaqmx.constants.ExcitationSource.NONE,
            ),
        )

        expected_specific_channels_parameters.append(
            nipcbatt.TemperatureRtdMeasurementChannelParameters(
                channel_name="Dev/ai1",
                sensor_resistance_ohms=11.0,
                current_excitation_value_amperes=3.0,
                rtd_type=nidaqmx.constants.RTDType.PT_3928,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.THREE_WIRE,
                excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
            ),
        )
        expected_specific_channels_parameters.append(
            nipcbatt.TemperatureRtdMeasurementChannelParameters(
                channel_name="Dev/ai2",
                sensor_resistance_ohms=7.0,
                current_excitation_value_amperes=6.0,
                rtd_type=nidaqmx.constants.RTDType.PT_3911,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.TWO_WIRE,
                excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
            ),
        )

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100,
            number_of_samples_per_channel=10,
            sample_timing_engine=nipcbatt.SampleTimingEngine.TE0,
        )

        expected_measurement_execution_type = nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
            digital_start_trigger_source="trigger_source",
            digital_start_trigger_edge=nidaqmx.constants.Edge.FALLING,
        )

        logging.debug(
            "%s = %s",
            nameof(expected_specific_channels_parameters),
            expected_specific_channels_parameters,
        )

        # Act
        temperature_rtd_configuration_instance = nipcbatt.TemperatureRtdMeasurementConfiguration(
            global_channel_parameters=expected_global_channel_parameters,
            specific_channels_parameters=expected_specific_channels_parameters,
            measurement_execution_type=expected_measurement_execution_type,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        logging.debug(
            "%s = %s",
            nameof(temperature_rtd_configuration_instance),
            temperature_rtd_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            expected_specific_channels_parameters,
            temperature_rtd_configuration_instance.specific_channels_parameters,
        )
        self.assertEqual(
            expected_global_channel_parameters,
            temperature_rtd_configuration_instance.global_channel_parameters,
        )
        self.assertEqual(
            expected_measurement_execution_type,
            temperature_rtd_configuration_instance.measurement_execution_type,
        )
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            temperature_rtd_configuration_instance.sample_clock_timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            temperature_rtd_configuration_instance.digital_start_trigger_parameters,
        )


class TestTemperatureRtdMeasurementTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureRtdMeasurementTerminalParameters` class is ready to use.

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

    def test_temperature_rtd_measurement_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(
        self,
    ):
        """unit test of TemperatureRtdMeasurementTerminalParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureRtdMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    current_excitation_value_amperes=1.5,
                    sensor_resistance_ohms=25.0,
                    rtd_type=nidaqmx.constants.RTDType.PT_3750,
                    excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                    adc_timing_mode=nidaqmx.constants.ADCTimingMode.AUTOMATIC,
                )
            )

        # Assert
        self.assertEqual(
            "The value temperature_minimum_value_celsius_degrees must be less than 1.0.",
            str(ctx.exception),
        )

    def test_temperature_rtd_measurement_terminal_parameters(self):
        """unit test of TemperatureRtdMeasurementTerminalParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (169 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        expected_temperature_rtd_measurement_terminal_parameters = (
            nipcbatt.TemperatureRtdMeasurementTerminalParameters(
                temperature_minimum_value_celsius_degrees=1.0,
                temperature_maximum_value_celsius_degrees=99.0,
                current_excitation_value_amperes=1.5,
                sensor_resistance_ohms=25.0,
                rtd_type=nidaqmx.constants.RTDType.PT_3750,
                excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                adc_timing_mode=nidaqmx.constants.ADCTimingMode.AUTOMATIC,
            )
        )

        # Assert
        self.assertEqual(
            1.0,
            expected_temperature_rtd_measurement_terminal_parameters.temperature_minimum_value_celsius_degrees,
        )
        self.assertEqual(
            99.0,
            expected_temperature_rtd_measurement_terminal_parameters.temperature_maximum_value_celsius_degrees,
        )
        self.assertEqual(
            1.5,
            expected_temperature_rtd_measurement_terminal_parameters.current_excitation_value_amperes,
        )
        self.assertEqual(
            25.0,
            expected_temperature_rtd_measurement_terminal_parameters.sensor_resistance_ohms,
        )
        self.assertEqual(
            nidaqmx.constants.RTDType.PT_3750,
            expected_temperature_rtd_measurement_terminal_parameters.rtd_type,
        )
        self.assertEqual(
            nidaqmx.constants.ExcitationSource.EXTERNAL,
            expected_temperature_rtd_measurement_terminal_parameters.excitation_source,
        )
        self.assertEqual(
            nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
            expected_temperature_rtd_measurement_terminal_parameters.resistance_configuration,
        )
        self.assertEqual(
            nidaqmx.constants.ADCTimingMode.AUTOMATIC,
            expected_temperature_rtd_measurement_terminal_parameters.adc_timing_mode,
        )


class TestTemperatureRtdMeasurementChannelParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureRtdMeasurementTerminalParameters` class is ready to use.

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

    def test_temperature_rtd_measurement_channel_parameters_init_fails_if_channel_name_is_none(
        self,
    ):
        """unit test of TemperatureRtdMeasurementChannelParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureRtdMeasurementChannelParameters(
                    channel_name=None,
                    sensor_resistance_ohms=25.0,
                    current_excitation_value_amperes=1.5,
                    rtd_type=nidaqmx.constants.RTDType.PT_3750,
                    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                    excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                )
            )

        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_temperature_rtd_measurement_channel_parameters_init_fails_if_channel_name_is_empty(
        self,
    ):
        """unit test of TemperatureRtdMeasurementChannelParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureRtdMeasurementChannelParameters(
                    channel_name="",
                    sensor_resistance_ohms=25.0,
                    current_excitation_value_amperes=1.5,
                    rtd_type=nidaqmx.constants.RTDType.PT_3750,
                    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                    excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                )
            )

        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_temperature_rtd_measurement_channel_parameters_init_fails_if_channel_name_is_whitespace(
        self,
    ):
        """unit test of TemperatureRtdMeasurementChannelParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureRtdMeasurementChannelParameters(
                    channel_name=" ",
                    sensor_resistance_ohms=25.0,
                    current_excitation_value_amperes=1.5,
                    rtd_type=nidaqmx.constants.RTDType.PT_3750,
                    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                    excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
                )
            )

        # Assert
        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_temperature_rtd_measurement_channel_parameters(self):
        """unit test of TemperatureRtdMeasurementChannelParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        expected_temperature_rtd_measurement_channel_parameters = (
            nipcbatt.TemperatureRtdMeasurementChannelParameters(
                channel_name="Dev/ai0",
                sensor_resistance_ohms=25.0,
                current_excitation_value_amperes=1.5,
                rtd_type=nidaqmx.constants.RTDType.PT_3750,
                resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
                excitation_source=nidaqmx.constants.ExcitationSource.EXTERNAL,
            )
        )

        # Assert
        self.assertEqual(
            "Dev/ai0",
            expected_temperature_rtd_measurement_channel_parameters.channel_name,
        )
        self.assertEqual(
            25.0,
            expected_temperature_rtd_measurement_channel_parameters.sensor_resistance_ohms,
        )
        self.assertEqual(
            1.5,
            expected_temperature_rtd_measurement_channel_parameters.current_excitation_value_amperes,
        )
        self.assertEqual(
            nidaqmx.constants.RTDType.PT_3750,
            expected_temperature_rtd_measurement_channel_parameters.rtd_type,
        )
        self.assertEqual(
            nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
            expected_temperature_rtd_measurement_channel_parameters.resistance_configuration,
        )
        self.assertEqual(
            nidaqmx.constants.ExcitationSource.EXTERNAL,
            expected_temperature_rtd_measurement_channel_parameters.excitation_source,
        )


class TestTemperatureMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureMeasurementResultData` class is ready to use.

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

    def test_temperature_measurement_result_data_init_fails_when_waveforms_is_none(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (158 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [25.0, 23.0, 10.0]
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureMeasurementResultData(
                    waveforms=None,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual("The object waveforms is None.", str(ctx.exception))

    def test_temperature_measurement_result_data_init_fails_when_waveforms_is_empty(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (158 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [25.0, 23.0, 10.0]
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureMeasurementResultData(
                    waveforms=[],
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

    def test_temperature_measurement_result_data_init_fails_when_waveforms_contains_object_that_are_not_of_analog_waveform(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (158 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [25.0, 23.0, 10.0]
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.TemperatureMeasurementResultData(
                    waveforms=[2.0, "3.5"],
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_celsius_degrees_is_none(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=None,
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual(
            "The object average_temperatures_celsius_degrees is None.",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_celsius_degrees_is_empty(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=[],
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual(
            "The iterable average_temperatures_celsius_degrees of type list is empty.",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_celsius_degrees_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_kelvin = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=["2.3", 23.0, 27.0],
                    average_temperatures_kelvin=expected_average_temperatures_kelvin,
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_kelvins_is_none(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=None,
                )
            )

        # Assert
        self.assertEqual(
            "The object average_temperatures_kelvin is None.",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_kelvins_is_empty(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=[],
                )
            )

        # Assert
        self.assertEqual(
            "The iterable average_temperatures_kelvin of type list is empty.",
            str(ctx.exception),
        )

    def test_temperature_measurement_result_data_init_fails_when_average_temperatures_kelvins_contains_object_that_are_not_of_float(
        self,
    ):
        """unit test of TemperatureMeasurementResultData."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (235 > 100 characters) (auto-generated noqa)

        # Arrange
        self._initialize_waveforms()
        expected_acquisition_duration_seconds = 0.3
        expected_average_temperatures_celsius_degrees = [1.0, 1.0, 1.0]

        # Act
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.TemperatureMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    acquisition_duration_seconds=expected_acquisition_duration_seconds,
                    average_temperatures_celsius_degrees=expected_average_temperatures_celsius_degrees,
                    average_temperatures_kelvin=["2.3", 23.0, 27.0],
                )
            )

        # Assert
        self.assertEqual(
            "Not all elements of the list are of the type (float).",
            str(ctx.exception),
        )

    def _initialize_waveforms(self):
        self._expected_waveforms = []
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai0",
                delta_time_seconds=1.0 / 100,
                samples=numpy.ones(shape=(10), dtype=numpy.float64),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai1",
                delta_time_seconds=1.0 / 100,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 10)],
                    dtype=numpy.float64,
                ),
            )
        )
        self._expected_waveforms.append(
            nipcbatt.AnalogWaveform(
                channel_name="Dev/ai2",
                delta_time_seconds=1.0 / 100,
                samples=numpy.array(
                    [random.random() * 0.1 for item in range(0, 10)],
                    dtype=numpy.float64,
                ),
            )
        )


class TestTemperatureThermistorMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermistorMeasurementConfiguration` class is ready to use.

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

    def test_temperature_thermistor_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_temperature_thermistor_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_temperature_thermistor_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_temperature_thermistor_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermistorMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_temperature_thermistor_measurement_configuration(self):
        """unit test of TemperatureThermistorMeasurementConfiguration."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (248 > 100 characters) (auto-generated noqa)

        # Arrange

        expected_global_channel_parameters = (
            nipcbatt.DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS
        )

        expected_specific_channels_parameters = []
        expected_specific_channels_parameters.append(
            nipcbatt.TemperatureThermistorChannelRangeAndTerminalParameters(
                channel_name="Dev/ai0",
                channel_parameters=nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
                    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DEFAULT,
                    temperature_minimum_value_celsius_degrees=10.0,
                    temperature_maximum_value_celsius_degrees=89.0,
                    voltage_excitation_value_volts=15.0,
                    thermistor_resistor_ohms=5.0,
                    steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
                    coefficients_steinhart_hart_parameters=nipcbatt.CoefficientsSteinhartHartParameters(
                        coefficient_steinhart_hart_a=10.0,
                        coefficient_steinhart_hart_b=20.0,
                        coefficient_steinhart_hart_c=10.0,
                    ),
                    beta_coefficient_and_sensor_resistance_parameters=nipcbatt.BetaCoefficientAndSensorResistanceParameters(
                        coefficient_steinhart_hart_beta_kelvins=289.15,
                        sensor_resistance_ohms=5.0,
                    ),
                ),
            ),
        )

        expected_specific_channels_parameters.append(
            nipcbatt.TemperatureThermistorChannelRangeAndTerminalParameters(
                channel_name="Dev/ai1",
                channel_parameters=nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
                    terminal_configuration=nidaqmx.constants.TerminalConfiguration.NRSE,
                    temperature_minimum_value_celsius_degrees=1.0,
                    temperature_maximum_value_celsius_degrees=79.0,
                    voltage_excitation_value_volts=10.0,
                    thermistor_resistor_ohms=10.0,
                    steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
                    coefficients_steinhart_hart_parameters=nipcbatt.CoefficientsSteinhartHartParameters(
                        coefficient_steinhart_hart_a=1.5,
                        coefficient_steinhart_hart_b=2.5,
                        coefficient_steinhart_hart_c=10.0,
                    ),
                    beta_coefficient_and_sensor_resistance_parameters=nipcbatt.BetaCoefficientAndSensorResistanceParameters(
                        coefficient_steinhart_hart_beta_kelvins=303.15,
                        sensor_resistance_ohms=15.0,
                    ),
                ),
            ),
        )
        expected_specific_channels_parameters.append(
            nipcbatt.TemperatureThermistorChannelRangeAndTerminalParameters(
                channel_name="Dev/ai2",
                channel_parameters=nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
                    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
                    temperature_minimum_value_celsius_degrees=0.0,
                    temperature_maximum_value_celsius_degrees=100.0,
                    voltage_excitation_value_volts=10.0,
                    thermistor_resistor_ohms=15.0,
                    steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
                    coefficients_steinhart_hart_parameters=nipcbatt.CoefficientsSteinhartHartParameters(
                        coefficient_steinhart_hart_a=15.0,
                        coefficient_steinhart_hart_b=25.0,
                        coefficient_steinhart_hart_c=16.0,
                    ),
                    beta_coefficient_and_sensor_resistance_parameters=nipcbatt.BetaCoefficientAndSensorResistanceParameters(
                        coefficient_steinhart_hart_beta_kelvins=289.15,
                        sensor_resistance_ohms=5.0,
                    ),
                ),
            ),
        )

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100,
            number_of_samples_per_channel=10,
            sample_timing_engine=nipcbatt.SampleTimingEngine.TE0,
        )

        expected_measurement_execution_type = nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
            digital_start_trigger_source="trigger_source",
            digital_start_trigger_edge=nidaqmx.constants.Edge.FALLING,
        )

        logging.debug(
            "%s = %s",
            nameof(expected_specific_channels_parameters),
            expected_specific_channels_parameters,
        )

        # Act
        temperature_thermistor_configuration_instance = (
            nipcbatt.TemperatureThermistorMeasurementConfiguration(
                global_channel_parameters=expected_global_channel_parameters,
                specific_channels_parameters=expected_specific_channels_parameters,
                measurement_execution_type=expected_measurement_execution_type,
                sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
                digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
            )
        )

        logging.debug(
            "%s = %s",
            nameof(temperature_thermistor_configuration_instance),
            temperature_thermistor_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            expected_specific_channels_parameters,
            temperature_thermistor_configuration_instance.specific_channels_parameters,
        )
        self.assertEqual(
            expected_global_channel_parameters,
            temperature_thermistor_configuration_instance.global_channel_parameters,
        )
        self.assertEqual(
            expected_measurement_execution_type,
            temperature_thermistor_configuration_instance.measurement_execution_type,
        )
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            temperature_thermistor_configuration_instance.sample_clock_timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            temperature_thermistor_configuration_instance.digital_start_trigger_parameters,
        )


class TestCoefficientsSteinhartHartParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `CoefficientsSteinhartHartParameters` class is ready to use.

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

    def test_coefficients_steinhart_hart_parameters(self):
        """unit test of CoefficientsSteinhartHartParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        expected_coefficients_steinhart_hart_parameters = (
            nipcbatt.CoefficientsSteinhartHartParameters(
                coefficient_steinhart_hart_a=10.0,
                coefficient_steinhart_hart_b=25.0,
                coefficient_steinhart_hart_c=5.0,
            )
        )

        # Assert
        self.assertEqual(
            10.0,
            expected_coefficients_steinhart_hart_parameters.coefficient_steinhart_hart_a,
        )
        self.assertEqual(
            25.0,
            expected_coefficients_steinhart_hart_parameters.coefficient_steinhart_hart_b,
        )
        self.assertEqual(
            5.0,
            expected_coefficients_steinhart_hart_parameters.coefficient_steinhart_hart_c,
        )


class TestBetaCoefficientAndSensorResistanceParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `BetaCoefficientAndSensorResistanceParameters` class is ready to use.

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

    def test_beta_coefficient_and_sensor_resistance_parameters(self):
        """unit test of BetaCoefficientAndSensorResistanceParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (170 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        expected_beta_coefficient_and_sensor_resistance_parameters = (
            nipcbatt.BetaCoefficientAndSensorResistanceParameters(
                coefficient_steinhart_hart_beta_kelvins=289.15,
                sensor_resistance_ohms=10.0,
            )
        )

        # Assert
        self.assertEqual(
            289.15,
            expected_beta_coefficient_and_sensor_resistance_parameters.coefficient_steinhart_hart_beta_kelvins,
        )
        self.assertEqual(
            10.0,
            expected_beta_coefficient_and_sensor_resistance_parameters.sensor_resistance_ohms,
        )


class TestTemperatureThermistorRangeAndTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermistorRangeAndTerminalParameters` class is ready to use.

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

    def test_temperature_thermistor_range_and_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(
        self,
    ):
        """unit test of TemperatureThermistorRangeAndTerminalParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_coefficients_steinhart_hart_parameters = (
            nipcbatt.CoefficientsSteinhartHartParameters(
                coefficient_steinhart_hart_a=10.0,
                coefficient_steinhart_hart_b=25.0,
                coefficient_steinhart_hart_c=5.0,
            )
        )
        expected_beta_coefficient_and_sensor_resistance_parameters = (
            nipcbatt.BetaCoefficientAndSensorResistanceParameters(
                coefficient_steinhart_hart_beta_kelvins=289.15,
                sensor_resistance_ohms=10.0,
            )
        )
        # Act

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
                    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    voltage_excitation_value_volts=5.0,
                    thermistor_resistor_ohms=10.0,
                    steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
                    coefficients_steinhart_hart_parameters=expected_coefficients_steinhart_hart_parameters,
                    beta_coefficient_and_sensor_resistance_parameters=expected_beta_coefficient_and_sensor_resistance_parameters,
                )
            )

        # Assert
        self.assertEqual(
            "The value temperature_minimum_value_celsius_degrees must be less than 1.0.",
            str(ctx.exception),
        )

    def test_temperature_thermistor_range_and_terminal_parameters(self):
        """unit test of TemperatureThermistorRangeAndTerminalParameters."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_coefficients_steinhart_hart_parameters = (
            nipcbatt.CoefficientsSteinhartHartParameters(
                coefficient_steinhart_hart_a=10.0,
                coefficient_steinhart_hart_b=25.0,
                coefficient_steinhart_hart_c=5.0,
            )
        )
        expected_beta_coefficient_and_sensor_resistance_parameters = (
            nipcbatt.BetaCoefficientAndSensorResistanceParameters(
                coefficient_steinhart_hart_beta_kelvins=289.15,
                sensor_resistance_ohms=10.0,
            )
        )

        # Act
        expected_temperature_thermistor_range_and_terminal_parameters = nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            temperature_minimum_value_celsius_degrees=0.0,
            temperature_maximum_value_celsius_degrees=100.0,
            voltage_excitation_value_volts=5.0,
            thermistor_resistor_ohms=10.0,
            steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
            coefficients_steinhart_hart_parameters=expected_coefficients_steinhart_hart_parameters,
            beta_coefficient_and_sensor_resistance_parameters=expected_beta_coefficient_and_sensor_resistance_parameters,
        )

        # Assert
        self.assertEqual(
            nidaqmx.constants.TerminalConfiguration.RSE,
            expected_temperature_thermistor_range_and_terminal_parameters.terminal_configuration,
        )
        self.assertEqual(
            0.0,
            expected_temperature_thermistor_range_and_terminal_parameters.temperature_minimum_value_celsius_degrees,
        )
        self.assertEqual(
            100.0,
            expected_temperature_thermistor_range_and_terminal_parameters.temperature_maximum_value_celsius_degrees,
        )
        self.assertEqual(
            5.0,
            expected_temperature_thermistor_range_and_terminal_parameters.voltage_excitation_value_volts,
        )
        self.assertEqual(
            10.0,
            expected_temperature_thermistor_range_and_terminal_parameters.thermistor_resistor_ohms,
        )
        self.assertEqual(
            nipcbatt.SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS,
            expected_temperature_thermistor_range_and_terminal_parameters.steinhart_hart_equation_option,
        )
        self.assertEqual(
            expected_coefficients_steinhart_hart_parameters,
            expected_temperature_thermistor_range_and_terminal_parameters.coefficients_steinhart_hart_parameters,
        )
        self.assertEqual(
            expected_beta_coefficient_and_sensor_resistance_parameters,
            expected_temperature_thermistor_range_and_terminal_parameters.beta_coefficient_and_sensor_resistance_parameters,
        )


class TestTemperatureThermocoupleMeasurementConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermocoupleMeasurementConfiguration` class is ready to use.

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

    def test_temperature_thermocouple_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_temperature_thermocouple_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_temperature_thermocouple_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_temperature_thermocouple_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_temperature_thermocouple_measurement_configuration(self):
        """unit test of TemperatureThermocoupleMeasurementConfiguration."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (250 > 100 characters) (auto-generated noqa)

        # Arrange
        expected_global_channel_parameters = (
            nipcbatt.DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS
        )

        expected_specific_channels_parameters = []
        expected_specific_channels_parameters.append(
            nipcbatt.TemperatureThermocoupleChannelRangeAndTerminalParameters(
                channel_name="Dev/ai0",
                channel_parameters=nipcbatt.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=10.0,
                    temperature_maximum_value_celsius_degrees=89.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                ),
            ),
        )

        expected_specific_channels_parameters.append(
            nipcbatt.TemperatureThermocoupleChannelRangeAndTerminalParameters(
                channel_name="Dev/ai1",
                channel_parameters=nipcbatt.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=1.0,
                    temperature_maximum_value_celsius_degrees=79.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                ),
            ),
        )
        expected_specific_channels_parameters.append(
            nipcbatt.TemperatureThermocoupleChannelRangeAndTerminalParameters(
                channel_name="Dev/ai2",
                channel_parameters=nipcbatt.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=0.0,
                    temperature_maximum_value_celsius_degrees=100.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                ),
            ),
        )

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100,
            number_of_samples_per_channel=10,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        expected_measurement_execution_type = nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.FALLING,
        )

        logging.debug(
            "%s = %s",
            nameof(expected_specific_channels_parameters),
            expected_specific_channels_parameters,
        )

        # Act
        temperature_thermocouple_configuration_instance = (
            nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
                global_channel_parameters=expected_global_channel_parameters,
                specific_channels_parameters=expected_specific_channels_parameters,
                measurement_execution_type=expected_measurement_execution_type,
                sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
                digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
            )
        )

        logging.debug(
            "%s = %s",
            nameof(temperature_thermocouple_configuration_instance),
            temperature_thermocouple_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            expected_specific_channels_parameters,
            temperature_thermocouple_configuration_instance.specific_channels_parameters,
        )
        self.assertEqual(
            expected_global_channel_parameters,
            temperature_thermocouple_configuration_instance.global_channel_parameters,
        )
        self.assertEqual(
            expected_measurement_execution_type,
            temperature_thermocouple_configuration_instance.measurement_execution_type,
        )
        self.assertEqual(
            expected_sample_clock_timing_parameters,
            temperature_thermocouple_configuration_instance.sample_clock_timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            temperature_thermocouple_configuration_instance.digital_start_trigger_parameters,
        )


class TestTemperatureThermocoupleMeasurementTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermocoupleMeasurementTerminalParameters` class is ready to use.

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

    def test_temperature_thermocouple_measurement_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        # Act

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermocoupleMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_temperature=25.0,
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )
            )

        # Assert
        self.assertEqual(
            "The value temperature_minimum_value_celsius_degrees must be less than 1.0.",
            str(ctx.exception),
        )

    def test_temperature_thermocouple_measurement_terminal_parameters_fails_if_perform_auto_zero_mode_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError):
            print(
                nipcbatt.TemperatureThermocoupleMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_temperature=25.0,
                    perform_auto_zero_mode=None,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )
            )

    def test_temperature_thermocouple_measurement_terminal_parameters_fails_if_auto_zero_mode_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleMeasurementTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError):
            print(
                nipcbatt.TemperatureThermocoupleMeasurementTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_temperature=25.0,
                    perform_auto_zero_mode=True,
                    auto_zero_mode=None,
                )
            )

    def test_temperature_thermocouple_measurement_terminal_parameters(self):
        """unit test of TemperatureThermocoupleMeasurementTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

        # Act
        expected_temperature_thermocouple_measurement_terminal_parameters = (
            nipcbatt.TemperatureThermocoupleMeasurementTerminalParameters(
                temperature_minimum_value_celsius_degrees=0.0,
                temperature_maximum_value_celsius_degrees=100.0,
                thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                cold_junction_compensation_temperature=25.0,
                perform_auto_zero_mode=False,
                auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
            )
        )

        # Assert
        self.assertEqual(
            0.0,
            expected_temperature_thermocouple_measurement_terminal_parameters.temperature_minimum_value_celsius_degrees,
        )
        self.assertEqual(
            100.0,
            expected_temperature_thermocouple_measurement_terminal_parameters.temperature_maximum_value_celsius_degrees,
        )
        self.assertEqual(
            nidaqmx.constants.ThermocoupleType.J,
            expected_temperature_thermocouple_measurement_terminal_parameters.thermocouple_type,
        )
        self.assertEqual(
            25.0,
            expected_temperature_thermocouple_measurement_terminal_parameters.cold_junction_compensation_temperature,
        )
        self.assertEqual(
            False,
            expected_temperature_thermocouple_measurement_terminal_parameters.perform_auto_zero_mode,
        )
        self.assertEqual(
            nidaqmx.constants.AutoZeroType.NONE,
            expected_temperature_thermocouple_measurement_terminal_parameters.auto_zero_mode,
        )


class TestTemperatureThermocoupleRangeAndTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TemperatureThermocoupleRangeAndTerminalParameters` class is ready to use.

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

    def test_temperature_thermocouple_range_and_terminal_parameters_init_fails_if_maximum_is_less_that_minimum(
        self,
    ):
        """unit test of TemperatureThermocoupleRangeAndTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (252 > 100 characters) (auto-generated noqa)

        # Act

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=False,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )
            )

        # Assert
        self.assertEqual(
            "The value temperature_minimum_value_celsius_degrees must be less than 1.0.",
            str(ctx.exception),
        )

    def test_temperature_thermocouple_range_and_terminal_parameters_fails_if_perform_auto_zero_mode_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleRangeAndTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (252 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError):
            print(
                nipcbatt.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=None,
                    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
                )
            )

    def test_temperature_thermocouple_range_and_terminal_parameters_fails_if_auto_zero_mode_is_none(
        self,
    ):
        """unit test of TemperatureThermocoupleRangeAndTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (252 > 100 characters) (auto-generated noqa)

        with self.assertRaises(ValueError):
            print(
                nipcbatt.TemperatureThermocoupleRangeAndTerminalParameters(
                    temperature_minimum_value_celsius_degrees=99.0,
                    temperature_maximum_value_celsius_degrees=1.0,
                    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                    cold_junction_compensation_temperature=25.0,
                    cold_junction_compensation_channel_name="",
                    perform_auto_zero_mode=True,
                    auto_zero_mode=None,
                )
            )

    def test_temperature_thermocouple_range_and_terminal_parameters(self):
        """unit test of TemperatureThermocoupleRangeAndTerminalParameters."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (252 > 100 characters) (auto-generated noqa)

        # Act
        expected_temperature_thermocouple_range_and_terminal_parameters = (
            nipcbatt.TemperatureThermocoupleRangeAndTerminalParameters(
                temperature_minimum_value_celsius_degrees=0.0,
                temperature_maximum_value_celsius_degrees=100.0,
                thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
                cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
                cold_junction_compensation_temperature=25.0,
                cold_junction_compensation_channel_name="",
                perform_auto_zero_mode=False,
                auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
            )
        )

        # Assert
        self.assertEqual(
            0.0,
            expected_temperature_thermocouple_range_and_terminal_parameters.temperature_minimum_value_celsius_degrees,
        )
        self.assertEqual(
            100.0,
            expected_temperature_thermocouple_range_and_terminal_parameters.temperature_maximum_value_celsius_degrees,
        )
        self.assertEqual(
            nidaqmx.constants.ThermocoupleType.J,
            expected_temperature_thermocouple_range_and_terminal_parameters.thermocouple_type,
        )
        self.assertEqual(
            nidaqmx.constants.CJCSource.BUILT_IN,
            expected_temperature_thermocouple_range_and_terminal_parameters.cold_junction_compensation_source,
        )
        self.assertEqual(
            25.0,
            expected_temperature_thermocouple_range_and_terminal_parameters.cold_junction_compensation_temperature,
        )
        self.assertEqual(
            "",
            expected_temperature_thermocouple_range_and_terminal_parameters.cold_junction_compensation_channel_name,
        )
        self.assertEqual(
            False,
            expected_temperature_thermocouple_range_and_terminal_parameters.perform_auto_zero_mode,
        )
        self.assertEqual(
            nidaqmx.constants.AutoZeroType.NONE,
            expected_temperature_thermocouple_range_and_terminal_parameters.auto_zero_mode,
        )


if __name__ == "__main__":
    unittest.main()
