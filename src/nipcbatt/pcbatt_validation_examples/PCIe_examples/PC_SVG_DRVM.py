# Signal Voltage Generation connected to Time Domain Measurement 
### Ensure correct hardware and corresponding trigger names before running this example

from enum import Enum

import nidaqmx.constants

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

drvm = nipcbatt.DcRmsVoltageMeasurement()
drvm.initialize("Dev1/ai1")

# region configure SVG
voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
    range_min_volts=-10, range_max_volts=10
)

timing_parameters = nipcbatt.SignalVoltageGenerationTimingParameters(
    sample_clock_source="OnboardClock",
    sampling_rate_hertz=100000,
    generated_signal_duration_seconds=0.2,
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
            tone_frequency_hertz=500, tone_amplitude_volts=1, tone_phase_radians=0
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
        generated_signal_offset_volts=0,
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

# region DRVM configure and measure

global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
    terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
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

# endregion

drvm_result_data = drvm.configure_and_measure(drvm_config)

drvm.close()
svg.close()

print("DRVM result :\n")
print(drvm_result_data)

# region save traces

save_traces(config=drvm_config, file_name="DRVM", result_data=drvm_result_data)

save_traces(config=svg_config, file_name="SVG")

if plot_results is True:
    drvm_w = drvm_result_data.waveforms[0].samples.tolist()
    pl.graph_plot(
        y=drvm_w,
        title="DRVM Voltage",
        ylabel="Voltage (V)",
        xlabel="Samples",
        save_fig=save_fig,
    )

# #endregion
