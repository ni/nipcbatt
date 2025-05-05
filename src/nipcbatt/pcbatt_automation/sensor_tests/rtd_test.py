"""Demonstrates temprature measurement using RTD using AI lines or Modules"""  

import os  
import sys  

import nidaqmx
import nidaqmx.constants

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# ignore:
"""To use the specific channel change the use_specific_channel to True"""
# Global variable
use_specific_channel = False

"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
in the below initialize step"""

# Default channels
INPUT_TERMINAL = "TP_RTD"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\RTD_test.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
def setup(input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH):
    """Creates the necessary objects for the measurement of Temprature"""  

    # Creates the instances of measurement class required for the test
    trtdm = nipcbatt.TemperatureMeasurementUsingRtd()

    # Initialize measurement object
    """Initializes the channels of the trtdm module to prepare for measurement"""
    trtdm.initialize(input_terminal)
    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(trtdm)
    # returns initializated objects
    return trtdm


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND MEASURE ###########################
def main( 
    trtdm: nipcbatt.TemperatureMeasurementUsingRtd, input_terminal=INPUT_TERMINAL
):
    results_map = {}  # this structure will hold results in key-value pairs

    # region TRTDM configure and measure
    global_channel_parameters = nipcbatt.TemperatureRtdMeasurementTerminalParameters(
        temperature_minimum_value_celsius_degrees=0,
        temperature_maximum_value_celsius_degrees=100,
        current_excitation_value_amperes=0.001,
        sensor_resistance_ohms=100,
        rtd_type=nidaqmx.constants.RTDType.PT_3750,
        excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
        resistance_configuration=nidaqmx.constants.ResistanceConfiguration.THREE_WIRE,
        adc_timing_mode=nidaqmx.constants.ADCTimingMode.AUTOMATIC,
    )

    # region specific_channels_parameters
    channel0 = nipcbatt.TemperatureRtdMeasurementChannelParameters(
        channel_name=input_terminal,
        sensor_resistance_ohms=100,
        current_excitation_value_amperes=0.001,
        rtd_type=nidaqmx.constants.RTDType.PT_3750,
        resistance_configuration=nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE,
        excitation_source=nidaqmx.constants.ExcitationSource.INTERNAL,
    )

    # endregion specific_channels_parameters

    specific_channels_parameters = []
    if use_specific_channel:
        specific_channels_parameters.append(channel0)

    # Configure the sampling rate and the number of sample per channel according to requirement
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100,
        number_of_samples_per_channel=10,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    trtdm_config = nipcbatt.TemperatureRtdMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion TRTDM configure and measure
    ####################################################################################################  

    trtdm_result_data = trtdm.configure_and_measure(configuration=trtdm_config)
    print("TRTDM result :\n")
    print(trtdm_result_data)
    # region close

    # record results
    results_map["RTD data"] = trtdm_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    trtdm: nipcbatt.TemperatureMeasurementUsingRtd,
):
    trtdm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def rtd_test(
    measurement_input_channel=INPUT_TERMINAL,
):
    """Execute all steps in the sequence"""  
    
    # Run setup function
    trtdm = setup(
        input_terminal=measurement_input_channel,
    )
    # Run main function
    main(trtdm, input_terminal=measurement_input_channel)
    # Run cleanup function
    cleanup(trtdm)


# endregion test
