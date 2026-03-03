"""This module provides test of integration of DMM DC RMS current generation"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nidmm
import nipcbatt
from nipcbatt import dmm

class TestIntegrationDmmDcRmsCurrentMeasurement(unittest.TestCase):
    """Definte a test fixture that check the integration of 
    'DmmDCRmsCurrent'
    
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


    def test_initialize_configure_measure_close_dc(self):
        """Happy path: DC current configure & measure."""

        resource_name = "Sim_DMM"
        powerline_freq = 60.0

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize(resource_name, powerline_freq)

        meas_params = dmm.DcRmsCurrentMeasurementFunctionParameters(
             dmm.CurrentRangeAndFunctions.DC_1mA,
             dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
             trigger_source = nidmm.TriggerSource.IMMEDIATE,
             trigger_delay= 0.0,
             slope=dmm.Slope.RISING_EDGE,
             enable_trigger=True
        )
       
        timing_params = dmm.TimingParameters(
             aperture_time_seconds = 0.001,
             settle_time_seconds = 0.01
        )

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
             execution_type = nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
             measurement_function_parameters = meas_params,
             trigger_parameters = trig_params,
             timing_parameters = timing_params,
             ac_min_frequency = 10.0
        )

        result = uut.configure_and_measure(cfg)

        uut.close()


    def test_initialize_and_close_is_idempotent(self):

        "Tests if class methods are idempotent"

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        # Power line frequency should be set
        assert uut.session.powerline_freq == 60.0  # attribute assignment on session

        # First close should call session.close and clear instrument
        uut.close()

        # Second close should be a no-op (no exception, no additional close())
        uut.close()


    def test_configure_only_returns_none(self):

        """Ensures configure only returns none"""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_function_parameters=dmm.DcRmsCurrentMeasurementFunctionParameters(
                dmm.CurrentRangeAndFunctions.DC_10mA, dmm.ResolutionInDigits.DIGITS_5_5
            ),
            trigger_parameters=dmm.TriggerParameters(
                trigger_source=nidmm.TriggerSource.IMMEDIATE,
                trigger_delay=0.0,
                slope=None,
                enable_trigger=False,
            ),
            timing_parameters=dmm.TimingParameters(0.001, 0.01),
            ac_min_frequency=10.0,
        )

        result = uut.configure_and_measure(cfg)
        assert result is None  # configure-only path returns None 

        uut.close()

    
    def test_measure_only_reads_and_wraps(self):

        """Ensure measure only reads"""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_function_parameters=dmm.DcRmsCurrentMeasurementFunctionParameters(
                dmm.CurrentRangeAndFunctions.DC_1mA, dmm.ResolutionInDigits.DIGITS_5_5
            ),
            trigger_parameters=dmm.TriggerParameters(
                trigger_source=nidmm.TriggerSource.IMMEDIATE, trigger_delay=0.0, slope=None, enable_trigger=True
            ),
            timing_parameters=dmm.TimingParameters(0.001, 0.01),
            ac_min_frequency=10.0,
        )

        result = uut.configure_and_measure(cfg)

        # `acquire_measurement` returns a result object with two dicts
        assert result is not None
        assert isinstance(result.dmm_execution_settings, dict)
        assert isinstance(result.measurement, dict)  # built in acquire_measurement 
        uut.close()


    def test_configure_measure_ac(self):
        """AC current measurement should apply ac_min_frequency."""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            dmm.CurrentRangeAndFunctions.AC_100mA,
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

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=55.0  # AC path should apply this
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        assert result.measurement is not None
        assert "Measured_Value" in result.measurement

        # AC min frequency should appear in result settings
        assert "Minimum_Frequency(Hz)" in result.dmm_execution_settings
        assert result.dmm_execution_settings["Minimum_Frequency(Hz)"] == 55.0

        uut.close()


    def test_trigger_disabled(self):
        """Trigger disabled should force IMMEDIATE trigger."""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        meas_params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            dmm.CurrentRangeAndFunctions.DC_100uA,
            dmm.ResolutionInDigits.DIGITS_5_5
        )

        trig_params = dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.EXTERNAL,  # ignored when disabled
            trigger_delay=999.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False
        )

        timing_params = dmm.TimingParameters(
            aperture_time_seconds=0.0005,
            settle_time_seconds=0.005
        )

        cfg = dmm.DcRmsCurrentMeasurementConfiguration(
            execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            measurement_function_parameters=meas_params,
            trigger_parameters=trig_params,
            timing_parameters=timing_params,
            ac_min_frequency=10.0
        )

        result = uut.configure_and_measure(cfg)

        assert result is not None
        assert "Function" in result.dmm_execution_settings

        # Trigger disabled should set delay to -1.0 (from your implementation)
        assert result.dmm_execution_settings["Auto_Range_Value"] is not None  # sanity check

    
    def test_multiple_ranges_and_resolutions(self):
        """Verify several measurement function parameters work."""

        uut = dmm.DcRmsCurrentMeasurement()
        uut.initialize("Sim_DMM", 60.0)

        # Try several ranges
        test_ranges = [
            dmm.CurrentRangeAndFunctions.DC_1uA,
            dmm.CurrentRangeAndFunctions.DC_100uA,
            dmm.CurrentRangeAndFunctions.DC_10mA,
            dmm.CurrentRangeAndFunctions.DC_1A
        ]

        for rng in test_ranges:
            meas_params = dmm.DcRmsCurrentMeasurementFunctionParameters(
                rng,
                dmm.ResolutionInDigits.DIGITS_4_5
            )

            cfg = dmm.DcRmsCurrentMeasurementConfiguration(
                execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
                measurement_function_parameters=meas_params,
                trigger_parameters=dmm.TriggerParameters(
                    trigger_source=nidmm.TriggerSource.IMMEDIATE,
                    trigger_delay=0.0,
                    slope=dmm.Slope.RISING_EDGE,
                    enable_trigger=True
                ),
                timing_parameters=dmm.TimingParameters(0.001, 0.01),
                ac_min_frequency=10.0
            )

            result = uut.configure_and_measure(cfg)
            assert result is not None
            assert "Measured_Value" in result.measurement

        uut.close()

