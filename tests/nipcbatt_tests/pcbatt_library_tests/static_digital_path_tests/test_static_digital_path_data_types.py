"""This module provides static digital path data types check."""

import importlib.metadata
import logging
import random
import string
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.switch.static_digital_path_generations.static_digital_path_data_types import (
    StaticDigitalPathGenerarionPathStatus,
    StaticDigitalPathGenerationChannelParameters,
    StaticDigitalPathGenerationModuleCharacteristics,
    StaticDigitalPathGenerationStateParameters,
    StaticDigitalPathGenerationTerminalAndStateSettings,
    StaticDigitalPathGenerationTimingParameters
)

class TestStaticDigitalPathGenerationData(unittest.TestCase):
    """Defines a test fixture that ensures the class 
       'StaticDigitalStateGenerationData' is correct and
       ready to use

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    
    def test_static_digital_path_generation_channel_parameters(self):
        """Test the creation of a StaticDigitalStateGenerationData object"""
        channel_one = 'chan1'
        channel_two = 'chan2'

        instance = StaticDigitalPathGenerationChannelParameters(channel_one, channel_two)
        
        self.assertTrue(instance.channel_one == channel_one)
        self.assertTrue(instance.channel_two == channel_two)

    def test_static_digital_generation_channel_parameters_with_invalid_data(self):
        """Tests the creation of StaticDigitalStateGenerationData object with
            invalid data. The value errors should be caught."""
        
        channel_one = 'chan1'
        channel_two = 'chan2'
        
        #Test if a value error is thrown when channel_one is None
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters(None, channel_two)
        )

        #Test if a value error is thrown when channel_one is an empty string
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters('', channel_two)
        )

        #Test if a value error is thrown when channel_two is None
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters(channel_one, None)
        )

        #Test if a value erro is thrown when channel_two is empty 
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters(channel_one, "")
        )

    def test_static_digital_path_generation_status_with_valid_data(self):
        """Tests the generation static digital path status with valid data"""

        path_status = True 
        instance = StaticDigitalPathGenerarionPathStatus(path_status)
        self.assertTrue(instance.path_status == path_status)

    def test_static_digital_path_generation_status_false_is_valid(self):
        """False should also be accepted as a valid status (non-float, non-None)."""

        path_status = False
        instance = StaticDigitalPathGenerarionPathStatus(path_status)
        self.assertIs(instance.path_status, False)

    def test_static_digital_path_generation_status_with_invalid_data(self):
        """Tests the generation static digital path status with invalid data
            throws a ValueError as expected"""

        #Tests if a path is None and will throw an error if so
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerarionPathStatus(None)
        )

        #Tests if a path is a float and will throw an error if so
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerarionPathStatus(1.1)
        )
        
    def test_static_digital_path_generation_timing_parameters_with_valid_data(self):
        """Tests if a StaticDigitalTimingParameters object correctly 
        instantiates when given valid data"""

        max_wait = 100

        parameters = StaticDigitalPathGenerationTimingParameters(max_wait)

        self.assertTrue(parameters.max_debounce_wait == max_wait)

    
    def test_static_digital_generation_channel_parameters_with_whitespace(self):
        """Whitespace-only channel names should be rejected."""
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters("   ", "chan2"),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationChannelParameters("chan1", " \t "),
        )


    def test_static_digital_path_generation_state_parameters_valid_true_false(self):
        """Both True and False should be accepted."""
        p_true = StaticDigitalPathGenerationStateParameters(True)
        p_false = StaticDigitalPathGenerationStateParameters(False)

        self.assertTrue(p_true.connect is True)
        self.assertTrue(p_false.connect is False)

    def test_static_digital_path_generation_state_parameters_invalid(self):
        """Invalid types should be rejected."""
        self.assertRaises(
            ValueError, lambda: StaticDigitalPathGenerationStateParameters(None)
        )
        self.assertRaises(
            ValueError, lambda: StaticDigitalPathGenerationStateParameters(1.0)
        )


    def test_static_digital_path_generation_timing_parameters_zero_and_positive(self):
        """Zero and positive max_debounce_wait are valid."""
        p0 = 0
        p100 = 100

        p0 = StaticDigitalPathGenerationTimingParameters(p0)
        p100 = StaticDigitalPathGenerationTimingParameters(p100)

        self.assertEqual(p0.max_debounce_wait, 0)
        self.assertEqual(p100.max_debounce_wait, 100)

    def test_static_digital_path_generation_timing_parameters_invalid_negative(self):
        """Negative values should be rejected."""
        self.assertRaises(
            ValueError, lambda: StaticDigitalPathGenerationTimingParameters(-1)
        )
        # If Guard compares numerically, negative floats should also fail:
        self.assertRaises(
            ValueError, lambda: StaticDigitalPathGenerationTimingParameters(-1.0)
        )

    def test_static_digital_path_generation_terminal_and_state_settings_valid(self):
        """Valid aggregation of channel + state parameters."""
        ch = StaticDigitalPathGenerationChannelParameters("c1", "c2")
        st = StaticDigitalPathGenerationStateParameters(True)
        settings = StaticDigitalPathGenerationTerminalAndStateSettings(ch, st)

        self.assertIs(settings.channel_parameters, ch)
        self.assertIs(settings.connection_state, st)
        self.assertEqual(settings.channel_parameters.channel_one, "c1")
        self.assertEqual(settings.channel_parameters.channel_two, "c2")
        self.assertIs(settings.connection_state.connect, True)

    def test_static_digital_path_generation_terminal_and_state_settings_invalid(self):
        """None for either parameter should be rejected."""
        ch = StaticDigitalPathGenerationChannelParameters("c1", "c2")
        st = StaticDigitalPathGenerationStateParameters(False)

        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationTerminalAndStateSettings(None, st),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationTerminalAndStateSettings(ch, None),
        )


    def test_static_digital_path_generation_module_characteristics_valid(self):
        """Non-negative floats should be accepted; properties should return exact values."""
        mc = StaticDigitalPathGenerationModuleCharacteristics(
            max_dc_voltage=5.0,
            max_ac_voltage=10.0,
            max_switching_dc_current=0.5,
            max_switching_ac_current=0.75,
        )
        self.assertEqual(mc.max_dc_voltage, 5.0)
        self.assertEqual(mc.max_ac_voltage, 10.0)


    def test_static_digital_path_generation_module_characteristics_invalid_none(self):
        """Each field None should be rejected individually."""
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                None, 10.0, 0.5, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, None, 0.5, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, 10.0, None, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, 10.0, 0.5, None
            ),
        )

    def test_static_digital_path_generation_module_characteristics_invalid_negative(self):
        """Negative values should be rejected for each field."""
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                -1.0, 10.0, 0.5, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, -1.0, 0.5, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, 10.0, -0.01, 0.75
            ),
        )
        self.assertRaises(
            ValueError,
            lambda: StaticDigitalPathGenerationModuleCharacteristics(
                5.0, 10.0, 0.5, -0.01
            ),
        )


    




