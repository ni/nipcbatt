"""This module provides test of integration of DigitalPwmMeasurement."""

import importlib
import logging
import sys
import unittest

import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_data_types import (
    DigitalPwmMeasurementConfiguration,
    DigitalPwmMeasurementCounterChannelParameters,
    DigitalPwmMeasurementData,
    DigitalPwmMeasurementRangeParameters,
    DigitalPwmMeasurementResultData,
    DigitalPwmMeasurementTimingParameters,
)
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_measurement import (
    DigitalPwmMeasurement,
)

# constants used across multiple tests
CHANNEL = "NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/ctr0"
TERMINAL = "/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"


class TestIntegrationDigitalPwmMeasurement(unittest.TestCase):
    """Defines a test fixture to verify the integration of the
       'DigitalPwmMeasurment' class

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

    def test_integration_digital_pwm_measurement_channel_expression_empty(self):
        """Integration test ensuring that if channel expression
        is empty then initialize() catches the error
        """

        with DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression="", input_terminal_name=TERMINAL)

            meas.close()

    def test_integration_digital_pwm_measurement_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression
        is null then initialize() catches the error
        """

        with DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=None, input_terminal_name=TERMINAL)

            meas.close()

    def test_integration_digital_pwm_measurement_input_terminal_empty(self):
        """Integration test ensuring that if input terminal
        is empty then initialize() catches the error
        """

        with DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=CHANNEL, input_terminal_name="")

            meas.close()

    def test_integration_digital_pwm_measurement_input_terminal_is_none(self):
        """Integration test ensuring that if input terminal
        is null then initialize() catches the error
        """

        with DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=CHANNEL, input_terminal_name=None)

            meas.close()

    def test_integration_digital_pwm_measurement_configure_only(self):
        """Integration test of Digital PWM Measurement that ensures an instance
        of DigitalPwmMeasurement is successfully initialized and configured
        given correct inputs"""

        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_ONLY

        range_params = DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)

        timing_params = DigitalPwmMeasurementTimingParameters(cycles)

        counter_channel_params = DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )

        config = DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsNone(result_data)

    def test_integration_digital_pwm_measurement_measure_only(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when measure only
        is selected as the execution option"""

        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.MEASURE_ONLY

        range_params = DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = DigitalPwmMeasurementTimingParameters(cycles)
        counter_channel_params = DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )
        config = DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, DigitalPwmMeasurementResultData)

    def test_integration_digital_pwm_measurement_both_configure_and_measure(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when both configure
        and measure is selected as the execution option"""
        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        range_params = DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = DigitalPwmMeasurementTimingParameters(cycles)
        counter_channel_params = DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )
        config = DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, DigitalPwmMeasurementResultData)

    def test_integration_digital_pwm_negative_values(self):
        """Integration test of Digital Pwm measurement that ensures
        a DigitalPwmMeasurement instantiation fails if given a negative
        value for any parameter
        """

        min_semiperiod = -50.0e-9
        max_semiperiod = 50.0
        cycles = 10
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        with DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                range_params = DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
                timing_params = DigitalPwmMeasurementTimingParameters(cycles)
                counter_channel_params = DigitalPwmMeasurementCounterChannelParameters(
                    range_params, timing_params, edge
                )
                config = DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

                meas.initialize(CHANNEL, TERMINAL)
                meas.configure_and_measure(config)

        min_semiperiod = 50.0e-9
        max_semiperiod = -50.0
        cycles = 10
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        with DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                range_params = DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
                timing_params = DigitalPwmMeasurementTimingParameters(cycles)
                counter_channel_params = DigitalPwmMeasurementCounterChannelParameters(
                    range_params, timing_params, edge
                )
                config = DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

                meas.initialize(CHANNEL, TERMINAL)
                meas.configure_and_measure(config)

        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = -10
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        with DigitalPwmMeasurement() as meas:
            with self.assertRaises(ValueError):
                range_params = DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
                timing_params = DigitalPwmMeasurementTimingParameters(cycles)
                counter_channel_params = DigitalPwmMeasurementCounterChannelParameters(
                    range_params, timing_params, edge
                )
                config = DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

                meas.initialize(CHANNEL, TERMINAL)
                meas.configure_and_measure(config)

    def test_integration_digital_pwm_measurement_no_edge_defined(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when the user does not
        define an edge"""
        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        range_params = DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = DigitalPwmMeasurementTimingParameters(cycles)
        counter_channel_params = DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params
        )
        config = DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, DigitalPwmMeasurementResultData)

    def test_integration_digital_pwm_measurement_no_cycles_defined(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when the user does not
        define a value for cycles"""
        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
        execution_type = MeasurementExecutionType.CONFIGURE_AND_MEASURE

        range_params = DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = DigitalPwmMeasurementTimingParameters()
        counter_channel_params = DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )
        config = DigitalPwmMeasurementConfiguration(counter_channel_params, execution_type)

        with DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, DigitalPwmMeasurementResultData)

    def test_integration_digital_pwm_measurement_no_execution_type_defined(self):
        """Integration test of Digital PWM measurement that ensures an instance
        of DigitalPwmMeasurement is successfully executed when the user does not
        define a value for execution type"""
        min_semiperiod = 50.0e-9
        max_semiperiod = 50.0
        cycles = 100
        edge = ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE

        range_params = DigitalPwmMeasurementRangeParameters(min_semiperiod, max_semiperiod)
        timing_params = DigitalPwmMeasurementTimingParameters(cycles)
        counter_channel_params = DigitalPwmMeasurementCounterChannelParameters(
            range_params, timing_params, edge
        )
        config = DigitalPwmMeasurementConfiguration(counter_channel_params)

        with DigitalPwmMeasurement() as meas:
            meas.initialize(CHANNEL, TERMINAL)
            result_data = meas.configure_and_measure(configuration=config)
            meas.close()

        self.assertIsInstance(result_data, DigitalPwmMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
