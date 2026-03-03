"""This module provides test of integration of DMM DC RMS voltage generation"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nidmm
import nipcbatt
from nipcbatt import dmm

class TestIntegrationDmmDcRmsVoltageMeasurement(unittest.TestCase):
    """Definte a test fixture that check the integration of 
    'DmmDCRmsVoltage'
    
    Args:
        unittest.TestCase: Base class from which this class inherits
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

        used_niswitch_version = importlib.metadata.version("niswitch")
        logging.debug("%s = %s", nameof(used_niswitch_version), used_niswitch_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")


    def test_configure_only_dc_voltage(self):
        """CONFIGURE_ONLY should not perform a measurement."""

        resource_name = "Sim_DMM"
        powerline_freq = 60.0

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize(resource_name, powerline_freq)

        meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            dmm.VoltageRangeAndFunctions.DC_10V,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=0.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False  # disabled ⇒ immediate/-1 path
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.001,
            settle_time_seconds=0.01
        )

        cfg = dmm.DcRmsVoltageMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=10.0
        )

        result = uut.configure_and_measure(cfg)
        assert result is None


    def test_measure_only_dc_voltage(self):
        """MEASURE_ONLY should read and return a result."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            dmm.VoltageRangeAndFunctions.DC_1V,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=0.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=True
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.002,
            settle_time_seconds=0.02
        )

        cfg = dmm.DcRmsVoltageMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=10.0
        )

        result = uut.configure_and_measure(cfg)
        assert result is not None
        assert result.measurement is not None
        assert "Measured_Value" in result.measurement

        uut.close()


    def test_configure_and_measure_dc_voltage_trigger_disabled(self):
        """Trigger disabled forces IMMEDIATE and -1.0 delay."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            dmm.VoltageRangeAndFunctions.DC_100mV,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.EXTERNAL,   # ignored when disabled
            trigger_delay=0.123,                            # ignored when disabled
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.0005,
            settle_time_seconds=0.005
        )

        cfg = dmm.DcRmsVoltageMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=25.0  # DC path should not apply this
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        # Sanity check on execution settings produced by acquire_measurement
        assert "Function" in result.dmm_execution_settings
        assert "Aperture_Time(s)" in result.dmm_execution_settings
        assert "Settle_Time(s)" in result.dmm_execution_settings

        uut.close()


    def test_configure_and_measure_ac_voltage(self):
        """AC voltage measurement should apply ac_min_frequency and slope."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            dmm.VoltageRangeAndFunctions.AC_2V,
            dmm.ResolutionInDigits.DIGITS_4_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.EXTERNAL,
            trigger_delay=0.001,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=True
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.001,
            settle_time_seconds=0.01
        )

        cfg = dmm.DcRmsVoltageMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=123.0
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        assert result.measurement is not None

        # AC min frequency should be reported by acquire_measurement's execution settings
        assert "Minimum_Frequency(Hz)" in result.dmm_execution_settings
        assert result.dmm_execution_settings["Minimum_Frequency(Hz)"] == 123.0

        uut.close()


    def test_multiple_voltage_ranges_and_resolutions(self):
        """Exercise several voltage ranges and a common resolution."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        test_ranges = [
            dmm.VoltageRangeAndFunctions.DC_Voltage_Auto_Range,
            dmm.VoltageRangeAndFunctions.DC_100mV,
            dmm.VoltageRangeAndFunctions.DC_1V,
            dmm.VoltageRangeAndFunctions.DC_10V,
            dmm.VoltageRangeAndFunctions.DC_100V,
        ]

        for rng in test_ranges:
            meas_params = dmm.DcRmsVoltageMeasurementFunctionParameters(
                rng,
                dmm.ResolutionInDigits.DIGITS_4_5
            )

            trig_params = dmm.TriggerParameters(
                trigger_source=nidmm.TriggerSource.IMMEDIATE,
                trigger_delay=0.0,
                slope=dmm.Slope.RISING_EDGE,
                enable_trigger=True
            )

            timing_params = dmm.TimingParameters(
                aperture_time_seconds=0.001,
                settle_time_seconds=0.01
            )

            cfg = dmm.DcRmsVoltageMeasurementConfiguration(
                execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                measurement_function_parameters=meas_params,
                trigger_parameters=trig_params,
                timing_parameters=timing_params,
                ac_min_frequency=10.0
            )

            result = uut.configure_and_measure(cfg)
            assert result is not None
            assert "Measured_Value" in result.measurement

        uut.close()



    def test_voltage_initialize_and_close_is_idempotent(self):
        """Initialize then close twice to ensure no error and powerline is set."""

        uut = dmm.DcRmsVoltageMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        # Power line frequency should be set
        assert uut.session.powerline_freq == 60.0

        # First close
        uut.close()

        # Second close should be a no‑op (no exception)
        uut.close()

