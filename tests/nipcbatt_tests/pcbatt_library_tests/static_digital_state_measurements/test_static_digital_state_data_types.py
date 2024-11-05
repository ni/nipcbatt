"""This module provides Static digital state data types check."""

import importlib.metadata
import logging
import random
import string
import sys
import unittest
from typing import Dict

from varname import nameof

import nipcbatt


class TestStaticDigitalStateMeasurementResultData(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'StaticDigitalStateMeasurementResultData' is correct
       and ready to use

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

    def test_static_digital_state_measurement_result_data(self):
        """Tests the creation of a StaticDigitalStateMeasurementResultData object"""
        expected_digital_states = [random.choice([True, False]) for item in range(0, 20)]
        expected_channel_identifiers = [
            "".join(random.choice(string.ascii_letters + string.digits) for n in range(4))
            for item in range(20)
        ]

        # create channel states map to check against instance
        expected_states_per_channels: Dict[str, bool] = {}
        for i, state in enumerate(expected_digital_states):
            expected_states_per_channels[expected_channel_identifiers[i]] = state

        instance = nipcbatt.StaticDigitalStateMeasurementResultData(
            digital_states=expected_digital_states,
            channel_identifiers=expected_channel_identifiers,
        )

        actual_digital_states = instance.digital_states
        actual_channel_identifiers = instance.channel_identifiers
        actual_states_per_channels = instance.states_per_channels

        self.assertTrue((expected_digital_states == actual_digital_states))
        self.assertTrue((expected_channel_identifiers == actual_channel_identifiers))
        self.assertTrue((expected_states_per_channels == actual_states_per_channels))

    def test_static_digital_state_measurement_result_data_with_invalid_data(self):
        """Tests if expected error is thrown when creating an instance of
        'StaticDigitalStateMeasurementResultData with invalid data"""

        expected_digital_states = [random.choice([True, False]) for item in range(0, 20)]
        expected_channel_identifiers = [
            "".join(random.choice(string.ascii_letters + string.digits) for n in range(4))
            for item in range(20)
        ]

        # create channel states map to check against instance
        expected_channel_states: Dict[str, bool] = {}
        for i, state in enumerate(expected_digital_states):
            expected_channel_states[expected_channel_identifiers[i]] = state

        # Test if a value error is thrown when digital_states is None
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.StaticDigitalStateMeasurementResultData(
                digital_states=None, channel_identifiers=expected_channel_identifiers
            ),
        )

        # Test if a value error is thrown when digital_states is empty
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.StaticDigitalStateMeasurementResultData(
                digital_states=[], channel_identifiers=expected_channel_identifiers
            ),
        )

        # Test if a value error is thrown when channel_identifiers is None
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.StaticDigitalStateMeasurementResultData(
                digital_states=expected_digital_states, channel_identifiers=None
            ),
        )

        # Test if a value error is thrown when channel_identifiers is empty
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.StaticDigitalStateMeasurementResultData(
                digital_states=expected_digital_states, channel_identifiers=[]
            ),
        )


if __name__ == "__main__":
    unittest.main()
