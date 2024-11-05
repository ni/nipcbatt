# Digital Clock Generation to Digital Edge Count Measurement
### Ensure correct hardware and corresponding trigger names before running this example

import nipcbatt
import nidaqmx.constants
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Initialize
dcg = nipcbatt.DigitalClockGeneration()
decm = nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer()

dcg.initialize(counter_channel_expression="Dev1/ctr0", output_terminal_name="/Dev1/PFI2")

decm.initialize(
    measurement_channel_expression="Dev1/ctr2",
    measurement_input_terminal_name="/Dev1/PFI3",
    timer_channel_expression="Dev1/ctr3",
)

# begin decm configure
counter_channel_parameters = nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
    edge_type=nidaqmx.constants.Edge.FALLING
)
timing_parameters = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(
    edge_counting_duration=1.0,
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

# begin dcg configure and generate
channel_parameters = nipcbatt.DigitalClockGenerationCounterChannelParameters(
    frequency_hertz=1000.0,
    duty_cycle_ratio=0.5,
)
clock_timing_parameters = nipcbatt.DigitalClockGenerationTimingParameters(
    clock_duration_seconds=1.0,
)
dcg_configuration = nipcbatt.DigitalClockGenerationConfiguration(
    counter_channel_parameters=channel_parameters,
    timing_parameters=clock_timing_parameters,
)
# end region dcg configure and generate
dcg_results = dcg.configure_and_generate(configuration=dcg_configuration)

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
dcg.close()
decm.close()

print(dcg_results)
print(decm_results)

save_traces(config=decm_configuration, file_name="DECM", result_data=decm_results)

save_traces(config=dcg_configuration, file_name="DCG", result_data=dcg_results)
