"""This module provides common data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class TestMeasurementOptions(unittest.TestCase):
    """Defines a test fixture that checks
    `MeasurementOptions` class is ready to use.

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

    def test_measurement_options(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementOptions."""
        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        instance = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        actual_execution_option = instance.execution_option
        actual_measurement_analysis_requirement = instance.measurement_analysis_requirement
        self.assertEqual(expected_execution_option, actual_execution_option)
        self.assertEqual(
            expected_measurement_analysis_requirement,
            actual_measurement_analysis_requirement,
        )


class TestSampleClockTimingParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SampleClockTimingParameters` class is ready to use.

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

    def test_sample_clock_timing_parameters_init_fails_when_sample_clock_source_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SampleClockTimingParameters(
                    sample_clock_source=None,
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    number_of_samples_per_channel=expected_number_of_samples_per_channel,
                    sample_timing_engine=expected_sample_timing_engine,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_sample_clock_timing_parameters_init_fails_when_sample_clock_source_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SampleClockTimingParameters(
                    sample_clock_source="",
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    number_of_samples_per_channel=expected_number_of_samples_per_channel,
                    sample_timing_engine=expected_sample_timing_engine,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_sample_clock_timing_parameters_init_fails_when_sample_clock_source_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SampleClockTimingParameters(
                    sample_clock_source=" ",
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    number_of_samples_per_channel=expected_number_of_samples_per_channel,
                    sample_timing_engine=expected_sample_timing_engine,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_sample_clock_timing_parameters_init_fails_when_sampling_rate_hertz_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""
        expected_sample_clock_source = "OnboardClock"
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SampleClockTimingParameters(
                    sample_clock_source=expected_sample_clock_source,
                    sampling_rate_hertz=-6,
                    number_of_samples_per_channel=expected_number_of_samples_per_channel,
                    sample_timing_engine=expected_sample_timing_engine,
                )
            )

        self.assertEqual(
            "The value sampling_rate_hertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_sample_clock_timing_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SampleClockTimingParameters."""
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_number_of_samples_per_channel = 1500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        instance = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        actual_sample_clock_source = instance.sample_clock_source
        actual_sampling_rate_hertz = instance.sampling_rate_hertz
        actual_number_of_samples_per_channel = instance.number_of_samples_per_channel
        actual_sample_timing_engine = instance.sample_timing_engine
        self.assertEqual(expected_sample_clock_source, actual_sample_clock_source)
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate_hertz)
        self.assertEqual(
            expected_number_of_samples_per_channel, actual_number_of_samples_per_channel
        )
        self.assertEqual(
            expected_sample_timing_engine,
            actual_sample_timing_engine,
        )


class TestDigitalStartTriggerParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DigitalStartTriggerParameters` class is ready to use.

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

    def test_digital_start_trigger_parameters_init_should_not_fail_if_trigger_select_is_no_trigger(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters.
        """
        expected_trigger_select = nipcbatt.StartTriggerType.NO_TRIGGER
        expected_digital_start_trigger_source = ""
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        instance = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        actual_trigger_select = instance.trigger_select
        actual_digital_start_trigger_source = instance.digital_start_trigger_source
        actual_digital_start_trigger_edge = instance.digital_start_trigger_edge
        self.assertEqual(expected_trigger_select, actual_trigger_select)
        self.assertEqual(expected_digital_start_trigger_source, actual_digital_start_trigger_source)
        self.assertEqual(expected_digital_start_trigger_edge, actual_digital_start_trigger_edge)

    def test_digital_start_trigger_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters.
        """
        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        instance = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        actual_trigger_select = instance.trigger_select
        actual_digital_start_trigger_source = instance.digital_start_trigger_source
        actual_digital_start_trigger_edge = instance.digital_start_trigger_edge
        self.assertEqual(expected_trigger_select, actual_trigger_select)
        self.assertEqual(expected_digital_start_trigger_source, actual_digital_start_trigger_source)
        self.assertEqual(expected_digital_start_trigger_edge, actual_digital_start_trigger_edge)


class TestMeasurementData(unittest.TestCase):
    """Defines a test fixture that checks
    `MeasurementData` class is ready to use.

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

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)
        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_measurement_data_init_fails_when_samples_is_none(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData."""
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.MeasurementData(
                    data_samples=None,
                )
            )

        self.assertEqual(
            "The object data_samples is None.",
            str(ctx.exception),
        )

    def test_measurement_data_init_fails_when_samples_is_empty(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData."""
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.MeasurementData(
                    data_samples=numpy.array([]),
                )
            )

        self.assertEqual(
            "The iterable data_samples of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_measurement_data_fails_if_the_array_has_more_than_two_dimensions(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData."""
        data_samples = numpy.zeros(shape=(10, 10, 10))
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.MeasurementData(
                    data_samples=data_samples,
                )
            )

        self.assertEqual(
            "The size of shape must less than or equal to 2.",
            str(ctx.exception),
        )

    def test_measurement_data(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.MeasurementData."""
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        instance = nipcbatt.MeasurementData(
            data_samples=expected_samples_numpy_array,
        )

        for sample_array in instance.samples_per_channel:
            actual_array_count = len(sample_array)

            self.assertEqual(expected_array_count, actual_array_count)
            for index in range(0, expected_array_count):
                self.assertAlmostEqual(
                    first=expected_samples_numpy_array[index],
                    second=sample_array[index],
                    delta=0.0001,
                )


class TestAnalogWaveform(unittest.TestCase):
    """Defines a test fixture that checks
    `AnalogWaveform` class is ready to use.

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

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)
        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_analog_waveform_init_fails_when_channel_name_is_none(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_delta_time_seconds = invert_value(10000)
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=None,
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_channel_name_is_empty(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_delta_time_seconds = invert_value(10000)
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name="",
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_channel_name_is_whitespace(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_delta_time_seconds = invert_value(10000)
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=" ",
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_delta_time_seconds_is_less_than_or_equal_to_zero(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_channel_name = "name_of_channel"
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=expected_channel_name,
                    delta_time_seconds=-0.0001,
                    samples=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The value delta_time_seconds must be greater than 0.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_samples_is_none(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_channel_name = "name_of_channel"
        expected_delta_time_seconds = invert_value(10000)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=expected_channel_name,
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=None,
                )
            )

        self.assertEqual(
            "The object samples is None.",
            str(ctx.exception),
        )

    def test_analog_waveform_init_fails_when_samples_is_empty(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_channel_name = "name_of_channel"
        expected_delta_time_seconds = invert_value(10000)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AnalogWaveform(
                    channel_name=expected_channel_name,
                    delta_time_seconds=expected_delta_time_seconds,
                    samples=numpy.array([]),
                )
            )

        self.assertEqual(
            "The iterable samples of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_analog_waveform(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AnalogWaveform."""
        expected_channel_name = "name_of_channel"
        expected_delta_time_seconds = 1.0 / 10000
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        instance = nipcbatt.AnalogWaveform(
            channel_name=expected_channel_name,
            delta_time_seconds=expected_delta_time_seconds,
            samples=expected_samples_numpy_array,
        )

        actual_channel_name = instance.channel_name
        actual_delta_time_seconds = instance.delta_time_seconds
        actual_samples_numpy_array = instance.samples
        actual_array_count = actual_samples_numpy_array.size

        self.assertEqual(expected_channel_name, actual_channel_name)
        self.assertEqual(expected_delta_time_seconds, actual_delta_time_seconds)
        self.assertEqual(expected_array_count, actual_array_count)
        for index in range(0, expected_array_count):
            self.assertAlmostEqual(
                first=expected_samples_numpy_array[index],
                second=actual_samples_numpy_array[index],
                delta=0.0001,
            )


class TestAmplitudeSpectrum(unittest.TestCase):
    """Defines a test fixture that checks
    `AmplitudeSpectrum` class is ready to use.

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

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)
        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_amplitude_spectrum_init_fails_when_channel_name_is_none(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=None,
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_channel_name_is_empty(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name="",
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_channel_name_is_whitespace(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=" ",
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The string value channel_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_spectrum_frequency_resolution_hertz_is_less_than_or_equal_to_zero(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_channel_name = "name_of_channel"
        expected_spectrum_start_frequency_hertz = 135000
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=expected_channel_name,
                    spectrum_start_frequency_hertz=(expected_spectrum_start_frequency_hertz),
                    spectrum_frequency_resolution_hertz=-1.0,
                    amplitudes=expected_samples_numpy_array,
                )
            )

        self.assertEqual(
            "The value spectrum_frequency_resolution_hertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_amplitudes_is_none(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_channel_name = "name_of_channel"
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=expected_channel_name,
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=None,
                )
            )

        self.assertEqual(
            "The object amplitudes is None.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum_init_fails_when_amplitudes_is_empty(
        self,
    ):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_channel_name = "name_of_channel"
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.AmplitudeSpectrum(
                    channel_name=expected_channel_name,
                    spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
                    spectrum_frequency_resolution_hertz=(
                        expected_spectrum_frequency_resolution_hertz
                    ),
                    amplitudes=numpy.array([]),
                )
            )

        self.assertEqual(
            "The iterable amplitudes of type ndarray is empty.",
            str(ctx.exception),
        )

    def test_amplitude_spectrum(self):
        """Unit test of nipcbatt.pcbatt_library.common.common_data_types.AmplitudeSpectrum."""
        expected_channel_name = "name_of_channel"
        expected_spectrum_start_frequency_hertz = 135000
        expected_spectrum_frequency_resolution_hertz = 1.0
        expected_array_count = 1500
        expected_samples_array = list(
            4.95 + random.random() * 0.1 for i in range(0, expected_array_count)
        )
        expected_samples_numpy_array = numpy.array(expected_samples_array, dtype=numpy.float64)

        instance = nipcbatt.AmplitudeSpectrum(
            channel_name=expected_channel_name,
            spectrum_start_frequency_hertz=expected_spectrum_start_frequency_hertz,
            spectrum_frequency_resolution_hertz=(expected_spectrum_frequency_resolution_hertz),
            amplitudes=expected_samples_numpy_array,
        )

        actual_channel_name = instance.channel_name
        actual_spectrum_start_frequency_hertz = instance.spectrum_start_frequency_hertz
        actual_spectrum_frequency_resolution_hertz = instance.spectrum_frequency_resolution_hertz
        actual_samples_numpy_array = instance.amplitudes
        actual_array_count = actual_samples_numpy_array.size

        self.assertEqual(expected_channel_name, actual_channel_name)
        self.assertEqual(
            expected_spectrum_start_frequency_hertz,
            actual_spectrum_start_frequency_hertz,
        )
        self.assertEqual(
            expected_spectrum_frequency_resolution_hertz,
            actual_spectrum_frequency_resolution_hertz,
        )
        self.assertEqual(expected_array_count, actual_array_count)

        for index in range(0, expected_array_count):
            self.assertAlmostEqual(
                first=expected_samples_numpy_array[index],
                second=actual_samples_numpy_array[index],
                delta=0.0001,
            )


if __name__ == "__main__":
    unittest.main()
