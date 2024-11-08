"""This module provides Digital pulse data types check."""

import importlib.metadata  # noqa: F401 - 'importlib.metadata' imported but unused (auto-generated noqa)
import logging  # noqa: F401 - 'logging' imported but unused (auto-generated noqa)
import sys  # noqa: F401 - 'sys' imported but unused (auto-generated noqa)
import unittest

import nidaqmx.constants  # noqa: F401 - 'nidaqmx.constants' imported but unused (auto-generated noqa)
from varname import (  # noqa: F401 - 'varname.nameof' imported but unused (auto-generated noqa)
    nameof,
)

from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_constants import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_data_types import (
    DigitalPulseGenerationConfiguration,
    DigitalPulseGenerationCounterChannelParameters,
    DigitalPulseGenerationData,
    DigitalPulseGenerationTimingParameters,
)


class TestDigitalPulseGenerationDataTypes(unittest.TestCase):
    """Defines a test fixture to test the data types used in
       digital pulse generation

    Args:
        unittest.TestCase: Base class from which this class inherits
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def test_digital_pulse_counter_channel_parameters(self):
        """Tests if an instance of 'DigitalPulseGenerationCounterChannelParameters
        is created when given correct values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (417 > 100 characters) (auto-generated noqa)

        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = 0.5

        instance = DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high)

        self.assertEqual(idle_state, instance.pulse_idle_state)
        self.assertEqual(t_low, instance.low_time_seconds)
        self.assertEqual(t_high, instance.high_time_seconds)
        self.assertIsInstance(instance, DigitalPulseGenerationCounterChannelParameters)

    def test_digital_pulse_generation_counter_channel_parameters_invalid(self):
        """Ensures an instance of DigitalPulseGenerationCounterChannel parameters
        is not generated when given invalid values"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (423 > 100 characters) (auto-generated noqa)

        idle_state = None
        t_low = 0.5
        t_high = 0.5

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = None
        t_high = 0.5

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = -0.1
        t_high = 0.5

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = int(1)
        t_high = 0.5

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = None

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = -0.1

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = int(1)

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high),
        )

    def test_digital_pulse_generation_timing_parameters(self):
        """Tests if an instance of DigitalPulseGenerationTimingParameters
        is created successfully when given valid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (432 > 100 characters) (auto-generated noqa)

        count = 10
        instance = DigitalPulseGenerationTimingParameters(count)
        self.assertEqual(count, instance.pulses_count)
        self.assertIsInstance(instance, DigitalPulseGenerationTimingParameters)

    def test_digital_pulse_generation_timing_parameters_invalid(self):
        """Ensures an instance of DigitalPulseGenerationTimingParameters
        is not created when given invalid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (425 > 100 characters) (auto-generated noqa)

        count = None
        self.assertRaises(ValueError, lambda: DigitalPulseGenerationTimingParameters(count))

        count = float(1.99)
        self.assertRaises(ValueError, lambda: DigitalPulseGenerationTimingParameters(count))

        count = -1
        self.assertRaises(ValueError, lambda: DigitalPulseGenerationTimingParameters(count))

    def test_digital_pulse_generation_configuration(self):
        """Ensures an instance of DigitalPulseGenerationConfiguration is
        created when given correct parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (418 > 100 characters) (auto-generated noqa)

        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = 0.5
        count = 10
        cc_params = DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high)
        t_params = DigitalPulseGenerationTimingParameters(count)

        instance = DigitalPulseGenerationConfiguration(cc_params, t_params)

        self.assertEqual(cc_params, instance.counter_channel_parameters)
        self.assertEqual(t_params, instance.timing_parameters)
        self.assertIsInstance(instance, DigitalPulseGenerationConfiguration)

    def test_digital_pulse_generation_configuration_invalid_params(self):
        """Ensures that the creation of an instance of
        DigitalPusleGenerationConfiguration fails when given
        invalid data"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (393 > 100 characters) (auto-generated noqa)

        idle_state = ConstantsForDigitalPulseGeneration.DEFAULT_GENERATION_IDLE_STATE
        t_low = 0.5
        t_high = 0.5
        count = 10
        cc_params = None
        t_params = DigitalPulseGenerationTimingParameters(count)

        self.assertRaises(
            ValueError, lambda: DigitalPulseGenerationConfiguration(cc_params, t_params)
        )

        cc_params = DigitalPulseGenerationCounterChannelParameters(idle_state, t_low, t_high)
        t_params = None

        self.assertRaises(
            ValueError, lambda: DigitalPulseGenerationConfiguration(cc_params, t_params)
        )

    def test_digital_pulse_generation_data(self):
        """Tests if an instance of DigitalPulseGenerationData is correctly
        created when given correct input"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (413 > 100 characters) (auto-generated noqa)

        freq = 10.0
        duration = 10.0
        low_time = 10.0
        high_time = 10.0

        instance = DigitalPulseGenerationData(freq, duration, low_time, high_time)

        self.assertEqual(freq, instance.timebase_frequency_hertz)
        self.assertEqual(duration, instance.actual_pulse_train_duration_seconds)
        self.assertEqual(low_time, instance.actual_pulse_low_time_seconds)
        self.assertEqual(high_time, instance.actual_pulse_high_time_seconds)

    def test_digital_pulse_generation_data_invalid(self):
        """Ensures an instance of DigitalPulseGenerationData is not created
        when given invalid parameters"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (410 > 100 characters) (auto-generated noqa)

        freq = None
        duration = 10.0
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = int(10)
        duration = 10.0
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = -10.0
        duration = 10.0
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = None
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = int(10)
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = -10.0
        low_time = 10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = None
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = int(10)
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = -10.0
        high_time = 10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = 10.0
        high_time = None

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = 10.0
        high_time = int(10)

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )

        freq = 10.0
        duration = 10.0
        low_time = 10.0
        high_time = -10.0

        self.assertRaises(
            ValueError,
            lambda: DigitalPulseGenerationData(freq, duration, low_time, high_time),
        )


if __name__ == "__main__":
    unittest.main()
