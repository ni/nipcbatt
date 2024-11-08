"""Main Sequence for executing Action Button Test"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)

# pylint: disable=W0105

# import functions
from nipcbatt.pcbatt_automation.action_button_tests.action_button_test import (
    action_button_test,
)
from nipcbatt.pcbatt_automation.action_button_tests.turn_off_all_ao_channels import (
    power_down_all_ao_channels,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN ####################

"""Complete DC-RMS Voltage Measurements by performing button actions 
   (generating DC Voltages) on specific test points"""

action_button_test()

######## CLEAN UP ####################

# Turn off all configured AO channels by configuring to 0V
power_down_all_ao_channels()
