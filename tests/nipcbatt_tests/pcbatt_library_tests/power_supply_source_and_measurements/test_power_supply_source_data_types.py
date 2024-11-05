"""This module provides Power supply source data types check."""

import importlib.metadata
import logging
import random
import sys
import unittest

import nidaqmx.constants
import numpy
import numpy.testing
from varname import nameof

import nipcbatt


class TestPowerSupplySourceAndMeasureTerminalParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasureTerminalParameters` class is ready to use.

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

    def test_power_supply_source_and_measure_terminal_parameters(self):
        """unit test of PowerSupplySourceAndMeasureTerminalParameters."""
        expected_voltage_setpoint_volts = 5.0
        expected_current_setpoint_amperes = 0.5
        expected_power_sense = nidaqmx.constants.Sense.LOCAL
        expected_idle_output_behaviour = nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED
        expected_enable_output = True

        instance = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
            voltage_setpoint_volts=expected_voltage_setpoint_volts,
            current_setpoint_amperes=expected_current_setpoint_amperes,
            power_sense=expected_power_sense,
            idle_output_behaviour=expected_idle_output_behaviour,
            enable_output=expected_enable_output,
        )

        actual_voltage_setpoint_volts = instance.voltage_setpoint_volts
        actual_current_setpoint_amperes = instance.current_setpoint_amperes
        actual_power_sense = instance.power_sense
        actual_idle_output_behaviour = instance.idle_output_behaviour
        actual_enable_output = instance.enable_output

        self.assertEqual(expected_voltage_setpoint_volts, actual_voltage_setpoint_volts)
        self.assertEqual(expected_current_setpoint_amperes, actual_current_setpoint_amperes)
        self.assertEqual(expected_power_sense, actual_power_sense)
        self.assertEqual(expected_idle_output_behaviour, actual_idle_output_behaviour)
        self.assertEqual(expected_enable_output, actual_enable_output)


class TestPowerSupplySourceAndMeasureConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasureConfiguration` class is ready to use.

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

    def test_power_supply_source_and_measure_configuration(self):
        """unit test of PowerSupplySourceAndMeasureConfiguration."""
        expected_voltage_setpoint_volts = 0.5
        expected_current_setpoint_amperes = 0.02
        expected_power_sense = nidaqmx.constants.Sense.REMOTE
        expected_idle_output_behaviour = nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED
        expected_enable_output = False

        expected_terminal_parameters = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
            voltage_setpoint_volts=expected_voltage_setpoint_volts,
            current_setpoint_amperes=expected_current_setpoint_amperes,
            power_sense=expected_power_sense,
            idle_output_behaviour=expected_idle_output_behaviour,
            enable_output=expected_enable_output,
        )

        expected_execution_option = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE
        expected_measurement_analysis_requirement = (
            nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
        )

        expected_measurement_options = nipcbatt.MeasurementOptions(
            execution_option=expected_execution_option,
            measurement_analysis_requirement=expected_measurement_analysis_requirement,
        )

        expected_sample_clock_source = "OnboardClock"
        expected_sampling_rate_hertz = 1000
        expected_number_of_samples_per_channel = 500
        expected_sample_timing_engine = nipcbatt.SampleTimingEngine.TE1

        expected_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source=expected_sample_clock_source,
            sampling_rate_hertz=expected_sampling_rate_hertz,
            number_of_samples_per_channel=expected_number_of_samples_per_channel,
            sample_timing_engine=expected_sample_timing_engine,
        )

        expected_trigger_select = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
        expected_digital_start_trigger_source = "trigger_source"
        expected_digital_start_trigger_edge = nidaqmx.constants.Edge.FALLING

        expected_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=expected_trigger_select,
            digital_start_trigger_source=expected_digital_start_trigger_source,
            digital_start_trigger_edge=expected_digital_start_trigger_edge,
        )

        instance = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
            terminal_parameters=expected_terminal_parameters,
            measurement_options=expected_measurement_options,
            sample_clock_timing_parameters=expected_sample_clock_timing_parameters,
            digital_start_trigger_parameters=expected_digital_start_trigger_parameters,
        )

        logging.debug("%s = %s", nameof(instance), instance)

        actual_voltage_setpoint_volts = instance.terminal_parameters.voltage_setpoint_volts
        actual_current_setpoint_amperes = instance.terminal_parameters.current_setpoint_amperes
        actual_power_sense = instance.terminal_parameters.power_sense
        actual_idle_output_behaviour = instance.terminal_parameters.idle_output_behaviour
        actual_enable_output = instance.terminal_parameters.enable_output

        actual_execution_option = instance.measurement_options.execution_option
        actual_measurement_analysis_requirement = (
            instance.measurement_options.measurement_analysis_requirement
        )
        actual_sample_clock_source = instance.sample_clock_timing_parameters.sample_clock_source
        actual_sampling_rate_hertz = instance.sample_clock_timing_parameters.sampling_rate_hertz
        actual_number_of_samples_per_channel = (
            instance.sample_clock_timing_parameters.number_of_samples_per_channel
        )
        actual_sample_timing_engine = instance.sample_clock_timing_parameters.sample_timing_engine

        self.assertEqual(expected_voltage_setpoint_volts, actual_voltage_setpoint_volts)
        self.assertEqual(expected_current_setpoint_amperes, actual_current_setpoint_amperes)
        self.assertEqual(expected_power_sense, actual_power_sense)
        self.assertEqual(expected_idle_output_behaviour, actual_idle_output_behaviour)
        self.assertEqual(expected_enable_output, actual_enable_output)

        self.assertEqual(expected_execution_option, actual_execution_option)
        self.assertEqual(
            expected_measurement_analysis_requirement,
            actual_measurement_analysis_requirement,
        )
        self.assertEqual(expected_sample_clock_source, actual_sample_clock_source)
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate_hertz)
        self.assertEqual(
            expected_number_of_samples_per_channel, actual_number_of_samples_per_channel
        )
        self.assertEqual(
            expected_sample_timing_engine,
            actual_sample_timing_engine,
        )


class TestPowerSupplySourceAndMeasureData(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasureData` class is ready to use.

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

    def test_power_supply_source_and_measure_data(self):
        """unit test of PowerSupplySourceAndMeasureData."""
        expected_source_name = "test_power_source_name"
        expected_voltage_samples = numpy.array(
            [random.random() * 0.1 for item in range(0, 1000)],
            dtype=numpy.float64,
        )
        expected_current_samples = numpy.array(
            [random.random() * 0.1 for item in range(0, 1000)],
            dtype=numpy.float64,
        )
        expected_sampling_rate_hertz = 5000

        instance = nipcbatt.PowerSupplySourceAndMeasureData(
            source_name=expected_source_name,
            voltage_samples=expected_voltage_samples,
            current_samples=expected_current_samples,
            sampling_rate_hertz=expected_sampling_rate_hertz,
        )

        actual_source_name = instance.source_name
        actual_voltage_samples = instance.voltage_samples
        actual_current_samples = instance.current_samples
        actual_sampling_rate = instance.sampling_rate_hertz

        self.assertEqual(expected_source_name, actual_source_name)
        self.assertTrue((expected_voltage_samples == actual_voltage_samples).all())
        self.assertTrue((expected_current_samples == actual_current_samples).all())
        self.assertEqual(expected_sampling_rate_hertz, actual_sampling_rate)

    def test_power_supply_source_and_measure_data_with_invalid_data(self):
        """Tests if expected error is thrown when creating an instance of
        `PowerSupplySourceAndMeasureData` with invalid data"""

        expected_source_name = "test_power_source_name"
        expected_voltage_samples = numpy.array(
            [random.random() * 0.1 for item in range(0, 1000)],
            dtype=numpy.float64,
        )
        expected_current_samples = numpy.array(
            [random.random() * 0.1 for item in range(0, 1000)],
            dtype=numpy.float64,
        )
        expected_sampling_rate_hertz = 5000

        # Test if the value error is thrown if voltage_samples is None
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=None,
                current_samples=expected_current_samples,
                sampling_rate_hertz=expected_sampling_rate_hertz,
            ),
        )

        # Test if the value error is thrown if voltage_samples is empty
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=[],
                current_samples=expected_current_samples,
                sampling_rate_hertz=expected_sampling_rate_hertz,
            ),
        )

        # Test if the value error is thrown if current_samples is None
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=expected_voltage_samples,
                current_samples=None,
                sampling_rate_hertz=expected_sampling_rate_hertz,
            ),
        )

        # Test if the value error is thrown if current_samples is empty
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=expected_voltage_samples,
                current_samples=[],
                sampling_rate_hertz=expected_sampling_rate_hertz,
            ),
        )

        # Test if the value error is thrown if sampling_rate is 0
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.PowerSupplySourceAndMeasureData(
                source_name=expected_source_name,
                voltage_samples=expected_voltage_samples,
                current_samples=expected_current_samples,
                sampling_rate_hertz=0,
            ),
        )


class TestPowerSupplySourceAndMeasureResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasureResultData` class is ready to use.

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

    def test_power_supply_source_and_measure_result_data(self):
        """unit test of PowerSupplySourceAndMeasureResultData."""
        # todo: write test code
        expected_voltage_waveform = nipcbatt.AnalogWaveform(
            channel_name="Dev/pow0",
            delta_time_seconds=1.0 / 10000,
            samples=numpy.array(
                [random.random() * 0.1 for item in range(0, 1000)],
                dtype=numpy.float64,
            ),
        )

        expected_current_waveform = nipcbatt.AnalogWaveform(
            channel_name="Dev/pow1",
            delta_time_seconds=1.0 / 10000,
            samples=numpy.array(
                [random.random() * 0.1 for item in range(0, 1000)], dtype=numpy.float64
            ),
        )

        expected_max_voltage_level_volts = 1.0
        expected_max_current_level_amperes = 0.1
        expected_max_power_level_watts = 0.2
        expected_average_power_value_watts = 0.8
        expected_acquisition_duration_seconds = 0.01

        instance = nipcbatt.PowerSupplySourceAndMeasureResultData(
            voltage_waveform=expected_voltage_waveform,
            current_waveform=expected_current_waveform,
            max_voltage_level_volts=expected_max_voltage_level_volts,
            max_current_level_amperes=expected_max_current_level_amperes,
            max_power_level_watts=expected_max_power_level_watts,
            average_power_value_watts=expected_average_power_value_watts,
            acquisition_duration_seconds=expected_acquisition_duration_seconds,
        )

        actual_voltage_waveform = instance.voltage_waveform
        actual_current_waveform = instance.current_waveform
        actual_max_voltage_level_volts = instance.max_voltage_level_volts
        actual_max_current_level_amperes = instance.max_current_level_amperes
        actual_max_power_level_watts = instance.max_power_level_watts
        actual_average_power_value_watts = instance.average_power_value_watts
        actual_acquisition_duration_seconds = instance.acquisition_duration_seconds

        self.assertEqual(expected_voltage_waveform, actual_voltage_waveform)
        self.assertEqual(expected_current_waveform, actual_current_waveform)
        self.assertEqual(expected_max_voltage_level_volts, actual_max_voltage_level_volts)
        self.assertEqual(expected_max_current_level_amperes, actual_max_current_level_amperes)
        self.assertEqual(expected_max_power_level_watts, actual_max_power_level_watts)
        self.assertEqual(expected_average_power_value_watts, actual_average_power_value_watts)
        self.assertEqual(expected_acquisition_duration_seconds, actual_acquisition_duration_seconds)

    def test_power_supply_source_and_measure_result_data_with_invalid_waveforms(
        self,
    ):
        """Test if the expected error is thrown if the current or voltage waveform is None"""

        test_sample_waveform = nipcbatt.AnalogWaveform(
            channel_name="Dev/pow0",
            delta_time_seconds=1.0 / 10000,
            samples=numpy.array(
                [random.random() * 0.1 for item in range(0, 1000)],
                dtype=numpy.float64,
            ),
        )
        # Test if Value error is raised in voltage_waveform instance is None
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.PowerSupplySourceAndMeasureResultData(
                voltage_waveform=None,
                current_waveform=test_sample_waveform,
                max_voltage_level_volts=0.0,
                max_current_level_amperes=0.0,
                max_power_level_watts=0.0,
                average_power_value_watts=0.01,
                acquisition_duration_seconds=0.05,
            ),
        )

        # Test if Value error is raised in current_waveform instance is None
        self.assertRaises(
            ValueError,
            lambda: nipcbatt.PowerSupplySourceAndMeasureResultData(
                voltage_waveform=test_sample_waveform,
                current_waveform=None,
                max_voltage_level_volts=0.0,
                max_current_level_amperes=0.0,
                max_power_level_watts=0.0,
                average_power_value_watts=0.01,
                acquisition_duration_seconds=0.05,
            ),
        )


if __name__ == "__main__":
    unittest.main()
