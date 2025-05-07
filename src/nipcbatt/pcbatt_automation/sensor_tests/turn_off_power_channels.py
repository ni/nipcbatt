"""This example resets all the configured Power Channels to 0 volts and 0 amps"""  

import os
import sys

import nidaqmx
import nidaqmx.constants
import numpy as np  

import nipcbatt

parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)

"""Note to run with hardware: update virtual/physical channels info based
on NI MAX in the below Initialize Steps"""
# Default Channel
OUTPUT_TERMINAL = "Simulated_Power/power"


# Initialize Region
########################################   INITIALIZATION FUNCTION   #########################################################
def setup(output_terminal=OUTPUT_TERMINAL):
    """Creates the necessary objects for voltage generation""" 
    pssm = nipcbatt.PowerSupplySourceAndMeasure()
    # Create the instances of generation class reuired for the test
    pssm.initialize(output_terminal)
    # returns the initialized object
    return pssm


################################################################################################################################
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(pssm: nipcbatt.PowerSupplySourceAndMeasure):
    """Sets up the volatge and current to be generated."""  
    terminal_parameters = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
        voltage_setpoint_volts=0.1,
        current_setpoint_amperes=0.1,
        power_sense=nidaqmx.constants.Sense.LOCAL,
        idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED,  # Disable power output when idle
        enable_output=True,
    )

    measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    gen_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    gen_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    pssm_config = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
        terminal_parameters=terminal_parameters,
        measurement_options=measurement_options,
        sample_clock_timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
    )

    # endregion PSSM configure and measure
    ###################################################################################################

    pssm.configure_and_measure(configuration=pssm_config)


# pssm_result_data = pssm.configure_and_measure(configuration=pssm_config)
# close region


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    pssm: nipcbatt.PowerSupplySourceAndMeasure,
):
    pssm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def close_power_supply(generation_output_channel=OUTPUT_TERMINAL):
    """Executes all steps in Sequence"""  
    
    # Runs the Setup Function
    pssm = setup(output_terminal=generation_output_channel)

    # Runs the main function
    main(pssm)

    # Runs the cleanup function
    cleanup(pssm)


# endregion
