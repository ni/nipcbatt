"""This module provides test of integration of StaticDigitalStateMeasurement."""

import importlib
import logging
import sys
import unittest

from nidaqmx.errors import DaqError
from varname import nameof

import nipcbatt


class TestIntegrationStaticDigitalStateMeasurement(unittest.TestCase):
    """Defines a test fixture that check the integration of the
       'StaticDigitalStateMeasurement' class

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

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_integration_num_channels_and_num_data_len_9(self):
        """Integration test ensuring that the module creates
        the correct output object in terms of numbers of
        channels and the associated data, both of length 8
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateMeasurement() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line0:8"
            )
            result_data = measurement.configure_and_measure()

            print("result_data.channel_identifiers: ", result_data.channel_identifiers)
            print("result_data.digital_states: ", result_data.digital_states)

            self.assertEqual(len(result_data.digital_states), 9)
            self.assertEqual(len(result_data.channel_identifiers), len(result_data.digital_states))

            measurement.close()

    def test_integration_num_channels_and_num_data_len_5(self):
        """Integration test ensuring that the module creates
        the correct output object in terms of numbers of
        channels and the associated data, both of length 5
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateMeasurement() as measurement:
            measurement.initialize(
                channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0/line1:5"
            )
            result_data = measurement.configure_and_measure()

            print("result_data.channel_identifiers: ", result_data.channel_identifiers)
            print("result_data.digital_states: ", result_data.digital_states)

            self.assertEqual(len(result_data.digital_states), 5)
            self.assertEqual(len(result_data.channel_identifiers), len(result_data.digital_states))

            measurement.close()

    def test_integration_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression is None
        then initialize() properly catches this error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateMeasurement() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(channel_expression=None)

            measurement.close()

    def test_integration_channel_expression_is_empty(self):
        """Integration test ensuring that if channel expression is empty
        then initialize() properly catches this error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateMeasurement() as measurement:
            with self.assertRaises(ValueError):
                measurement.initialize(channel_expression="")

            measurement.close()

    def test_integration_channel_expression_port(self):
        """Integration test ensuring that channel expression value
        of only 'port' without channels designated throws the proper error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateMeasurement() as measurement:
            with self.assertRaises(DaqError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4/port0"
                )
            measurement.close()

    def test_integration_channel_expression_only_instrument(self):
        """Integration test ensuring that channel expression value
        of only 'port' without channels designated throws the proper error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.StaticDigitalStateMeasurement() as measurement:
            with self.assertRaises(DaqError):
                measurement.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod4"
                )

            measurement.close()


if __name__ == "__main__":
    unittest.main()
