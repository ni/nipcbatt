### Ensure correct hardware and corresponding trigger names before running this example  # noqa: D100, W505 - Missing docstring in public module (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)

import nidaqmx.constants

import nipcbatt
from nipcbatt.pcbatt_utilities.save_traces import save_traces

number_of_cycles = 101

# initialize
dpg = nipcbatt.DigitalPulseGeneration()
dpwmm = nipcbatt.DigitalPwmMeasurement()

# Terminals to be verified
dpg.initialize(channel_expression="Dev1/ctr0", output_terminal_name="/Dev1/PFI2")

dpwmm.initialize(
    channel_expression="Dev1/ctr2",
    input_terminal_name="/Dev1/PFI3",
)

# DPWMM configuration begins

range_parameters = nipcbatt.DigitalPwmMeasurementRangeParameters(
    semi_period_maximum_value_seconds=42.949672,
    semi_period_minimum_value_seconds=20e-9,
)

timing_parameters = nipcbatt.DigitalPwmMeasurementTimingParameters(
    semi_period_counter_wanted_cycles_count=number_of_cycles,
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


# begin dpg configure and generate
channel_parameters = nipcbatt.DigitalPulseGenerationCounterChannelParameters(
    pulse_idle_state=nidaqmx.constants.Level.LOW,
    low_time_seconds=0.00005,
    high_time_seconds=0.00015,
)
pulse_timing_parameters = nipcbatt.DigitalPulseGenerationTimingParameters(
    pulses_count=number_of_cycles,
)
dpg_configuration = nipcbatt.DigitalPulseGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=pulse_timing_parameters,
)
# end region dpg configure and generate
dpg_results = dpg.configure_and_generate(configuration=dpg_configuration)


dpwmm_configuration = nipcbatt.DigitalPwmMeasurementConfiguration(
    parameters=counter_channel_parameters,
    measurement_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
)

dpwmm_results = dpwmm.configure_and_measure(configuration=dpwmm_configuration)

# close generation and measurement session
dpg.close()
dpwmm.close()


print(dpg_results)
print(dpwmm_results)

save_traces(config=dpwmm_configuration, file_name="DPWMM", result_data=dpwmm_results)

save_traces(config=dpg_configuration, file_name="DPG", result_data=dpg_results)
