"""This example demonstrates the digital pattern generation and capture using digital input and 
   output modules with trigger for synchronization"""

# pylint: disable=W0105


import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt.pcbatt_library.common.helper_functions import digital_ramp_pattern_generator
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
GENERATION_CHANNEL = "TS_DIn0:1"  # physical channel = Sim_PC_basedDAQ/port0/line0:1
MEASUREMENT_CHANNEL = "TP_DOut2:3"  # physical channel = Sim_PC_basedDAQ/port0/line2:3

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_pattern_test_results.txt"

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

    # return initialized objects
    return generation_instance, measurement_instance


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
    The default file path is C:\\Windows\\Temp\\digital_pattern_test_results.txt"""
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with Hardware: Review the configurations and update the trigger configurations"""

    """Note to run with Hardware: Sampling rate at measurement end should be same as the sampling 
       rate at generation end (Onboard Clock for same backplane or external PFI signals)"""

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    #### Create a configuration for measurement
    #### First configuration option will configure only

    # initialize an instance of 'MeasurementOptions' with options to configure only
    meas_options_configure_only = nipcbatt.MeasurementOptions(
        nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    # intialize an instance of 'DynamicDigitalPatternTimingParameters'
    meas_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
        sampling_rate_hertz=10000.0,
        number_of_samples_per_channel=1000,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        digital_start_trigger_source="/Sim_PC_basedDAQ/do/StartTrigger",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
    )

    # initialize an instance of 'DynamicDigitalPatternMeasurementConfiguration' to configure only
    meas_config_configure_only = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
        measurement_options=meas_options_configure_only,
        timing_parameters=meas_timing_parameters,
        trigger_parameters=meas_trigger_parameters,
    )

    # use the config object to execute configure_and_measure and wait for generation
    measurement_instance.configure_and_measure(configuration=meas_config_configure_only)

    """Note to run with Hardware: Review & update the "number_of_digital_lines" and 
       "number_of_samples" required to be generated"""

    # create ramp data to output on digital port
    num_lines, num_samples = 2, 50
    data = digital_ramp_pattern_generator(
        number_of_digital_lines=num_lines, number_of_samples=num_samples
    )

    # package digital signal into 2D numpy array with number of channels
    data_lines = []
    for i in range(generation_instance.task.number_of_channels):
        data_lines.append(data)
    digital_port_data = np.array(data_lines, np.uint32)

    """Note to run with Hardware: Sampling rate at generation and measurement should be same 
       (Onboard Clock for same Backplane or external PFI signals)"""

    # create a generation instance for DynamicDigitalPatternTimingParameters
    gen_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
        sample_clock_source="OnboardClock", sampling_rate_hertz=10000.0
    )

    # create a generation instance for DigitalStartTriggerParameters
    gen_trigger_parameters = nipcbatt.DynamicDigitalStartTriggerParameters(
        digital_start_trigger_source="/Sim_PC_basedDAQ/PFI0",  # placeholder- not used
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        trigger_type=nipcbatt.StartTriggerType.NO_TRIGGER,
    )

    # create an instance of DynamicDigitalPatternGenerationConfiguration
    generation_config = nipcbatt.DynamicDigitalPatternGenerationConfiguration(
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
        pulse_signal=digital_port_data,
    )

    # generate the configured digital pattern from the digital module
    generation_instance.configure_and_generate(configuration=generation_config)

    #### Second measurement configuration will skip configuring and go straight to measurement
    # initialize an instance of 'MeasurementOptions' with options to go measure only
    meas_options_measure_only = nipcbatt.MeasurementOptions(
        nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'DynamicDigitalPatternMeasurementConfiguration' for measure only
    meas_config_measure_only = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
        measurement_options=meas_options_measure_only,
        timing_parameters=meas_timing_parameters,
        trigger_parameters=meas_trigger_parameters,
    )

    # read digital pattern stored in buffer (capture starts as soon as start
    # trigger is received from the digital output module)
    # use post trigger configuration
    result_data = measurement_instance.configure_and_measure(meas_config_measure_only)

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
):
    """Closes out the created objects used in the generation and measurement"""
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def digital_pattern_test(
    generation_channel=GENERATION_CHANNEL,
    measurement_channel=MEASUREMENT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""

    # Run setup function
    gen, meas = setup(generation_channel, measurement_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test
