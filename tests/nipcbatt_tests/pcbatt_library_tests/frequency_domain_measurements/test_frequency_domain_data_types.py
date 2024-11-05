"""This module provides Frequency domain data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt


class TestFrequencyDomainMeasurementConfiguration(unittest.TestCase):
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

    def test_frequency_domain_measurement_configuration_init_fails_when_global_channel_parameters_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=None,
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object global_channel_parameters is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration_init_fails_when_specific_channels_parameters_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=None,
                    measurement_options=nipcbatt.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object specific_channels_parameters is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration_init_fails_when_measurement_options_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=None,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object measurement_options is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration_init_fails_when_sample_clock_timing_parameters_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=None,
                    digital_start_trigger_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS
                    ),
                )
            )

        # Assert
        self.assertEqual("The object sample_clock_timing_parameters is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration_init_fails_when_digital_start_trigger_parameters_is_none(
        self,
    ):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementConfiguration(
                    global_channel_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS
                    ),
                    specific_channels_parameters=[],
                    measurement_options=nipcbatt.DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
                    sample_clock_timing_parameters=(
                        nipcbatt.DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS
                    ),
                    digital_start_trigger_parameters=None,
                )
            )

        # Assert
        self.assertEqual("The object digital_start_trigger_parameters is None.", str(ctx.exception))

    def test_frequency_domain_measurement_configuration(self):
        """unit test of FrequencyDomainMeasurementConfiguration."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)
        # Arrange
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

        # Act
        measurement_configuration_instance = nipcbatt.FrequencyDomainMeasurementConfiguration(
            global_channel_parameters=expected_global_channel_parameters,
            specific_channels_parameters=specific_channels_parameters,
            measurement_options=expected_measurement_options,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        logging.debug(
            "%s = %s",
            nameof(measurement_configuration_instance),
            measurement_configuration_instance,
        )

        # Assert
        self.assertListEqual(
            specific_channels_parameters,
            measurement_configuration_instance.specific_channels_parameters,
        )

        actual_global_channel_parameters = (
            measurement_configuration_instance.global_channel_parameters
        )

        actual_measurement_options = measurement_configuration_instance.measurement_options
        actual_sample_clock_timing_parameters = (
            measurement_configuration_instance.sample_clock_timing_parameters
        )

        self.assertEqual(expected_global_channel_parameters, actual_global_channel_parameters)

        self.assertEqual(expected_measurement_options, actual_measurement_options)

        self.assertEqual(
            expected_sample_clock_timing_parameters,
            actual_sample_clock_timing_parameters,
        )


class TestMultipleTonesMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `MultipleTonesMeasurementResultData` class is ready to use.

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

    def test_multiple_tones_measurement_result_data_for_value_error(self):
        """Tests if expected ValueError in thrown when inputs are None"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (261 > 100 characters) (auto-generated noqa)

        # Test for tones_amplitudes_volts set to None
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=None,
                    tones_frequencies_hertz=[1000],
                )
            )

        self.assertEqual("The object tones_amplitudes_volts is None.", str(ctx.exception))

        # Test for tones_frequencies_hertz set to None
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=[1.0],
                    tones_frequencies_hertz=None,
                )
            )

        self.assertEqual("The object tones_frequencies_hertz is None.", str(ctx.exception))

    def test_multiple_tones_measurement_result_data_for_type_error(self):
        """Tests if expected TypeError in thrown when inputs are None"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (260 > 100 characters) (auto-generated noqa)

        # Test for tones_amplitudes_volts with values that are not float
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=[1.0, "1.5", 2.0],
                    tones_frequencies_hertz=[100, 1000, 250],
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (float).", str(ctx.exception)
        )

        # Test for tones_frequencies_hertz with values that are not float
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=[1.0, 1.5, 2.0],
                    tones_frequencies_hertz=[100, 1000, True],
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (float).", str(ctx.exception)
        )

    def test_multiple_tones_measurement_result_data_with_input_lists_of_different_lengths(
        self,
    ):
        """Tests if expected ValueError in thrown when the two input lists have different length."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (186 > 100 characters) (auto-generated noqa)

        # Test for tones_amplitudes_volts and tones_frequencies_hertz lists
        # with different number of element
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.MultipleTonesMeasurementResultData(
                    tones_amplitudes_volts=[1.0, 2.0, 3.0],
                    tones_frequencies_hertz=[100.0, 200.0],
                )
            )

        self.assertEqual(
            "The iterables (tones_amplitudes_volts and tones_frequencies_hertz)"
            + " do not have same size.",
            str(ctx.exception),
        )

    def test_multiple_tones_measurement_result_data(self):
        """Test for proper functioning of TestMultipleTonesMeasurementResultData"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)
        expected_tones_amplitude = [1.2, 1.6, 1.8, 1.0]
        expected_tones_frequencies = [100.05, 200.0, 500.0, 1000.1]

        instance = nipcbatt.MultipleTonesMeasurementResultData(
            tones_frequencies_hertz=expected_tones_frequencies,
            tones_amplitudes_volts=expected_tones_amplitude,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_tones_amplitude = instance.tones_amplitudes_volts
        actual_tones_frequencies = instance.tones_frequencies_hertz

        self.assertListEqual(expected_tones_amplitude, actual_tones_amplitude)
        self.assertListEqual(expected_tones_frequencies, actual_tones_frequencies)


class TestFrequencyDomainMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `FrequencyDomainMeasurementResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self,
        methodName: str = "runTest",  # noqa: N803 - argument name 'methodName' should be lowercase (auto-generated noqa)
    ) -> None:
        super().__init__(methodName)
        self._expected_waveforms = None

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

    def setUp(self):
        """Creates some common test data to be used in different test methods."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (167 > 100 characters) (auto-generated noqa)

        # Create test data for waveforms.
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

        array_count1 = 1500
        array_count2 = 2000

        # Create test data for magnitude peak.
        self._expected_magnitude_peak = []

        samples_array1 = list(4.95 + random.random() * 0.1 for i in range(0, array_count1))
        samples_numpy_array1 = numpy.array(samples_array1, dtype=numpy.float64)

        self._expected_magnitude_peak.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel1",
                spectrum_start_frequency_hertz=13500,
                spectrum_frequency_resolution_hertz=1.0,
                amplitudes=samples_numpy_array1,
            )
        )

        samples_array2 = list(5.08 + random.random() * 0.1 for i in range(0, array_count2))
        samples_numpy_array2 = numpy.array(samples_array2, dtype=numpy.float64)

        self._expected_magnitude_peak.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel2",
                spectrum_start_frequency_hertz=20000,
                spectrum_frequency_resolution_hertz=10.0,
                amplitudes=samples_numpy_array2,
            )
        )

        # Create test data for magnitude rms.
        self._expected_magnitude_rms = []
        samples_array3 = list(2.95 + random.random() * 0.1 for i in range(0, array_count1))
        samples_numpy_array3 = numpy.array(samples_array3, dtype=numpy.float64)

        self._expected_magnitude_rms.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel1",
                spectrum_start_frequency_hertz=25431,
                spectrum_frequency_resolution_hertz=5.0,
                amplitudes=samples_numpy_array3,
            )
        )

        samples_array4 = list(3.08 + random.random() * 0.1 for i in range(0, array_count2))
        samples_numpy_array4 = numpy.array(samples_array4, dtype=numpy.float64)

        self._expected_magnitude_rms.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel2",
                spectrum_start_frequency_hertz=15684,
                spectrum_frequency_resolution_hertz=11.0,
                amplitudes=samples_numpy_array4,
            )
        )

        # Create test data for detected tones.
        self._expected_detected_tones = []
        self._expected_detected_tones.append(
            nipcbatt.MultipleTonesMeasurementResultData(
                tones_frequencies_hertz=[100.05, 200.0, 500.0, 1000.1],
                tones_amplitudes_volts=[1.2, 1.6, 1.8, 1.0],
            )
        )
        self._expected_detected_tones.append(
            nipcbatt.MultipleTonesMeasurementResultData(
                tones_frequencies_hertz=[1000.5, 2000.15, 1500.0, 10000.89, 200000.0],
                tones_amplitudes_volts=[1.02, 2.76, 3.2, 5.15, 4.87],
            )
        )

    def tearDown(self):
        pass

    def test_frequency_domain_measurement_result_data_for_invalid_values_for_waveforms(
        self,
    ):
        """Unit test to check if `FrequencyDomainMeasurementResultData` throws Value Error
        for invalid values for `waveforms` input."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (422 > 100 characters) (auto-generated noqa)

        # Test if expected error is thrown if waveforms is set to None.
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=None,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The object waveforms is None.", str(ctx.exception))

        # Test if expected error is thrown if waveforms is set to an empty list.
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=[],
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )
        self.assertEqual("The iterable waveforms of type list is empty.", str(ctx.exception))

        # Test if expected error is thrown if magnitude_rms contains elements
        # that are not of type AnalogWaveform.
        self._expected_waveforms.append(5.67)
        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (AnalogWaveform).",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_for_invalid_values_for_magnitude_rms(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData' with invalid values for `magnitude_rms`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Test if expected error is thrown if magnitude_rms is set to None.
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=None,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The object magnitude_rms is None.", str(ctx.exception))

        # Test if expected Value error is thrown if magnitude_rms is an empty list.
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=[],
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The iterable magnitude_rms of type list is empty.", str(ctx.exception))

        # Test if expected error is thrown if magnitude_rms contains elements
        # that are not of type AmplitudeSpectrum.

        self._expected_magnitude_rms.append(5.67)

        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (AmplitudeSpectrum).",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_for_invalid_values_for_magnitude_peak(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData' with invalid values for `magnitude_peak`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Test if expected error is thrown if magnitude_peak is set to None.
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=None,
                    magnitude_rms=self._expected_magnitude_peak,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The object magnitude_peak is None.", str(ctx.exception))

        # Test if expected Value error is thrown if magnitude_peak is an empty list.
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=[],
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual("The iterable magnitude_peak of type list is empty.", str(ctx.exception))

        # Test if expected error is thrown if magnitude_peak contains elements
        # that are not of type AmplitudeSpectrum.
        self._expected_magnitude_peak.append(5.67)

        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (AmplitudeSpectrum).",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_with_waveforms_and_magnitude_rms_are_of_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData'
        with diffrent list size for`waveforms` and `magnitude_rms`
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        samples_array = list(3.08 + random.random() * 0.1 for i in range(0, 200))
        samples_numpy_array = numpy.array(samples_array, dtype=numpy.float64)

        self._expected_magnitude_rms.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel3",
                spectrum_start_frequency_hertz=15684,
                spectrum_frequency_resolution_hertz=11.0,
                amplitudes=samples_numpy_array,
            )
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )
        self.assertEqual(
            "The iterables (waveforms and magnitude_rms) do not have same size.",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_with_waveforms_and_magnitude_peak_are_of_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating instance
        of `FrequencyDomainMeasurementResultData'
        with diffrent list size for`waveforms` and `magnitude_peak`
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        samples_array = list(3.08 + random.random() * 0.1 for i in range(0, 200))
        samples_numpy_array = numpy.array(samples_array, dtype=numpy.float64)

        self._expected_magnitude_peak.append(
            nipcbatt.AmplitudeSpectrum(
                channel_name="channel3",
                spectrum_start_frequency_hertz=15684,
                spectrum_frequency_resolution_hertz=11.0,
                amplitudes=samples_numpy_array,
            )
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )
        self.assertEqual(
            "The iterables (waveforms and magnitude_peak) do not have same size.",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_with_waveforms_and_detected_tones_are_of_different_lengths(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData'
        with diffrent list size for`waveforms` and `detected_tones`
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        self._expected_detected_tones.append(
            nipcbatt.MultipleTonesMeasurementResultData(
                tones_amplitudes_volts=[1.0, 2.0],
                tones_frequencies_hertz=[100.12, 1000.00],
            )
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )
        self.assertEqual(
            "The iterables (waveforms and detected_tones) do not have same size.",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data_for_invalid_values_for_detected_tones(
        self,
    ):
        """Tests if expected error is thrown when creating instance of
        `FrequencyDomainMeasurementResultData' with invalid values for `detected_tones`.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Test if expected error is thrown if detected_tones is set to None.
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_peak,
                    detected_tones=None,
                )
            )

        self.assertEqual("The object detected_tones is None.", str(ctx.exception))

        # Test if expected Value error is thrown if magnitude_peak is an empty list.
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=[],
                )
            )

        self.assertEqual("The iterable detected_tones of type list is empty.", str(ctx.exception))

        # Test if expected error is thrown if detected_tones contains elements
        # that are not of type MultipleTonesMeasurementResultData.
        self._expected_detected_tones.append([5.67])

        with self.assertRaises(TypeError) as ctx:
            print(
                nipcbatt.FrequencyDomainMeasurementResultData(
                    waveforms=self._expected_waveforms,
                    magnitude_peak=self._expected_magnitude_peak,
                    magnitude_rms=self._expected_magnitude_rms,
                    detected_tones=self._expected_detected_tones,
                )
            )

        self.assertEqual(
            "Not all elements of the list are of the type (MultipleTonesMeasurementResultData).",
            str(ctx.exception),
        )

    def test_frequency_domain_measurement_result_data(self):
        """Test for proper functioning of `FrequencyDomainMeasurementResultData` class"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (277 > 100 characters) (auto-generated noqa)

        fdvm_result_data_instance = nipcbatt.FrequencyDomainMeasurementResultData(
            waveforms=self._expected_waveforms,
            magnitude_peak=self._expected_magnitude_peak,
            magnitude_rms=self._expected_magnitude_rms,
            detected_tones=self._expected_detected_tones,
        )

        actual_waveforms = fdvm_result_data_instance.waveforms
        actual_magnitude_peak = fdvm_result_data_instance.magnitude_peak
        actual_magnitude_rms = fdvm_result_data_instance.magnitude_rms
        actual_detected_tones = fdvm_result_data_instance.detected_tones

        logging.debug("%s = %s", nameof(fdvm_result_data_instance), fdvm_result_data_instance)

        self.assertListEqual(self._expected_waveforms, actual_waveforms)
        self.assertListEqual(self._expected_magnitude_peak, actual_magnitude_peak)
        self.assertListEqual(self._expected_magnitude_rms, actual_magnitude_rms)
        self.assertListEqual(self._expected_detected_tones, actual_detected_tones)


if __name__ == "__main__":
    unittest.main()
