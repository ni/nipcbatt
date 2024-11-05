"""This module provides test of integration of DigitalFrequencyMeasurement."""

import importlib
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_constants import (
    ConstantsForDigitalFrequencyMeasurement,
)
from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_data_types import (
    DigitalFrequencyMeasurementConfiguration,
    DigitalFrequencyMeasurementCounterChannelParameters,
    DigitalFrequencyMeasurementResultData,
    DigitalFrequencyRangeParameters,
)
from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_measurement import (
    DigitalFrequencyMeasurement,
)

# constants used across multiple tests
CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
TERMINAL = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestIntegrationDigitalFrequencyMeasurement(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DigitalFrequencyMeasurment' class

    Args:
        unittest.TestCase: Base class of the unittest framework
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

    def test_integration_digital_frequency_measurement_channel_expression_is_empty(
        self,
    ):
        """Integration test ensuring that is channel expression
        is empty then initialize() catches the error
        """

        with DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression="", input_terminal_name=TERMINAL)

            meas.close()

    def test_integration_digital_frequency_measurement_channel_expression_is_none(self):
        """Integration test ensuring that is channel expression
        is null then initialize() catches the error
        """

        with DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=None, input_terminal_name=TERMINAL)

            meas.close()

    def test_integration_digital_frequency_measurement_input_terminal_is_empty(self):
        """Integration test ensuring that is input terminal
        is empty then initialize() catches the error
        """

        with DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0",
                    input_terminal_name="",
                )

            meas.close()

    def test_integration_digital_frequency_measurement_input_terminal_is_none(self):
        """Integration test ensuring that is input terminal
        is null then initialize() catches the error
        """

        with DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0",
                    input_terminal_name=None,
                )

            meas.close()

    def test_integration_digital_frequency_measurement_configure_counter_channel_only(
        self,
    ):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalFrequencyMeasurement is successfully configured
        when given the necessary inputs
        """

        min_frequency = 1.0
        max_frequency = 10000000.0
        input_divisor = 10
        measurement_duration = 1.0

        with DigitalFrequencyMeasurement() as meas:
            range_parameters = DigitalFrequencyRangeParameters(min_frequency, max_frequency)
            counter_channel_parameters = DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, input_divisor, measurement_duration
            )

            meas.initialize(CHANNEL, TERMINAL)
            meas.configure_counter_channel(counter_channel_parameters)
            meas.close()

    def test_integration_digital_frequency_measurement_configure_and_measure(self):
        """Integration test of Digital Frequency Measurement that ensures
        a DigitalFrequencyMeasurementResultData is successfully returned
        when given the necessary inputs
        """

        min_frequency = 1.0
        max_frequency = 10000000.0
        input_divisor = 10
        measurement_duration = 1.0

        with DigitalFrequencyMeasurement() as meas:
            range_parameters = DigitalFrequencyRangeParameters(min_frequency, max_frequency)
            counter_channel_parameters = DigitalFrequencyMeasurementCounterChannelParameters(
                range_parameters, input_divisor, measurement_duration
            )

            meas.initialize(CHANNEL, TERMINAL)

            cfg = DigitalFrequencyMeasurementConfiguration(counter_channel_parameters)
            results = meas.configure_and_measure(cfg)

            self.assertIsInstance(results, DigitalFrequencyMeasurementResultData)

            meas.close()

    def test_integration_digital_frequency_measurement_negative_frequency(
        self,
    ):
        """Integration test of Digital Frequency Measurement that ensures
        an error is thrown when a negative minimum frequency is used
        """

        min_frequency = -0.1
        max_frequency = 10000000.0
        input_divisor = 10
        measurement_duration = 1.0

        with DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression=CHANNEL,
                    input_terminal_name=TERMINAL,
                )

                range_parameters = DigitalFrequencyRangeParameters(min_frequency, max_frequency)
                counter_channel_parameters = DigitalFrequencyMeasurementCounterChannelParameters(
                    range_parameters, input_divisor, measurement_duration
                )

    def test_integration_digital_frequency_measurement_zero_divisor(
        self,
    ):
        """Integration test of Digital Frequency Measurement that ensures
        an error is thrown when 0 is used for the input divisor
        """

        min_frequency = -0.1
        max_frequency = 10000000.0
        input_divisor = 0
        measurement_duration = 1.0

        with DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression=CHANNEL,
                    input_terminal_name=TERMINAL,
                )

                range_parameters = DigitalFrequencyRangeParameters(min_frequency, max_frequency)
                counter_channel_parameters = DigitalFrequencyMeasurementCounterChannelParameters(
                    range_parameters, input_divisor, measurement_duration
                )

    def test_integration_digital_frequency_measurement_zero_duration(
        self,
    ):
        """Integration test of Digital Frequency Measurement that ensures
        an error is thrown when 0 is used for the measurement duration
        """

        min_frequency = 1.0
        max_frequency = 10000000.0
        input_divisor = 10
        measurement_duration = 0.0

        with DigitalFrequencyMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(
                    channel_expression=CHANNEL,
                    input_terminal_name=TERMINAL,
                )

                range_parameters = DigitalFrequencyRangeParameters(min_frequency, max_frequency)
                counter_channel_parameters = DigitalFrequencyMeasurementCounterChannelParameters(
                    range_parameters, input_divisor, measurement_duration
                )


if __name__ == "__main__":
    unittest.main()
