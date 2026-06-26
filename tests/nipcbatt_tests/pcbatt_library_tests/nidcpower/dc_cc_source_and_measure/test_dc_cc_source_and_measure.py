# pylint: disable=C0301
"""This module provides DC constant current source and measure data types unit tests."""

import importlib.metadata
import logging
import math
import sys
import unittest

import nidcpower
from varname import nameof

from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure_data_types import (
    CurrentChannelSettings,
    DCCurrentSourceAndMeasureParameters,
    DCCurrentSourceAndMeasureResultData,
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dcpower.dc_cc_source_and_measure.dc_cc_source_and_measure_constants import (
    ConstantsForDCCurrentSourceAndMeasure,
    DEFAULT_DC_CC_CHANNEL_SETTINGS,
    DEFAULT_DC_CC_EXECUTION_SETTINGS,
    DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS,
    DEFAULT_DC_CC_TIMING_PARAMETERS,
    DEFAULT_DC_CC_TRIGGER_PARAMETERS,
)


class TestMeasurementExecutionType(unittest.TestCase):
    """Defines a test fixture that checks
    `MeasurementExecutionType` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_measurement_execution_type_members(self):
        """Checks MeasurementExecutionType enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE.value,
            "CONFIGURE_SOURCE_AND_MEASURE",
        )
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_ONLY.value,
            "CONFIGURE_ONLY",
        )
        self.assertEqual(
            MeasurementExecutionType.START_SOURCE_ONLY.value,
            "START_SOURCE_ONLY",
        )
        self.assertEqual(
            MeasurementExecutionType.MEASURE_ONLY.value,
            "MEASURE_ONLY",
        )
        self.assertEqual(len(MeasurementExecutionType), 4)


class TestSourceTriggerBehavior(unittest.TestCase):
    """Defines a test fixture that checks
    `SourceTriggerBehavior` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_source_trigger_behavior_members(self):
        """Checks SourceTriggerBehavior enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(
            SourceTriggerBehavior.Start_Source_Trigger.value,
            "Start_Source_Trigger",
        )
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger.value,
            "Disable_Source_Trigger",
        )
        self.assertEqual(len(SourceTriggerBehavior), 2)


class TestExportEvent(unittest.TestCase):
    """Defines a test fixture that checks
    `ExportEvent` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_export_event_members(self):
        """Checks ExportEvent enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(ExportEvent.NONE.value, "NONE")
        self.assertEqual(ExportEvent.Route_Event.value, "Route_Event")
        self.assertEqual(len(ExportEvent), 2)


class TestEventSignalToExport(unittest.TestCase):
    """Defines a test fixture that checks
    `EventSignalToExport` enum is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_event_signal_to_export_members(self):
        """Checks EventSignalToExport enum has expected members and values."""  # noqa: D415, W505
        self.assertEqual(
            EventSignalToExport.Source_Complete_Event.value,
            "source_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Measure_Complete_Event.value,
            "measure_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Sequence_Iteration_Complete_Event.value,
            "sequence_iteration_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Sequence_Engine_Done_Event.value,
            "sequence_engine_done_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Pulse_Complete_Event.value,
            "pulse_complete_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Ready_for_Pulse_Trigger_Event.value,
            "ready_for_pulse_trigger_event_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Start_Trigger.value,
            "exported_start_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Source_Trigger.value,
            "exported_source_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Measure_Trigger.value,
            "exported_measure_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Sequence_Advance_Trigger.value,
            "exported_sequence_advance_trigger_output_terminal",
        )
        self.assertEqual(
            EventSignalToExport.Pulse_Trigger.value,
            "exported_pulse_trigger_output_terminal",
        )
        self.assertEqual(len(EventSignalToExport), 11)


class TestExecutionSettings(unittest.TestCase):
    """Defines a test fixture that checks
    `ExecutionSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_execution_settings(self):
        """Checks ExecutionSettings construction and property getters."""  # noqa: D415, W505
        expected_execution_type = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
        expected_skip_analysis = True

        instance = ExecutionSettings(
            execution_type=expected_execution_type,
            skip_analysis=expected_skip_analysis,
        )

        self.assertEqual(expected_execution_type, instance.execution_type)
        self.assertEqual(expected_skip_analysis, instance.skip_analysis)

    def test_execution_settings_configure_only(self):
        """Checks ExecutionSettings with CONFIGURE_ONLY execution type."""  # noqa: D415, W505
        expected_execution_type = MeasurementExecutionType.CONFIGURE_ONLY
        expected_skip_analysis = False

        instance = ExecutionSettings(
            execution_type=expected_execution_type,
            skip_analysis=expected_skip_analysis,
        )

        self.assertEqual(expected_execution_type, instance.execution_type)
        self.assertEqual(expected_skip_analysis, instance.skip_analysis)


class TestCurrentChannelSettings(unittest.TestCase):
    """Defines a test fixture that checks
    `CurrentChannelSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_current_channel_settings_remote_sensing(self):
        """Checks CurrentChannelSettings construction and property getters with REMOTE sensing."""  # noqa: D415, W505
        expected_current_level = 10e-6
        expected_current_level_range = 0.1
        expected_voltage_limit = 1.0
        expected_voltage_limit_range = 2.0
        expected_sensing = nidcpower.Sense.REMOTE
        expected_enable_output = True

        instance = CurrentChannelSettings(
            current_level=expected_current_level,
            current_level_range=expected_current_level_range,
            voltage_limit=expected_voltage_limit,
            voltage_limit_range=expected_voltage_limit_range,
            sensing=expected_sensing,
            enable_output=expected_enable_output,
        )

        self.assertEqual(expected_current_level, instance.current_level)
        self.assertEqual(expected_current_level_range, instance.current_level_range)
        self.assertEqual(expected_voltage_limit, instance.voltage_limit)
        self.assertEqual(expected_voltage_limit_range, instance.voltage_limit_range)
        self.assertEqual(expected_sensing, instance.sensing)
        self.assertEqual(expected_enable_output, instance.enable_output)

    def test_current_channel_settings_local_sensing_output_disabled(self):
        """Checks CurrentChannelSettings with LOCAL sensing and output disabled."""  # noqa: D415, W505
        expected_current_level = 50e-3
        expected_current_level_range = 0.2
        expected_voltage_limit = 5.0
        expected_voltage_limit_range = 6.0
        expected_sensing = nidcpower.Sense.LOCAL
        expected_enable_output = False

        instance = CurrentChannelSettings(
            current_level=expected_current_level,
            current_level_range=expected_current_level_range,
            voltage_limit=expected_voltage_limit,
            voltage_limit_range=expected_voltage_limit_range,
            sensing=expected_sensing,
            enable_output=expected_enable_output,
        )

        self.assertEqual(expected_current_level, instance.current_level)
        self.assertEqual(expected_current_level_range, instance.current_level_range)
        self.assertEqual(expected_voltage_limit, instance.voltage_limit)
        self.assertEqual(expected_voltage_limit_range, instance.voltage_limit_range)
        self.assertEqual(expected_sensing, instance.sensing)
        self.assertEqual(expected_enable_output, instance.enable_output)


class TestTimingParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_timing_parameters(self):
        """Checks TimingParameters construction and property getters."""  # noqa: D415, W505
        expected_source_delay = 0.1
        expected_aperture_time = 0.02
        expected_transient_response = nidcpower.TransientResponse.NORMAL

        instance = TimingParameters(
            source_delay=expected_source_delay,
            aperture_time=expected_aperture_time,
            transient_response=expected_transient_response,
        )

        self.assertEqual(expected_source_delay, instance.source_delay)
        self.assertEqual(expected_aperture_time, instance.aperture_time)
        self.assertEqual(expected_transient_response, instance.transient_response)

    def test_timing_parameters_fast_transient(self):
        """Checks TimingParameters with FAST transient response."""  # noqa: D415, W505
        expected_source_delay = 0.05
        expected_aperture_time = 0.01
        expected_transient_response = nidcpower.TransientResponse.FAST

        instance = TimingParameters(
            source_delay=expected_source_delay,
            aperture_time=expected_aperture_time,
            transient_response=expected_transient_response,
        )

        self.assertEqual(expected_source_delay, instance.source_delay)
        self.assertEqual(expected_aperture_time, instance.aperture_time)
        self.assertEqual(expected_transient_response, instance.transient_response)


class TestTriggerParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `TriggerParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_trigger_parameters_with_trigger_enabled(self):
        """Checks TriggerParameters with source trigger enabled and event routing."""  # noqa: D415, W505
        expected_source_trigger_behavior = SourceTriggerBehavior.Start_Source_Trigger
        expected_start_source_name = "/PXI1Slot2/PXI_Trig0"
        expected_export_event = ExportEvent.Route_Event
        expected_event_signal_to_export = EventSignalToExport.Source_Complete_Event
        expected_output_event_signal_terminal = "/PXI1Slot2/PXI_Trig1"

        instance = TriggerParameters(
            source_trigger_behavior=expected_source_trigger_behavior,
            start_source_name=expected_start_source_name,
            export_event=expected_export_event,
            event_signal_to_export=expected_event_signal_to_export,
            output_event_signal_terminal=expected_output_event_signal_terminal,
        )

        self.assertEqual(expected_source_trigger_behavior, instance.source_trigger_behavior)
        self.assertEqual(expected_start_source_name, instance.start_source_name)
        self.assertEqual(expected_export_event, instance.export_event)
        self.assertEqual(expected_event_signal_to_export, instance.event_signal_to_export)
        self.assertEqual(expected_output_event_signal_terminal, instance.output_event_signal_terminal)

    def test_trigger_parameters_with_trigger_disabled(self):
        """Checks TriggerParameters with source trigger disabled and no event routing."""  # noqa: D415, W505
        expected_source_trigger_behavior = SourceTriggerBehavior.Disable_Source_Trigger
        expected_start_source_name = ""
        expected_export_event = ExportEvent.NONE
        expected_event_signal_to_export = EventSignalToExport.Source_Complete_Event
        expected_output_event_signal_terminal = ""

        instance = TriggerParameters(
            source_trigger_behavior=expected_source_trigger_behavior,
            start_source_name=expected_start_source_name,
            export_event=expected_export_event,
            event_signal_to_export=expected_event_signal_to_export,
            output_event_signal_terminal=expected_output_event_signal_terminal,
        )

        self.assertEqual(expected_source_trigger_behavior, instance.source_trigger_behavior)
        self.assertEqual(expected_start_source_name, instance.start_source_name)
        self.assertEqual(expected_export_event, instance.export_event)
        self.assertEqual(expected_event_signal_to_export, instance.event_signal_to_export)
        self.assertEqual(expected_output_event_signal_terminal, instance.output_event_signal_terminal)


class TestDCCurrentSourceAndMeasureParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `DCCurrentSourceAndMeasureParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_current_source_and_measure_parameters(self):
        """Checks DCCurrentSourceAndMeasureParameters construction and property getters."""  # noqa: D415, W505
        expected_current_channel_settings = CurrentChannelSettings(
            current_level=10e-6,
            current_level_range=0.1,
            voltage_limit=1.0,
            voltage_limit_range=2.0,
            sensing=nidcpower.Sense.REMOTE,
            enable_output=True,
        )
        expected_execution_settings = ExecutionSettings(
            execution_type=MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            skip_analysis=False,
        )
        expected_timing_parameters = TimingParameters(
            source_delay=0.1,
            aperture_time=0.02,
            transient_response=nidcpower.TransientResponse.NORMAL,
        )
        expected_trigger_parameters = TriggerParameters(
            source_trigger_behavior=SourceTriggerBehavior.Disable_Source_Trigger,
            start_source_name="",
            export_event=ExportEvent.NONE,
            event_signal_to_export=EventSignalToExport.Source_Complete_Event,
            output_event_signal_terminal="",
        )

        instance = DCCurrentSourceAndMeasureParameters(
            current_channel_settings=expected_current_channel_settings,
            execution_settings=expected_execution_settings,
            timing_parameters=expected_timing_parameters,
            trigger_parameters=expected_trigger_parameters,
        )

        self.assertIs(expected_current_channel_settings, instance.current_channel_settings)
        self.assertIs(expected_execution_settings, instance.execution_settings)
        self.assertIs(expected_timing_parameters, instance.timing_parameters)
        self.assertIs(expected_trigger_parameters, instance.trigger_parameters)


class TestDCCurrentSourceAndMeasureResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `DCCurrentSourceAndMeasureResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_dc_current_source_and_measure_result_data(self):
        """Checks DCCurrentSourceAndMeasureResultData construction and property getters."""  # noqa: D415, W505
        expected_execution_settings = {
            "Current Level Setting (A)": "10.0 uA",
            "Current Level Range (A)": "100.00 mA",
            "Voltage Limit Setting (V)": "1.000000 V",
            "Voltage Limit Range (V)": "2.00 V",
            "Aperture Time (Sec)": "20.0 ms",
            "Output Function": "DC_CURRENT",
            "Device Model": "NI PXIe-4141",
        }
        expected_measurement_results = {
            "formatted_measurements": {
                "Voltage Measurement": "1.000000 V",
                "Current Measurement": "10.0 uA",
                "Power": "10.0 uW",
                "Resistance": "100.00 kOhm",
            },
            "raw_measurements": {
                "Voltage Measurement (V)": 1.0,
                "Current Measurement (A)": 10e-6,
                "Power (W)": 10e-6,
                "Resistance (Ohm)": 100000.0,
            },
            "Compliance/Limit Reached": False,
        }

        instance = DCCurrentSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            measurement_results=expected_measurement_results,
        )

        self.assertEqual(expected_execution_settings, instance.execution_settings)
        self.assertEqual(expected_measurement_results, instance.measurement_results)

    def test_dc_current_source_and_measure_result_data_with_nan_values(self):
        """Checks DCCurrentSourceAndMeasureResultData with NaN values when no measurement is performed."""  # noqa: D415, W505
        expected_execution_settings = {
            "Current Level Setting (A)": math.nan,
            "Current Level Range (A)": math.nan,
            "Voltage Limit Setting (V)": math.nan,
            "Voltage Limit Range (V)": math.nan,
            "Aperture Time (Sec)": math.nan,
            "Output Function": "DC_CURRENT",
        }
        expected_measurement_results = {
            "formatted_measurements": {
                "Voltage Measurement": math.nan,
                "Current Measurement": math.nan,
            },
            "raw_measurements": {
                "Voltage Measurement (V)": math.nan,
                "Current Measurement (A)": math.nan,
            },
            "Compliance/Limit Reached": False,
        }

        instance = DCCurrentSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            measurement_results=expected_measurement_results,
        )

        self.assertTrue(math.isnan(instance.execution_settings["Current Level Setting (A)"]))
        self.assertTrue(math.isnan(instance.execution_settings["Aperture Time (Sec)"]))
        self.assertEqual("DC_CURRENT", instance.execution_settings["Output Function"])
        self.assertTrue(
            math.isnan(
                instance.measurement_results["formatted_measurements"]["Voltage Measurement"]
            )
        )
        self.assertTrue(
            math.isnan(
                instance.measurement_results["raw_measurements"]["Voltage Measurement (V)"]
            )
        )
        self.assertFalse(instance.measurement_results["Compliance/Limit Reached"])

    def test_dc_current_source_and_measure_result_data_compliance_reached(self):
        """Checks DCCurrentSourceAndMeasureResultData when compliance limit is reached."""  # noqa: D415, W505
        expected_execution_settings = {
            "Current Level Setting (A)": 10e-6,
            "Output Function": "DC_CURRENT",
        }
        expected_measurement_results = {
            "formatted_measurements": {
                "Voltage Measurement": "5.000000 V",
                "Current Measurement": "10.0 uA",
            },
            "raw_measurements": {
                "Voltage Measurement (V)": 5.0,
                "Current Measurement (A)": 10e-6,
            },
            "Compliance/Limit Reached": True,
        }

        instance = DCCurrentSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            measurement_results=expected_measurement_results,
        )

        self.assertTrue(instance.measurement_results["Compliance/Limit Reached"])


class TestConstantsForDCCurrentSourceAndMeasure(unittest.TestCase):
    """Defines a test fixture that checks
    `ConstantsForDCCurrentSourceAndMeasure` and default instances are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

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

        used_nidcpower_version = importlib.metadata.version("nidcpower")
        logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_default_execution_settings(self):
        """Checks DEFAULT_DC_CC_EXECUTION_SETTINGS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            DEFAULT_DC_CC_EXECUTION_SETTINGS.execution_type,
        )
        self.assertEqual(False, DEFAULT_DC_CC_EXECUTION_SETTINGS.skip_analysis)

    def test_default_channel_settings(self):
        """Checks DEFAULT_DC_CC_CHANNEL_SETTINGS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_AMPERES,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.current_level,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_RANGE_AMPERES,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.current_level_range,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_VOLTS,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.voltage_limit,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_VOLTAGE_LIMIT_RANGE_VOLTS,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.voltage_limit_range,
        )
        self.assertEqual(
            nidcpower.Sense.REMOTE,
            DEFAULT_DC_CC_CHANNEL_SETTINGS.sensing,
        )
        self.assertEqual(True, DEFAULT_DC_CC_CHANNEL_SETTINGS.enable_output)

    def test_default_timing_parameters(self):
        """Checks DEFAULT_DC_CC_TIMING_PARAMETERS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
            DEFAULT_DC_CC_TIMING_PARAMETERS.source_delay,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
            DEFAULT_DC_CC_TIMING_PARAMETERS.aperture_time,
        )
        self.assertEqual(
            nidcpower.TransientResponse.NORMAL,
            DEFAULT_DC_CC_TIMING_PARAMETERS.transient_response,
        )

    def test_default_trigger_parameters(self):
        """Checks DEFAULT_DC_CC_TRIGGER_PARAMETERS has expected default values."""  # noqa: D415, W505
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger,
            DEFAULT_DC_CC_TRIGGER_PARAMETERS.source_trigger_behavior,
        )
        self.assertEqual("", DEFAULT_DC_CC_TRIGGER_PARAMETERS.start_source_name)
        self.assertEqual(ExportEvent.NONE, DEFAULT_DC_CC_TRIGGER_PARAMETERS.export_event)
        self.assertEqual(
            EventSignalToExport.Source_Complete_Event,
            DEFAULT_DC_CC_TRIGGER_PARAMETERS.event_signal_to_export,
        )
        self.assertEqual("", DEFAULT_DC_CC_TRIGGER_PARAMETERS.output_event_signal_terminal)

    def test_default_source_and_measure_parameters(self):
        """Checks DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS has expected default sub-objects."""  # noqa: D415, W505
        params = DEFAULT_DC_CC_SOURCE_AND_MEASURE_PARAMETERS

        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_CURRENT_LEVEL_AMPERES,
            params.current_channel_settings.current_level,
        )
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            params.execution_settings.execution_type,
        )
        self.assertEqual(
            ConstantsForDCCurrentSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
            params.timing_parameters.source_delay,
        )
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger,
            params.trigger_parameters.source_trigger_behavior,
        )


if __name__ == "__main__":
    unittest.main()
