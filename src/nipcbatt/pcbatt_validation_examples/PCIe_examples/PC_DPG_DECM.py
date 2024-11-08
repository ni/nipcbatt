# Digital Pulse Generation to Digital Edge Count Measurement  # noqa: D100, W505 - Missing docstring in public module (auto-generated noqa), doc line too long (133 > 100 characters) (auto-generated noqa)
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize

dpg = nipcbatt.DigitalPulseGeneration()
decm = nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer()

dpg.initialize(channel_expression="Dev1/ctr0", output_terminal_name="/Dev1/PFI2")

decm.initialize(
    measurement_channel_expression="Dev1/ctr1",
    measurement_input_terminal_name="/Dev1/PFI3",
    timer_channel_expression="Dev1/ctr2",
)

# begin decm configure
counter_channel_parameters = nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
    edge_type=nidaqmx.constants.Edge.FALLING
)
timing_parameters = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(
    edge_counting_duration=5e-3,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev1/PFI3",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

decm_configuration = nipcbatt.DigitalEdgeCountHardwareTimerConfiguration(
    measurement_options=measurement_options,
    counter_channel_parameters=counter_channel_parameters,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
decm.configure_and_measure(configuration=decm_configuration)
# end region decm configure

# begin dpg configure and generate
channel_parameters = nipcbatt.DigitalPulseGenerationCounterChannelParameters(
    pulse_idle_state=nidaqmx.constants.Level.LOW,
    low_time_seconds=500e-6,
    high_time_seconds=500e-6,
)
pulses_timing_parameters = nipcbatt.DigitalPulseGenerationTimingParameters(
    pulses_count=5,
)
dpg_configuration = nipcbatt.DigitalPulseGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=pulses_timing_parameters,
)
# end region dpg configure and generate
dpg_results = dpg.configure_and_generate(configuration=dpg_configuration)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

decm_configuration = nipcbatt.DigitalEdgeCountHardwareTimerConfiguration(
    measurement_options=measurement_options,
    counter_channel_parameters=counter_channel_parameters,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
decm_results = decm.configure_and_measure(configuration=decm_configuration)

# close generation and measurement session
dpg.close()
decm.close()

print(dpg_results)
print(decm_results)

save_traces(config=decm_configuration, file_name="DECM", result_data=decm_results)

save_traces(config=dpg_configuration, file_name="DPG", result_data=dpg_results)
