"""This module provide test of integration of StaticDigitalPathGeneration"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt import switch

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

    def test_static_digital_path_initialize_generate_close(self):
        
        """Checks happy path -- initialize/close are called without incident"""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "SimSwitch"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch0, ch1 = "ch0", "ch1"
        connect = True 
        max_wait_debounce = 100

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch0, ch1)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        
        status = generation.configure_and_generate(ts_settings, timing_settings)

        return status.path_status
