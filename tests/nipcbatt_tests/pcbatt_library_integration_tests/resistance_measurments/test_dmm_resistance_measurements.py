"""This module provides test of integration of DMM resistance measurement"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nidmm
import nipcbatt
from nipcbatt import dmm

class TestIntegrationDmmResistanceMeasurement(unittest.TestCase):
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


    def test_configure_only_resistance(self):
        """CONFIGURE_ONLY should not perform a measurement."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.ResistanceMeasurementFunctionParameters(
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=0.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False   # disabled ⇒ immediate/-1.0 path
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.001,
            settle_time_seconds=0.01
        )

        cfg = dmm.ResistanceMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
        )

        result = uut.configure_and_measure(cfg)
        assert result is None  # configure-only should return None per implementation

        uut.close()


    def test_measure_only_resistance(self):
        """MEASURE_ONLY should read and return a result."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.ResistanceMeasurementFunctionParameters(
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_10k_Ohm,
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

        cfg = dmm.ResistanceMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
        )

        result = uut.configure_and_measure(cfg)
        assert result is not None
        assert result.measurement is not None
        assert "Measured_Value" in result.measurement  # packaged by acquire_measurement 

        uut.close()

    
    def test_configure_and_measure_resistance_2w_trigger_disabled(self):
        """Trigger disabled forces IMMEDIATE and -1.0 delay."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.ResistanceMeasurementFunctionParameters(
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_100_Ohm,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.EXTERNAL,  # ignored when disabled
            trigger_delay=0.123,                            # ignored when disabled
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.0005,
            settle_time_seconds=0.005
        )

        cfg = dmm.ResistanceMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        # Sanity checks on execution settings dictionary created in acquire_measurement
        for key in ["Function", "Aperture_Time(s)", "Settle_Time(s)", "Digits_Resolution"]:
            assert key in result.dmm_execution_settings  # fields produced by acquire_measurement 

        uut.close()


    def test_configure_and_measure_resistance_4w_trigger_enabled(self):
        """4-wire resistance with trigger enabled uses provided source/delay and slope."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.ResistanceMeasurementFunctionParameters(
            dmm.ResistanceRangeAndFunctions.FOUR_W_RES_1k_Ohm,
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

        cfg = dmm.ResistanceMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
        )

        result = uut.configure_and_measure(cfg)

        # Should get a measurement packaged by acquire_measurement
        assert result is not None
        assert result.measurement is not None
        assert "Measured_Value" in result.measurement  # produced by FormatMeasurement.measurement(...) 

        uut.close()


    def test_multiple_resistance_ranges_and_resolutions(self):
        """Exercise several 2W and 4W resistance ranges with a common resolution."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        test_ranges = [
            dmm.ResistanceRangeAndFunctions.TWO_W_Resistance_Auto_Range,
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm,
            dmm.ResistanceRangeAndFunctions.TWO_W_RES_1M_Ohm,
            dmm.ResistanceRangeAndFunctions.FOUR_W_Resistance_Auto_Range,
            dmm.ResistanceRangeAndFunctions.FOUR_W_RES_100_Ohm,
            dmm.ResistanceRangeAndFunctions.FOUR_W_RES_10k_Ohm,
        ]

        for rng in test_ranges:
            meas_params = dmm.ResistanceMeasurementFunctionParameters(
                rng,
                dmm.ResolutionInDigits.DIGITS_4_5
            )

            cfg = dmm.ResistanceMeasurementConfiguration(
                execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                measurement_function_parameters=meas_params,
                trigger_parameters=dmm.TriggerParameters(
                    trigger_source=nidmm.TriggerSource.IMMEDIATE,
                    trigger_delay=0.0,
                    slope=dmm.Slope.RISING_EDGE,
                    enable_trigger=True
                ),
                timing_parameters=dmm.TimingParameters(0.001, 0.01),
            )

            result = uut.configure_and_measure(cfg)
            assert result is not None
            assert "Measured_Value" in result.measurement  # validates measurement path and packaging 

        uut.close()


    def test_resistance_initialize_and_close_is_idempotent(self):
        """Initialize then close twice to ensure no error and powerline is set."""

        uut = dmm.DcRmsResistanceMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        # Power line frequency should be set onto the NI-DMM session
        assert uut.session.powerline_freq == 60.0  # assigned during initialize 
        # First close
        uut.close()

        # Second close should be a no-op (no exception)
        uut.close()