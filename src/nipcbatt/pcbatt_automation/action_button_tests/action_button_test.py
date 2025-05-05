"""Example demonstrates DC-RMS Voltage Measurements by performing button actions 
   (generating DC Voltages) on specific test points"""  

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

## Setup: Get the physical channels required for the test.

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
BUTTON_CHANNEL = "TS_ButtonEnable0"  # physical channel = Sim_PC_basedDAQ/ao0
DC_RMS_VOLTAGE_TEST_POINT_CHANNEL = "TP_LineOut0:1"  # physical channel = Sim_PC_basedDAQ/ai0:1

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\action_button_test_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    button_channel=BUTTON_CHANNEL,
    voltage_channel=DC_RMS_VOLTAGE_TEST_POINT_CHANNEL,
):
    """Creates the necessary objects for the simulation and measurement of the action button"""  

    # Create the instances of generation and measurement classes required for the test.
    button_instance = nipcbatt.DcVoltageGeneration()
    dc_rms_voltage_test_point = nipcbatt.DcRmsVoltageMeasurement()

    # Initialize Action Button
    """Initializes the configured channels of AO module to perform action button functionality"""
    button_instance.initialize(analog_output_channel_expression=button_channel)

    # Initialize TP
    """Initializes the configured channels of AI module to perform DC-RMS voltage measuerement"""
    dc_rms_voltage_test_point.initialize(analog_input_channel_expression=voltage_channel)

    return button_instance, dc_rms_voltage_test_point


####################################################################################################
# endregion initialize


# region configure_and_generate
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    button_instance: nipcbatt.DcVoltageGeneration,
    dc_rms_voltage_test_point: nipcbatt.DcRmsVoltageMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """If write_to_file is True, the Logger is used to output the results to a file.
    The Logger can be used to store configurations and outputs in a .txt or .csv file.
    The default file path is C:\\Windows\\Temp\\action_button_test_results.txt
    """  
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(button_instance)
        logger.attach(dc_rms_voltage_test_point)

    """Button ON Action"""

    # create a configuration that will generate 3.3V to simulate a button press
    button_configuration = nipcbatt.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=nipcbatt.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
        output_voltages=[3.3],  # ON voltage = 3.3V
    )

    """Note to run with Hardware: Update DC Voltage for Action Button ON condition  # noqa: W505 - doc line too long (176 > 100 characters) (auto-generated noqa)
       This step can be replaced with actual button action"""

    # Turn ON the simulated button using CONFIGURE_AND_GENERATE method
    button_instance.configure_and_generate(configuration=button_configuration)

    """To ensure the DUT can detect the action button changes, you can add
    a short software delay after the voltage is generated:"""

    # uncomment the next two lines to create a 100 millisecond delay after 3.3V signal is generated
    # import time
    # time.sleep(.1)

    # Acquire the data from the test points using CONFIGURE_AND_MEASURE (button should be on)
    test_point_result_data_after_button_on = dc_rms_voltage_test_point.configure_and_measure(
        configuration=nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
    )

    """Storing results -- create both a Python dictionary (hashmap)
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record intermediate result
    results_map["on"] = test_point_result_data_after_button_on

    """ Button OFF Action """
    """ Note to run with Hardware: Update DC Voltage for Action Button OFF condition 
        This step can be replaced with actual button action"""

    # Reconfigure the button object with 0V to prepare it to turn off in next step
    button_configuration = nipcbatt.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=nipcbatt.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
        output_voltages=[0.0],  # OFF voltage = 0V
    )

    # Run CONFIGURE_AND_GENERATE again with 0V setting to ensure the button is turned OFF
    button_instance.configure_and_generate(configuration=button_configuration)

    # Acquire the data from the test points again using CONFIGURE_AND_MEASURE (button should be off)
    test_point_result_data_after_button_off = dc_rms_voltage_test_point.configure_and_measure(
        configuration=nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
    )

    # record intermediate result
    results_map["off"] = test_point_result_data_after_button_off

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(button_instance, dc_rms_voltage_test_point):
    """Closes out the created objects used in the generation and measurement"""  
    button_instance.close()  # Close Action Button
    dc_rms_voltage_test_point.close()  # Close TP


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def action_button_test(
    button_channel=BUTTON_CHANNEL,
    voltage_channel=DC_RMS_VOLTAGE_TEST_POINT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  

    # Run setup function
    button, voltage_test_point = setup(button_channel, voltage_channel)

    # Run main function
    main(button, voltage_test_point, write_to_file, filepath)

    # Run cleanup function
    cleanup(button, voltage_test_point)


####################################################################################################
# endregion test 
