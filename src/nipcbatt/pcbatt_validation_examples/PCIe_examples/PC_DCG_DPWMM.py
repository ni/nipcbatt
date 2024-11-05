# Digital Clock Generation to Digital Pulse Width Measurement  # noqa: D100, W505 - Missing docstring in public module (auto-generated noqa), doc line too long (134 > 100 characters) (auto-generated noqa)
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize

dcg = nipcbatt.DigitalClockGeneration()
dpwmm = nipcbatt.DigitalPwmMeasurement()

dcg.initialize(
    counter_channel_expression="Dev1/ctr0",
    output_terminal_name="/Dev1/PFI2",
)

dpwmm.initialize(
    channel_expression="Dev1/ctr2",
    input_terminal_name="/Dev1/PFI3",
)

# begin dpwmm configure

range_parameters = nipcbatt.DigitalPwmMeasurementRangeParameters(
    semi_period_maximum_value_seconds=53.687,
    semi_period_minimum_value_seconds=20e-9,
)

timing_parameters = nipcbatt.DigitalPwmMeasurementTimingParameters(
    semi_period_counter_wanted_cycles_count=2,
)

counter_channel_parameters = nipcbatt.DigitalPwmMeasurementCounterChannelParameters(
    timing_parameters=timing_parameters,
    range_parameters=range_parameters,
    semi_period_counter_starting_edge=nidaqmx.constants.Edge.RISING,
)


dpwmm_configuration = nipcbatt.DigitalPwmMeasurementConfiguration(
    parameters=counter_channel_parameters,
    measurement_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
)

dpwmm.configure_and_measure(configuration=dpwmm_configuration)
# end region dpwmm configure

# begin dcg configure and generate
channel_parameters = nipcbatt.DigitalClockGenerationCounterChannelParameters(
    frequency_hertz=10000.0,
    duty_cycle_ratio=0.5,
)
clock_timing_parameters = nipcbatt.DigitalClockGenerationTimingParameters(
    clock_duration_seconds=0.10,
)
dcg_configuration = nipcbatt.DigitalClockGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=clock_timing_parameters,
)
# end region dcg configure and generate
dcg_results = dcg.configure_and_generate(configuration=dcg_configuration)

dpwmm_configuration = nipcbatt.DigitalPwmMeasurementConfiguration(
    parameters=counter_channel_parameters,
    measurement_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
)
dpwmm_results = dpwmm.configure_and_measure(configuration=dpwmm_configuration)

# close generation and measurement session
dcg.close()
dpwmm.close()

print(dcg_results)
print(dpwmm_results)

save_traces(config=dpwmm_configuration, file_name="DPWMM", result_data=dpwmm_results)

save_traces(config=dcg_configuration, file_name="DCG", result_data=dcg_results)
