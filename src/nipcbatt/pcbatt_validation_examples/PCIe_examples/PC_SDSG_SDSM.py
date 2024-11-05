"""Static Digital State Generation and Measurement"""

### Ensure correct hardware and corresponding trigger names before running this example

import nipcbatt
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize
sdsg = nipcbatt.StaticDigitalStateGeneration()
sdsg.initialize(channel_expression="Dev1/port0/line0:3")

# region SDSG configure and generate

sdsg_config = nipcbatt.StaticDigitalStateGenerationConfiguration(
    data_to_write=[False, True, False, True]
)

# endregion SDSG configure and generate

sdsg_result_data = sdsg.configure_and_generate(configuration=sdsg_config)

# region SDSM configure and measure

sdsm = nipcbatt.StaticDigitalStateMeasurement()
sdsm.initialize(channel_expression="Dev2/port0/line0:3")

# end region SDSM configure and measure

sdsm_result_data = sdsm.configure_and_measure()

sdsm.close()
sdsg.close()


print(sdsg_result_data)
print(sdsm_result_data.states_per_channels)

print("data_to_write-", sdsg_config.data_to_write)
print()
print("sdsm_result-", sdsm_result_data.digital_states)
print()
print("sdsm_channel_identifiers-", sdsm_result_data.channel_identifiers)
print()

save_traces(config=sdsg_config, file_name="SDSG", result_data=sdsg_result_data)

save_traces(config=None, file_name="SDSM", result_data=sdsm_result_data)
