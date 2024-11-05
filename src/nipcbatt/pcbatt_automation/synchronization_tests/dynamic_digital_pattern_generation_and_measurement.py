"""This example demonstrates synchronization using Dynamic Digital Pattern Generation Library to 
   generate Digital Pattern from one Backplane and capture it using Dynamic Digital Pattern 
   Measuerment library in another Backplane"""

# pylint: disable=W0105,E0401
import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt.pcbatt_library.common.helper_functions import digital_ramp_pattern_generator
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Global Channel Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
GENERATION_CHANNEL = "TS_Digital0,TS_Digital1"
MEASUREMENT_CHANNEL = "TP_Digital2,TP_Digital3"

# Default signal lines
SAMPLE_CLOCK_LINE = "/Sim_PC_basedDAQ/PFI0"  # Exporting Sample Clock to PFI0 Terminal
START_TRIGGER_LINE = "/Sim_PC_basedDAQ/PFI1"  # Exporting Start Trigger to PFI1 Terminal

# Default test results location
DEFAULT_FILEPATH = (
    "C:\\Windows\\Temp\\dynamic_digital_pattern_generation_and_measurement_results.txt"
)


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL):
    """Creates the necessary objects for the generation and measurement of digital patterns"""

    # Create the instances of generation and measurement classes required for the test.
    generation_instance = nipcbatt.DynamicDigitalPatternGeneration()
    measurement_instance = nipcbatt.DynamicDigitalPatternMeasurement()

    # Initialize generation object
    """Initializes the channel(s) of the DDPG module to prepare for generation"""
    generation_instance.initialize(channel_expression=generation_channel)

    # Initialize measurement object
    """Initializes the channel(s) of the DDPM module to prepare for measurement"""
    measurement_instance.initialize(channel_expression=measurement_channel)

    # Export signals to PFI lines
    sync_signals = nipcbatt.SynchronizationSignalRouting()
    sync_signals.route_sample_clock_signal_to_terminal(terminal_name=SAMPLE_CLOCK_LINE)
    sync_signals.route_start_trigger_signal_to_terminal(terminal_name=START_TRIGGER_LINE)

    # return initialized objects
    return generation_instance, measurement_instance, sync_signals


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: nipcbatt.DynamicDigitalPatternGeneration,
    measurement_instance: nipcbatt.DynamicDigitalPatternMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path for the results of this sequence is:
    C:\\Windows\\Temp\\dynamic_digital_pattern_generation_and_measurement_results.txt"""

    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Configure test point"""

    # Note to run with Hardware: Review the Configurations & update the Sample Clock Source and
    # Digital Start Trigger Settings based on NI MAX and Setup Connections

    """Consider below items when measuring Digital patterns
       1. Sampling rate at measurement end should be same as the sampling rate at generation end
       2. Configure Trigger to start capture as soon as pattern generated using Dynamic 
       digital pattern measurement"""

    # initialize an instance of 'MeasurementOptions' with options to configure only
    meas_options_configure_only = nipcbatt.MeasurementOptions(
        nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    # intialize an instance of 'DynamicDigitalPatternTimingParameters'
    timing_parameters_configure_only = nipcbatt.DynamicDigitalPatternTimingParameters(
        sampling_rate_hertz=10000.0,  # Provide exact sample clock rate set in Generation for the
        # shared clock. Note: external clock signals cannot be divided down to lesser rates
        number_of_samples_per_channel=1000,
        active_edge=nidaqmx.constants.Edge.FALLING,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    trigger_parameters_configure_only = nipcbatt.DigitalStartTriggerParameters(
        digital_start_trigger_source=START_TRIGGER_LINE,
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    )

    # initialize an instance of 'DynamicDigitalPatternMeasurementConfiguration' for configure only
    pre_trigger_measurement_config = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
        measurement_options=meas_options_configure_only,
        timing_parameters=timing_parameters_configure_only,
        trigger_parameters=trigger_parameters_configure_only,
    )

    # use the config object to execute configure_and_measure to configure only
    measurement_instance.configure_and_measure(configuration=pre_trigger_measurement_config)

    # Note to run with Hardware: Review & update "Number of Digital Line" initialized in
    # Generation Task in the below step

    # create ramp data to output on digital port
    data = digital_ramp_pattern_generator(number_of_digital_lines=2, number_of_samples=100)

    # package digital signal into 2D numpy array with number of channels
    data_lines = []
    for i in range(generation_instance.task.number_of_channels):
        data_lines.append(data)
    digital_port_data = np.array(data_lines, np.uint32)

    # create a generation instance for DynamicDigitalPatternTimingParameters
    gen_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000.0,
        active_edge=nidaqmx.constants.Edge.RISING,
    )

    # create a generation instance for DigitalStartTriggerParameters
    gen_trigger_parameters = nipcbatt.DynamicDigitalStartTriggerParameters(
        trigger_type=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/PFI0",  # placeholder- not used
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # create an instance of DynamicDigitalPatternGenerationConfiguration
    generation_config = nipcbatt.DynamicDigitalPatternGenerationConfiguration(
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
        pulse_signal=digital_port_data,
    )

    # generate the configured digital pattern from the digital module
    generation_instance.configure_and_generate(configuration=generation_config)

    # Create second measurement configuration to configure only
    # intialize an instance of 'DynamicDigitalPatternTimingParameters'
    timing_parameters_measure_only = nipcbatt.DynamicDigitalPatternTimingParameters(
        sampling_rate_hertz=10000.0,
        number_of_samples_per_channel=1000,
        active_edge=nidaqmx.constants.Edge.RISING,
    )

    # create an instance for DigitalStartTriggerParameters
    trigger_parameters_measure_only = nipcbatt.DynamicDigitalStartTriggerParameters(
        trigger_type=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="/Sim_PC_basedDAQ/PFI0",  # placeholder- not used
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'MeasurementOptions' for measure only
    meas_options_measure_only = nipcbatt.MeasurementOptions(
        nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'DynamicDigitalPatternMeasurementConfiguration' for post-generation
    post_gen_measurement_config = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
        measurement_options=meas_options_measure_only,
        timing_parameters=timing_parameters_measure_only,
        trigger_parameters=trigger_parameters_measure_only,
    )

    # read digital pattern stored in buffer using postgeneration configuration
    result_data = measurement_instance.configure_and_measure(post_gen_measurement_config)

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record results
    results_map["DIGITAL DATA"] = result_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: nipcbatt.DynamicDigitalPatternGeneration,
    measurement_instance: nipcbatt.DynamicDigitalPatternMeasurement,
    sync_signals: nipcbatt.SynchronizationSignalRouting,
):
    """Closes out the created objects used in the generation and measurement"""
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement
    sync_signals.close()  # Close signal synchronization


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def dynamic_digital_pattern_generation_and_measurement(
    generation_channel=GENERATION_CHANNEL,
    measurement_channel=MEASUREMENT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""

    # Run setup function
    gen, meas, sync = setup(generation_channel, measurement_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas, sync)


# endregion test
