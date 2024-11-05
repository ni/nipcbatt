"""This example demonstrates Sine Wave Generation and Frequency Domain 
   Measurement using AO and AI channels or Modules"""

# pylint: disable=W0105

import nipcbatt
import nidaqmx.constants
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger
import os

# Setup: Get the physical channels required for the test.

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
SIGNAL_VOLTAGE_GEN_CHANNEL = "TS_Speaker0"  # physical channel = Sim_PC_basedDAQ/ao0
FREQ_DOMAIN_MEAS_CHANNEL = "TP_MIC0:2"  # physical channel = Sim_PC_basedDAQ/ai0:1
DIGITAL_STATRT_TRIGGER = "/Sim_PC_basedDAQ/ao/StartTrigger"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Signal_Generation_and_Frequency_Domain_Analysis.txt"

generation_time = 0.1


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################
def setup(
    svg_channel=SIGNAL_VOLTAGE_GEN_CHANNEL,
    fdvm_channel=FREQ_DOMAIN_MEAS_CHANNEL,
    file_path=DEFAULT_FILEPATH,
):
    """Creates the necessary objects for generation of sine wave and Frequency
    Domain Measurement"""

    # Create the instances of generation and measurement classes required for the test.
    microphone_instance = nipcbatt.SignalVoltageGeneration()
    freq_domain_meas_test_point = nipcbatt.FrequencyDomainMeasurement()

    # Initialize Microphone
    """Initializes the configured channels of AO module to perform microphone functionality"""
    microphone_instance.initialize(channel_expression=svg_channel)

    # Initialize TP
    """Initializes the configured channels of AI module to perform DC-RMS voltage measurement"""
    freq_domain_meas_test_point.initialize(analog_input_channel_expression=fdvm_channel)

    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(microphone_instance)
    logger.attach(freq_domain_meas_test_point)
    # returns the initialized objects
    return microphone_instance, freq_domain_meas_test_point


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    microphone_instance: nipcbatt.SignalVoltageGeneration,
    freq_domain_meas_test_point: nipcbatt.FrequencyDomainMeasurement,
    digital_start_trigger=DIGITAL_STATRT_TRIGGER,
):
    results_map = {}  # this structure will hold results in key-value pairs

    """Configure Freq Domain Measurement settings to wait for Hardware Trigger"""
    # Set the maximum and minimum range for FDVM measurement
    global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )
    # Set the sampling rate and number of samples per channel as required
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    specific_channels_parameters = []
    # Specify the Measurement Execution Type
    meas_config_configure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )
    # Set the Digital Trigger Type, Digital Trigger Source and Digital Trigger Edge
    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source=digital_start_trigger,
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    fdvm_config = nipcbatt.FrequencyDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=meas_config_configure_only,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )
    # endregion fdvm configure only
    freq_domain_meas_test_point.configure_and_measure(configuration=fdvm_config)

    # Region Configure Signal Voltage Generation

    """Generates Sine wave and Trigger to Initiate measurement"""

    # region configure SVG

    # Set the Siganl Voltage Generation Range
    voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
        range_min_volts=-2, range_max_volts=2
    )
    # Set the Sampling rate hertz and the generated siganl duration
    gen_timing_parameters = nipcbatt.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100000,
        generated_signal_duration_seconds=generation_time,
    )

    gen_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # Set the Sine wave Parameters
    generated_signal_tone_parameters = nipcbatt.ToneParameters(
        tone_frequency_hertz=1000, tone_amplitude_volts=1, tone_phase_radians=0
    )

    waveform_parameters = nipcbatt.SignalVoltageGenerationSineWaveParameters(
        generated_signal_offset_volts=0,
        generated_signal_tone_parameters=generated_signal_tone_parameters,
    )

    svg_config = nipcbatt.SignalVoltageGenerationSineWaveConfiguration(
        voltage_generation_range_parameters=voltage_generation_range_parameters,
        waveform_parameters=waveform_parameters,
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
    )

    # endregion
    microphone_instance.configure_and_generate_sine_waveform(svg_config)

    """Measures the Analog Input voltage waveforms (Started measure when Signal Voltage generation sends Trigger after source) and returns Freq Domain Analysis"""
    # Region FDVM Measure Only
    meas_options_measure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    fdvm_config = nipcbatt.FrequencyDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=meas_options_measure_only,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion fdvm configure and measure
    ####################################################################################################
    # end region configure and measure
    fdvm_result_data = freq_domain_meas_test_point.configure_and_measure(configuration=fdvm_config)

    print(fdvm_result_data)
    # region close

    # record results
    results_map["FDVM data"] = fdvm_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(
    microphone_instance: nipcbatt.SignalVoltageGeneration,
    freq_domain_meas_test_point: nipcbatt.TimeDomainMeasurement,
):
    microphone_instance.close()
    freq_domain_meas_test_point.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def signal_voltage_generation_and_measurement(
    generation_channel=SIGNAL_VOLTAGE_GEN_CHANNEL,
    measurement_channel=FREQ_DOMAIN_MEAS_CHANNEL,
):
    """Execute all steps in the sequence"""

    # Run setup function
    microphone_instance, freq_domain_meas_test_point = setup(
        generation_channel, measurement_channel
    )

    # Run main function
    main(
        microphone_instance,
        freq_domain_meas_test_point,
        digital_start_trigger=DIGITAL_STATRT_TRIGGER,
    )

    # Run cleanup function
    cleanup(microphone_instance, freq_domain_meas_test_point)


####################################################################################################
# endregion test
