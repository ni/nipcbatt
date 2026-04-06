"""This module interacts with the NI-DMM and NI-SWITCH drivers to control NI-DMM instruments
and provide a corresponding instrument handle according to the topology selected"""

from nipcbatt import switch
from nipcbatt import dmm
from nipcbatt.pcbatt_library.dmm.common.common_data_types import ResolutionInDigits

#edit this list to define the configurations to use during the scan
#each entry should be a list in the format [channel, range & function, resolution]
scan_configuration = [
    ['0',  dmm.VoltageRangeAndFunctions.DC_100mV, ResolutionInDigits.DIGITS_6_5],
    ['1',  dmm.VoltageRangeAndFunctions.DC_1V,    ResolutionInDigits.DIGITS_5_5],
    ['2',  dmm.VoltageRangeAndFunctions.DC_10V,   ResolutionInDigits.DIGITS_4_5],
    ['16', dmm.VoltageRangeAndFunctions.AC_200mV, ResolutionInDigits.DIGITS_7_5],
    ['17', dmm.VoltageRangeAndFunctions.AC_2V,    ResolutionInDigits.DIGITS_5_5],
    ['18', dmm.VoltageRangeAndFunctions.AC_20V,   ResolutionInDigits.DIGITS_4_5]
]


################## INTIIALIZATION #################################################################

#Generate switch objects for scan
mux_generation = switch.StaticDigitalPathGeneration()
shunt_generation = switch.StaticDigitalPathGeneration()
dmm_generation = dmm.DcRmsVoltageMeasurement()

#Close shunts to run scan
close_all_shunts = True

#Declare constants for initialization
mux_resource_name = "Sim_MUX"
shunt_resource_name = "Sim_SHUNT"
dmm_resource_name = "Sim_DMM"

mux_topology_name = "2527/2-Wire Dual 16x1 Mux"
shunt_topology_name = "2568/31-SPST"

max_wait = 5000
powerline_freq = 50

#Initialize objects
mux_generation.initialize(mux_resource_name, mux_topology_name, reset_device=True, simulate=False)
shunt_generation.initialize(shunt_resource_name, shunt_topology_name, reset_device=True, simulate=False)
dmm_generation.initialize(dmm_resource_name, powerline_freq)

# Close all shunt relays from 16 to 30 (NI 2568) in a fixed
# channel topology mapping - option to open shunts only for 2-wire resistance measuerments
if close_all_shunts:

    #cycle across all 16 channel pairs
    for i in range(15):

        #adjust channel index
        idx = i + 16

        #declare channels
        ch1 = f'ch{idx}'
        ch2 = f'com{idx}'

        #create channel parameters and state objects
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(ch1, ch2)
        state = switch.StaticDigitalPathGenerationStateParameters(True)

        #configure terminal and timing settings
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait)

        #configure and generate
        shunt_generation.configure_and_generate(ts_settings, timing_settings)


############################### MEASUREMENT SCAN ##########################################################



print('SUCCESS')

#close and release all resources
mux_generation.close()
shunt_generation.close()
dmm_generation.close()
