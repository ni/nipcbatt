"""Main sequence for Analog PWM test"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (150 > 100 characters) (auto-generated noqa)

# Import Functions
from analog_pwm_test import analog_pwm_test
from analog_voltage_measurement_test import analog_voltage_measurement
from turn_off_all_ao_channels import power_down_all_ao_channels

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN #####################
"""Example 1 - Demonstrates DC RMS Voltage Measurement using the Analog Input 
   Channels or Modules"""
analog_voltage_measurement()

"""Example 2 - Demonstrates the Analog PWM Signal Voltage Generation and 
   Time Domain Voltage Measurement"""
analog_pwm_test()

######## CLEAN UP ####################
"""Turns off all configured AO channels by setting the output voltage to 0"""
power_down_all_ao_channels()
