# DcRmsCurrentMeasurement connected with Power Supply Source and Measure without Trigger
### Ensure correct hardware and corresponding trigger names before running this example

import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces
import nidaqmx.constants
import nipcbatt
import numpy as np

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# Initialize
pssm = nipcbatt.PowerSupplySourceAndMeasure()
pssm.initialize("TS1_Power/power")
drcm = nipcbatt.DcRmsCurrentMeasurement()
drcm.initialize("TS1_AI/ai4")

# region PSSM configure and measure

terminal_parameters = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
    voltage_setpoint_volts=6,
    current_setpoint_amperes=3,
    power_sense=nidaqmx.constants.Sense.LOCAL,
    idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE,
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

pssm_result_data = pssm.configure_and_measure(configuration=pssm_config)

# region DRCM configure and measure

global_channel_parameters = nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
    range_min_amperes=-3.0,
    range_max_amperes=3.0,
    shunt_resistor_ohms=0.13,
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
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

# Specific channel parameters

#    Channel 0
cp0 = nipcbatt.DcRmsCurrentMeasurementTerminalRangeParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_amperes=-3,
    range_max_amperes=3,
    shunt_resistor_ohms=0.13,
)

channel0 = nipcbatt.DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(
    channel_name="TS1_AI/ai4",
    channel_parameters=cp0,
)

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

drcm_config = nipcbatt.DcRmsCurrentMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion DRCM Configure and Measure

drcm_result_data = drcm.configure_and_measure(configuration=drcm_config)

drcm.close()
pssm.close()

print("PSSM result :\n")
print(pssm_result_data)
print("DRCM result :\n")
print(drcm_result_data)

# region save traces

save_traces(config=pssm_config, file_name="PSSM")

save_traces(config=drcm_config, file_name="DRCM", result_data=drcm_result_data)

# endregion save traces

# region plot results

if plot_results is True:
    pssm_v = pssm_result_data.voltage_waveform.samples
    drcm_w = drcm_result_data.waveforms[0].samples.tolist()
    x1 = np.arange(0, len(pssm_v))
    x2 = np.arange(0, len(drcm_w))
    pssm_c = pssm_result_data.current_waveform.samples
    pl.plot_two(
        y1=pssm_v,
        y2=drcm_w,
        x1=x1,
        ylabel1="Voltage (V)",
        ylabel2="Current (A)",
        x2=x2,
        stitle="PSSM Voltage and DRCM Current",
    )

# endregion plot results
