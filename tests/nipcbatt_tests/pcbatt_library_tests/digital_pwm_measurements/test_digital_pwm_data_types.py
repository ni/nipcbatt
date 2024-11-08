"""This module provides digital PWM data types check."""

import importlib.metadata
import logging
import sys
import unittest

import numpy as np

# import numpy as np
from varname import (  # noqa: I202 - Additional newline in a group of imports. 'from varname import nameof' is identified as Third Party and 'import numpy' is identified as Third Party. (auto-generated noqa)
    nameof,
)

from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_data_types import (
    DigitalPwmMeasurementCounterChannelParameters,
    DigitalPwmMeasurementData,
    DigitalPwmMeasurementRangeParameters,
    DigitalPwmMeasurementResultData,
    DigitalPwmMeasurementTimingParameters,
)


class TestDigitalPwmMeasurementDataTypes(unittest.TestCase):
    """Defines a test fixture to unsure the data types class used for digital PWM
       measurement are ready to use.

    Args:
        unittest.testCase: Parent class of the unittest framework"""  # noqa: D205, D209, D414, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Section has no content (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (413 > 100 characters) (auto-generated noqa)

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

    def test_dpwmm_range_parameters(self):
        """Tests if an instance of DigitalPwmMeasurementRangeParameters is
        created when given correct values"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (337 > 100 characters) (auto-generated noqa)
        ex_min_value_seconds = 0.005
        ex_max_value_seconds = 0.5

        instance = DigitalPwmMeasurementRangeParameters(ex_min_value_seconds, ex_max_value_seconds)

        self.assertIsInstance(instance, DigitalPwmMeasurementRangeParameters)

        self.assertEqual(ex_min_value_seconds, instance.semi_period_minimum_value_seconds)
        self.assertEqual(ex_max_value_seconds, instance.semi_period_maximum_value_seconds)

    def test_dpwmm_range_parameters_invalid_input(self):
        """Ensures an instance of DigitalPwmMeasurementRangeParameters is
        not created when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        min_val_seconds = 0.0
        max_value_seconds = 1.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

        min_val_seconds = None
        max_value_seconds = 1.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

        min_val_seconds = 0.05
        max_value_seconds = 100.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

        min_val_seconds = 0.05
        max_value_seconds = None

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

        # min_val > max_val
        min_val_seconds = 5.0
        max_value_seconds = 4.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementRangeParameters(min_val_seconds, max_value_seconds),
        )

    def test_dpwmm_timing_parameters(self):
        """Tests if an instance of DigitalPwmMeasurementTimingParameters is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        cycles_count = 42
        instance = DigitalPwmMeasurementTimingParameters(cycles_count)

        self.assertIsInstance(instance, DigitalPwmMeasurementTimingParameters)
        self.assertEqual(cycles_count, instance.semi_period_counter_wanted_cycles_count)

    def test_dpwmm_timing_parameters_invalid_input(self):
        """Ensures an instance of DigitalPwmMeasurementTimingParameters is
        not created when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        cycles_count = -0.1
        self.assertRaises(ValueError, lambda: DigitalPwmMeasurementTimingParameters(cycles_count))

        cycles_count = 2147483648
        self.assertRaises(ValueError, lambda: DigitalPwmMeasurementTimingParameters(cycles_count))

        cycles_count = None
        self.assertRaises(ValueError, lambda: DigitalPwmMeasurementTimingParameters(cycles_count))

    def test_dpwmm_counter_channel_parameters(self):
        """Tests if an instance of DigitalPwmMeasurementCounterChannelParameters is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        range_params = DigitalPwmMeasurementRangeParameters(1.0, 10.0)
        timing = DigitalPwmMeasurementTimingParameters(10.0)
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE

        instance = DigitalPwmMeasurementCounterChannelParameters(range_params, timing, edge)

        self.assertIsInstance(instance, DigitalPwmMeasurementCounterChannelParameters)
        self.assertEqual(range_params, instance.range_parameters)
        self.assertEqual(timing, instance.timing_parameters)
        self.assertEqual(edge, instance.semi_period_counter_starting_edge)

    def test_dpwmm_counter_channel_parameters_invalid_data(self):
        """Ensures an instance of DigitalPwmMeasurementCounterChannelParameters is
        not created when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        range_params = None
        timing = DigitalPwmMeasurementTimingParameters(10.0)
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementCounterChannelParameters(range_params, timing, edge),
        )

        range_params = DigitalPwmMeasurementRangeParameters(1.0, 10.0)
        timing = None
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementCounterChannelParameters(range_params, timing, edge),
        )

        range_params = DigitalPwmMeasurementRangeParameters(1.0, 10.0)
        timing = DigitalPwmMeasurementTimingParameters(10.0)
        edge = None

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementCounterChannelParameters(range_params, timing, edge),
        )

    def test_dpwmm_data(self):
        """Tests if an instance of DigitalPwmMeasurementData is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        data = np.array([1, 2, 3, 4, 5])
        instance = DigitalPwmMeasurementData(data)

        self.assertIsInstance(instance, DigitalPwmMeasurementData)
        self.assertEqual(data.all(), instance.data.all())

    def test_dpwmm_data_invalid_input(self):
        """Ensures an instance of DigitalPwmMeasurementCounterChannelParameters is
        not created when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        data = None
        self.assertRaises(ValueError, lambda: DigitalPwmMeasurementData(data))

        data = np.array([])
        self.assertRaises(ValueError, lambda: DigitalPwmMeasurementData(data))

    def test_dpwmm_result_data(self):
        """Tests if an instance of DigitalPwmMeasurementResultData is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        instance = DigitalPwmMeasurementResultData(
            actual_cycles_count,
            duty_cycle,
            period_duration,
            frequency,
            high_state_duration,
            low_state_duration,
        )

        self.assertIsInstance(instance, DigitalPwmMeasurementResultData)
        self.assertEqual(actual_cycles_count, instance.actual_cycles_count)
        self.assertEqual(duty_cycle, instance.duty_cycle)
        self.assertEqual(period_duration, instance.period_duration)
        self.assertEqual(frequency, instance.frequency)
        self.assertEqual(high_state_duration, instance.high_state_duration)
        self.assertEqual(low_state_duration, instance.low_state_duration)

    def test_dpwmm_result_data_invalid_input(self):
        """Tests if an instance of DigitalPwmMeasurementResultData is
        created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (414 > 100 characters) (auto-generated noqa)

        actual_cycles_count = None
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = -1
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = None
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = -0.1
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 1.1
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = None
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = -0.1
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = None
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = -0.1
        high_state_duration = 0.4
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = None
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = -0.1
        low_state_duration = 0.4

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = None

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )

        actual_cycles_count = 10
        duty_cycle = 0.5
        period_duration = 0.8
        frequency = 1000.0
        high_state_duration = 0.4
        low_state_duration = -0.1

        self.assertRaises(
            ValueError,
            lambda: DigitalPwmMeasurementResultData(
                actual_cycles_count,
                duty_cycle,
                period_duration,
                frequency,
                high_state_duration,
                low_state_duration,
            ),
        )


if __name__ == "__main__":
    unittest.main()
