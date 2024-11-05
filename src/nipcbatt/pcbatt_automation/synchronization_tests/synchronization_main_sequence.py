"""Main Sequence for executing Power Supply Tests"""

# pylint: disable=W0105,C0413,E0401,C0301
# import functions
from nipcbatt.pcbatt_automation.synchronization_tests.digital_clock_generation_and_pwm_measurement import (
    digital_clock_generation_and_pwm_measurement,
)
from nipcbatt.pcbatt_automation.synchronization_tests.dynamic_digital_pattern_generation_and_measurement import (
    dynamic_digital_pattern_generation_and_measurement,
)
from nipcbatt.pcbatt_automation.synchronization_tests.signal_voltage_and_time_domain_measure import (
    signal_voltage_and_time_domain_measurement,
)
from nipcbatt.pcbatt_automation.synchronization_tests.turn_off_all_ao_channels import (
    power_down_all_ao_channels,
)
from nipcbatt.pcbatt_automation.synchronization_tests.turn_off_all_do_channels import (
    power_down_all_do_channels,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""


############# MAIN ####################

"""Example demonstrates synchronization with two TestScale backplane 
   using Analog and Digital Libraries"""

# Synchronization using Analog Libraries

signal_voltage_and_time_domain_measurement()

# Synchronization using Digital Libraries

dynamic_digital_pattern_generation_and_measurement()

# Synchronization using Digital Counter Libraries

digital_clock_generation_and_pwm_measurement()


######## CLEAN UP ####################

# Turn off all configured AO channels by configuring to 0V

power_down_all_ao_channels()

# Turn off all configured DO channels by setting digital low state

power_down_all_do_channels()
