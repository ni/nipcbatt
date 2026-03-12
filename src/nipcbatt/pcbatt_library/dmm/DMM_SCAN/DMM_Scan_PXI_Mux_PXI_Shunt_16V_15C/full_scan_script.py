# pylint: disable=C0200, C0103, C0301

"""This module interacts with the NI-DMM and NI-SWITCH drivers to control NI-DMM instruments
and provide a corresponding instrument handle according to the topology selected"""

import time

from nipcbatt import switch
from nipcbatt import dmm
from nipcbatt.pcbatt_library.dmm.common.common_data_types import ResolutionInDigits

#edit this list to define the configurations to use during the scan
#each entry should be a list in the format:
#  [channel (int), range & function (<type>RangeAndFunctions), resolution (ResolutionInDigits)]
scan_configuration = [
    [0,  dmm.VoltageRangeAndFunctions.DC_100mV,             ResolutionInDigits.DIGITS_6_5],
    [1,  dmm.VoltageRangeAndFunctions.DC_1V,                ResolutionInDigits.DIGITS_5_5],
    [2,  dmm.VoltageRangeAndFunctions.AC_2V,                ResolutionInDigits.DIGITS_4_5],
    [3,  dmm.ResistanceRangeAndFunctions.TWO_W_RES_10k_Ohm, ResolutionInDigits.DIGITS_4_5],
    [16, dmm.CurrentRangeAndFunctions.DC_100mA,             ResolutionInDigits.DIGITS_6_5],
    [17, dmm.CurrentRangeAndFunctions.DC_10mA,              ResolutionInDigits.DIGITS_5_5],
    [18, dmm.CurrentRangeAndFunctions.AC_10mA,              ResolutionInDigits.DIGITS_4_5]
]

# Data structures for output
raw_measurements = []
formatted_measurements = []
execution_settings = []


################## INTIIALIZATION #################################################################

#Generate switch objects for scan
mux_generation = switch.StaticDigitalPathGeneration()
shunt_generation = switch.StaticDigitalPathGeneration()

# Generate dmm object for mixed measurements
dmm_generation = dmm.MixedMeasurement()

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
mux_generation.close()
shunt_generation.close()
dmm_generation.close()

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
        config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        #configure and generate
        shunt_generation.configure_and_generate(config)


############################### MEASUREMENT SCAN ##########################################################

# extract range & function, resolution in digits and channel from scan configuration
function_range_resolution = []
channel_list = []
for cfg in scan_configuration:
    channel_list.append(cfg[0])
    function_range_resolution.append((cfg[1], cfg[2]))
    
# pair channels with respective com -- ch 0-15 -> com0, ch 16-30 -> com1
channel_pairs = []
for ch in channel_list:
    if ch < 16:
        pair = (ch, 'com0')
    else:
        pair = (ch, 'com1')
    channel_pairs.append(pair)

# previous function, range, resolution for comparison
prev = None

# start wall time counter
start_time = time.perf_counter()

# Main Scan Loop
for i in range(len(scan_configuration)):

    #extract ch (int) and com (string)
    ch, com = channel_pairs[i][0], channel_pairs[i][1]
    channel_name = 'ch' + str(ch)

    # MUX handling -- close MUX channel for respective ch#, com#
    channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
    state = switch.StaticDigitalPathGenerationStateParameters(True) # Use TRUE value to CLOSE mux channel
    ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
    timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait)
    mux_config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

    # execute configure and generate for max channel pair
    mux_generation.configure_and_generate(mux_config)


    # SHUNT handling -- if channel is a current channel, open SHUNT
    if ch >= 16 and close_all_shunts:   # current channels are ch16 - ch30
        com = 'com' + str(ch)
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
        state = switch.StaticDigitalPathGenerationStateParameters(False)  # False state to OPEN shunt
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait)
        shunt_config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        # execute configure and generate for shunt channel pair 
        shunt_generation.configure_and_generate(shunt_config)


    # DMM handling -- configure and acquire measurement
    function_and_range = function_range_resolution[i][0]
    resolution = function_range_resolution[i][1]

    # if previous function, range, and resolution are the same skip dmm configuration, otherwise configure
    if prev != function_range_resolution[i]:
        
        # instantiate parameters object
        params = dmm.MixedMeasurementFunctionParameters(function_and_range, resolution)
        dmm_generation.configure_measurement_function(params)

    # measure only
    dmm_read = dmm_generation.acquire_measurement(resolution.value)

    # SHUNT handling -- close current shunt if opened
    if ch >= 16 and close_all_shunts:   # current channels are ch16 - ch30
        com = 'com' + str(ch)
        channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
        state = switch.StaticDigitalPathGenerationStateParameters(True)  # True state to CLOSE shunt
        ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
        timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait)
        shunt_config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

        # execute configure and generate for shunt channel pair 
        shunt_generation.configure_and_generate(shunt_config)

    # MUX handling -- open MUX channel to release it
    ch, com = channel_pairs[i][0], channel_pairs[i][1]
    channel_name = 'ch' + str(ch)
    channel_params = switch.StaticDigitalPathGenerationChannelParameters(channel_name, com)
    state = switch.StaticDigitalPathGenerationStateParameters(False) # Use FALSE value to OPEN mux channel
    ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
    timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait)
    mux_config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

    # execute configure and generate for max channel pair
    mux_generation.configure_and_generate(mux_config)

    #measure elapsed time
    switch_time = time.perf_counter() - start_time

    #store raw output
    meas_type = params.measurement_function.value[0].name
    value = dmm_read.measurement
    raw_data = (channel_name, value, meas_type)
    raw_measurements.append(raw_data)

    #store formatted measurement output
    data = dmm_generation.acquire_measurement(resolution.value)
    meas = data.measurement
    formatted_meaurement = (channel_name, meas['Formatted_Measurement'], switch_time)
    formatted_measurements.append(formatted_meaurement)

    #store execution ettings
    exec_settings = data.dmm_execution_settings
    execution_settings.append(exec_settings)

    #store current function/range/resolution settings for comparison in next loop
    prev = function_range_resolution[i]

total_time_elapsed = time.perf_counter() - start_time

print()
print('------------- SCAN TIME --------------')
print('Total Scan Time (s):', f'{total_time_elapsed: .2f}')
print('\n')

print('------- FORMATTED MEASUREMENTS -------')
print(f'{"Channel":<10} {"Measurement":<18} {"Time":>8}')

for i in range(len(formatted_measurements)):
    measurement = formatted_measurements[i]
    full_unit = raw_measurements[i][2]

    if 'DC' in full_unit:
        unit = '(dc)'
    elif 'AC' in full_unit:
        unit = '(ac)'
    else:
        unit = '(ohm)'

    channel = measurement[0]
    value = f'{measurement[1]} {unit}'
    time = measurement[2]

    print(f'{channel:<10} {value:<18} {time:>8.3f}')
print('\n')

print('--------- EXECUTION SETTINGS ---------')
for setting in execution_settings:
    for key, value in setting.items():
        print(str(key) + ': ' + str(value))
    print()
print('\n')


#prepare raw measurements for output -- get largest width
values_as_str = [
    f"{m[1]['Measured_Value']:.16g}" for m in raw_measurements
]
value_width = max(len(v) for v in values_as_str)

print('----------- RAW MEASUREMENTS -------------')
print(f'{"Channel":<10} {"Value":^23} {"Units":^8}')

for measurement, value_str in zip(raw_measurements, values_as_str):
    channel = measurement[0]
    unit = measurement[1]['Unit']

    print(f'{channel:<10} {value_str:<{value_width}} {unit:>8}')
print('\n')


#close and release all resources
mux_generation.close()
shunt_generation.close()
dmm_generation.close()
