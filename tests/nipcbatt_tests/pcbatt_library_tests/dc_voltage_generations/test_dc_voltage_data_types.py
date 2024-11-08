"""This module provides DC Voltage data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt


class TestDcVoltageGenerationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    'DcVoltageGenerationConfiguration' class is ready to use.

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

    def test_dc_voltage_generation_configuration(self):
        """Tests if the instance of `DcVoltageGenerationConfiguration` is created as expected"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (207 > 100 characters) (auto-generated noqa)
        expected_range_min_volts = -5.0
        expected_range_max_volts = 5.0
        expected_output_voltages = [1.2, 2.8, 3.2]
        expected_voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=expected_range_min_volts,
            range_max_volts=expected_range_max_volts,
        )

        instance = nipcbatt.DcVoltageGenerationConfiguration(
            voltage_generation_range_parameters=expected_voltage_generation_range_parameters,
            output_voltages=expected_output_voltages,
        )

        actual_range_min_volts = instance.voltage_generation_range_parameters.range_min_volts
        actual_range_max_volts = instance.voltage_generation_range_parameters.range_max_volts
        actual_output_voltages = instance.output_voltages

        self.assertEqual(expected_range_min_volts, actual_range_min_volts)
        self.assertEqual(expected_range_max_volts, actual_range_max_volts)

        self.assertListEqual(expected_output_voltages, actual_output_voltages)

    def test_dc_voltage_generation_configuration_with_empty_channel_parameters(self):
        """Tests if the Value error is raised when tried to create an
        instance of `DcVoltageGenerationConfiguration` with empty channel parameters"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (380 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.DcVoltageGenerationConfiguration(
                voltage_generation_range_parameters=None,
                output_voltages=[],
            ),
        )

    def test_dc_voltage_generation_configuration_with_empty_output_voltages(self):
        """Tests if the Value error is raised when tried to create an
        instance of `DcVoltageGenerationConfiguration` with empty output_voltages array
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.DcVoltageGenerationConfiguration(
                voltage_generation_range_parameters=(
                    nipcbatt.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS
                ),
                output_voltages=[],
            ),
        )


if __name__ == "__main__":
    unittest.main()
