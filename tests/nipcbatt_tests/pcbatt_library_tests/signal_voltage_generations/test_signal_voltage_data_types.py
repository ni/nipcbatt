"""This module provides Signal Voltage data types check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
from varname import nameof

import nipcbatt


class TestToneParameters(unittest.TestCase):
    """Defines a test fixture that checks
    'ToneParameters' class is ready to use.

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

    def test_tone_parameters(self):
        """Tests if the instance of `ToneParameters` is created as expected"""
        expected_tone_frequency = 100
        expected_amplitude = 1.0
        expected_phase = 0

        instance = nipcbatt.ToneParameters(
            tone_frequency_hertz=expected_tone_frequency,
            tone_amplitude_volts=expected_amplitude,
            tone_phase_radians=expected_phase,
        )

        actual_tone_frequency = instance.tone_frequency_hertz
        actual_amplitude = instance.tone_amplitude_volts
        actual_phase = instance.tone_phase_radians

        self.assertEqual(expected_tone_frequency, actual_tone_frequency)
        self.assertEqual(expected_amplitude, actual_amplitude)
        self.assertEqual(expected_phase, actual_phase)

    def test_tone_parameters_with_invalid_parameters(self):
        """Tests if  expected ValueError is thrown when an instance of
        `ToneParameters` is created with invalid parameters"""

        expected_tone_frequency = 100
        expected_amplitude = 1.0
        expected_phase = 0.785

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.ToneParameters(
                tone_frequency_hertz=0,
                tone_amplitude_volts=expected_amplitude,
                tone_phase_radians=expected_phase,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.ToneParameters(
                tone_frequency_hertz=expected_tone_frequency,
                tone_amplitude_volts=0,
                tone_phase_radians=expected_phase,
            ),
        )


class TestSignalVoltageGenerationTimingParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SignalVoltageGenerationTimingParameters` class is ready to use.

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

    def test_signal_voltage_generation_timing_parameters_init_fails_when_sample_clock_source_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationTimingParameters(
                    sample_clock_source=None,
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters_init_fails_when_sample_clock_source_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationTimingParameters(
                    sample_clock_source="",
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters_init_fails_when_sample_clock_source_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationTimingParameters(
                    sample_clock_source=" ",
                    sampling_rate_hertz=expected_sampling_rate_hertz,
                    generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
                )
            )

        self.assertEqual(
            "The string value sample_clock_source is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters_init_fails_when_sampling_rate_hertz_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """
        expected_sample_clock_source = "OnboardClock"
        expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationTimingParameters(
                    sample_clock_source=expected_sample_clock_source,
                    sampling_rate_hertz=-6,
                    generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
                )
            )

        self.assertEqual(
            "The value sampling_rate_hertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters_init_fails_when_generated_signal_duration_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """
        expected_sample_clock_source = "OnboardClock"
        # expected_generated_signal_duration_seconds = 0.200

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationTimingParameters(
                    sample_clock_source=expected_sample_clock_source,
                    sampling_rate_hertz=1000,
                    generated_signal_duration_seconds=0,
                )
            )

        self.assertEqual(
            "The value generated_signal_duration_seconds must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_timing_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.common.common_data_types.SignalVoltageGenerationTimingParameters.
        """
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.200

        instance = nipcbatt.SignalVoltageGenerationTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
        )

        actual_sample_clock_source = instance.sample_clock_source
        actual_sampling_rate_hertz = instance.sampling_rate_hertz
        actual_generated_signal_duration_seconds = instance.generated_signal_duration_seconds
        self.assertEqual(expected_sample_clock_source, actual_sample_clock_source)
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate_hertz)
        self.assertEqual(
            expected_generated_signal_duration_seconds,
            actual_generated_signal_duration_seconds,
        )


class TestSignalVoltageGenerationSineWaveParameters(unittest.TestCase):
    """Defines a test fixture that checks
    'ToneParameters' class is ready to use.

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

    def test_signal_voltage_generation_sine_wave_parameters(self):
        """Tests if the instance of `SignalVoltageGenerationSineWaveParameters`
        is created as expected"""
        expected_generated_signal_offset_volts = 0.25
        expected_tone_frequency = 100
        expected_amplitude = 1.0
        expected_phase = 0

        expected_generated_signal_tone_parameters = nipcbatt.ToneParameters(
            tone_frequency_hertz=expected_tone_frequency,
            tone_amplitude_volts=expected_amplitude,
            tone_phase_radians=expected_phase,
        )

        instance = nipcbatt.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=expected_generated_signal_offset_volts,
            generated_signal_tone_parameters=expected_generated_signal_tone_parameters,
        )
        actual_generated_signal_offset_volts = instance.generated_signal_offset_volts
        actual_tone_frequency = instance.generated_signal_tone_parameters.tone_frequency_hertz
        actual_amplitude = instance.generated_signal_tone_parameters.tone_amplitude_volts
        actual_phase = instance.generated_signal_tone_parameters.tone_phase_radians

        self.assertEqual(expected_amplitude, actual_amplitude)
        self.assertEqual(expected_tone_frequency, actual_tone_frequency)
        self.assertEqual(expected_phase, actual_phase)
        self.assertEqual(
            expected_generated_signal_offset_volts, actual_generated_signal_offset_volts
        )

    def test_signal_voltage_generation_sine_wave_parameters_init_fails_when_tone_parameters_is_none(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSineWaveParameters` is created with signal_tone_parameters is none.
        """
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationSineWaveParameters(
                    generated_signal_offset_volts=0.0,
                    generated_signal_tone_parameters=None,
                )
            )
        self.assertEqual("The object generated_signal_tone_parameters is None.", str(ctx.exception))


class TestSignalVoltageGenerationSquareWaveParameters(unittest.TestCase):
    """Defines a test fixture that checks
    'SignalVoltageGenerationSquareWaveParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        self._expected_generated_signal_offset_volts = 0.1
        self._expected_generated_signal_frequency_hertz = 50
        self._expected_generated_signal_amplitude_volts = 0.5
        self._expected_generated_signal_duty_cycle_percent = 50.0
        self._expected_generated_signal_phase_radians = 0.2

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

    def test_signal_voltage_generation_square_wave_parameters(self):
        """Tests if the instance of `SignalVoltageGenerationSquareWaveParameters`
        is created as expected"""

        instance = nipcbatt.SignalVoltageGenerationSquareWaveParameters(
            generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
            generated_signal_frequency_hertz=self._expected_generated_signal_frequency_hertz,
            generated_signal_amplitude_volts=self._expected_generated_signal_amplitude_volts,
            generated_signal_duty_cycle_percent=self._expected_generated_signal_duty_cycle_percent,
            generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
        )
        actual_generated_signal_offset_volts = instance.generated_signal_offset_volts
        actual_generated_signal_frequency_hertz = instance.generated_signal_frequency_hertz
        actual_generated_signal_amplitude_volts = instance.generated_signal_amplitude_volts
        actual_generated_signal_duty_cycle_percent = instance.generated_signal_duty_cycle_percent
        actual_generated_signal_phase_radians = instance.generated_signal_phase_radians
        self.assertEqual(
            self._expected_generated_signal_offset_volts,
            actual_generated_signal_offset_volts,
        )
        self.assertEqual(
            self._expected_generated_signal_frequency_hertz,
            actual_generated_signal_frequency_hertz,
        )
        self.assertEqual(
            self._expected_generated_signal_amplitude_volts,
            actual_generated_signal_amplitude_volts,
        )
        self.assertEqual(
            self._expected_generated_signal_duty_cycle_percent,
            actual_generated_signal_duty_cycle_percent,
        )
        self.assertEqual(
            self._expected_generated_signal_phase_radians,
            actual_generated_signal_phase_radians,
        )

    def test_signal_voltage_generation_square_wave_parameters_init_fails_when_signal_frequency_is_less_than_zero(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveParameters` is created with signal frequency is set to 0.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationSquareWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_frequency_hertz=0.0,
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    generated_signal_duty_cycle_percent=(
                        self._expected_generated_signal_duty_cycle_percent
                    ),
                    generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
                )
            )

        self.assertEqual(
            "The value generated_signal_frequency_hertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_square_wave_parameters_init_fails_when_signal_amplitude_is_less_than_zero(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveParameters` is created with signal amplitude is set to 0.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationSquareWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_frequency_hertz=(
                        self._expected_generated_signal_frequency_hertz
                    ),
                    generated_signal_amplitude_volts=0.0,
                    generated_signal_duty_cycle_percent=(
                        self._expected_generated_signal_duty_cycle_percent
                    ),
                    generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
                )
            )

        self.assertEqual(
            "The value generated_signal_amplitude_volts must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_square_wave_parameters_init_fails_when_duty_cycle_is_not_within_limits(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveParameters` is created
        with duty_cycle value not within 0 and 100.
        """

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationSquareWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_frequency_hertz=(
                        self._expected_generated_signal_frequency_hertz
                    ),
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    generated_signal_duty_cycle_percent=102.0,
                    generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
                )
            )

        self.assertEqual(
            "The value of generated_signal_duty_cycle_percent must be greater than 0 and less than 100.",
            str(ctx.exception),
        )

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationSquareWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_frequency_hertz=(
                        self._expected_generated_signal_frequency_hertz
                    ),
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    generated_signal_duty_cycle_percent=0.0,
                    generated_signal_phase_radians=self._expected_generated_signal_phase_radians,
                )
            )

        self.assertEqual(
            "The value of generated_signal_duty_cycle_percent must be greater than 0 and less than 100.",
            str(ctx.exception),
        )


class TestSignalVoltageGenerationMultipleTonesWaveParameters(unittest.TestCase):
    """Defines a test fixture that checks
    'SignalVoltageGenerationMultipleTonesWaveParameters' class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        self._expected_generated_signal_offset_volts = 0.05
        self._expected_generated_signal_amplitude_volts = 0.75

        self._expected_multiple_tones_parameters = []

        self._expected_multiple_tones_parameters.append(
            nipcbatt.ToneParameters(
                tone_frequency_hertz=100,
                tone_amplitude_volts=0.5,
                tone_phase_radians=0.2,
            )
        )

        self._expected_multiple_tones_parameters.append(
            nipcbatt.ToneParameters(
                tone_frequency_hertz=200,
                tone_amplitude_volts=1.0,
                tone_phase_radians=0,
            )
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

    def test_signal_voltage_generation_multiple_tones_wave_parameters(self):
        """Tests if the instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
        is created as expected"""

        instance = nipcbatt.SignalVoltageGenerationMultipleTonesWaveParameters(
            generated_signal_amplitude_volts=self._expected_generated_signal_amplitude_volts,
            generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
            multiple_tones_parameters=self._expected_multiple_tones_parameters,
        )
        actual_generated_signal_offset_volts = instance.generated_signal_offset_volts
        actual_generated_signal_amplitude_volts = instance.generated_signal_amplitude_volts

        actual_multiple_tones_parameters = instance.multiple_tones_parameters

        self.assertEqual(
            self._expected_generated_signal_amplitude_volts,
            actual_generated_signal_amplitude_volts,
        )

        self.assertEqual(
            self._expected_generated_signal_offset_volts,
            actual_generated_signal_offset_volts,
        )
        self.assertCountEqual(
            self._expected_multiple_tones_parameters, actual_multiple_tones_parameters
        )
        self.assertEqual(self._expected_multiple_tones_parameters, actual_multiple_tones_parameters)

    def test_signal_voltage_generation_multiple_tones_wave_parameters_with_signal_amplitude_zero(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationMultipleTonesWaveParameters` is created
        with signal_amplitude is set to 0.
        """
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationMultipleTonesWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_amplitude_volts=0.0,
                    multiple_tones_parameters=self._expected_multiple_tones_parameters,
                )
            )

        self.assertEqual(
            "The value generated_signal_amplitude_volts must be greater than 0.",
            str(ctx.exception),
        )

    def test_signal_voltage_generation_multiple_tones_wave_parameters_with_tones_parameter_is_none(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationMultipleTonesWaveParameters` is created with
        multiple_tones_parameters is set to None.
        """
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationMultipleTonesWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    multiple_tones_parameters=None,
                )
            )

        self.assertEqual("The object multiple_tones_parameters is None.", str(ctx.exception))

    def test_signal_voltage_generation_multiple_tones_wave_parameters_with_tones_parameter_is_empty(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationMultipleTonesWaveParameters` is created with
        multiple_tones_parameters is set to empty list.
        """
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SignalVoltageGenerationMultipleTonesWaveParameters(
                    generated_signal_offset_volts=self._expected_generated_signal_offset_volts,
                    generated_signal_amplitude_volts=(
                        self._expected_generated_signal_amplitude_volts
                    ),
                    multiple_tones_parameters=[],
                )
            )

        self.assertEqual(
            "The iterable multiple_tones_parameters of type list is empty.",
            str(ctx.exception),
        )


class TestSignalVoltageGenerationSineWaveConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    'ToneParametersSignalVoltageGenerationSineWaveConfiguration' class is ready to use.

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

    def test_signal_voltage_generation_sine_wave_configuration(self):
        """Tests if the instance of `SignalVoltageGenerationSineWaveConfiguration`
        is created as expected"""

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000
        expected_generated_signal_duration_seconds = 0.01

        expected_timing_parameters = nipcbatt.SignalVoltageGenerationTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
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

        # Create test values for voltage generation range parameters.
        expected_range_min_volts = -1.0
        expected_range_max_volts = 1.0

        expected_voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        # Create test values for Sine wave signal parameters

        expected_generated_signal_offset_volts = 0.25
        expected_tone_frequency = 100
        expected_amplitude = 1.0
        expected_phase = 0

        expected_generated_signal_tone_parameters = nipcbatt.ToneParameters(
            tone_frequency_hertz=expected_tone_frequency,
            tone_amplitude_volts=expected_amplitude,
            tone_phase_radians=expected_phase,
        )

        expected_waveform_parameters = nipcbatt.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=expected_generated_signal_offset_volts,
            generated_signal_tone_parameters=expected_generated_signal_tone_parameters,
        )

        instance = nipcbatt.SignalVoltageGenerationSineWaveConfiguration(
            voltage_generation_range_parameters=expected_voltage_generation_range_parameters,
            waveform_parameters=expected_waveform_parameters,
            timing_parameters=expected_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        # Log the class name with the values of the instance created for
        # SignalVoltageGenerationSineWaveConfiguration
        logging.debug(
            "%s = %s",
            nameof(nipcbatt.SignalVoltageGenerationSineWaveConfiguration),
            instance,
        )

        self.assertEqual(
            expected_voltage_generation_range_parameters,
            instance.voltage_generation_range_parameters,
        )
        self.assertEqual(expected_waveform_parameters, instance.waveform_parameters)
        self.assertEqual(
            expected_timing_parameters,
            instance.timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            instance.digital_start_trigger_parameters,
        )

    def test_signal_voltage_generation_sine_wave_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationSineWaveConfiguration(
                voltage_generation_range_parameters=None,
                waveform_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationSineWaveConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=None,
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationSineWaveConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
                timing_parameters=None,
                digital_start_trigger_parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationSineWaveConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=None,
            ),
        )


class TestSignalVoltageGenerationSquareWaveConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    'SignalVoltageGenerationSquareWaveConfiguration' class is ready to use.

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

    def test_signal_voltage_generation_square_wave_configuration(self):
        """Tests if the instance of `SignalVoltageGenerationSquareWaveConfiguration`
        is created as expected"""
        # Create test values for signal voltage generation square wave parameters.
        expected_generated_signal_duration_seconds = 0.01
        expected_generated_signal_offset_volts = 0.1
        expected_generated_signal_frequency_hertz = 50
        expected_generated_signal_amplitude_volts = 0.5
        expected_generated_signal_duty_cycle_percent = 50.0
        expected_generated_signal_phase_radians = 0.2

        expected_square_wave_generation_parameters = (
            nipcbatt.SignalVoltageGenerationSquareWaveParameters(
                generated_signal_offset_volts=expected_generated_signal_offset_volts,
                generated_signal_frequency_hertz=expected_generated_signal_frequency_hertz,
                generated_signal_amplitude_volts=expected_generated_signal_amplitude_volts,
                generated_signal_duty_cycle_percent=expected_generated_signal_duty_cycle_percent,
                generated_signal_phase_radians=expected_generated_signal_phase_radians,
            )
        )

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000

        expected_timing_parameters = nipcbatt.SignalVoltageGenerationTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
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

        # Create test values for voltage generation range parameters.
        expected_range_min_volts = -1.0
        expected_range_max_volts = 1.0

        expected_voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        square_wave_configuration = nipcbatt.SignalVoltageGenerationSquareWaveConfiguration(
            voltage_generation_range_parameters=expected_voltage_generation_range_parameters,
            waveform_parameters=expected_square_wave_generation_parameters,
            timing_parameters=expected_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        self.assertEqual(
            expected_voltage_generation_range_parameters,
            square_wave_configuration.voltage_generation_range_parameters,
        )
        self.assertEqual(
            expected_square_wave_generation_parameters,
            square_wave_configuration.waveform_parameters,
        )
        self.assertEqual(
            expected_timing_parameters,
            square_wave_configuration.timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            square_wave_configuration.digital_start_trigger_parameters,
        )

    def test_signal_voltage_generation_square_wave_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if  expected ValueError is thrown when an instance of
        `SignalVoltageGenerationSquareWaveConfiguration` is created with invalid parameters
        """
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationSquareWaveConfiguration(
                voltage_generation_range_parameters=None,
                waveform_parameters=(
                    nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS
                ),
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationSquareWaveConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=None,
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationSquareWaveConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=(
                    nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS
                ),
                timing_parameters=None,
                digital_start_trigger_parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationSquareWaveConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=(
                    nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS
                ),
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=None,
            ),
        )


class TestSignalVoltageGenerationMultipleTonesConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `SignalVoltageGenerationMultipleTonesConfiguration` class is ready to use.

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

    def test_signal_voltage_generation_multiple_tones_configuration(self):
        """Tests if the instance of `SignalVoltageGenerationMultipleTonesConfiguration`
        is created as expected"""
        # Create test values for signal voltage generation multi-tone wave parameters.
        expected_generated_signal_duration_seconds = 0.20
        expected_generated_signal_offset_volts = 0.05
        expected_generated_signal_amplitude_volts = 0.75

        expected_multiple_tones_parameters = []

        expected_multiple_tones_parameters.append(
            nipcbatt.ToneParameters(
                tone_frequency_hertz=100,
                tone_amplitude_volts=0.5,
                tone_phase_radians=0.2,
            )
        )

        expected_multiple_tones_parameters.append(
            nipcbatt.ToneParameters(
                tone_frequency_hertz=200,
                tone_amplitude_volts=1.0,
                tone_phase_radians=0,
            )
        )

        expected_multi_tone_parameters = (
            nipcbatt.SignalVoltageGenerationMultipleTonesWaveParameters(
                generated_signal_amplitude_volts=expected_generated_signal_amplitude_volts,
                generated_signal_offset_volts=expected_generated_signal_offset_volts,
                multiple_tones_parameters=expected_multiple_tones_parameters,
            )
        )

        # Create test values for the Sample clock timing parameters
        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 10000

        expected_timing_parameters = nipcbatt.SignalVoltageGenerationTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            generated_signal_duration_seconds=expected_generated_signal_duration_seconds,
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

        # Create test values for voltage generation range parameters.
        expected_range_min_volts = -1.0
        expected_range_max_volts = 1.0

        expected_voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        multi_tone_generation_configuration = (
            nipcbatt.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=expected_voltage_generation_range_parameters,
                waveform_parameters=expected_multi_tone_parameters,
                timing_parameters=expected_timing_parameters,
                digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
            )
        )

        self.assertEqual(
            expected_voltage_generation_range_parameters,
            multi_tone_generation_configuration.voltage_generation_range_parameters,
        )
        self.assertEqual(
            expected_multi_tone_parameters,
            multi_tone_generation_configuration.waveform_parameters,
        )
        self.assertEqual(
            expected_timing_parameters,
            multi_tone_generation_configuration.timing_parameters,
        )
        self.assertEqual(
            expected_digital_start_trigger_parameters,
            multi_tone_generation_configuration.digital_start_trigger_parameters,
        )

    def test_signal_voltage_generation_multiple_tones_configuration_with_invalid_parameters(
        self,
    ):
        """Tests if the instance creation with invalid parameters throws exception as expected"""

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=None,
                waveform_parameters=nipcbatt.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )

        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=None,
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=nipcbatt.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
                timing_parameters=None,
                digital_start_trigger_parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.SignalVoltageGenerationMultipleTonesConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
                ),
                waveform_parameters=nipcbatt.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
                digital_start_trigger_parameters=None,
            ),
        )


if __name__ == "__main__":
    unittest.main()
