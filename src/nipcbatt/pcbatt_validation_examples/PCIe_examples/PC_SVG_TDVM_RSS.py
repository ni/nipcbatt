# Signal Voltage Generation from DAQ1 connected to Time Domain Measurement in DAQ2 using Route Synchronization 
### Ensure correct hardware and corresponding trigger names before running this example

from enum import Enum

import nidaqmx.constants

import nipcbatt
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variable to plot
plot_results = True
save_fig = False
use_specific_channel = False

# Enums to select generation and Waveform types


class Generation_type(  
    Enum
):
    Single_tone = 0
    Multi_tone = 1


class Waveform_type(  
    Enum
):
    Sine_wave = 0
    Square_wave = 1


# INPUTS

# Configure Generation and Waveform types
generation_type = Generation_type.Single_tone
waveform_type = Waveform_type.Square_wave

# Multiple tones settings
multiple_tones_parameters = []
multiple_tones_parameters.append(
    nipcbatt.ToneParameters(
        tone_frequency_hertz=100, tone_amplitude_volts=1.0, tone_phase_radians=0
    )
)
multiple_tones_parameters.append(
    nipcbatt.ToneParameters(
        tone_frequency_hertz=200, tone_amplitude_volts=1.0, tone_phase_radians=0
    )
)

# Initialize
svg = nipcbatt.SignalVoltageGeneration()
svg.initialize(channel_expression="Dev1/ao1")

tdvm = nipcbatt.TimeDomainMeasurement()
tdvm.initialize(analog_input_channel_expression="Dev2/ai0")


# Configure Routing paths
svg.route_start_trigger_signal_to_terminal(terminal_name="/Dev1/PFI0")
svg.route_sample_clock_signal_to_terminal(terminal_name="/Dev1/PFI1")


# region tdvm configure only

global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    range_min_volts=-10,
    range_max_volts=10,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="/Dev2/PFI1",
    sampling_rate_hertz=100000,
    number_of_samples_per_channel=10000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev2/PFI0",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

# Specific channel parameters

#    Channel 0
cp0 = nipcbatt.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
    range_min_volts=-10,
    range_max_volts=10,
)

channel0 = nipcbatt.VoltageMeasurementChannelAndTerminalRangeParameters(
    channel_name="Dev2/ai0",
    channel_parameters=cp0,
)

specific_channels_parameters = []
if use_specific_channel is True:
    specific_channels_parameters.append(channel0)

tdvm_config = nipcbatt.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion tdvm configure only
tdvm.configure_and_measure(configuration=tdvm_config)


# region configure SVG
voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
    range_min_volts=-10, range_max_volts=10
)

timing_parameters = nipcbatt.SignalVoltageGenerationTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=100000,
    generated_signal_duration_seconds=0.1,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

if generation_type == Generation_type.Single_tone:
    if waveform_type == Waveform_type.Sine_wave:
        # region SVG SineWave configure and generate

        generated_signal_tone_parameters = nipcbatt.ToneParameters(
            tone_frequency_hertz=100, tone_amplitude_volts=1, tone_phase_radians=0
        )

        waveform_parameters = nipcbatt.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=0,
            generated_signal_tone_parameters=generated_signal_tone_parameters,
        )

        svg_config = nipcbatt.SignalVoltageGenerationSineWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        # endregion
        svg.configure_and_generate_sine_waveform(svg_config)

    else:
        # region SVG SquareWave configure and generate

        waveform_parameters = nipcbatt.SignalVoltageGenerationSquareWaveParameters(
            generated_signal_amplitude_volts=1.0,
            generated_signal_duty_cycle_percent=50.00,
            generated_signal_frequency_hertz=100,
            generated_signal_phase_radians=4.71,
            generated_signal_offset_volts=0,
        )

        svg_config = nipcbatt.SignalVoltageGenerationSquareWaveConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )
        # endregion
        svg.configure_and_generate_square_waveform(svg_config)

else:
    # region SVG MultiTone configure and generate

    waveform_parameters = nipcbatt.SignalVoltageGenerationMultipleTonesWaveParameters(
        generated_signal_amplitude_volts=1.0,
        generated_signal_offset_volts=0.0,
        multiple_tones_parameters=multiple_tones_parameters,
    )

    svg_config = nipcbatt.SignalVoltageGenerationMultipleTonesConfiguration(
        voltage_generation_range_parameters=voltage_generation_range_parameters,
        waveform_parameters=waveform_parameters,
        timing_parameters=timing_parameters,
        digital_start_trigger_parameters=digital_start_trigger_parameters,
    )
    # endregion
    svg.configure_and_generate_multiple_tones_waveform(svg_config)


# region tdvm measure only

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="/Dev1/ao/StartTrigger",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

tdvm_config = nipcbatt.TimeDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion tdvm measure only
tdvm_result_data = tdvm.configure_and_measure(configuration=tdvm_config)

svg.close()
tdvm.close()

print("TDVM result :\n")
print(tdvm_result_data)

# region save traces

save_traces(config=tdvm_config, file_name="TDVM", result_data=tdvm_result_data)

save_traces(config=svg_config, file_name="SVG")

# endregion save traces

# region plot results

if plot_results is True:
    tdvm_w = tdvm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=tdvm_w,
        title="TDVM Voltage",
        ylabel="Voltage (V)",
        xlabel="Samples",
        save_fig=save_fig,
    )

# # endregion plot results
