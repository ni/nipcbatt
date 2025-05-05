"""This example demonstrates digital pulse generation and digital edge count measurement through 
   counter-based measurements using Core Digital IO Modules. Digital edge counting is performed 
   at Software timed using an external wait""" 


import time  

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Terminal and Physical Counter Channels based on NI MAX 
   in the below initialize step"""

# Default channels
OUTPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI7"  # Output terminal to generate digital clock
GEN_PHYSICAL_CHANNEL_COUNTER = "Sim_PC_basedDAQ/ctr3"  # counter used to generate digital clock

INPUT_TERMINAL = "/Simulated_Core/PFI3"  # input terminal to measure the digital clock
MEAS_PHYSICAL_CHANNEL_COUNTER = "Simulated_Core/ctr1"  # counter used for digital clock measurement
COUNTER_TIMER = ""  # No timer operation is performed in SW timed mode

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_pwm_test_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################

"""Note to run with Hardware: Update the Cycles to capture value in the below step based on the 
   digital signals to be measured"""


def setup(
    output_terminal=OUTPUT_TERMINAL,
    gen_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    input_terminal=INPUT_TERMINAL,
    meas_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER,
):
    """Creates the necessary objects for the generation and measurement of PWM""" 

    # Create the instances of generation and measurement classes required for the test
    generation_instance = nipcbatt.DigitalPulseGeneration()
    measurement_instance = nipcbatt.DigitalPwmMeasurement()

    # Initialize generation object
    generation_instance.initialize(
        channel_expression=gen_counter_channel, output_terminal_name=output_terminal
    )

    # initialize measurement object
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
    generation_instance: nipcbatt.DigitalPulseGeneration,
    measurement_instance: nipcbatt.DigitalPwmMeasurement,
    write_to_file: True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_pwm_test_results.txt
    """ 
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """Note to run with Hardware: Update the Cycles to capture value in the below step based on the  # noqa: W505 - doc line too long (176 > 100 characters) (auto-generated noqa)
    digital signals to be measured"""

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # create constants needed for measurement configuration objects
    min_semiperiod, max_semiperiod, cycles_count = 2.5e-8, 53.68709, 2
    edge = nipcbatt.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE
    execution_type_cfg_only = nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY

    # create configuration sub-objects
    meas_range_parameters = nipcbatt.DigitalPwmMeasurementRangeParameters(
        semi_period_minimum_value_seconds=min_semiperiod,
        semi_period_maximum_value_seconds=max_semiperiod,
    )

    meas_timing_parameters = nipcbatt.DigitalPwmMeasurementTimingParameters(
        semi_period_counter_wanted_cycles_count=cycles_count
    )

    meas_counter_parameters = nipcbatt.DigitalPwmMeasurementCounterChannelParameters(
        range_parameters=meas_range_parameters,
        timing_parameters=meas_timing_parameters,
        semi_period_counter_starting_edge=edge,
    )

    # create configuration object to configure only
    meas_cfg_config_only = nipcbatt.DigitalPwmMeasurementConfiguration(
        parameters=meas_counter_parameters, measurement_option=execution_type_cfg_only
    )

    # configure measurement instance
    measurement_instance.configure_and_measure(configuration=meas_cfg_config_only)

    """Note to run with Hardware: Update the digital pulse settings in the below step 
       based on the required digital signal to be generated"""

    # create constants needed to create generation configuration
    low_time, high_time, num_pulses = 0.003, 0.001, 100
    level = nipcbatt.ConstantsForDigitalPulseGeneration.DEFAULT_FREQUENCY_GENERATION_UNIT

    gen_counter_parameters = nipcbatt.DigitalPulseGenerationCounterChannelParameters(
        pulse_idle_state=level, low_time_seconds=low_time, high_time_seconds=high_time
    )

    gen_timing_parameters = nipcbatt.DigitalPulseGenerationTimingParameters(pulses_count=num_pulses)

    gen_config = nipcbatt.DigitalPulseGenerationConfiguration(
        counter_channel_parameters=gen_counter_parameters, timing_parameters=gen_timing_parameters
    )

    # configure and generate generation instance
    generation_instance.configure_and_generate(configuration=gen_config)

    # create separate configuration to be used to measure only after generation has started
    execution_type_measure_only = nipcbatt.MeasurementExecutionType.MEASURE_ONLY
    meas_cfg_measure_only = nipcbatt.DigitalPwmMeasurementConfiguration(
        parameters=meas_counter_parameters, measurement_option=execution_type_measure_only
    )

    # configure_and_measure with measure only
    pwm_data = measurement_instance.configure_and_measure(configuration=meas_cfg_measure_only)

    # record results
    results_map["PWM DATA"] = pwm_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    generation_instance: nipcbatt.DigitalPulseGeneration,
    measurement_instance: nipcbatt.DigitalPwmMeasurement,
):
    """Closes out the created objects used in the generation and measurement""" 
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close

# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################


def digital_pwm_test(
    generation_output_channel=OUTPUT_TERMINAL,
    generation_counter_channel=GEN_PHYSICAL_CHANNEL_COUNTER,
    measurement_input_channel=INPUT_TERMINAL,
    measurement_counter_channel=MEAS_PHYSICAL_CHANNEL_COUNTER,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

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


# endregion test  
