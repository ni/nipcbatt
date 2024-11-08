"""Standalone for TemperatureMeasurementUsingThermocouple"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)

### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# initialize 'TemperatureMeasurementUsingThermocouple' class instance
ttcm = nipcbatt.TemperatureMeasurementUsingThermocouple()
ttcm.initialize(
    channel_expression="cDAQ1_TC/ai0:1",
    cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
    cold_junction_compensation_channel="TP_RTD0",
)

# region ttcm configure and measure

global_channel_parameters = nipcbatt.TemperatureThermocoupleMeasurementTerminalParameters(
    temperature_minimum_value_celsius_degrees=0.0,
    temperature_maximum_value_celsius_degrees=100.0,
    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
    cold_junction_compensation_temperature=25.0,
    perform_auto_zero_mode=False,
    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
)

# region specific_channels_parameters

channel_parameters = nipcbatt.TemperatureThermocoupleRangeAndTerminalParameters(
    temperature_minimum_value_celsius_degrees=0.0,
    temperature_maximum_value_celsius_degrees=100.0,
    thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
    cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
    cold_junction_compensation_temperature=25.0,
    cold_junction_compensation_channel_name="TP_RTD0",
    perform_auto_zero_mode=False,
    auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
)

channel1 = nipcbatt.TemperatureThermocoupleChannelRangeAndTerminalParameters(
    channel_name="cDAQ1_TC/ai0",
    channel_parameters=channel_parameters,
)

# endregion specific_channels_parameters

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel1)

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

ttcm_config = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion ttcm configure and measure

ttcm_result_data = ttcm.configure_and_measure(configuration=ttcm_config)

ttcm.close()

print("ttcm result :\n")
print(ttcm_result_data)

save_traces(config=ttcm_config, file_name="ttcm", result_data=ttcm_result_data)

# region plot results

if plot_results is True:
    ttcm_w = ttcm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=ttcm_w,
        title="Thermocouple Temperature",
        ylabel="Temp *C",
        xlabel="Samples",
        save_fig=save_fig,
    )

# endregion plot results
