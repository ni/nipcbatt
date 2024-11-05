"""This module provides test of integration of StaticDigitalStateGeneration."""

import importlib
import logging
import random
import sys
import unittest

from nidaqmx.errors import DaqError
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx_if_not_installed,
)


class TestIntegrationStaticDigitalStateGeneration(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'StaticDigitalStateGeneration' class

    Args:
        unittest.TestCase: Base class of the unittest framework
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
        _replace_daqmx_if_not_installed(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_num_channels_8(self):
        """Integration test ensuring the module creates the correct output
        when given 8 channels of data to write
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # create configuration object
        num_channels = 8
        test_data_to_write = [random.choice([True, False]) for item in range(num_channels)]
        cfg = nipcbatt.StaticDigitalStateGenerationConfiguration(data_to_write=test_data_to_write)

        with nipcbatt.StaticDigitalStateGeneration() as gen:
            test_channel_expression = (
                "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:7"
            )

            gen.initialize(channel_expression=test_channel_expression)
            generated_data = gen.configure_and_generate(cfg)

            expected_generated_data = []
            for i in range(len(generated_data.channel_identifiers)):
                n = test_channel_expression.find("line") + len("line")
                expected_generated_data.append(test_channel_expression[0:n] + str(i))

        self.assertTrue(generated_data.channel_identifiers == expected_generated_data)

    def test_integration_num_channels_23(self):
        """Integration test ensuring the module creates the correct output
        when given 23 channels of data to write
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # create configuration object
        num_channels = 23
        test_data_to_write = [random.choice([True, False]) for item in range(num_channels)]
        cfg = nipcbatt.StaticDigitalStateGenerationConfiguration(data_to_write=test_data_to_write)

        with nipcbatt.StaticDigitalStateGeneration() as gen:
            test_channel_expression = (
                "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:22"
            )

            gen.initialize(channel_expression=test_channel_expression)
            generated_data = gen.configure_and_generate(cfg)

            expected_generated_data = []
            for i in range(len(generated_data.channel_identifiers)):
                n = test_channel_expression.find("line") + len("line")
                expected_generated_data.append(test_channel_expression[0:n] + str(i))

        self.assertTrue(generated_data.channel_identifiers == expected_generated_data)

    def test_integration_channel_expression_is_empty(self):
        """Integration test ensuring that is channel expression
        is empty then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression="")

            gen.close()

    def test_integration_channel_expression_is_none(self):
        """Integration test ensuring that is channel expression
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateGeneration() as gen:
            with self.assertRaises(ValueError):
                gen.initialize(channel_expression=None)

            gen.close()

    def test_integration_channel_expression_port(self):
        """Integration test ensuring that the channel expression
        value consisting of only 'port' with channel
        designated will throw an error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateGeneration() as gen:
            with self.assertRaises(DaqError) as ctx:
                gen.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0"
                )

            print(ctx.exception)

            gen.close()

    def test_integration_channel_expression_only_instrument(self):
        """Integration test that channel expression value of only 'port'
        without channels designated throws an error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateGeneration() as gen:
            with self.assertRaises(DaqError):
                gen.initialize(channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4")
            gen.close()


if __name__ == "__main__":
    unittest.main()
