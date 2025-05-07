### Ensure correct hardware and corresponding trigger names before running this example  

import matplotlib.pyplot as plt
import nidaqmx.constants
import numpy as np  

import nipcbatt
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# Initialize
drvg = nipcbatt.DcVoltageGeneration()
drvg.initialize("Dev1/ao2:3")
drcm = nipcbatt.DcRmsCurrentMeasurement()
drcm.initialize("Dev1/ai2:4", use_specific_channel)

# region DRVG configure and generate

voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
    range_min_volts=-10, range_max_volts=10
)

output_voltages = [10.0, 10.0]

drvg_config = nipcbatt.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=voltage_generation_range_parameters,
    output_voltages=output_voltages,
)

# endregion DRVG configure and generate

drvg.configure_and_generate(configuration=drvg_config)

# region drcm configure and measure

global_channel_parameters = nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_amperes=-0.001,
    range_max_amperes=0.001,
    shunt_resistor_ohms=1000.0,
)

# region specific channels

channel_parameters1 = nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    range_min_amperes=-0.002,
    range_max_amperes=0.002,
    shunt_resistor_ohms=5000.0,
)

channel1 = nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
    channel_name="Dev1/ai2", channel_parameters=channel_parameters1
)

channel_parameters2 = nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_amperes=-0.002,
    range_max_amperes=0.002,
    shunt_resistor_ohms=5000.0,
)

channel2 = nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
    channel_name="Dev1/ai3", channel_parameters=channel_parameters2
)

channel_parameters3 = nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_amperes=-0.001,
    range_max_amperes=0.001,
    shunt_resistor_ohms=10000.0,
)

channel3 = nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
    channel_name="Dev1/ai4", channel_parameters=channel_parameters3
)

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel1)
    specific_channels_parameters.append(channel2)
    specific_channels_parameters.append(channel3)

# endregion specific channels

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

drcm_config = nipcbatt.DcRmsCurrentMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion drcm configure and measure

drcm_result_data = drcm.configure_and_measure(drcm_config)

drcm.close()
drvg.close()

print(drcm_result_data)

# plot results

if plot_results is True:
    c1 = drcm_result_data.waveforms[0].samples.tolist()
    c2 = drcm_result_data.waveforms[1].samples.tolist()
    c3 = drcm_result_data.waveforms[2].samples.tolist()
    plt.plot(c1)
    plt.plot(c2)
    plt.plot(c3)
    plt.show()

# region save traces

save_traces(config=drcm_config, file_name="DRCM", result_data=drcm_result_data)


save_traces(
    config=drvg_config,
    file_name="DRVG",
)

# endregion save traces
