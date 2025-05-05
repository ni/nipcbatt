"""Demonstrates DC Voltage Generation using AO lines or Modules and Temprature
   measurement with Thermistor using AI lines or Modules of cDAQ"""  

import os
import sys

import nidaqmx
import numpy as np  

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)

"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
   in the below initialize step"""

# Default channels
OUTPUT_TERMINAL = "TS_THEX"
# Physical Channel name is Simulated_cDAQ_9263_ao0

INPUT_TERMINAL = "TP_TH0"
# Physical channel name is Simulated_cDAQ_9211/ai0

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Thermistor_test_cDAQ.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
def setup(
    output_terminal=OUTPUT_TERMINAL, input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH
):
    """Creates the necessary objects for DC voltage generation
    and the Temprature Measurement"""  

    # Create the instances of generation class required for the test
    drvg = nipcbatt.DcVoltageGeneration()

    """Initializes the channels for the drvg module to prepare 
       for DC voltage generation"""
    drvg.initialize(analog_output_channel_expression=output_terminal)
    # Creates the necessary instances of measurement class required for the test
    ttr = nipcbatt.TemperatureMeasurementUsingThermistor()

    # Initialize the measurement objective
    """Initializes the channels of ttr module to prepare for temprature
       measuremnt"""
    ttr.initialize(input_terminal)
    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(drvg)
    logger.attach(ttr)

    # returns initialized objects
    return drvg, ttr


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(  
    drvg: nipcbatt.DcVoltageGeneration,
    ttr: nipcbatt.TemperatureMeasurementUsingThermistor,
    input_terminal=INPUT_TERMINAL,
):
    results_map = {}  # this structure will hold results in key-value pairs

    """Set up the minimum and maximum range for the generation of voltage"""
    range_settings = nipcbatt.VoltageGenerationChannelParameters(
        range_min_volts=-10.0, range_max_volts=10.0
    )

    # Set the volatge that has to be generated
    output_voltages = [5.00]

    drvg_config = nipcbatt.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
    )

    # endregion drvg configure and generate

    drvg.configure_and_generate(drvg_config)

    # region TTR configure and measure

    # Set the parameters for the Thermistor
    coefficients_steinhart_hart_parameters = nipcbatt.CoefficientsSteinhartHartParameters(
        coefficient_steinhart_hart_a=1.29536e-3,
        coefficient_steinhart_hart_b=234.31590e-6,
        coefficient_steinhart_hart_c=101.87030e-9,
    )

    beta_coefficient_and_sensor_resistance_parameters = (
        nipcbatt.BetaCoefficientAndSensorResistanceParameters(
            coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
        )
    )

    global_channel_parameters = nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.DIFF,
        temperature_minimum_value_celsius_degrees=0,
        temperature_maximum_value_celsius_degrees=100,
        voltage_excitation_value_volts=5.0,
        thermistor_resistor_ohms=1000,
        steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
        coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters,
        beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters,
    )

    specific_channels_parameters = []

    # endregion specific_channels_parameters

    # Set the Sampling rate and the Number of Samples to read per channel as required
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

    ttr_config = nipcbatt.TemperatureThermistorMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion TTR configure and measure
    #################################################################################################### 

    ttr_result_data = ttr.configure_and_measure(configuration=ttr_config)

    # Set DC Voltage to 0 to turn off the DC voltage generation
    output_voltages = [0.0]

    drvg_config1 = nipcbatt.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=range_settings, output_voltages=output_voltages
    )

    drvg.configure_and_generate(drvg_config1)

    print("TTR result :\n")
    print(ttr_result_data)
    # close region
    # record results
    results_map["Thermistor data"] = ttr_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup( 
    drvg: nipcbatt.DcVoltageGeneration,
    ttr: nipcbatt.TemperatureMeasurementUsingThermistor,
):
    drvg.close()
    ttr.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def thermistor_test_cdaq(
    generation_output_channel=OUTPUT_TERMINAL,
    measurement_input_channel=INPUT_TERMINAL,
):
    """Execute all the steps in sequence"""  
    
    # Run the setup function
    drvg, ttr = setup(
        output_terminal=generation_output_channel,
        input_terminal=measurement_input_channel,
    )
    # Run the main function
    main(drvg, ttr, input_terminal=measurement_input_channel)
    # Run the cleanup function
    cleanup(drvg, ttr)


# endregion
