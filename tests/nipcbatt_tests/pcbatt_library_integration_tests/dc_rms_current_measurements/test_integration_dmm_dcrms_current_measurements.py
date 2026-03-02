"""This module provides test of integration of DMM DC RMS current generation"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nidmm
import nipcbatt
from nipcbatt import dmm

from nidmm import errors as nidmm_errors

class TestIntegrationStaticDigitalPathGeneration(unittest.TestCase):
    """Definte a test fixture that chceck the integration of 
    'StaticDigitalPathGneration'
    
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
