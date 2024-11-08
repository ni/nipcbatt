"""PSSM to TDVM"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (129 > 100 characters) (auto-generated noqa)

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
pssm.initialize(power_channel_name="TS1_Power/power")

tdvm = nipcbatt.TimeDomainMeasurement()
tdvm.initialize(analog_input_channel_expression="TS1_AI/ai2")

# region TDVM configure only

global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_volts=-10,
    range_max_volts=10,
)

# Specific channel parameters

channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    range_max_volts=5,
    range_min_volts=-5,
)

channel0 = nipcbatt.VoltageMeasurementChannelAndTerminalRangeParameters(
    channel_name="TS1_AI/ai2",
    channel_parameters=channel_parameters,
)

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/TS1/te0/StartTrigger",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

tdvm_config = nipcbatt.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TDVM configure only

tdvm.configure_and_measure(configuration=tdvm_config)

# region PSSM configure and measure

terminal_parameters = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
    voltage_setpoint_volts=6,
    current_setpoint_amperes=3,
    power_sense=nidaqmx.constants.Sense.LOCAL,
    idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED,
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
    sample_timing_engine=nipcbatt.SampleTimingEngine.TE0,
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

pssm_result_data = pssm.configure_and_measure(configuration=pssm_config)

# region TDVM measure only

global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_volts=-10,
    range_max_volts=10,
)

specific_channels_parameters = []

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
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

tdvm_config = nipcbatt.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TDVM measure only

tdvm_result_data = tdvm.configure_and_measure(configuration=tdvm_config)

tdvm.close()
pssm.close()

print("PSSM result :\n")
print(pssm_result_data)

print("TDVM result :\n")
print(tdvm_result_data)


# region plot results

if plot_results is True:
    pssm_v = pssm_result_data.voltage_waveform.samples
    pssm_c = pssm_result_data.current_waveform.samples
    # np.linspace( )
    x1 = np.arange(0, len(pssm_v))
    x2 = np.arange(0, len(pssm_c))

    tdvm_w = tdvm_result_data.waveforms[0].samples.tolist()
    t = np.arange(0, len(tdvm_w))

    pl.plot_three(
        y1=pssm_v,
        y2=pssm_c,
        y3=tdvm_w,
        x1=x1,
        xlabel1="Samples",
        ylabel1="Voltage (V)",
        title1="PSSM Voltage",
        x2=x2,
        xlabel2="Samples",
        ylabel2="Current (A)",
        title2="PSSM Current",
        x3=t,
        xlabel3="Samples",
        ylabel3="Voltage (V))",
        title3="TDVM Voltage",
        stitle="PSSM to TDVM Waveforms",
        save_fig=save_fig,
    )

# endregion plot results

# region save traces

save_traces(config=pssm_config, file_name="PSSM", result_data=pssm_result_data)

save_traces(config=tdvm_config, file_name="TDVM", result_data=tdvm_result_data)

# endregion save traces
