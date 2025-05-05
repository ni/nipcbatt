# Signal Voltage Generation connected to Frequency Domain Measurement  
### Ensure correct hardware and corresponding trigger names before running this example

from enum import Enum

import nidaqmx.constants
import numpy as np

import nipcbatt
import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt.pcbatt_utilities.save_traces import save_traces

# Global variable to plot
plot_results = True
save_fig = False

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
waveform_type = Waveform_type.Sine_wave

generation_time = 0.1  # change this according to the sampling rate

# Configure Multiple tones settings
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

fdvm = nipcbatt.FrequencyDomainMeasurement()
fdvm.initialize(analog_input_channel_expression="Dev1/ai1")

# region fdvm configure only

global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
    range_min_volts=-10,
    range_max_volts=10,
)

sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=10000,
    number_of_samples_per_channel=1000,
    sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
)

specific_channels_parameters = []

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    digital_start_trigger_source="/Dev1/ao/StartTrigger",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

fdvm_config = nipcbatt.FrequencyDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion fdvm configure only
fdvm.configure_and_measure(configuration=fdvm_config)

# region configure SVG
voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
    range_min_volts=-10, range_max_volts=10
)

timing_parameters = nipcbatt.SignalVoltageGenerationTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=100000,
    generated_signal_duration_seconds=generation_time,
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
            tone_frequency_hertz=50, tone_amplitude_volts=0.5, tone_phase_radians=0
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
            generated_signal_phase_radians=0,
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


# region fdvm measure only

measurement_options = nipcbatt.MeasurementOptions(
    execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
)

digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
    trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
    digital_start_trigger_source="",
    digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
)

fdvm_config = nipcbatt.FrequencyDomainMeasurementConfiguration(
    global_channel_parameters=global_channel_parameters,
    specific_channels_parameters=specific_channels_parameters,
    measurement_options=measurement_options,
    sample_clock_timing_parameters=sample_clock_timing_parameters,
    digital_start_trigger_parameters=digital_start_trigger_parameters,
)

# endregion fdvm measure only
fdvm_result_data = fdvm.configure_and_measure(configuration=fdvm_config)

svg.close()
fdvm.close()

print("fdvm Result :\n")
print(fdvm_result_data)

print("Detected Tones")
print("Amplitudes (V)", fdvm_result_data.detected_tones[0].tones_amplitudes_volts)
print("Frequencies (Hz)", fdvm_result_data.detected_tones[0].tones_frequencies_hertz)


# region save traces

save_traces(config=fdvm_config, file_name="FDVM", result_data=fdvm_result_data)

save_traces(config=svg_config, file_name="SVG")

# endregion save traces

# region plot results

if plot_results is True:
    fdvm_w = fdvm_result_data.waveforms[0].samples.tolist()
    fdvm_mr = fdvm_result_data.magnitude_rms[0].amplitudes.tolist()
    fdvm_mp = fdvm_result_data.magnitude_peak[0].amplitudes.tolist()

    dt = fdvm_result_data.waveforms[0].delta_time_seconds
    t = np.arange(start=0, stop=generation_time, step=dt)
    df = fdvm_result_data.magnitude_rms[0].spectrum_frequency_resolution_hertz
    f = np.arange(start=0, stop=len(fdvm_mr) * df, step=df)

    pl.plot_three(
        y1=fdvm_w,
        y2=fdvm_mr,
        y3=fdvm_mp,
        x1=t,
        xlabel1="Time (s)",
        ylabel1="Voltage (V)",
        title1="Voltage waveforms",
        x2=f,
        xlabel2="Frequency (Hz)",
        ylabel2="Magnitude RMS (dBV)",
        title2="Magnitude RMS (dBV)",
        x3=f,
        xlabel3="Frequency (Hz)",
        ylabel3="Magnitude Peak (dBV)",
        title3="Magnitude Peak (dBV)",
        stitle="FDVM Waveforms",
        save_fig=save_fig,
    )

# endregion plot results
