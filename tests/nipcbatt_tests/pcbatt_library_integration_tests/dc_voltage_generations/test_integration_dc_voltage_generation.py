"""This module provides test of integration of DcVoltageGeneration."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestIntegrationDcVoltageGeneration(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `DcVoltageGeneration` class.

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
        _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_voltage_generation_generate_only(self):
        """Checks if class `DcVoltageGeneration' can generate with just the initial configurations"""  # noqa: W505, D202, D415 - doc line too long (101 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        generation = nipcbatt.DcVoltageGeneration()
        generation.initialize(
            analog_output_channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0"
        )
        generation.generate_voltage(output_voltages=[0.8])
        generation.close()

    def test_dc_voltage_generation_generate_voltage_with_configure_and_generate_in_loop(
        self,
    ):
        """Checks if class `DcVoltageGeneration' can configure and generate when they are called one after the other."""  # noqa: W505, D202 - doc line too long (120 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa)

        generation_channel_parameters_1 = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=-5.0,
            range_max_volts=5.0,
        )
        output_voltages_1 = [2.0, 3.7]

        generation_channel_parameters_2 = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=-8.0,
            range_max_volts=8.0,
        )
        output_voltages_2 = [6.5, 7.5]

        output_voltages_3 = [1.2, 2.8]

        # Create a list of tuples of VoltageGenerationChannelParameters and output_voltages to test
        parameters_list = []
        parameters_list.append((generation_channel_parameters_1, output_voltages_1))
        parameters_list.append((generation_channel_parameters_2, output_voltages_2))

        generation = nipcbatt.DcVoltageGeneration()
        generation.initialize(
            analog_output_channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )

        # With the instance of DCVoltageGeneration Initialized, test for configure and generate in loop with different Voltage ranges  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
        for generation_parameters, output_voltages_list in parameters_list:
            generation.configure_all_channels(
                parameters=generation_parameters,
            )
            generation.generate_voltage(output_voltages_list)

        # With the same configuration, test for generate_voltage consecutively with a different set output_voltages  # noqa: W505 - doc line too long (115 > 100 characters) (auto-generated noqa)
        generation.generate_voltage(output_voltages_3)
        generation.close()

    def test_dc_voltage_generation_generate_voltage_with_incorrect_output_voltages(
        self,
    ):
        """Checks if class `DcVoltageGeneration' throws expected error when called with invalid output_voltages"""  # noqa: W505, D202, D415 - doc line too long (114 > 100 characters) (auto-generated noqa), No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

        generation = nipcbatt.DcVoltageGeneration()
        generation.initialize(
            analog_output_channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_all_channels(
            parameters=nipcbatt.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
        )
        # The generate_voltage with valid output_voltages shoudl not throw any error
        generation.generate_voltage([0.5, 0.7])

        # Checks if the expected error is thrown when the size of output_voltages is more than the number of channels.  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: generation.generate_voltage(output_voltages=[1.0, 2.0, 2.8]),
        )

        # Checks if the expected error is thrown when the size of output_voltages is less than the number of channels.  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
        self.assertRaises(
            ValueError,
            lambda: generation.generate_voltage(output_voltages=[1.5]),
        )

        # Checks if the expected error is thrown when the output_voltages is an empty array.
        self.assertRaises(ValueError, lambda: generation.generate_voltage(output_voltages=[]))
        generation.close()


if __name__ == "__main__":
    unittest.main()
