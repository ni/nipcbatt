"""Main sequence for executing audio test sequence"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)

# pylint: disable=W0105

# import functions
from nipcbatt.pcbatt_automation.audio_tests.audio_filter_check import audio_filter_check
from nipcbatt.pcbatt_automation.audio_tests.audio_line_check import audio_line_check
from nipcbatt.pcbatt_automation.audio_tests.turn_off_all_ao_channels import (
    power_down_all_ao_channels,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN ####################

""" Demonstrates extraction of tones (Frequency domain measurement) from the captured 
    Audio Signal (Single tone sine wave)"""

audio_line_check()

"""Example 2 - Demonstrates extraction of tones (Frequency domain measurement) from 
   the captured Multi tone Audio Signal"""

audio_filter_check()

######## CLEAN UP #####################

# Turn off all configured AO channels by configuring to 0V
power_down_all_ao_channels()
