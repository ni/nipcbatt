"""This example demonstrates digital pulse generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Software timed using an external wait"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (339 > 100 characters) (auto-generated noqa)

# pylint: disable=W0105, C0413

import time  # noqa: F401 - 'time' imported but unused (auto-generated noqa)

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Terminal and Physical Counter Channels based on NI MAX 
   in the below initialize step"""

# Default channels
OUTPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI7"  # Output terminal to generate digital clock
GEN_PHYSICAL_CHANNEL_COUNTER = "Sim_PC_basedDAQ/ctr3"  # counter used to generate digital clock

INPUT_TERMINAL = "/Simulated_Core/PFI3"  # terminal to measure the digital edge count measurements
EDGE_COUNTER = "Simulated_Core/ctr1"  # counter used for digital edge count ceasurements

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_edge_count_sw_timed_test_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    output_terminal=OUTPUT_TERMINAL,
    gen_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    input_terminal=INPUT_TERMINAL,
    edge_count_channel=EDGE_COUNTER,
):
    """Creates the necessary objects for the generation and measurement of digital edge count"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (284 > 100 characters) (auto-generated noqa)

    # Create the instances of generation and measurement classes required for the test
    generation_instance = nipcbatt.DigitalPulseGeneration()
    measurement_instance = nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer()

    # Initialize generation object
    generation_instance.initialize(
        channel_expression=gen_counter_channel, output_terminal_name=output_terminal
    )

    # Initialize measurement object
    measurement_instance.initialize(
        measurement_channel_expression=edge_count_channel,
        measurement_input_terminal_name=input_terminal,
    )

    # return initialzied objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################


def main(
    generation_instance: nipcbatt.DigitalPulseGeneration,
    measurement_instance: nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_edge_count_sw_timed_test_results.txt"""  # noqa: D205, D209, D301 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Use r""" if any backslashes in a docstring (auto-generated noqa)
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Configure and generate/measure signals"""

    """Storing results -- create both a Python dictionary (hashmap)  # noqa: W505 - doc line too long (358 > 100 characters) (auto-generated noqa)
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs
    configure_only_option = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    channel_params = nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
        edge_type=nipcbatt.ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE
    )

    timing_params = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(edge_counting_duration=0.1)
    init_config = nipcbatt.DigitalEdgeCountSoftwareTimerConfiguration(
        measurement_options=configure_only_option,
        counter_channel_parameters=channel_params,
        timing_parameters=timing_params,
    )

    # configures to measure digital edges
    measurement_instance.configure_and_measure(configuration=init_config)

    """Note to run with Hardware: Update the Digital pulse settings in the below step based 
       on the required digital signal to be generated"""

    # create constants needed to create generation configuration
    low_time, high_time, num_pulses = 0.0003, 0.0005, 2000
    level = nipcbatt.ConstantsForDigitalPulseGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT

    gen_counter_parameters = nipcbatt.DigitalPulseGenerationCounterChannelParameters(
        pulse_idle_state=level, low_time_seconds=low_time, high_time_seconds=high_time
    )

    gen_timing_parameters = nipcbatt.DigitalPulseGenerationTimingParameters(pulses_count=num_pulses)

    gen_config = nipcbatt.DigitalPulseGenerationConfiguration(
        counter_channel_parameters=gen_counter_parameters, timing_parameters=gen_timing_parameters
    )

    # generates digital pulse signals
    generation_instance.configure_and_generate(configuration=gen_config)

    """Note to run with Hardware: Update and uncomment the software wait time in the below step 
       based on the measurement window to be captured"""

    # time.sleep(0.1) #100 ms

    # create new configuration to read edge counts
    measure_only_option = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    meas_config = nipcbatt.DigitalEdgeCountSoftwareTimerConfiguration(
        measurement_options=measure_only_option,
        counter_channel_parameters=channel_params,
        timing_parameters=timing_params,
    )

    # read the digital edge counts
    sw_count_data = measurement_instance.configure_and_measure(configuration=meas_config)

    # record results
    results_map["SW TIMED COUNT DATA"] = sw_count_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: nipcbatt.DigitalPulseGeneration,
    measurement_instance: nipcbatt.DigitalEdgeCountMeasurementUsingSoftwareTimer,
):
    """Closes out the created objects used in the generation and measurement"""  # noqa: D415 - First line should end with a period, question mark, or exclamation point (auto-generated noqa)
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################


def digital_count_events_sw_timed_test(
    generation_output_channel=OUTPUT_TERMINAL,
    generation_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    measurement_input_channel=INPUT_TERMINAL,
    edge_counter=EDGE_COUNTER,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  # noqa: D202, D415 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

    # Run setup function
    gen, meas = setup(
        output_terminal=generation_output_channel,
        gen_counter_channel=generation_counter_channel,
        input_terminal=measurement_input_channel,
        edge_count_channel=edge_counter,
    )

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test  # noqa: W505 - doc line too long (190 > 100 characters) (auto-generated noqa)
