"""This module provides digital frequency data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_data_types import (
    DigitalFrequencyMeasurementConfiguration,
    DigitalFrequencyMeasurementCounterChannelParameters,
    DigitalFrequencyMeasurementResultData,
    DigitalFrequencyRangeParameters,
)


class TestDigitalFrequencyRangeParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DigitalFrequencyRangeParameters` class is ready to use.

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

    def test_digital_frequency_range_parameters(self):
        """Tests if an instance of `DigitalFrequencyRangeParameters`
        is created with the specific values.
        """

        expected_minimum_frequency = 1.0
        expected_maximum_frequency = 999999999.0

        instance = DigitalFrequencyRangeParameters(
            frequency_minimum_value_hertz=expected_minimum_frequency,
            frequency_maximum_value_hertz=expected_maximum_frequency,
        )

        actual_minimum_frequency = instance.frequency_minimum_value_hertz
        actual_maximum_frequency = instance.frequency_maximum_value_hertz

        self.assertEqual(expected_minimum_frequency, actual_minimum_frequency)
        self.assertEqual(expected_maximum_frequency, actual_maximum_frequency)

    def test_digital_frequency_range_parameters_with_invalid_data(self):
        """Tests if an instance of `DigitalFrequencyRangeParameters`
        is created with the invalid values.
        """

        expected_minimum_frequency = None
        expected_maximum_frequency = 999999999.0

        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

        expected_minimum_frequency = -0.01
        expected_maximum_frequency = 999999999.0

        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

        expected_minimum_frequency = 1.0
        expected_maximum_frequency = None

        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

        expected_minimum_frequency = 1.0
        expected_maximum_frequency = -0.01

        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

        expected_minimum_frequency = 10.0
        expected_maximum_frequency = 5.0

        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyRangeParameters(
                frequency_minimum_value_hertz=expected_minimum_frequency,
                frequency_maximum_value_hertz=expected_maximum_frequency,
            ),
        )

    def test_digital_frequency_measurement_configuration(self):
        """Tests if an instance of DigitalFrequencyMeasurementConfiguration
        is created successfully when given correct input
        """

        min_freq = 1.0
        max_freq = 999999999.0

        expected_range_param = DigitalFrequencyRangeParameters(min_freq, max_freq)
        expected_input_divisor = 100.0
        expected_duration = 1.0

        expected_config = DigitalFrequencyMeasurementCounterChannelParameters(
            expected_range_param, expected_input_divisor, expected_duration
        )

        instance = DigitalFrequencyMeasurementConfiguration(expected_config)

        actual_config = instance.counter_channel_configuration_parameters

        self.assertEqual(expected_config, actual_config)

    def test_digital_frequency_measurement_configuration_with_invalid_data(self):
        """Tests if an instance of DigitalFrequencyMeasurementConfiguration
        throws errors during instantiation when given incorrect input
        """

        # DigitalFrequencyMeasurementCounterChannelParameters is None
        self.assertRaises(ValueError, lambda: DigitalFrequencyMeasurementConfiguration(None))

    def test_digital_frequency_measurement_counter_channel_parameters(self):
        """Tests if an instance of DigitalFrequencyMeasurementCounterChannelParameters
        is created successfully when given correct input
        """

        expected_min_freq = 0.0
        expected_max_freq = 999999999.0
        expected_range_param = DigitalFrequencyRangeParameters(expected_min_freq, expected_max_freq)
        expected_input_divisor = 100.0
        expected_duration = 1.0

        instance = DigitalFrequencyMeasurementCounterChannelParameters(
            expected_range_param, expected_input_divisor, expected_duration
        )

        actual_min_frequency = instance.range_parameters.frequency_minimum_value_hertz
        actual_max_frequency = instance.range_parameters.frequency_maximum_value_hertz
        actual_input_divisor = instance.input_divisor_for_frequency_measurement
        actual_measurement_duration = instance.measurement_duration_seconds

        self.assertEqual(actual_min_frequency, expected_min_freq)
        self.assertEqual(actual_max_frequency, expected_max_freq)
        self.assertEqual(actual_input_divisor, expected_input_divisor)
        self.assertEqual(actual_measurement_duration, expected_duration)

    def test_digital_frequency_measurement_counter_channel_parameters_with_invalid_data(
        self,
    ):
        """Tests if an instance of DigitalFrequencyMeasurementCounterChannelParameters
        throws errors when given incorrect input
        """

        min_frequency = 0.0
        max_frequency = 999999999.0
        range_parameters = DigitalFrequencyRangeParameters(min_frequency, max_frequency)
        input_divisor = 10.0
        measurement_duration = 1.0

        # range_parameters is None
        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyMeasurementCounterChannelParameters(
                None, input_divisor, measurement_duration
            ),
        )

        # input_divisor is None
        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, None, measurement_duration
            ),
        )

        # input_divisor is 0
        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, 0, measurement_duration
            ),
        )

        # measurement_duration is None
        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, input_divisor, None
            ),
        )

        # measurment_duration is 0
        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, input_divisor, 0
            ),
        )

    def test_digital_frequency_measurement_result_data(self):
        """Tests if an instance of DigitalFrequencyMeasurementResultData
        is generated correctly when given correct data
        """

        expected_frequency = 10000000
        instance = DigitalFrequencyMeasurementResultData(expected_frequency)
        self.assertEqual(expected_frequency, instance.frequency)

    def test_digital_frequency_measurement_result_data_with_invalid_data(self):
        """Tests if an instance of DigitalFrequencyMeasurementResultData
        throws an error when given incorrect data
        """

        expected_frequency = None
        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyMeasurementResultData(expected_frequency),
        )

        expected_frequency = -0.1
        self.assertRaises(
            ValueError,
            lambda: DigitalFrequencyMeasurementResultData(expected_frequency),
        )


if __name__ == "__main__":
    unittest.main()
