# DC Voltage Generation connected to DC-RMS Voltage Measurement (single ch.)  # noqa: D100, W505 - Missing docstring in public module (auto-generated noqa), doc line too long (149 > 100 characters) (auto-generated noqa)
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variable to plot
plot_results = True
save_fig = False

drvg = nipcbatt.DcVoltageGeneration()
drvg.initialize(analog_output_channel_expression="Dev1/ao0")

drvm = nipcbatt.DcRmsVoltageMeasurement()
drvm.initialize(analog_input_channel_expression="Dev1/ai0")

# region drvg configure and generate

range_settings = nipcbatt.VoltageGenerationChannelParameters(
    range_min_volts=-10.0, range_max_volts=10.0
)

output_voltages = [1.00]

drvg_config = nipcbatt.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

# endregion drvg configure and generate

drvg.configure_and_generate(drvg_config)

# region DC-RMS VM Configure and Measure

global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_volts=-10,
    range_max_volts=10,
)

specific_channels_parameters = []

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

drvm_config = nipcbatt.DcRmsVoltageMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion DC-RMS VM Configure and Measure

drvm_result_data = drvm.configure_and_measure(configuration=drvm_config)

# Close drvm Measurement Task
drvm.close()

# Set DC Voltage to 0
output_voltages = [0.0]

drvg_config1 = nipcbatt.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

drvg.configure_and_generate(drvg_config1)

# Close drvg Measurement Task
drvg.close()

# DcRmsVoltageMeasurementResultData
print("drvm result :\n")
print(drvm_result_data)

# region save traces

save_traces(config=drvm_config, file_name="DRVM", result_data=drvm_result_data)

save_traces(config=drvg_config, file_name="DRVG")

# endregion save traces

# region plot results

if plot_results is True:
    drvm_w = drvm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=drvm_w,
        title="DRVM Voltage",
        ylabel="Voltage (V)",
        xlabel="Samples",
        save_fig=save_fig,
    )
# # endregion plot results
