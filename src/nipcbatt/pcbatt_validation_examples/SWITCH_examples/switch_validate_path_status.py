""" Validates that the path capability between points is detected and reported correctly """

import niswitch
from nipcbatt import switch
generation = switch.StaticDigitalPathGeneration()

resource_name = "Sim_MUX"
topology = "2527/2-Wire Dual 16x1 Mux"
max_wait_debounce = 100

#initialize session
module_characteristics = generation.initialize(resource_name, topology)

################## ch0 to ch1 connection ########################################################
channel_params1 = switch.StaticDigitalPathGenerationChannelParameters("ch0", "ch1")
state1 = switch.StaticDigitalPathGenerationStateParameters(True)
ts_settings1 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params1, state1)
timing_settings1 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
configuration1 = switch.StaticDigitalPathGenerationConfiguration(ts_settings1, timing_settings1)

path_status1 = generation.configure_and_generate(configuration1)
assert path_status1.path_status == niswitch.PathCapability.PATH_UNSUPPORTED

print()
print('ch0 to ch1')
generation.display_status(path_status1)

################# ch0 to com0 connection #########################################################
channel_params2 = switch.StaticDigitalPathGenerationChannelParameters("ch0", "com0")
state2 = switch.StaticDigitalPathGenerationStateParameters(True)
ts_settings2 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params2, state2)
timing_settings2 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
configuration2 = switch.StaticDigitalPathGenerationConfiguration(ts_settings2, timing_settings2)

path_status2 = generation.configure_and_generate(configuration2)
assert path_status2.path_status == niswitch.PathCapability.PATH_AVAILABLE

print()
print('ch0 to com0')
generation.display_status(path_status2)

################ ch1 to com0 connection ##########################################################
channel_params3 = switch.StaticDigitalPathGenerationChannelParameters("ch1", "com0")
state3 = switch.StaticDigitalPathGenerationStateParameters(True)
ts_settings3 = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params3, state3)
timing_settings3 = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
configuration3 = switch.StaticDigitalPathGenerationConfiguration(ts_settings3, timing_settings3)

path_status3 = generation.configure_and_generate(configuration3)
assert path_status3.path_status == niswitch.PathCapability.RESOURCE_IN_USE

print()
print('ch1 to com0')
generation.display_status(path_status3)

#close switch session
generation.close()

#print module characteristics
print()
generation.display_module_characteristics(module_characteristics)

print('\n')