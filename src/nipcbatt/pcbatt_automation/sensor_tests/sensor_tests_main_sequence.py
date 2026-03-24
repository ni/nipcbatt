"""Main sequence forr executing the Sensor Test"""  

from rtd_test import rtd_test
from thermistor_test_cdaq import thermistor_test_cdaq
from thermistor_test_testscale import thermistor_test_testscale
from thermocouple_test import thermocouple_test
from turn_off_all_ao_channels import power_down_all_ao_channels
from turn_off_power_channels import close_power_supply

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN #####################
"""Example 1 - Demonstrates the DC Voltgae generaion and Temperature measurement 
   with Thermistor using the Output and Input lines of cDAQ"""

thermistor_test_cdaq()

"""Example 2 - Demonstrates the DC Voltgae generaion and Temperature measurement 
   with Thermistor using the Power Module and Analog Input Module of TestScale """

thermistor_test_testscale()


"""Example 3 - Demonstrates Temprature measurement with RTD using AI lines or
   Module of cDAQ"""

rtd_test()

"""Example 4 - Demonstrates Temprature measurement with Thermocouple using AI 
   lines or Module of cDAQ"""
thermocouple_test()

######## CLEAN UP ####################
"""Turn of all the Power lines and AO channels """
power_down_all_ao_channels()
close_power_supply()
