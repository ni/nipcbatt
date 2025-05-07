"""Demonstrates DC RMS Voltage Measurement using AI lines""" 

import os
import sys
from enum import Enum  

import nidaqmx.constants

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# To use save_traces and plotter from utils folder
# from pcbatt_logger import PcbattLogger
parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)

"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
in the below initialize step"""
# Default Channel
INPUT_TERMINAL = "Sim_PC_basedDAQ/ai1"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\DRVM_test.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
def setup(input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH):
    """Creates the necessary objects for measurement of Voltage""" 

    # Creates the instance of measurement class required for the test
    drvm = nipcbatt.DcRmsVoltageMeasurement()
    """Initializes the channels for drvm module to prepare for measurement"""
    drvm.initialize(analog_input_channel_expression=input_terminal)

    # Sets the logger function
    logger = PcbattLogger(file_path)
    logger.attach(drvm)

    # returns the initialized objects
    return drvm


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND MEASURE ###########################
def main(  
    drvm: nipcbatt.DcRmsVoltageMeasurement,
):
    results_map = {}  # this structure will hold results in key-value pairs

    # Set the minimum and maximum voltage range
    global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
        range_min_volts=-10,
        range_max_volts=10,
    )

    specific_channels_parameters = []

    # Set the Measurement Execution Type
    measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # Set the Sampling rate and the Number of Samples per Channel
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

    drvm_config = nipcbatt.DcRmsVoltageMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=measurement_options,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion drvm configure and measure
    ####################################################################################################  
    # end region configure and measure

    drvm_result_data = drvm.configure_and_measure(drvm_config)
    print("DRVM result :\n")
    print(drvm_result_data)
    # region close
    # record results
    results_map["DRVM data"] = drvm_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    drvm: nipcbatt.DcRmsVoltageMeasurement,
):
    drvm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def analog_voltage_measurement(
    generation_input_channel=INPUT_TERMINAL,
):
    # Runs setup function
    drvm = setup(input_terminal=generation_input_channel)
    # Runs the main function
    main(drvm)
    # Runs the cleanup function
    cleanup(drvm)


# endregion test
