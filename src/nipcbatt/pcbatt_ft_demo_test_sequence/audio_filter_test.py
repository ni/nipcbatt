"""Audio Filter Test""" 

import os  
import sys  
from time import sleep  

import nidaqmx.constants
from limit_exception import (  
    LimitException,
)

import nipcbatt


class AudioFilterTest:  
    def __init__(self):  
        self.signal_voltage_gen_task = None
        self.freq_domain_meas_task = None

        self.setup()
        self.main()
        self.cleanup()

    def setup(  
        self,
    ) -> None:
        self.initialize_multi_tone_audio_signal_gen()
        self.initialize_audio_meas()

    def initialize_multi_tone_audio_signal_gen( 
        self,
    ) -> None:
        self.signal_voltage_gen_task = nipcbatt.SignalVoltageGeneration()
        self.signal_voltage_gen_task.initialize("TS_LINE_IN0")

    def initialize_audio_meas(  
        self,
    ) -> None:
        self.freq_domain_meas_task = nipcbatt.FrequencyDomainMeasurement()
        self.freq_domain_meas_task.initialize("TP_LINE_OUT0")

    def main(self) -> None:  
        self.configure_audio_meas()
        self.send_multi_tone_audio_signal()
        self.measure_tone()

    def configure_audio_meas( 
        self,
    ) -> None:
        # Configure Freq Domain Measurement settings to wait for Hardware Trigger from Audio Signal Generation  

        global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100000,
            number_of_samples_per_channel=10000,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
            digital_start_trigger_source="/Sim_PC_basedDAQ/ao/StartTrigger",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = nipcbatt.FrequencyDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        self.freq_domain_meas_task.configure_and_measure(configuration=configuration)

    def send_multi_tone_audio_signal(  
        self,
    ) -> None:
        voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=-10, range_max_volts=10
        )

        tone1 = nipcbatt.ToneParameters(
            tone_frequency_hertz=10, tone_amplitude_volts=1, tone_phase_radians=0
        )

        tone2 = nipcbatt.ToneParameters(
            tone_frequency_hertz=100, tone_amplitude_volts=1, tone_phase_radians=0
        )

        tone3 = nipcbatt.ToneParameters(
            tone_frequency_hertz=1000, tone_amplitude_volts=1, tone_phase_radians=0
        )

        tone4 = nipcbatt.ToneParameters(
            tone_frequency_hertz=10000, tone_amplitude_volts=1, tone_phase_radians=0
        )

        multiple_tones_parameters = [tone1, tone2, tone3, tone4]

        waveform_parameters = nipcbatt.SignalVoltageGenerationMultipleTonesWaveParameters(
            generated_signal_offset_volts=0,
            generated_signal_amplitude_volts=1,
            multiple_tones_parameters=multiple_tones_parameters,
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

        configuration = nipcbatt.SignalVoltageGenerationMultipleTonesConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            waveform_parameters=waveform_parameters,
            timing_parameters=timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        self.signal_voltage_gen_task.configure_and_generate_multiple_tones_waveform(
            configuration=configuration
        )

    def measure_tone( 
        self,
    ) -> None:
        # Fetches the Analog Input voltage waveforms (Started measure when Signal Voltage generation sends Trigger) and returns Freq Domain Analysis 

        global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

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

        configuration = nipcbatt.FrequencyDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.freq_domain_meas_task.configure_and_measure(configuration=configuration)

        print("\n\n -- Measure Tone Frequencies -- \n")

        lower_limit = 9
        upper_limit = 11
        tested_value = result_data.detected_tones[0].tones_frequencies_hertz[0]

        print("Tone 0:")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Failed  -- Measured frequency: ", tested_value)
            print("Measured frequency must be between 9 and 11 hz", "\n")
        else:
            print("Status: Pass -- Measured frequency: ", tested_value, "\n")

        val_min = 90
        val_max = 110
        tested_value = result_data.detected_tones[0].tones_frequencies_hertz[1]

        print("Tone 1:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured frequency:", tested_value)
            print("Measured frequency must be between 90 and 110 hz", "\n")
        else:
            print("Status: Pass -- Measured frequency: ", tested_value, "\n")

        val_min = 900
        val_max = 1100
        tested_value = result_data.detected_tones[0].tones_frequencies_hertz[2]

        print("Tone 2:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured frequency:", tested_value)
            print("Measured frequency must be between 900 and 1100 hz", "\n")
        else:
            print("Status: Pass -- Measured frequency: ", tested_value, "\n")

        val_min = 9000
        val_max = 11000
        tested_value = result_data.detected_tones[0].tones_frequencies_hertz[3]

        print("Tone 3:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured frequency:", tested_value)
            print("Measured frequency must be between 9000 and 11000 hz", "\n")
        else:
            print("Status: Pass -- Measured frequency: ", tested_value, "\n")

        print("\n -- Measure Tone Amplitudes -- \n")

        val_min = 0.9
        val_max = 1.2
        tested_value = result_data.detected_tones[0].tones_amplitudes_volts[0]

        print("Tone 0:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured amplitude:", tested_value)
            print("Measured amplitude must be between 0.9 and 1.2 volts", "\n")
        else:
            print("Status: Pass -- Measured amplitude: ", tested_value, "\n")

        val_min = 0.9
        val_max = 1.1
        tested_value = result_data.detected_tones[0].tones_amplitudes_volts[1]

        print("Tone 1:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured amplitude:", tested_value)
            print("Measured amplitude must be between 0.9 and 1.1 volts", "\n")
        else:
            print("Status: Pass -- Measured amplitude: ", tested_value, "\n")

        val_min = 0.9
        val_max = 1.1
        tested_value = result_data.detected_tones[0].tones_amplitudes_volts[2]
        print("Tone 2:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured amplitude:", tested_value)
            print("Measured amplitude must be between 0.9 and 1.1 volts", "\n")
        else:
            print("Status: Pass -- Measured amplitude: ", tested_value, "\n")

        val_min = 0.9
        val_max = 1.1
        tested_value = result_data.detected_tones[0].tones_amplitudes_volts[3]
        print("Tone 3:")
        if tested_value < val_min or tested_value > val_max:
            print("Status: Failed  -- Measured amplitude:", tested_value)
            print("Measured amplitude must be between 0.9 and 1.1 volts", "\n")
        else:
            print("Status: Pass -- Measured amplitude: ", tested_value, "\n")

    def cleanup(  
        self,
    ) -> None:
        self.close_multi_tone_audio_signal_gen()
        self.close_audio_meas()

    def close_multi_tone_audio_signal_gen(  
        self,
    ) -> None:
        self.signal_voltage_gen_task.close()

    def close_audio_meas(  
        self,
    ) -> None:
        self.freq_domain_meas_task.close()
