# Temperature Thermistor Measurement connected with Power Supply Source and Measure  # noqa: D100, W505 - Missing docstring in public module (auto-generated noqa), doc line too long (156 > 100 characters) (auto-generated noqa)
### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants
import numpy as np

import nipcbatt
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# Initialize
pssm = nipcbatt.PowerSupplySourceAndMeasure()
pssm.initialize("TS1_Power/power")
ttr = nipcbatt.TemperatureMeasurementUsingThermistor()
ttr.initialize("TP_Rth0")

# region PSSM configure and measure

terminal_parameters = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
    voltage_setpoint_volts=6,
    current_setpoint_amperes=3,
    power_sense=nidaqmx.constants.Sense.LOCAL,
    idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED,  # Disable power output when idle
    enable_output=True,
)

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

pssm_config = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
    terminal_parameters=terminal_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion PSSM configure and measure

pssm.configure_and_measure(configuration=pssm_config)

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
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=6,
    thermistor_resistor_ohms=9980,
    steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters,
    beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters,
)

# region specific_channels_parameters

channel_coefficients_steinhart_hart_parameters = nipcbatt.CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=0,
    coefficient_steinhart_hart_b=0,
    coefficient_steinhart_hart_c=0,
)

channel_beta_coefficient_and_sensor_resistance_parameters = (
    nipcbatt.BetaCoefficientAndSensorResistanceParameters(
        coefficient_steinhart_hart_beta_kelvins=0, sensor_resistance_ohms=0
    )
)

channel_parameters = nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    voltage_excitation_value_volts=6,
    thermistor_resistor_ohms=9980,
    steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
    coefficients_steinhart_hart_parameters=channel_coefficients_steinhart_hart_parameters,
    beta_coefficient_and_sensor_resistance_parameters=channel_beta_coefficient_and_sensor_resistance_parameters,
)

channel0 = nipcbatt.TemperatureThermistorChannelRangeAndTerminalParameters(
    channel_name="TP_RTH0",
    channel_parameters=channel_parameters,
)

# endregion specific_channels_parameters

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

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

ttr_result_data = ttr.configure_and_measure(configuration=ttr_config)

pssm.close()
ttr.close()

print("TTR result :\n")
print(ttr_result_data)

# region save traces

save_traces(config=pssm_config, file_name="PSSM")

save_traces(config=ttr_config, file_name="TTR", result_data=ttr_result_data)

# endregion save traces

# region plot results

if plot_results is True:
    ttr_w = ttr_result_data.waveforms[0].samples.tolist()
    dt = ttr_result_data.waveforms[0].delta_time_seconds
    tf = ttr_result_data.acquisition_duration_seconds
    t = np.arange(start=0, stop=tf, step=dt)

    pl.graph_plot(ttr_w)

# endregion plot results
