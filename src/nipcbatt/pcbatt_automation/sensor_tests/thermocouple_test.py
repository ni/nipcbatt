"""Demonstrates temprature measurement using Thermocouple using AI lines or Modules"""  

import os
import sys

import nidaqmx
import nidaqmx.constants

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# To use save_traces and plotter from utils folder
parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)

"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
in the below initialize step"""
# Default channels
INPUT_TERMINAL = "TP_TC"
COLD_JUNCTION_CHANNEL = "Simulated_cDAQ_9217/ai0"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Thermocouple_test.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ###################################################
def setup(
    input_terminal=INPUT_TERMINAL,
    cold_junction_terminal=COLD_JUNCTION_CHANNEL,
    file_path=DEFAULT_FILEPATH,
):
    """Creates the necessary objects for the measurement of Temprature"""  

    # Creates the instance of measurement class required for the test
    ttcm = nipcbatt.TemperatureMeasurementUsingThermocouple()

    """Initializes the channels of the ttcm module to prepare for measurement"""
    ttcm.initialize(
        channel_expression=input_terminal,
        cold_junction_compensation_source=nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE,
        cold_junction_compensation_channel=cold_junction_terminal,
    )
    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(ttcm)
    # returns initializated objects
    return ttcm


############################################################################################################################
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND MEASURE ###########################
def main(  
    ttcm: nipcbatt.TemperatureMeasurementUsingThermocouple,
    input_terminal=INPUT_TERMINAL,
    cold_junction_terminal=COLD_JUNCTION_CHANNEL,
):
    results_map = {}  # this structure will hold results in key-value pairs

    # region ttcm configure and measure
    global_channel_parameters = nipcbatt.TemperatureThermocoupleMeasurementTerminalParameters(
        temperature_minimum_value_celsius_degrees=0.0,
        temperature_maximum_value_celsius_degrees=100.0,
        thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
        cold_junction_compensation_temperature=25.0,
        perform_auto_zero_mode=False,
        auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
    )

    # region specific_channels_parameters

    channel_parameters = nipcbatt.TemperatureThermocoupleRangeAndTerminalParameters(
        temperature_minimum_value_celsius_degrees=0.0,
        temperature_maximum_value_celsius_degrees=100.0,
        thermocouple_type=nidaqmx.constants.ThermocoupleType.J,
        cold_junction_compensation_source=nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL,
        cold_junction_compensation_temperature=25.0,
        cold_junction_compensation_channel_name=cold_junction_terminal,
        perform_auto_zero_mode=False,
        auto_zero_mode=nidaqmx.constants.AutoZeroType.NONE,
    )

    channel1 = nipcbatt.TemperatureThermocoupleChannelRangeAndTerminalParameters(  
        channel_name=input_terminal, channel_parameters=channel_parameters
    )

    # endregion specific_channels_parameters

    specific_channels_parameters = []
    # Configure the sampling rate and the number of sample per channel according to requirement
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    ttcm_config = nipcbatt.TemperatureThermocoupleMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion ttcm configure and measure
    #################################################################################################
    # end region configure and measure

    ttcm_result_data = ttcm.configure_and_measure(configuration=ttcm_config)
    print("ttcm result :\n")
    print(ttcm_result_data)
    # region close

    # record results
    results_map["TTCM data"] = ttcm_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    ttcm: nipcbatt.TemperatureMeasurementUsingThermocouple,
):
    ttcm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def thermocouple_test(
    generation_input_channel=INPUT_TERMINAL,
    cold_input_channel=COLD_JUNCTION_CHANNEL,
):
    """Execute all steps in the sequence""" 
    
    # Runs setup function
    ttcm = setup(input_terminal=generation_input_channel, cold_junction_terminal=cold_input_channel)
    # Runs main function
    main(ttcm, input_terminal=generation_input_channel, cold_junction_terminal=cold_input_channel)
    # Runs cleanup function
    cleanup(ttcm)


# endregion test
