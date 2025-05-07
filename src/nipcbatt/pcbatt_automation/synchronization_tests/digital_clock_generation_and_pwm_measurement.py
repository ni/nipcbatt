"""This example demonstrates generation of Digital Clock signal using Digital Clock Generation 
   Library and measurement of the same signal using Digital PWM Measurement Library"""  

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

"""Note to run with Hardware: Update the Physical Channel (Counter) and its Terminals  
   based on NI MAX in the below initialize step"""

# Default channels
PHYSICAL_CHANNEL_OUT = "/Sim_PC_basedDAQ/ctr0"
OUTPUT_TERMINAL = "/Sim_PC_basedDAQ/PFI0"

PHYSICAL_CHANNEL_IN = "/Sim_PC_basedDAQ1/ctr0"
INPUT_TERMINAL = "/Sim_PC_basedDAQ1/PFI0"
GLOBAL_CHANNEL_COUNTER = ""

# Set the defaut filepath to save the acquired data
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\digital_clock_generation_and_pwm_measurement_results.txt"

# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    output_terminal=OUTPUT_TERMINAL,
    gen_counter_channel=PHYSICAL_CHANNEL_OUT,
    input_terminal=INPUT_TERMINAL,
    meas_counter_channel=PHYSICAL_CHANNEL_IN,
):
    """Creates the necessary objects for the generation and measurement of digital clock"""  

    # Create the instances of generation and measurement classes required for the test
    generation_instance = nipcbatt.DigitalClockGeneration()
    measurement_instance = nipcbatt.DigitalPwmMeasurement()

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
    measurement_instance: nipcbatt.DigitalPwmMeasurement,
    write_to_file: True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\digital_clock_generation_and_pwm_measurement_results.txt
    """  
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(generation_instance)
        logger.attach(measurement_instance)

    """1. Configure PWM Measurement settings to wait for Digital PWM Signal from Digital Clock Generation
    2. Generate PWM waveform from digital IO module
    3. Fetch and Validate Digital PWM Signal""" 

    # create configuration sub-objects
    meas_range_parameters = nipcbatt.DigitalPwmMeasurementRangeParameters(
        semi_period_minimum_value_seconds=25e-9,  # default minimum semiperiod (s)
        semi_period_maximum_value_seconds=53.68709,  # default maximum semiperiod (s)
    )

    meas_timing_parameters = nipcbatt.DigitalPwmMeasurementTimingParameters(
        semi_period_counter_wanted_cycles_count=100
    )

    meas_counter_parameters = nipcbatt.DigitalPwmMeasurementCounterChannelParameters(
        range_parameters=meas_range_parameters,
        timing_parameters=meas_timing_parameters,
        semi_period_counter_starting_edge=nipcbatt.ConstantsForDigitalPwmMeasurement.DEFAULT_PWM_STARTING_EDGE,
    )

    # create configuration object to configure only
    meas_cfg_config_only = nipcbatt.DigitalPwmMeasurementConfiguration(
        parameters=meas_counter_parameters,
        measurement_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
    )

    # configure measurement instance
    measurement_instance.configure_and_measure(configuration=meas_cfg_config_only)

    # initialize instances of counter channel parameters and timing parameters for generation
    # then initialize an instance of 'DigitalClockGenerationConfiguration' with the settings
    gen_channel_parameters = nipcbatt.DigitalClockGenerationCounterChannelParameters(
        frequency_hertz=1000.0, duty_cycle_ratio=0.5
    )

    gen_timing_parameters = nipcbatt.DigitalClockGenerationTimingParameters(
        clock_duration_seconds=0.1
    )

    gen_configuration = nipcbatt.DigitalClockGenerationConfiguration(
        counter_channel_parameters=gen_channel_parameters, timing_parameters=gen_timing_parameters
    )

    # launch generation with configure_and_generate
    generation_instance.configure_and_generate(configuration=gen_configuration)

    # create separate measurement configuration to be used to measure only
    meas_cfg_measure_only = nipcbatt.DigitalPwmMeasurementConfiguration(
        parameters=meas_counter_parameters,
        measurement_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
    )

    # configure_and_measure with measure only
    pwm_data = measurement_instance.configure_and_measure(configuration=meas_cfg_measure_only)

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record results
    results_map["PWM DATA"] = pwm_data

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate


# Close all tasks
def cleanup(
    generation_instance: nipcbatt.DigitalClockGeneration,
    measurement_instance: nipcbatt.DigitalPwmMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""  
    generation_instance.close()  # Close generation
    measurement_instance.close()  # Close measurement


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def digital_clock_generation_and_pwm_measurement(
    generation_output_channel=OUTPUT_TERMINAL,
    generation_counter_channel=PHYSICAL_CHANNEL_OUT,
    measurement_input_channel=INPUT_TERMINAL,
    measurement_counter_channel=PHYSICAL_CHANNEL_IN,
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
