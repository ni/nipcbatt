"""This example demonstrates synchronization using Signal Voltage Generation Library to generate 
   a Analog Sine waveform from one Backplane and capture it using Time Domain Measuerment 
   library in another Backplane"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (327 > 100 characters) (auto-generated noqa)

# pylint: disable=W0105,E0401

import nidaqmx.constants

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

## Setup: Get the physical channels required for the test.

"""Note to run with Hardware: Update the Global Channel Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
SIGNAL_CHANNEL = "TS_Analog0"
ANALOG_INPUT_CHANNEL = "TP_Analog1"

# Default signal lines
SAMPLE_CLOCK_LINE = "/Sim_PC_basedDAQ/PFI0"  # Exporting Sample Clock to PFI0 Terminal
START_TRIGGER_LINE = "/Sim_PC_basedDAQ/PFI1"  # Exporting Start Trigger to PFI1 Terminal

# Default test results location
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\signal_voltage_and_time_domain_measurement_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    signal_channel=SIGNAL_CHANNEL,
    measurement_channel=ANALOG_INPUT_CHANNEL,
):
    """Creates the necessary objects for the generation and measurement of the signal"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (276 > 100 characters) (auto-generated noqa)

    # Create the instances of generation and measurement classes required for the test.
    generation_instance = nipcbatt.SignalVoltageGeneration()
    measurement_instance = nipcbatt.TimeDomainMeasurement()

    # Initialize Generation
    """Initializes the configured channels of signal voltage generation module"""
    generation_instance.initialize(channel_expression=signal_channel)

    # Initialize Test Point
    """Initializes the configured channels of AI module to perform Time domain measuerement"""
    measurement_instance.initialize(analog_input_channel_expression=measurement_channel)

    """Note to run with Hardware: Update the routing paths based on NI MAX and 
       Setup Connections in the below step"""

    # Export signals to PFI lines
    sync_signals = nipcbatt.SynchronizationSignalRouting()
    sync_signals.route_sample_clock_signal_to_terminal(terminal_name=SAMPLE_CLOCK_LINE)
    sync_signals.route_start_trigger_signal_to_terminal(terminal_name=START_TRIGGER_LINE)

    return generation_instance, measurement_instance, sync_signals


####################################################################################################
# endregion initialize


# region configure_and_measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: nipcbatt.SignalVoltageGeneration,
    measurement_instance: nipcbatt.TimeDomainMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Note to run with Hardware: Review the Configurations & update the Sample Clock Source
    and Digital Start Trigger Settings based on NI MAX and Setup Connections"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (449 > 100 characters) (auto-generated noqa)

    # Configure Time Domain Measurement settings to wait for Hardware Trigger and Sample Clock
    # from Signal generation. Configure exact sample clock rate set in generation for the shared
    # clock. Note: external clock signals cannot be diveded down to lesser rates

    """Configure test point"""
    """ If write_to_file is True, the Logger is used to output the results to a file.
        The Logger can be used to store configurations and outputs in a .txt or .csv file.
        The default file path is C:\\Windows\\Temp\\signal_voltage_and_time_domain_measurement_results.txt"""  # noqa: W505 - doc line too long (109 > 100 characters) (auto-generated noqa)
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    #### First configuration option will configure only
    meas_options_configure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    # intialize an instance of 'VoltageRangeAndTerminalParameters'
    meas_global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )

    # initialize an instance of 'List[VoltageMeasurementChannelAndTerminalRangeParameters]'
    meas_specific_channels_parameters = []

    # initialize an instance of 'SampleClockTimingParameters'
    meas_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source=SAMPLE_CLOCK_LINE,
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    meas_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source=START_TRIGGER_LINE,
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'TimeDomainMeasurementConfiguration'
    pre_trigger_measurement_config = nipcbatt.TimeDomainMeasurementConfiguration(
        global_channel_parameters=meas_global_channel_parameters,
        specific_channels_parameters=meas_specific_channels_parameters,
        measurement_options=meas_options_configure_only,
        sample_clock_timing_parameters=meas_sample_clock_timing_parameters,
        digital_start_trigger_parameters=meas_digital_start_trigger_parameters,
    )

    # use theconfig object to execute configure_and_measure and wait for generation
    test_point_result_data_after_configuring = measurement_instance.configure_and_measure(
        configuration=pre_trigger_measurement_config
    )

    """Storing results -- create both a Python dictionary (hashmap)
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record intermediate result
    results_map["tdvm_configure_only"] = test_point_result_data_after_configuring

    ### MOVE TO SIGNAL GENERATION ###

    """Generate sine wave from analog module"""
    range_params = nipcbatt.VoltageGenerationChannelParameters(
        range_min_volts=-10.0, range_max_volts=10.0
    )

    tone_params = nipcbatt.ToneParameters(
        tone_frequency_hertz=100.0, tone_amplitude_volts=1.0, tone_phase_radians=0.0
    )

    waveform_params = nipcbatt.SignalVoltageGenerationSineWaveParameters(
        generated_signal_offset_volts=0.0, generated_signal_tone_parameters=tone_params
    )

    timing_parms = nipcbatt.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        generated_signal_duration_seconds=0.1,
    )

    trigger_params = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="OnboardClock",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    sine_wave_configuration = nipcbatt.SignalVoltageGenerationSineWaveConfiguration(
        voltage_generation_range_parameters=range_params,
        waveform_parameters=waveform_params,
        timing_parameters=timing_parms,
        digital_start_trigger_parameters=trigger_params,
    )

    # Generate sine wave
    sine_wave_source_generation = generation_instance.configure_and_generate_sine_waveform(
        configuration=sine_wave_configuration
    )

    # record intermediate generation result
    results_map["sine_wave_generation"] = sine_wave_source_generation

    ### Prepare Second Measurement Configuration  ###

    """Note to run with Hardware: Update "Periodic Waveform" input to "True" to calculate 
       all Time Domain Measurements"""

    meas_options_measure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'SampleClockTimingParameters'
    timing_parameters_measure_only = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    trigger_parameters_measure_only = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="OnboardClock",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'TimeDomainMeasurementConfiguration' for measure only
    measurement_config_measure_only = nipcbatt.TimeDomainMeasurementConfiguration(
        global_channel_parameters=meas_global_channel_parameters,
        specific_channels_parameters=meas_specific_channels_parameters,
        measurement_options=meas_options_measure_only,
        sample_clock_timing_parameters=timing_parameters_measure_only,
        digital_start_trigger_parameters=trigger_parameters_measure_only,
    )

    # Fetch and Validate Sine waveform via analog buffer
    # execute using measure only configuration
    test_point_result_data_after_measurement = measurement_instance.configure_and_measure(
        configuration=measurement_config_measure_only
    )

    # record results
    results_map["post_gen_measurement"] = test_point_result_data_after_measurement

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: nipcbatt.SignalVoltageGeneration,
    measurement_instance: nipcbatt.TimeDomainMeasurement,
    sync_signals: nipcbatt.SynchronizationSignalRouting,
):
    """Closes out the created objects used in the generation and measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (190 > 100 characters) (auto-generated noqa)
    generation_instance.close()  # Close TS
    measurement_instance.close()  # Close TP
    sync_signals.close()  # Close sync


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def signal_voltage_and_time_domain_measurement(
    generation_channel=SIGNAL_CHANNEL,
    measurement_channel=ANALOG_INPUT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (231 > 100 characters) (auto-generated noqa)

    # Run setup function
    gen, meas, sync = setup(generation_channel, measurement_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas, sync)


# endregion test
