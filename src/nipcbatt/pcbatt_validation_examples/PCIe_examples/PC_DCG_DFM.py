# Digital Clock Generation to Digital Frequency Measurement 
### Ensure correct hardware and corresponding trigger names before running this example

import nipcbatt
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize
dcg = nipcbatt.DigitalClockGeneration()
dfm = nipcbatt.DigitalFrequencyMeasurement()

dcg.initialize(
    counter_channel_expression="Dev1/ctr0",
    output_terminal_name="/Dev1/PFI2",
)

dfm.initialize(
    channel_expression="Dev1/ctr2",
    input_terminal_name="/Dev1/PFI3",
)
# begin dcg configure

channel_parameters = nipcbatt.DigitalClockGenerationCounterChannelParameters(
    frequency_hertz=10000.0,
    duty_cycle_ratio=0.5,
)
clock_timing_parameters = nipcbatt.DigitalClockGenerationTimingParameters(
    clock_duration_seconds=0.1,
)
dcg_configuration = nipcbatt.DigitalClockGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=clock_timing_parameters,
)
# end region dcg configure

# begin dfm configure

range_parameters = nipcbatt.DigitalFrequencyRangeParameters(
    frequency_maximum_value_hertz=20000000.0,
    frequency_minimum_value_hertz=1.0,
)

counter_channel_parameter = nipcbatt.DigitalFrequencyMeasurementCounterChannelParameters(
    range_parameters=range_parameters,
    input_divisor_for_frequency_measurement=4,
    measurement_duration_seconds=0.10,
)

dfm_configuration = nipcbatt.DigitalFrequencyMeasurementConfiguration(
    counter_channel_configuration_parameters=counter_channel_parameter,
)
# end dfm configure

# begin generate and measure
dcg_results = dcg.configure_and_generate(configuration=dcg_configuration)
dfm_results = dfm.configure_and_measure(configuration=dfm_configuration)

# close generation and measurement session
dcg.close()
dfm.close()

print(dcg_results)
print()
print("detected_frequency(Hz):", dfm_results.frequency)
print()

save_traces(config=dfm_configuration, file_name="DFM", result_data=dfm_results)

save_traces(config=dcg_configuration, file_name="DCG", result_data=dcg_results)
