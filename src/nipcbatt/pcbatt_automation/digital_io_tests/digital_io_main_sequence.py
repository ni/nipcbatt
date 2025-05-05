"""Main sequence for executing Digital IO Test"""  

# import functions
from nipcbatt.pcbatt_automation.digital_io_tests.digital_clock_test import (
    digital_clock_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.digital_count_events_sw_timed import (
    digital_count_events_sw_timed_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.digital_pattern_test import (
    digital_pattern_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.digital_pwm_test import (
    digital_pwm_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.digital_state_test import (
    digital_state_test,
)
from nipcbatt.pcbatt_automation.digital_io_tests.turn_off_all_do_channels import (
    power_down_all_do_channels,
)

############# SETUP ###################
# Import the simulated hardware to NI Max for running the example
"""In NI MAX, select File -> Import, and use the textbox under 'Import
   from File' to import the configuration file 'Hardware Config.ini' 
   to ensure the proper naming of global channels which will be
   used with this sequence and its dependencies"""

############# MAIN #####################

"""Example 1 - Demonstrates static digital state generation and measurement using Digital 
   output and input lines or modules"""

digital_state_test()

"""Example 2 - Demonstrates digital pattern generation and measurement using Digital input 
   and output lines or modules, Hardware Trigger is used for synchronization between generate 
   and capture."""

digital_pattern_test()

"""Example 3 - Demonstrates digital clock generation and frequency measurement through 
   counter-based measurements using Digital IO lines or Modules."""

digital_clock_test()

"""Example 4 - Demonstrates digital pulse generation and PWM measurement through counter-based 
   measurements using Core Digital IO Modules."""

digital_pwm_test()

"""Example 5 - Demonstrates digital pulse generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Software timed using an external wait."""

digital_count_events_sw_timed_test()

#### Note to run with Hardware: Enable the below example for HW Run #####
"""Example 6 - Demonstrates digital pattern generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Hardware timed using with Trigger to create a measurement window for fixed duration."""

# the below test is disabled as hw timed count digital events will throw errors during simulation
# digital_count_events_tests_hw_timed()


######## CLEAN UP ####################

"""Turn off all configured DO channels by setting Digital LOW state"""

power_down_all_do_channels()
