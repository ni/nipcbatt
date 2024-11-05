"""This module provides state digital state data types check."""

import importlib.metadata
import logging
import random
import string
import sys
import unittest

from varname import nameof

import nipcbatt


class TestStaticDigitalStateGenerationData(unittest.TestCase):
    """Defines a test fixture that ensures the class
       'StaticDigitalStateGenerationData' is correct and
       ready to use

    Args:
        unittest.TestCase: Base class from which this class inherits
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

    def test_static_digital_state_generation_data(self):
        """Tests the creation of a StaticDigitalStateGenerationData object"""
        num_channels = 20
        name_length = 9

        expected_channel_identifiers = [
            "".join(random.choice(string.ascii_letters + string.digits) for n in range(name_length))
            for item in range(num_channels)
        ]

        instance = nipcbatt.StaticDigitalStateGenerationData(
            channel_identifiers=expected_channel_identifiers
        )

        actual_channel_identifiers = instance.channel_identifiers
        self.assertTrue((expected_channel_identifiers == actual_channel_identifiers))

    def test_static_digital_state_generation_data_with_invalid_data(self):
        """Tests the creation of an instance of StaticDigitalStateGeneration
        when using invalid data. It should produce and catch the associated error.
        """

        # Test if a value error is thrown when channel_identifiers is None
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.StaticDigitalStateGenerationData(channel_identifiers=None),
        )

        # Test is a value error is thrown when channel_identifiers is empty
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.StaticDigitalStateGenerationData(channel_identifiers=[]),
        )

    def test_static_digital_state_generation_configuration(self):
        """Tests the creation of an instance of StaticDigitalStateGeneration"""
        num_states = 20

        expected_data_to_write = [random.choice([True, False]) for item in range(0, num_states)]

        # create instance with generated digital states
        instance = nipcbatt.StaticDigitalStateGenerationConfiguration(
            data_to_write=expected_data_to_write
        )

        # verify states are created correctly
        actual_data_to_write = instance.data_to_write

        self.assertTrue((expected_data_to_write == actual_data_to_write))

    def test_static_digital_state_generation_configuration_with_invalid_data(self):
        """Create an instance of DigitalStateGenerationConfiguration which is
        invalid and ensure this throws an error
        """

        # create instance with data_to_write as None
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.StaticDigitalStateGenerationConfiguration(data_to_write=None),
        )

        # create instance with data_to_write empty
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.StaticDigitalStateGenerationConfiguration(data_to_write=[]),
        )


if __name__ == "__main__":
    unittest.main()
