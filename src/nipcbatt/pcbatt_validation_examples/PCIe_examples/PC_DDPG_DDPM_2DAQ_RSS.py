### Ensure correct hardware and corresponding trigger names before running this example 

import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# DDPG_Initialization
ddpg = nipcbatt.DynamicDigitalPatternGeneration()
ddpg.initialize(channel_expression="Dev1/port0/line0:15")

# RouteSyncSignal
ddpg.route_start_trigger_signal_to_terminal(terminal_name="/Dev1/PFI0")
ddpg.route_sample_clock_signal_to_terminal(terminal_name="/Dev1/PFI1")

# DDPM_Initialization
ddpm = nipcbatt.DynamicDigitalPatternMeasurement()
ddpm.initialize(
    channel_expression="Dev2/port0/line0:15",
)

# begin ddpm configure

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
)

timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
    sample_clock_source="/Dev2/PFI1",
    sampling_rate_hertz=10000.0,
    number_of_samples_per_channel=65536,
    active_edge=nidaqmx.constants.Edge.FALLING,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev2/PFI0",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ddpm_configuration = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
    measurement_options=measurement_options,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)

ddpm.configure_and_measure(configuration=ddpm_configuration)

# end region ddpm configure


# begin region ddpg configuration
timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000.0,
    number_of_samples_per_channel=65536,
    active_edge=nidaqmx.constants.Edge.FALLING,
)

trigger_parameters = nipcbatt.DynamicDigitalStartTriggerParameters(
    digital_start_trigger_source="/Dev1/PFI6",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    trigger_type=nipcbatt.StartTriggerType.NO_TRIGGER,
)

# data to generate

values_list = list(range(65536))
digital_lis = []
digital_lis.append(values_list)

pulse_signal = np.array(digital_lis, dtype=np.uint32)

ddpg_configuration = nipcbatt.DynamicDigitalPatternGenerationConfiguration(
    timing_parameters=timing_parameters,
    digital_start_trigger_parameters=trigger_parameters,
    pulse_signal=pulse_signal,
)
# end region ddpg configuration

ddpg_results = ddpg.configure_and_generate(configuration=ddpg_configuration)

# close generation session


# begin ddpm measurement

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
    sample_clock_source="/Dev2/PFI1",
    sampling_rate_hertz=10000.0,
    number_of_samples_per_channel=65536,
    active_edge=nidaqmx.constants.Edge.FALLING,
)
trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev2/PFI0",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

ddpm_configuration = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
    measurement_options=measurement_options,
    timing_parameters=timing_parameters,
    trigger_parameters=trigger_parameters,
)
# end region ddpm measurement

ddpm_results = ddpm.configure_and_measure(configuration=ddpm_configuration)

ddpm.close()
ddpg.close()

print(ddpg_results.generation_time_seconds)

print(ddpm_results)

save_traces(config=ddpg_configuration, file_name="DDPG", result_data=ddpg_results)


save_traces(config=ddpm_configuration, file_name="DDPM", result_data=ddpm_results)
