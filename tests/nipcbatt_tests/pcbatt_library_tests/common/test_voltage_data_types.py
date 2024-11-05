# pylint: disable=C0116
"""This module provides voltage data types check."""

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
from varname import nameof

import nipcbatt


class TestVoltageRangeAndTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `VoltageRangeAndTerminalParameters` class is ready to use.

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

    def test_voltage_range_and_terminal_parameters(self):
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expected_range_min_volts = -9.0
        expected_range_max_volts = 6.3

        instance = nipcbatt.VoltageRangeAndTerminalParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        actual_terminal_configuration = instance.terminal_configuration
        actual_range_min_volts = instance.range_min_volts
        actual_range_max_volts = instance.range_max_volts

        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expected_range_min_volts, actual_range_min_volts)
        self.assertEqual(expected_range_max_volts, actual_range_max_volts)


class TestVoltageMeasurementChannelAndTerminalRangeParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `VoltageMeasurementChannelAndTerminalRangeParameters` class is ready to use.

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

    def test_voltage_measurement_channel_and_terminal_range_parameters(self):
        expected_terminal_configuration = nidaqmx.constants.TerminalConfiguration.NRSE
        expected_range_min_volts = -9.0
        expected_range_max_volts = 6.3
        expected_channel_name = "Dev/ai0"

        channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
            terminal_configuration=expected_terminal_configuration,
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        instance = nipcbatt.VoltageMeasurementChannelAndTerminalRangeParameters(
            channel_name=expected_channel_name,
            channel_parameters=channel_parameters,
        )

        actual_channel_name = instance.channel_name
        actual_terminal_configuration = instance.channel_parameters.terminal_configuration
        actual_range_min_volts = instance.channel_parameters.range_min_volts
        actual_range_max_volts = instance.channel_parameters.range_max_volts

        self.assertEqual(expected_channel_name, actual_channel_name)
        self.assertEqual(expected_terminal_configuration, actual_terminal_configuration)
        self.assertEqual(expected_range_min_volts, actual_range_min_volts)
        self.assertEqual(expected_range_max_volts, actual_range_max_volts)


class TestVoltageGenerationChannelParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `VoltageGenerationChannelParameters` class is ready to use.

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

    def test_voltage_generation_channel_parameters(self):
        expected_range_min_volts = -3.5
        expected_range_max_volts = 4.0

        instance = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        self.assertEqual(expected_range_min_volts, instance.range_min_volts)
        self.assertEqual(expected_range_max_volts, instance.range_max_volts)

    def test_voltage_generation_channel_parameters_with_invalid_inputs(self):
        """Tests if the instance creation with invalid parameters throws exception as expected"""

        # Test if Valus error is raised when range Max = Min value
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.VoltageGenerationChannelParameters(
                range_min_volts=3.0, range_max_volts=3.0
            ),
        )

        # Test if value error is raised when Min is greater than Max
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.VoltageGenerationChannelParameters(
                range_min_volts=4.0,
                range_max_volts=3.5,
            ),
        )


if __name__ == "__main__":
    unittest.main()
