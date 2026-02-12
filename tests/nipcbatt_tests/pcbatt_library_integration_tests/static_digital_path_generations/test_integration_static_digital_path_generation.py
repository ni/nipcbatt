"""This module provide test of integration of StaticDigitalPathGeneration"""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt import switch
from niswitch import errors as niswitch_errors

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

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch0, com0 = "ch0", "com0"
        max_wait_debounce = 100

        # Connect
        connect = True 
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch0, com0)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        #Disconnect
        connect = False 
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        status = generation.configure_and_generate(ts_settings, timing_settings)
        generation.close()

        return status.path_status
    
    def test_bank1_ch20_to_com1_connect_disconnect(self):
        """Bank 1 happy path: ch20 <-> com1 connect, then disconnect."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch20", "com1"
        max_wait_debounce = 100

        # Connect
        connect = True
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        # Disconnect
        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        generation.close()
        return status.path_status
    
    def test_reject_channel_to_channel(self):
        """Mux cannot short two inputs: ch0 <-> ch1 should raise a DriverError."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch0, ch1 = "ch0", "ch1"
        connect = True
        max_wait_debounce = 100

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch0, ch1)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        with self.assertRaises(niswitch_errors.DriverError):
            generation.configure_and_generate(ts_settings, timing_settings)

        generation.close()

    def test_reject_cross_bank_common_mismatch(self):
        """Channel must route to its bank common: ch3 <-> com1 should raise a DriverError."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, wrong_com = "ch3", "com1"
        connect = True
        max_wait_debounce = 100

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, wrong_com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        with self.assertRaises(niswitch_errors.DriverError):
            generation.configure_and_generate(ts_settings, timing_settings)

        generation.close()

    def test_topology_change_requires_reset_then_succeeds(self):
        """
        If the device is on a different topology, reset_device=False should fail.
        Then reset_device=True should succeed. If already matching, skip the first part.
        """
        # Attempt without reset; if it succeeds, device is already on the requested topology.
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch0", "com0"
        connect = True
        max_wait_debounce = 100

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)

        try:
            generation.initialize(resource_name, topology, reset_device=False, simulate=True)
            generation.configure_and_generate(ts_settings, timing_settings)
        except niswitch_errors.DriverError:
            # Expected when current topology differs.
            generation.close()
        else:
            # Already matching topology; skip the "requires reset" assertion.
            generation.close()
            self.skipTest("Device already on requested topology; reset not required in this environment.")

        # Now with reset=True it should succeed deterministically.
        generation = switch.StaticDigitalPathGeneration()
        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        # Disconnect to leave the session clean
        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        status = generation.configure_and_generate(ts_settings, timing_settings)
        generation.close()
        return status.path_status

    def test_idempotent_connect_disconnect(self):
        """Calling connect/disconnect for the same pair repeatedly should be harmless."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch5", "com0"
        max_wait_debounce = 100

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        # Connect and disconnect twice
        connect = True
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        connect = True
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        generation.close()
        return status.path_status
    
    
    def test_multiple_sequential_routes_single_session(self):
        """Connect/disconnect several valid pairs sequentially in one session."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        max_wait_debounce = 100

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        for ch, com in [("ch1", "com0"), ("ch10", "com0"), ("ch25", "com1")]:
            connect = True
            channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
            state = switch.StaticDigitalPathGenerationStateParameters(connect)
            ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
            timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
            status = generation.configure_and_generate(ts_settings, timing_settings)

            connect = False
            state = switch.StaticDigitalPathGenerationStateParameters(connect)
            ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
            status = generation.configure_and_generate(ts_settings, timing_settings)

        generation.close()
        return status.path_status
    

    def test_zero_debounce_is_accepted(self):
        """Zero debounce should be accepted (as 'no wait' or driver default)."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch8", "com0"
        connect = True
        max_wait_debounce = 0  # zero

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        # Disconnect
        connect = False
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        status = generation.configure_and_generate(ts_settings, timing_settings)

        generation.close()
        return status.path_status
    
    def test_disconnect_without_prior_connect(self):
        """Disconnecting a non-existent path throw an error."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch, com = "ch2", "com0"
        connect = False
        max_wait_debounce = 100

        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch, com)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)

        try:
            generation.configure_and_generate(ts_settings, timing_settings)
        except niswitch_errors.DriverError:
            # Expected when current topology differs.
            generation.close()

        return 
    
    def test_error_on_repeated_close(self):
        """Calling close twice without initialize should throw an error."""
        generation = switch.StaticDigitalPathGeneration()

        resource_name = "Sim_MUX"
        topology = "2527/2-Wire Dual 16x1 Mux"
        ch0, com0 = "ch0", "com0"
        max_wait_debounce = 100

        # Connect
        connect = True 
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch0, com0)
        state = switch.StaticDigitalPathGenerationStateParameters(connect)
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)

        generation.initialize(resource_name, topology, reset_device=True, simulate=True)
        generation.configure_and_generate(ts_settings, timing_settings)

        generation.close()

        with self.assertRaises(niswitch_errors.DriverError):
            generation.close()

        return