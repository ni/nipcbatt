"""This module provides DynamicDigitalPatternMeasurement check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt import daq

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
)

# from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
#    _MockInterpreter,
# )
# from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
#    _replace_daqmx,
# )


class TestDynamicDigitalPatternMeasurement(unittest.TestCase):
    """Defines a test fixture that ensures the class'DynamicDigitalPatternMeasurement' is correct
       and ready to use

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
        # _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dynamic_digital_pattern_measurement(self):
        """Checks if class 'DynamicDigitalPatternMeasurement' is ready for use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (192 > 100 characters) (auto-generated noqa)
        meas = daq.DynamicDigitalPatternMeasurement()
        meas.initialize("Simulated_DAQ/port0/line0:7")
        timing_parameters = DynamicDigitalPatternTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000.0,
            number_of_samples_per_channel=50,
            active_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_ACTIVE_EDGE,
        )
        trigger_parameters = DigitalStartTriggerParameters(
            trigger_select=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_TRIGGER_TYPE,
            digital_start_trigger_source="/Simulated_DAQ/PFI0",
            digital_start_trigger_edge=daq.ConstantsForDynamicDigitalPatternMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
        )
        configuration = daq.DynamicDigitalPatternMeasurementConfiguration(
            measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )
        meas.configure_and_measure(
            configuration=configuration,
        )
        meas.close()


if __name__ == "__main__":
    unittest.main()
