# pylint: disable=C0301
"""This module provides waveform DC constant voltage source and measure data types unit tests."""

import importlib.metadata
import logging
import math
import sys
import unittest

import nidcpower
import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import AnalogWaveform
from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure_data_types import (
    EventSignalToExport,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TriggerParameters,
    WaveformExecutionSettings,
    WaveformTimingParameters,
    WaveformVoltageChannelSettings,
    WaveformVoltageSourceAndMeasureParameters,
    WaveformVoltageSourceAndMeasureResultData,
)
from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure_constants import (
    ConstantsForWaveformVoltageSourceAndMeasure,
    DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS,
    DEFAULT_WAVEFORM_CV_EXECUTION_SETTINGS,
    DEFAULT_WAVEFORM_CV_SOURCE_AND_MEASURE_PARAMETERS,
    DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS,
    DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS,
)


def _log_test_fixture_setup():
    """Logs the python and nidcpower versions used by the test fixtures."""  # noqa: D415, W505
    print("Setup test fixture")
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logging.debug("python version = %s", str(sys.version))
    logging.debug("python path = %s", sys.executable)

    used_nidcpower_version = importlib.metadata.version("nidcpower")
    logging.debug("%s = %s", nameof(used_nidcpower_version), used_nidcpower_version)


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
        _log_test_fixture_setup()

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
        _log_test_fixture_setup()

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
        _log_test_fixture_setup()

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
        _log_test_fixture_setup()

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_event_signal_to_export_members(self):
        """Checks EventSignalToExport enum members map to NI-DCPower attribute names."""  # noqa: D415, W505
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


class TestWaveformExecutionSettings(unittest.TestCase):
    """Defines a test fixture that checks
    `WaveformExecutionSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        _log_test_fixture_setup()

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_waveform_execution_settings(self):
        """Checks WaveformExecutionSettings construction and property getter."""  # noqa: D415, W505
        expected_execution_type = MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE

        instance = WaveformExecutionSettings(execution_type=expected_execution_type)

        self.assertEqual(expected_execution_type, instance.execution_type)

    def test_waveform_execution_settings_for_all_execution_types(self):
        """Checks WaveformExecutionSettings holds every MeasurementExecutionType value."""  # noqa: D415, W505
        for expected_execution_type in MeasurementExecutionType:
            instance = WaveformExecutionSettings(execution_type=expected_execution_type)

            self.assertEqual(expected_execution_type, instance.execution_type)


class TestWaveformVoltageChannelSettings(unittest.TestCase):
    """Defines a test fixture that checks
    `WaveformVoltageChannelSettings` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        _log_test_fixture_setup()

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_waveform_voltage_channel_settings(self):
        """Checks WaveformVoltageChannelSettings construction and property getters."""  # noqa: D415, W505
        expected_voltage_level_range = 6.0
        expected_current_limit_range = 0.1
        expected_current_limit = 0.01
        expected_step_time = 0.1
        expected_sensing = nidcpower.Sense.REMOTE
        expected_enable_output = True
        expected_voltage_setpoints = [0.0, 1.0, 2.0, 1.0, 0.0]

        instance = WaveformVoltageChannelSettings(
            voltage_level_range=expected_voltage_level_range,
            current_limit_range=expected_current_limit_range,
            current_limit=expected_current_limit,
            step_time=expected_step_time,
            sensing=expected_sensing,
            enable_output=expected_enable_output,
            voltage_setpoints=expected_voltage_setpoints,
        )

        self.assertEqual(expected_voltage_level_range, instance.voltage_level_range)
        self.assertEqual(expected_current_limit_range, instance.current_limit_range)
        self.assertEqual(expected_current_limit, instance.current_limit)
        self.assertEqual(expected_step_time, instance.step_time)
        self.assertEqual(expected_sensing, instance.sensing)
        self.assertEqual(expected_enable_output, instance.enable_output)
        self.assertListEqual(expected_voltage_setpoints, instance.voltage_setpoints)

    def test_waveform_voltage_channel_settings_local_sensing(self):
        """Checks WaveformVoltageChannelSettings with LOCAL sensing and output disabled."""  # noqa: D415, W505
        expected_voltage_level_range = 5.0
        expected_current_limit_range = 0.5
        expected_current_limit = 0.05
        expected_step_time = 0.02
        expected_sensing = nidcpower.Sense.LOCAL
        expected_enable_output = False
        expected_voltage_setpoints = [-1.0, 0.0, 1.0]

        instance = WaveformVoltageChannelSettings(
            voltage_level_range=expected_voltage_level_range,
            current_limit_range=expected_current_limit_range,
            current_limit=expected_current_limit,
            step_time=expected_step_time,
            sensing=expected_sensing,
            enable_output=expected_enable_output,
            voltage_setpoints=expected_voltage_setpoints,
        )

        self.assertEqual(expected_voltage_level_range, instance.voltage_level_range)
        self.assertEqual(expected_current_limit_range, instance.current_limit_range)
        self.assertEqual(expected_current_limit, instance.current_limit)
        self.assertEqual(expected_step_time, instance.step_time)
        self.assertEqual(expected_sensing, instance.sensing)
        self.assertEqual(expected_enable_output, instance.enable_output)
        self.assertListEqual(expected_voltage_setpoints, instance.voltage_setpoints)

    def test_waveform_voltage_channel_settings_with_single_setpoint(self):
        """Checks WaveformVoltageChannelSettings with a single voltage setpoint."""  # noqa: D415, W505
        expected_voltage_setpoints = [3.3]

        instance = WaveformVoltageChannelSettings(
            voltage_level_range=6.0,
            current_limit_range=0.1,
            current_limit=0.01,
            step_time=0.001,
            sensing=nidcpower.Sense.REMOTE,
            enable_output=True,
            voltage_setpoints=expected_voltage_setpoints,
        )

        self.assertListEqual(expected_voltage_setpoints, instance.voltage_setpoints)
        self.assertEqual(1, len(instance.voltage_setpoints))


class TestWaveformTimingParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `WaveformTimingParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        _log_test_fixture_setup()

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_waveform_timing_parameters(self):
        """Checks WaveformTimingParameters construction and property getters."""  # noqa: D415, W505
        expected_source_delay = 0.1
        expected_aperture_time = 0.02
        expected_transient_response = nidcpower.TransientResponse.NORMAL
        expected_voltage_gain_bandwidth = 5000.0
        expected_voltage_compensation_frequency = 50000.0
        expected_voltage_pole_zero_ratio = 0.16
        expected_current_gain_bandwidth = 50000.0
        expected_current_compensation_frequency = 250000.0
        expected_current_pole_zero_ratio = 5.0

        instance = WaveformTimingParameters(
            source_delay=expected_source_delay,
            aperture_time=expected_aperture_time,
            transient_response=expected_transient_response,
            voltage_gain_bandwidth=expected_voltage_gain_bandwidth,
            voltage_compensation_frequency=expected_voltage_compensation_frequency,
            voltage_pole_zero_ratio=expected_voltage_pole_zero_ratio,
            current_gain_bandwidth=expected_current_gain_bandwidth,
            current_compensation_frequency=expected_current_compensation_frequency,
            current_pole_zero_ratio=expected_current_pole_zero_ratio,
        )

        self.assertEqual(expected_source_delay, instance.source_delay)
        self.assertEqual(expected_aperture_time, instance.aperture_time)
        self.assertEqual(expected_transient_response, instance.transient_response)
        self.assertEqual(expected_voltage_gain_bandwidth, instance.voltage_gain_bandwidth)
        self.assertEqual(
            expected_voltage_compensation_frequency, instance.voltage_compensation_frequency
        )
        self.assertEqual(expected_voltage_pole_zero_ratio, instance.voltage_pole_zero_ratio)
        self.assertEqual(expected_current_gain_bandwidth, instance.current_gain_bandwidth)
        self.assertEqual(
            expected_current_compensation_frequency, instance.current_compensation_frequency
        )
        self.assertEqual(expected_current_pole_zero_ratio, instance.current_pole_zero_ratio)

    def test_waveform_timing_parameters_custom_transient(self):
        """Checks WaveformTimingParameters with CUSTOM transient response."""  # noqa: D415, W505
        expected_transient_response = nidcpower.TransientResponse.CUSTOM

        instance = WaveformTimingParameters(
            source_delay=0.0,
            aperture_time=0.001,
            transient_response=expected_transient_response,
            voltage_gain_bandwidth=100.0,
            voltage_compensation_frequency=200.0,
            voltage_pole_zero_ratio=0.5,
            current_gain_bandwidth=300.0,
            current_compensation_frequency=400.0,
            current_pole_zero_ratio=1.5,
        )

        self.assertEqual(expected_transient_response, instance.transient_response)
        self.assertEqual(0.0, instance.source_delay)
        self.assertEqual(0.001, instance.aperture_time)
        self.assertEqual(100.0, instance.voltage_gain_bandwidth)
        self.assertEqual(200.0, instance.voltage_compensation_frequency)
        self.assertEqual(0.5, instance.voltage_pole_zero_ratio)
        self.assertEqual(300.0, instance.current_gain_bandwidth)
        self.assertEqual(400.0, instance.current_compensation_frequency)
        self.assertEqual(1.5, instance.current_pole_zero_ratio)

    def test_waveform_timing_parameters_fast_transient(self):
        """Checks WaveformTimingParameters with FAST transient response."""  # noqa: D415, W505
        expected_transient_response = nidcpower.TransientResponse.FAST

        instance = WaveformTimingParameters(
            source_delay=0.05,
            aperture_time=0.01,
            transient_response=expected_transient_response,
            voltage_gain_bandwidth=5000.0,
            voltage_compensation_frequency=50000.0,
            voltage_pole_zero_ratio=0.16,
            current_gain_bandwidth=50000.0,
            current_compensation_frequency=250000.0,
            current_pole_zero_ratio=5.0,
        )

        self.assertEqual(expected_transient_response, instance.transient_response)
        self.assertEqual(0.05, instance.source_delay)
        self.assertEqual(0.01, instance.aperture_time)


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
        _log_test_fixture_setup()

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
        self.assertEqual(
            expected_output_event_signal_terminal, instance.output_event_signal_terminal
        )

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
        self.assertEqual(
            expected_output_event_signal_terminal, instance.output_event_signal_terminal
        )


class TestWaveformVoltageSourceAndMeasureParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `WaveformVoltageSourceAndMeasureParameters` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        _log_test_fixture_setup()

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_waveform_voltage_source_and_measure_parameters(self):
        """Checks WaveformVoltageSourceAndMeasureParameters construction and property getters."""  # noqa: D415, W505
        expected_voltage_channel_settings = WaveformVoltageChannelSettings(
            voltage_level_range=6.0,
            current_limit_range=0.1,
            current_limit=0.01,
            step_time=0.1,
            sensing=nidcpower.Sense.REMOTE,
            enable_output=True,
            voltage_setpoints=[0.0, 1.0, 0.0],
        )
        expected_execution_settings = WaveformExecutionSettings(
            execution_type=MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
        )
        expected_timing_parameters = WaveformTimingParameters(
            source_delay=0.0,
            aperture_time=0.001,
            transient_response=nidcpower.TransientResponse.NORMAL,
            voltage_gain_bandwidth=5000.0,
            voltage_compensation_frequency=50000.0,
            voltage_pole_zero_ratio=0.16,
            current_gain_bandwidth=50000.0,
            current_compensation_frequency=250000.0,
            current_pole_zero_ratio=5.0,
        )
        expected_trigger_parameters = TriggerParameters(
            source_trigger_behavior=SourceTriggerBehavior.Disable_Source_Trigger,
            start_source_name="",
            export_event=ExportEvent.NONE,
            event_signal_to_export=EventSignalToExport.Source_Complete_Event,
            output_event_signal_terminal="",
        )

        instance = WaveformVoltageSourceAndMeasureParameters(
            voltage_channel_settings=expected_voltage_channel_settings,
            execution_settings=expected_execution_settings,
            timing_parameters=expected_timing_parameters,
            trigger_parameters=expected_trigger_parameters,
        )

        self.assertIs(expected_voltage_channel_settings, instance.voltage_channel_settings)
        self.assertIs(expected_execution_settings, instance.execution_settings)
        self.assertIs(expected_timing_parameters, instance.timing_parameters)
        self.assertIs(expected_trigger_parameters, instance.trigger_parameters)


class TestWaveformVoltageSourceAndMeasureResultData(unittest.TestCase):
    """Defines a test fixture that checks
    `WaveformVoltageSourceAndMeasureResultData` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        _log_test_fixture_setup()

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_waveform_voltage_source_and_measure_result_data(self):
        """Checks WaveformVoltageSourceAndMeasureResultData construction and property getters."""  # noqa: D415, W505
        expected_execution_settings = {
            "Voltage Level Range (V)": "6.00 V",
            "Current Limit Setting (A)": "20.0 mA",
            "Current Limit Range (A)": "20.00 mA",
            "Sample Rate (S/s)": "1000.00 S/s",
            "Step Record Length (Samples)": 100,
            "Effective Step Time (Sec)": "100.0 ms",
            "Total Sequence Time (Sec)": "300.0 ms",
            "Transient Response": "NORMAL",
            "Device Model": "NI PXIe-4141",
        }
        expected_voltage_waveform = [
            AnalogWaveform(
                channel_name="Dev1/0",
                delta_time_seconds=0.001,
                samples=numpy.array([0.0, 0.5, 1.0]),
            )
        ]
        expected_current_waveform = [
            AnalogWaveform(
                channel_name="Dev1/0",
                delta_time_seconds=0.001,
                samples=numpy.array([0.001, 0.002, 0.003]),
            )
        ]

        instance = WaveformVoltageSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            voltage_waveform=expected_voltage_waveform,
            current_waveform=expected_current_waveform,
        )

        self.assertEqual(expected_execution_settings, instance.execution_settings)
        self.assertIs(expected_voltage_waveform, instance.voltage_waveform)
        self.assertIs(expected_current_waveform, instance.current_waveform)
        self.assertEqual("Dev1/0", instance.voltage_waveform[0].channel_name)
        self.assertEqual(0.001, instance.voltage_waveform[0].delta_time_seconds)
        numpy.testing.assert_allclose(
            numpy.array([0.0, 0.5, 1.0]), instance.voltage_waveform[0].samples
        )
        numpy.testing.assert_allclose(
            numpy.array([0.001, 0.002, 0.003]), instance.current_waveform[0].samples
        )

    def test_waveform_voltage_source_and_measure_result_data_with_nan_values(self):
        """Checks WaveformVoltageSourceAndMeasureResultData with NaN values and empty waveforms."""  # noqa: D415, W505
        expected_execution_settings = {
            "Voltage Level Range (V)": math.nan,
            "Current Limit Setting (A)": math.nan,
            "Current Limit Range (A)": math.nan,
            "Sample Rate (S/s)": math.nan,
            "Step Record Length (Samples)": math.nan,
            "Effective Step Time (Sec)": math.nan,
            "Total Sequence Time (Sec)": math.nan,
            "Transient Response": "NORMAL",
        }

        instance = WaveformVoltageSourceAndMeasureResultData(
            execution_settings=expected_execution_settings,
            voltage_waveform=[],
            current_waveform=[],
        )

        self.assertTrue(math.isnan(instance.execution_settings["Voltage Level Range (V)"]))
        self.assertTrue(math.isnan(instance.execution_settings["Sample Rate (S/s)"]))
        self.assertTrue(math.isnan(instance.execution_settings["Total Sequence Time (Sec)"]))
        self.assertEqual("NORMAL", instance.execution_settings["Transient Response"])
        self.assertListEqual([], instance.voltage_waveform)
        self.assertListEqual([], instance.current_waveform)


class TestConstantsForWaveformVoltageSourceAndMeasure(unittest.TestCase):
    """Defines a test fixture that checks
    `ConstantsForWaveformVoltageSourceAndMeasure` and default instances are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        _log_test_fixture_setup()

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_constants_values(self):
        """Checks ConstantsForWaveformVoltageSourceAndMeasure has expected scalar values."""  # noqa: D415, W505
        constants = ConstantsForWaveformVoltageSourceAndMeasure

        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            constants.DEFAULT_EXECUTION_TYPE,
        )
        self.assertEqual(6.0, constants.DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS)
        self.assertEqual(0.020, constants.DEFAULT_CURRENT_LIMIT_AMPERES)
        self.assertEqual(0.020, constants.DEFAULT_CURRENT_LIMIT_RANGE_AMPERES)
        self.assertEqual(0.1, constants.DEFAULT_STEP_TIME_SECONDS)
        self.assertEqual(nidcpower.Sense.REMOTE, constants.DEFAULT_SENSING)
        self.assertEqual(True, constants.DEFAULT_ENABLE_OUTPUT)
        self.assertListEqual([0.0, 1.0, 0.0], constants.DEFAULT_VOLTAGE_SETPOINTS)
        self.assertEqual(0.0, constants.DEFAULT_SOURCE_DELAY_SECONDS)
        self.assertEqual(0.001, constants.DEFAULT_APERTURE_TIME_SECONDS)
        self.assertEqual(nidcpower.TransientResponse.NORMAL, constants.DEFAULT_TRANSIENT_RESPONSE)
        self.assertEqual(5000.0, constants.DEFAULT_VOLTAGE_GAIN_BANDWIDTH)
        self.assertEqual(50000.0, constants.DEFAULT_VOLTAGE_COMPENSATION_FREQUENCY)
        self.assertEqual(0.16, constants.DEFAULT_VOLTAGE_POLE_ZERO_RATIO)
        self.assertEqual(50000.0, constants.DEFAULT_CURRENT_GAIN_BANDWIDTH)
        self.assertEqual(250000.0, constants.DEFAULT_CURRENT_COMPENSATION_FREQUENCY)
        self.assertEqual(5.0, constants.DEFAULT_CURRENT_POLE_ZERO_RATIO)
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger,
            constants.DEFAULT_SOURCE_TRIGGER_BEHAVIOR,
        )
        self.assertEqual("", constants.DEFAULT_START_SOURCE_NAME)
        self.assertEqual(ExportEvent.NONE, constants.DEFAULT_EXPORT_EVENT)
        self.assertEqual(
            EventSignalToExport.Source_Complete_Event,
            constants.DEFAULT_EVENT_SIGNAL_TO_EXPORT,
        )
        self.assertEqual("", constants.DEFAULT_OUTPUT_EVENT_SIGNAL_TERMINAL)

    def test_default_execution_settings(self):
        """Checks DEFAULT_WAVEFORM_CV_EXECUTION_SETTINGS has expected default values."""  # noqa: D415, W505
        self.assertIsInstance(DEFAULT_WAVEFORM_CV_EXECUTION_SETTINGS, WaveformExecutionSettings)
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_EXECUTION_TYPE,
            DEFAULT_WAVEFORM_CV_EXECUTION_SETTINGS.execution_type,
        )

    def test_default_channel_settings(self):
        """Checks DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS has expected default values."""  # noqa: D415, W505
        self.assertIsInstance(DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS, WaveformVoltageChannelSettings)
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS,
            DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS.voltage_level_range,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_RANGE_AMPERES,
            DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS.current_limit_range,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_LIMIT_AMPERES,
            DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS.current_limit,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_STEP_TIME_SECONDS,
            DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS.step_time,
        )
        self.assertEqual(nidcpower.Sense.REMOTE, DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS.sensing)
        self.assertEqual(True, DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS.enable_output)
        self.assertListEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_SETPOINTS,
            DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS.voltage_setpoints,
        )

    def test_default_timing_parameters(self):
        """Checks DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS has expected default values."""  # noqa: D415, W505
        self.assertIsInstance(DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS, WaveformTimingParameters)
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
            DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS.source_delay,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_APERTURE_TIME_SECONDS,
            DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS.aperture_time,
        )
        self.assertEqual(
            nidcpower.TransientResponse.NORMAL,
            DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS.transient_response,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_GAIN_BANDWIDTH,
            DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS.voltage_gain_bandwidth,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_COMPENSATION_FREQUENCY,
            DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS.voltage_compensation_frequency,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_POLE_ZERO_RATIO,
            DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS.voltage_pole_zero_ratio,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_GAIN_BANDWIDTH,
            DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS.current_gain_bandwidth,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_COMPENSATION_FREQUENCY,
            DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS.current_compensation_frequency,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_CURRENT_POLE_ZERO_RATIO,
            DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS.current_pole_zero_ratio,
        )

    def test_default_trigger_parameters(self):
        """Checks DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS has expected default values."""  # noqa: D415, W505
        self.assertIsInstance(DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS, TriggerParameters)
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger,
            DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS.source_trigger_behavior,
        )
        self.assertEqual("", DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS.start_source_name)
        self.assertEqual(ExportEvent.NONE, DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS.export_event)
        self.assertEqual(
            EventSignalToExport.Source_Complete_Event,
            DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS.event_signal_to_export,
        )
        self.assertEqual("", DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS.output_event_signal_terminal)

    def test_default_source_and_measure_parameters(self):
        """Checks DEFAULT_WAVEFORM_CV_SOURCE_AND_MEASURE_PARAMETERS has expected default sub-objects."""  # noqa: D415, W505
        params = DEFAULT_WAVEFORM_CV_SOURCE_AND_MEASURE_PARAMETERS

        self.assertIsInstance(params, WaveformVoltageSourceAndMeasureParameters)
        self.assertIs(DEFAULT_WAVEFORM_CV_CHANNEL_SETTINGS, params.voltage_channel_settings)
        self.assertIs(DEFAULT_WAVEFORM_CV_EXECUTION_SETTINGS, params.execution_settings)
        self.assertIs(DEFAULT_WAVEFORM_CV_TIMING_PARAMETERS, params.timing_parameters)
        self.assertIs(DEFAULT_WAVEFORM_CV_TRIGGER_PARAMETERS, params.trigger_parameters)
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_VOLTAGE_LEVEL_RANGE_VOLTS,
            params.voltage_channel_settings.voltage_level_range,
        )
        self.assertEqual(
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            params.execution_settings.execution_type,
        )
        self.assertEqual(
            ConstantsForWaveformVoltageSourceAndMeasure.DEFAULT_SOURCE_DELAY_SECONDS,
            params.timing_parameters.source_delay,
        )
        self.assertEqual(
            SourceTriggerBehavior.Disable_Source_Trigger,
            params.trigger_parameters.source_trigger_behavior,
        )


if __name__ == "__main__":
    unittest.main()
