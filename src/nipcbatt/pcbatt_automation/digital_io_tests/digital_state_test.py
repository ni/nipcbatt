"""This example demonstrates how to set Digital High & Low states using digital output modules and 
   measure the digital states of test points using digital input modules"""

# pylint: disable=W0105

import time

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
GENERATION_CHANNEL = "TS_DIn0:1"  # physical channel = Sim_PC_basedDAQ/port0/line0:1
MEASUREMENT_CHANNEL = "TP_DOut2:3"  # physical channel = Sim_PC_basedDAQ/port0/line0:1

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_state_test_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(generation_channel=GENERATION_CHANNEL, measurement_channel=MEASUREMENT_CHANNEL):
    """Creates the necessary objects for the generation and measurement of digital states"""

    # Create the instances of generation and measurement classes required for the test.
    generation_instance = nipcbatt.StaticDigitalStateGeneration()
    measurement_instance = nipcbatt.StaticDigitalStateMeasurement()

    # Initialze generation object
    """Intializes the channel(s) of the SDSG module to prepare for generation"""
    generation_instance.initialize(channel_expression=generation_channel)

    # Initialize measurement object
    """Initializes the channel(s) of the SDSM module to prepare for measurement"""
    measurement_instance.initialize(channel_expression=measurement_channel)

    # return initialized objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: nipcbatt.StaticDigitalStateGeneration,
    measurement_instance: nipcbatt.StaticDigitalStateMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_state_test_results.txt
    """
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with hardware: review the configurations for the intended use case"""

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    """Sequence to set static state HIGH and measure the test points: """

    # create a generation configuration that will implement HIGH digital state(s)
    gen_data_high = [True] * generation_instance.task.number_of_channels
    gen_configuration = nipcbatt.StaticDigitalStateGenerationConfiguration(gen_data_high)

    # Generate digital states with the HIGH configuration
    lines = generation_instance.configure_and_generate(configuration=gen_configuration)

    # measure the digital states
    measurement_data_high = measurement_instance.configure_and_measure()

    # record the measurement into the dictionary
    results_map["HIGH"] = measurement_data_high

    """Sequence to set static state low and measure the test points: """

    # create a generation configuration that will implement LOW digital state(s)
    gen_data_low = [False] * generation_instance.task.number_of_channels
    gen_configuration = nipcbatt.StaticDigitalStateGenerationConfiguration(gen_data_low)

    # Generate digital state with the LOW configuration
    lines = generation_instance.configure_and_generate(configuration=gen_configuration)

    # measure the digital states
    measurement_data_low = measurement_instance.configure_and_measure()

    # store digital LOW data in the results_map with corresponding keys
    results_map["LOW"] = measurement_data_low

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: nipcbatt.StaticDigitalStateGeneration,
    measurement_instance: nipcbatt.StaticDigitalStateMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def digital_state_test(
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
