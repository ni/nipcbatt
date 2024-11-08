# Temperature Thermistor Measurement connected with DC Voltage Generation  # noqa: D100, W505 - Missing docstring in public module (auto-generated noqa), doc line too long (146 > 100 characters) (auto-generated noqa)
# import plotter as pl
import os
import sys

import nidaqmx
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)

import nipcbatt

# To use save_traces and plotter from utils folder

parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)
# from save_traces import save_traces


# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# Initialize
drvg = nipcbatt.DcVoltageGeneration()
drvg.initialize(analog_output_channel_expression="cDAQ1_AO/ao2")
ttrm = nipcbatt.TemperatureMeasurementUsingThermistor()
ttrm.initialize("cDAQ1_AI_/ai3")  # cDAQ1_AI/ai3
# ttrm.initialize('TP_THcDAQ0')

# region drvg configure and generate

range_settings = nipcbatt.VoltageGenerationChannelParameters(
    range_min_volts=-10.0, range_max_volts=10.0
)

output_voltages = [10.0]

drvg_config = nipcbatt.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

# endregion drvg configure and generate

drvg.configure_and_generate(drvg_config)

# region TTR configure and measure

coefficients_steinhart_hart_parameters = nipcbatt.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

beta_coefficient_and_sensor_resistance_parameters = (
    nipcbatt.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
    )
)

global_channel_parameters = nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=10,
    thermistor_resistor_ohms=9910,
    steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters,
    beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters,
)

# region specific_channels_parameters

coefficients_steinhart_hart_parameters1 = nipcbatt.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

beta_coefficient_and_sensor_resistance_parameters1 = (
    nipcbatt.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
    )
)

channel_parameters1 = nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=10,
    thermistor_resistor_ohms=8000,
    steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters1,
    beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters1,
)

channel0 = nipcbatt.TemperatureThermistorChannelRangeAndTerminalParameters(
    # channel_name='cDAQ1_AI/ai3',
    channel_name="TP_THcDAQ0",
    channel_parameters=channel_parameters1,
)
specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

# endregion specific_channels_parameters

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

ttr_config = nipcbatt.TemperatureThermistorMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TTR configure and measure

ttr_result_data = ttrm.configure_and_measure(configuration=ttr_config)

# Set DC Voltage to 0
output_voltages = [0.0]

drvg_config1 = nipcbatt.DcVoltageGenerationConfiguration(
    voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
)

drvg.configure_and_generate(drvg_config1)

drvg.close()
ttrm.close()


print("TTR result :\n")
print(ttr_result_data)

# region save traces

# save_traces(
#     config=drvg_config,
#     file_name='DRVG'
# )

# save_traces(
#     config=ttr_config,
#     file_name='TTR',
#     result_data=ttr_result_data
# )

# endregion save traces

# region plot results

# if plot_results is True:
#     ttr_w = ttr_result_data.waveforms[0].samples.tolist()

#     pl.graph_plot(ttr_w)

# endregion plot results
