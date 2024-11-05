"""This module provides digital clock data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_data_types import (
    DigitalClockGenerationConfiguration,
    DigitalClockGenerationCounterChannelParameters,
    DigitalClockGenerationData,
    DigitalClockGenerationTimingParameters,
)


class TestDigitalClockGenerationDataTypes(unittest.TestCase):
    """Defines a test fixture to unsure the data types class used for digital clock
       generation are ready to use.

    Args:
        unittest.testCase: Parent class of the unittest framework
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

    def test_digital_clock_generation_timing_parameters(self):
        """Tests if an instance of DigitalClockGenerationTimingParameters is
        created with specific values"""

        expected_duration = 1.0
        instance = DigitalClockGenerationTimingParameters(expected_duration)
        actual_duration = instance.clock_duration_seconds

        self.assertEqual(expected_duration, actual_duration)

    def test_digital_clock_generation_timing_parameters_with_invalid_data(self):
        """Tests if an instance of DigitalClockGenerationTimingParameters throws
        an error if given invalid data"""

        expected_duration = 0.0

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationTimingParameters(expected_duration),
        )

        self.assertRaises(ValueError, lambda: DigitalClockGenerationTimingParameters(None))

    def test_digital_clock_generation_counter_channel_parameters(self):
        """Tests if an instance of DigitalClockGenerationCounterChannelParameters
        is produced with specfic values"""

        expected_frequency = 1000.0
        expected_duty_cycle = 0.95

        instance = DigitalClockGenerationCounterChannelParameters(
            expected_frequency, expected_duty_cycle
        )

        self.assertEqual(expected_frequency, instance.frequency_hertz)
        self.assertEqual(expected_duty_cycle, instance.duty_cycle_ratio)

    def test_digital_clock_generation_counter_channel_parameters_with_invalid_data(
        self,
    ):
        """Tests if an attempted instance of DigitalClockGenerationCounterChannelParameters
        throws an error when given incorrect values"""

        frequency = -0.1  # frequency can't be less than 0
        duty_cycle = 0.5

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationCounterChannelParameters(frequency, duty_cycle),
        )

        frequency = 10
        duty_cycle = 1.1  # duty cycle can't be greater than 1.0

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationCounterChannelParameters(frequency, duty_cycle),
        )

        frequency = 10
        duty_cycle = -0.1  # duty cycle can't be less than 0

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationCounterChannelParameters(frequency, duty_cycle),
        )

    def test_digital_clock_generation_configuration(self):
        """Tests if an instance of DigitalClockGenerationConfiguration is
        successfully created when given the proper arugments"""

        freq = 100.0
        duty_cycle = 0.5
        duration = 1.0

        counter_channel_parameters = DigitalClockGenerationCounterChannelParameters(
            freq, duty_cycle
        )
        timing_parameters = DigitalClockGenerationTimingParameters(duration)

        expected_channel_parameters = counter_channel_parameters
        expected_timing_parameters = timing_parameters

        instance = DigitalClockGenerationConfiguration(
            expected_channel_parameters, expected_timing_parameters
        )

        actual_channel_parameters = instance.counter_channel_parameters
        actual_timing_parameters = instance.timing_parameters

        self.assertEqual(expected_channel_parameters, actual_channel_parameters)
        self.assertEqual(expected_timing_parameters, actual_timing_parameters)

    def test_digital_clock_generation_configuration_with_invalid_data(self):
        """Tests if instantiaion of DigitalClockGenerationConfiguration fails
        when given invalid data"""

        freq = 100.0
        duty_cycle = 0.5
        duration = 1.0

        counter_channel_parameters = None
        timing_parameters = DigitalClockGenerationTimingParameters(duration)

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationConfiguration(
                counter_channel_parameters, timing_parameters
            ),
        )

        counter_channel_parameters = DigitalClockGenerationCounterChannelParameters(
            freq, duty_cycle
        )
        timing_parameters = None

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationConfiguration(
                counter_channel_parameters, timing_parameters
            ),
        )

    def test_digital_clock_generation_data(self):
        """Test if an instance of DigitalClockGenerationData is created
        successfully when given the proper values"""

        expected_timebase_freq = 1000.0
        expected_actual_clock_freq = 100.0
        expected_actual_clock_duty_cycle = 0.5
        expected_actual_clock_duration = 1.0

        instance = DigitalClockGenerationData(
            expected_timebase_freq,
            expected_actual_clock_freq,
            expected_actual_clock_duty_cycle,
            expected_actual_clock_duration,
        )

        self.assertEqual(expected_timebase_freq, instance.timebase_frequency_hertz)
        self.assertEqual(expected_actual_clock_freq, instance.actual_clock_frequency_hertz)
        self.assertEqual(expected_actual_clock_duty_cycle, instance.actual_clock_duty_cycle_ratio)
        self.assertEqual(expected_actual_clock_duration, instance.actual_clock_duration_seconds)

    def test_digital_clock_generation_with_invalid_data(self):
        """Ensures that the attempted creation of an instance of
        DigitalClockGenerationData with invalid data throws an error"""

        expected_timebase_freq = -1
        expected_actual_clock_freq = 100.0
        expected_actual_clock_duty_cycle = 0.5
        expected_actual_clock_duration = 1.0

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationData(
                expected_timebase_freq,
                expected_actual_clock_freq,
                expected_actual_clock_duty_cycle,
                expected_actual_clock_duration,
            ),
        )

        expected_timebase_freq = 1000.0
        expected_actual_clock_freq = -100.0
        expected_actual_clock_duty_cycle = 0.5
        expected_actual_clock_duration = 1.0

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationData(
                expected_timebase_freq,
                expected_actual_clock_freq,
                expected_actual_clock_duty_cycle,
                expected_actual_clock_duration,
            ),
        )

        expected_timebase_freq = 1000.0
        expected_actual_clock_freq = 100.0
        expected_actual_clock_duty_cycle = -0.5
        expected_actual_clock_duration = 1.0

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationData(
                expected_timebase_freq,
                expected_actual_clock_freq,
                expected_actual_clock_duty_cycle,
                expected_actual_clock_duration,
            ),
        )

        expected_timebase_freq = 1000.0
        expected_actual_clock_freq = 100.0
        expected_actual_clock_duty_cycle = 0.5
        expected_actual_clock_duration = -1.0

        self.assertRaises(
            ValueError,
            lambda: DigitalClockGenerationData(
                expected_timebase_freq,
                expected_actual_clock_freq,
                expected_actual_clock_duty_cycle,
                expected_actual_clock_duration,
            ),
        )


if __name__ == "__main__":
    unittest.main()
