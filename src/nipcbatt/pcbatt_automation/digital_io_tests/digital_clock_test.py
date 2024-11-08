"""Demonstrates digital clock generation and frequency measurement through 
   counter-based measurements using Digital IO lines or Modules."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (360 > 100 characters) (auto-generated noqa)

# pylint: disable=W0105

import time  # noqa: F401 - 'time' imported but unused (auto-generated noqa)

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Please note that usage of TestScale PFI7 and PFI3 for digital clock is arbitary, but in
   TestScale the same core module can only be divided into 4 Inputs / 4 Outputs"""

"""Note to run with Hardware: Update the Terminal and Physical Counter Channels based on NI MAX
   in the below initialize step"""


# Default channels
OUTPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI7"  # Output terminal to generate digital clock
GEN_PHYSICAL_CHANNEL_COUNTER = "Sim_PC_basedDAQ/ctr3"  # counter used to generate digital clock

INPUT_TERMINAL = "/Simulated_Core/PFI3"  # input terminal to measure the digital clock
MEAS_PHYSICAL_CHANNEL_COUNTER = "Simulated_Core/ctr1"  # counter used for digital clock measurement

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_clock_test_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    output_terminal=OUTPUT_TERMINAL,
    gen_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    input_terminal=INPUT_TERMINAL,
    meas_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER,
):
    """Creates the necessary objects for the generation and measurement of digital clock"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (279 > 100 characters) (auto-generated noqa)

    # Create the instances of generation and measurement classes required for the test
    generation_instance = nipcbatt.DigitalClockGeneration()
    measurement_instance = nipcbatt.DigitalFrequencyMeasurement()

    # Initialize generation object
    """Initializes the channels of the DCG module to prepare for generation"""
    generation_instance.initialize(
        counter_channel_expression=gen_counter_channel,
        output_terminal_name=output_terminal,
    )

    # Initialize measurement object
    """Initializes the channels of the DFM module to prepare for measurement"""
    measurement_instance.initialize(
        channel_expression=meas_counter_channel, input_terminal_name=input_terminal
    )

    # return initialized objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    generation_instance: nipcbatt.DigitalClockGeneration,
    measurement_instance: nipcbatt.DigitalFrequencyMeasurement,
    write_to_file: True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_clock_test_results.txt"""  # noqa: D205, D209, D301 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Use r""" if any backslashes in a docstring (auto-generated noqa)
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with Hardware: Update the digital clock settings based on the required pulse  # noqa: W505 - doc line too long (344 > 100 characters) (auto-generated noqa)
    train to be generated in the below step"""

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # initialize instances of counter channel parameters and timing parameters for generation
    # then initialize an instance of 'DigitalClockGenerationConfiguration' with the settings
    frequency, duty_cycle, duration = 1000.0, 0.5, 0.5
    gen_channel_parameters = nipcbatt.DigitalClockGenerationCounterChannelParameters(
        frequency_hertz=frequency, duty_cycle_ratio=duty_cycle
    )

    gen_timing_parameters = nipcbatt.DigitalClockGenerationTimingParameters(
        clock_duration_seconds=duration
    )

    gen_configuration = nipcbatt.DigitalClockGenerationConfiguration(
        counter_channel_parameters=gen_channel_parameters, timing_parameters=gen_timing_parameters
    )

    # launch generation with configure_and_generate
    generation_instance.configure_and_generate(configuration=gen_configuration)

    ## initialize instances of range and counter channel parameters for measuremennt
    # then initialize an instance of 'DigitalFrequencyMeasurementConfiguration' with the settings
    minimum, maximum, divisor, measurement_time = 2, 100, 4, 0.001
    meas_range_parameters = nipcbatt.DigitalFrequencyRangeParameters(
        frequency_minimum_value_hertz=minimum, frequency_maximum_value_hertz=maximum
    )

    meas_channel_parameters = nipcbatt.DigitalFrequencyMeasurementCounterChannelParameters(
        range_parameters=meas_range_parameters,
        input_divisor_for_frequency_measurement=divisor,
        measurement_duration_seconds=measurement_time,
    )

    meas_configuration = nipcbatt.DigitalFrequencyMeasurementConfiguration(
        counter_channel_configuration_parameters=meas_channel_parameters
    )

    # launch measurement with configure_and_measure
    freq_data = measurement_instance.configure_and_measure(configuration=meas_configuration)

    # record results
    results_map["FREQUENCY DATA"] = freq_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: nipcbatt.DigitalClockGeneration,
    measurement_instance: nipcbatt.DigitalFrequencyMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""  # noqa: D415 - First line should end with a period, question mark, or exclamation point (auto-generated noqa)
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def digital_clock_test(
    generation_output_channel=OUTPUT_TERMINAL,
    generation_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    measurement_input_channel=INPUT_TERMINAL,
    measurement_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  # noqa: D202, D415 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

    # Run setup function
    gen, meas = setup(
        output_terminal=generation_output_channel,
        gen_counter_channel=generation_counter_channel,
        input_terminal=measurement_input_channel,
        meas_counter_channel=measurement_counter_channel,
    )

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test  # noqa: W505 - doc line too long (231 > 100 characters) (auto-generated noqa)
