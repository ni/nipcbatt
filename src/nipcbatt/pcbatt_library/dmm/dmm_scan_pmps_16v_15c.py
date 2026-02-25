"""This module interacts with the NI-DMM and NI-SWITCH drivers to control NI-DMM instruments
and provide a corresponding instrument handle according to the topology selected"""

from nipcbatt import switch
from nipcbatt import dmm

#Close shunts to run scan
close_all_shunts = True

#Generate switch objects for scan
mux_generation = switch.StaticDigitalPathGeneration()
shunt_generation = switch.StaticDigitalPathGeneration()

#Declare constants for initialization
mux_resource_name = "MUX_2527"
shunt_resource_name = "Shunt_2568"

mux_topology_name = "2527/2-Wire Dual 16x1 Mux"
shunt_topology_name = "2568/31-SPST"

max_wait = 5000

#Initialize switch objects
mux_generation.initialize(mux_resource_name, mux_topology_name, reset_device=True, simulate=False)
shunt_generation.initialize(shunt_resource_name, shunt_topology_name, reset_device=True, simulate=False)

# Close all shunt relays from 16 to 30 (NI 2568) in a fixed
# channel topology mapping - option to open shunts only for 2-wire resistance measuerments
if close_all_shunts:

    #cycle across all 16 channel pairs
    for i in range(15):

        #declare channels
        ch1 = 'ch' + str(i)
        ch2 = 'com' + str(i + 16)

        #create channel parameters and state objects
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch1, ch2)
        state = switch.StaticDigitalPathGenerationStateParameters(True)

        #configure terminal and timing settings
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait)

        #configure and generate
        shunt_generation.configure_and_generate(ts_settings, timing_settings)