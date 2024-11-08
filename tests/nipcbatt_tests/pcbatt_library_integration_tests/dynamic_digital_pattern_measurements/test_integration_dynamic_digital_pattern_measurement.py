"""This module provides test of integration of DynamicDigitalPatternMeasurement."""

import importlib
import importlib.metadata
import logging
import sys
import unittest

import nidaqmx.constants
import nidaqmx.stream_writers  # noqa: F401 - 'nidaqmx.stream_writers' imported but unused (auto-generated noqa)
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library.common.common_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.common.common_data_types.DigitalStartTriggerParameters' imported but unused (auto-generated noqa)
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_data_types.DynamicDigitalPatternMeasurementConfiguration' imported but unused (auto-generated noqa)
    DynamicDigitalPatternMeasurementConfiguration,
    DynamicDigitalPatternMeasurementResultData,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement import (
    DynamicDigitalPatternMeasurement,
)


class TestIntegrationDynamicDigitalPatternMeasurement(unittest.TestCase):
    """Defines a test fixture that check the integration of the
       'DynamicDigitalPatternMeasurement' class

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

    def test_integration_dynamic_digital_pattern_meas_channel_expression_empty(self):
        """Integration test ensuring that if channel expression is empty then
        initialize() catches the error"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (411 > 100 characters) (auto-generated noqa)

        with DynamicDigitalPatternMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression="")

            meas.close()

    def test_integration_dynamic_digital_pattern_meas_channel_expression_is_none(self):
        """Integration test ensuring that if channel expression
        is null then initialize() catches the error
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with DynamicDigitalPatternMeasurement() as meas:
            with self.assertRaises(ValueError):
                meas.initialize(channel_expression=None)

            meas.close()

    def test_integration_test_dynamic_digital_pattern_measurement_configure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement.
        DynamicDigitalPatternMeasurement with MeasurementExecutionType.CONFIGURE_ONLY
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.DynamicDigitalPatternMeasurement() as meas:
            meas.initialize(
                channel_expression="TS1_DIO/port0/line0:7",
            )
            timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
                sample_clock_source="OnboardClock",
                sampling_rate_hertz=10000.0,
                number_of_samples_per_channel=50,
                active_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
            )
            configuration = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = meas.configure_and_measure(configuration=configuration)
            meas.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            self.assertIs(None, results)

    def test_integration_test_dynamic_digital_pattern_measurement_configure_and_measure(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement.
        DynamicDigitalPatternMeasurement with MeasurementExecutionType.CONFIGURE_AND_MEASURE
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        with nipcbatt.DynamicDigitalPatternMeasurement() as meas:
            meas.initialize(
                channel_expression="TS1_DIO/port0/line0:1",
            )
            timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
                sample_clock_source="OnboardClock",
                sampling_rate_hertz=10000.0,
                number_of_samples_per_channel=50,
                active_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
            )
            configuration = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = meas.configure_and_measure(configuration=configuration)
            meas.close()

            print(f"parameters = {configuration}")
            print(f"results = {results}")
            print(type(results))
            self.assertIsInstance(results, DynamicDigitalPatternMeasurementResultData)

    def test_integration_test_dynamic_digital_pattern_measurement_configure_only_and_measure_only(
        self,
    ):
        """Integration test of
        nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement.
        DynamicDigitalPatternMeasurement with MeasurementExecutionType.MeasurementExecutionType.CONFIGURE_ONLY
        and MeasurementExecutionType.MEASURE_ONLY"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)

        with nipcbatt.DynamicDigitalPatternMeasurement() as meas:
            meas.initialize(
                channel_expression="TS1_DIO/port0/line0:7",
            )
            timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
                sample_clock_source="OnboardClock",
                sampling_rate_hertz=10000.0,
                number_of_samples_per_channel=50,
                active_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
            )
            trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
                trigger_select=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
                digital_start_trigger_source="/TS1_Core/PFI0",
                digital_start_trigger_edge=ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
            )
            configuration = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = meas.configure_and_measure(configuration=configuration)

            print(
                f"after configuration with MeasurementExecutionType.CONFIGURE_ONLY, results = {results}"
            )
            self.assertIs(None, results)

            configuration = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
                measurement_options=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
                timing_parameters=timing_parameters,
                trigger_parameters=trigger_parameters,
            )
            results = meas.configure_and_measure(configuration=configuration)
            meas.close()

            print(
                f"after configuration with MeasurementExecutionType.MEASURE_ONLY, results = {results}"
            )
            self.assertIsInstance(results, DynamicDigitalPatternMeasurementResultData)


if __name__ == "__main__":
    unittest.main()
