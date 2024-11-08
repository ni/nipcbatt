"""This module provides DigitalEdgeCountMeasurementUsingSoftwareTimer
   and DigitalEdgeCountMeasurementUsingHardwareTimer check."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (355 > 100 characters) (auto-generated noqa)

import importlib.metadata
import logging
import sys
import unittest

import nidaqmx
import nidaqmx.constants
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_constants import (  # noqa: F401 - 'nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_constants.ConstantsForDigitalEdgeCountMeasurement' imported but unused (auto-generated noqa)
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types import (  # noqa: F401 - 'nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types.DigitalEdgeCountMeasurementResultData' imported but unused (auto-generated noqa)
    DigitalEdgeCountHardwareTimerConfiguration,
    DigitalEdgeCountMeasurementCounterChannelParameters,
    DigitalEdgeCountMeasurementResultData,
    DigitalEdgeCountMeasurementTimingParameters,
    DigitalEdgeCountSoftwareTimerConfiguration,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_measurement_using_hardware_timer import (
    DigitalEdgeCountMeasurementUsingHardwareTimer,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_measurement_using_software_timer import (
    DigitalEdgeCountMeasurementUsingSoftwareTimer,
)

# from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
#    _MockInterpreter,
# )
# from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
#    _replace_daqmx,
# )


class TestDigitalEdgeCountMeasurement(unittest.TestCase):
    """Defines a test fixture that ensures the class'DigitalEdgeCountMeasurementUsingHardwareTimer'  or
    'DigitalEdgeCountMeasurementUsingHardwareTimer' is correct and ready to use,

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: W505, D205, D415 - doc line too long (103 > 100 characters) (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

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

    def test_digital_edge_count_measurement_using_hardware_timer(self):
        """Checks if class 'DigitalEdgeCountMeasurementUsingHardwareTimer' is ready for use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (205 > 100 characters) (auto-generated noqa)
        meas = DigitalEdgeCountMeasurementUsingHardwareTimer()
        meas.initialize(
            measurement_channel_expression="TS1_Core/ctr1",
            measurement_input_terminal_name="/TS1_Core/PFI6",
            timer_channel_expression="TS1_Core/ctr2",
        )

        counter_channel_parameters = DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=nidaqmx.constants.Edge.FALLING,
        )
        timing_parameters = DigitalEdgeCountMeasurementTimingParameters(
            edge_counting_duration=0.005,
        )
        trigger_parameters = DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
            digital_start_trigger_source="/TS1_Core/PFI0",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )
        configuration = DigitalEdgeCountHardwareTimerConfiguration(
            measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            counter_channel_parameters=counter_channel_parameters,
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )
        meas.configure_and_measure(
            configuration=configuration,
        )
        meas.close()

    def test_digital_edge_count_measurement_using_software_timer(self):
        """Checks if class 'DigitalEdgeCountMeasurementUsingSoftwareTimer' is ready for use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (205 > 100 characters) (auto-generated noqa)
        meas = DigitalEdgeCountMeasurementUsingSoftwareTimer()
        meas.initialize(
            measurement_channel_expression="TS1_Core/ctr1",
            measurement_input_terminal_name="/TS1_Core/PFI6",
        )
        counter_channel_parameters = DigitalEdgeCountMeasurementCounterChannelParameters(
            edge_type=nidaqmx.constants.Edge.FALLING,
        )
        timing_parameters = DigitalEdgeCountMeasurementTimingParameters(
            edge_counting_duration=0.005,
        )
        configuration = DigitalEdgeCountSoftwareTimerConfiguration(
            measurement_options=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            timing_parameters=timing_parameters,
            counter_channel_parameters=counter_channel_parameters,
        )
        meas.configure_and_measure(
            configuration=configuration,
        )
        meas.close()


if __name__ == "__main__":
    unittest.main()
