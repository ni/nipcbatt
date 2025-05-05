"""This example demonstrates digital pattern generation and digital edge count measurement through
   counter-based measurements using Digital IO Lines or Modules. Digital edge counting is 
   performed at Hardware timed using with Trigger to create a measurement window for 
   fixed duration"""  

import nidaqmx
import nidaqmx.constants
import numpy as np

import nipcbatt
from nipcbatt.pcbatt_library.common.helper_functions import (
    digital_ramp_pattern_generator,
)
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Terminals and Global/Physical Channels based on NI MAX 
   in the below initialize step"""

# Default channels
GENERATION_CHANNEL = "TS_DIn1"  # global channel to use for digital pattern generation
SESSION_NUMBER = 0

INPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI0"
EDGE_COUNTER = "Sim_PC_basedDAQ/ctr0"
COUNTER_TIMER = "Sim_PC_basedDAQ/ctr1"

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_edge_count_hw_timed_test_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup():
    """Creates the necessary objects for the generation and measurement of digital edge count"""  

    # Create the instances of generation and measurement classes required for the test
    generation_instance = nipcbatt.DynamicDigitalPatternGeneration()
    measurement_instance = nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer()

    # initialize generation object
    generation_instance.initialize(channel_expression=GENERATION_CHANNEL)

    # initialize measurement object
    measurement_instance.initialize(
        measurement_channel_expression=EDGE_COUNTER,
        measurement_input_terminal_name=INPUT_TERMINAL,
        timer_channel_expression=COUNTER_TIMER,
    )

    # return initialzied objects
    return generation_instance, measurement_instance


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################


def main(
    generation_instance: nipcbatt.DynamicDigitalPatternGeneration,
    measurement_instance: nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_edge_count_hw_timed_test_results.txt""" 
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with Hardware: Review the Configurations and update the Trigger &  # noqa: W505 - doc line too long (358 > 100 characters) (auto-generated noqa)
    Counter configurations"""

    """Storing results -- create both a Python dictionary (hashmap)
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # configure trigger
    trig_type = nipcbatt.StartTriggerType.DIGITAL_TRIGGER
    trig_source = "/Sim_PC_basedDAQ/do/StartTrigger"  # Update trigger source according to hw setup
    trig_edge = nidaqmx.constants.Edge.RISING
    trig_params = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=trig_type,
        digital_start_trigger_source=trig_source,
        digital_start_trigger_edge=trig_edge,
    )

    # configure timing

    configure_only_option = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.SKIP_ANALYSIS,
    )

    channel_params = nipcbatt.DigitalEdgeCountMeasurementCounterChannelParameters(
        edge_type=nipcbatt.ConstantsForDigitalEdgeCountMeasurement.DEFAULT_EDGE
    )

    timing_params = nipcbatt.DigitalEdgeCountMeasurementTimingParameters(edge_counting_duration=0.1)

    # create configuration out of trigger and timing configs
    init_config = nipcbatt.DigitalEdgeCountHardwareTimerConfiguration(
        measurement_options=configure_only_option,
        counter_channel_parameters=channel_params,
        timing_parameters=timing_params,
        trigger_parameters=trig_params,
    )

    # apply configuration to measurement instance
    # configures and arms to measure digital edges on rising edge of trigger
    measurement_instance.configure_and_measure(configuration=init_config)

    """Note to run with Hardware: Review & update the "Number of Digital Lines" and 
       "Number of Samples" required to be generated"""

    # create ramp pattern
    num_lines, num_samples = 1, 50
    data = digital_ramp_pattern_generator(num_lines, num_samples)

    # package digital signal into 2D numpy array with number of channels
    data_lines = []
    for i in range(generation_instance.task.number_of_channels):
        data_lines.append(data)
    digital_port_data = np.array(data_lines, np.uint32)

    # intialize an instance of 'DynamicDigitalPatternTimingParameters'
    gen_timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
        sampling_rate_hertz=10000.0,
        number_of_samples_per_channel=1000,
    )

    # create generation configuration
    gen_config = nipcbatt.DynamicDigitalPatternGenerationConfiguration(
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=trig_params,
        pulse_signal=digital_port_data,
    )

    # configure and generate the digital pattern
    generation_instance.configure_and_generate(
        configuration=gen_config, pulse_signal=digital_port_data
    )

    # configuration for measure only
    measure_only_option = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # create configuration from post trigger option settings
    config_meas_only = nipcbatt.DigitalEdgeCountHardwareTimerConfiguration(
        measurement_options=measure_only_option,
        counter_channel_parameters=channel_params,
        timing_parameters=timing_params,
        trigger_parameters=trig_params,
    )

    # read the digital edge counts
    result_data = measurement_instance.configure_and_measure(configuration=config_meas_only)

    # record results
    results_map["HW TIMED COUNT DATA"] = result_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: nipcbatt.DynamicDigitalPatternGeneration,
    measurement_instance: nipcbatt.DigitalEdgeCountMeasurementUsingHardwareTimer,
):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################


def digital_count_events_sw_timed_test(
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    gen, meas = setup()

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


# endregion test  
