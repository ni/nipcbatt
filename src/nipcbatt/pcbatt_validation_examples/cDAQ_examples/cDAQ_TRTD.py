"""Standalone for TemperatureMeasurementUsingRtd.""" 

### Ensure correct hardware and corresponding trigger names before running this example

import nidaqmx.constants

import nipcbatt
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variables
plot_results = True
save_fig = False
use_specific_channel = False

# initialize 'TemperatureMeasurementUsingRtd' class instance
trtdm = nipcbatt.TemperatureMeasurementUsingRtd()
trtdm.initialize("TP_RTD0")

# region TRTDM configure and measure

global_channel_parameters = nipcbatt.TemperatureRtdMeasurementTerminalParameters(
    temperature_minimum_value_celsius_degrees=0,
    temperature_maximum_value_celsius_degrees=100,
    current_excitation_value_amperes=0.001,
    sensor_resistance_ohms=100,
    rtd_type=nidaqmx.constants.RTDType.PT_3750,
    excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.THREE_WIRE,
    adc_timing_mode=nidaqmx.constants.ADCTimingMode.AUTOMATIC,
)

# region specific_channels_parameters

channel0 = nipcbatt.TemperatureRtdMeasurementChannelParameters(
    channel_name="TP_RTD0",
    sensor_resistance_ohms=100,
    current_excitation_value_amperes=0.001,
    rtd_type=nidaqmx.constants.RTDType.PT_3750,
    resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
    excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
)

# endregion specific_channels_parameters

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=100,
    number_of_samples_per_channel=10,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

trtdm_config = nipcbatt.TemperatureRtdMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion TRTDM configure and measure

trtdm_result_data = trtdm.configure_and_measure(configuration=trtdm_config)

trtdm.close()

print("TRTDM result :\n")
print(trtdm_result_data)

save_traces(config=trtdm_config, file_name="TRTDM", result_data=trtdm_result_data)

# region plot results

if plot_results is True:
    trtdm_w = trtdm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=trtdm_w,
        title="RTD Temperature",
        ylabel="Temp *C",
        xlabel="Samples",
        save_fig=save_fig,
    )

# endregion plot results
