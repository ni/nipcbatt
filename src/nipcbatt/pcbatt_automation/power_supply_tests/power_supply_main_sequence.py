"""Main Sequence for executing Power Supply Tests"""  

# import functions
from nipcbatt.pcbatt_automation.power_supply_tests.power_down_all_power_channels import (
    power_down_all_power_channels,
)
from nipcbatt.pcbatt_automation.power_supply_tests.power_supply_test_with_trigger import (
    power_supply_test_with_trigger,
)
from nipcbatt.pcbatt_automation.power_supply_tests.power_supply_test_without_trigger import (
    power_supply_test_without_trigger,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN ####################

"""Synchronization using analog libraries"""

power_supply_test_with_trigger()

"""Synchronziation using digital libraries"""

power_supply_test_without_trigger()

"""Synchronization using digital counter libraries"""

######## CLEAN UP ####################

# Power down all Power Supplies
power_down_all_power_channels()
