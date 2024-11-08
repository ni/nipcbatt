"""Demonstrates Voltage Generation using Power Module and Temprature 
   measurement with Thermistor using AI lines or Modules of Testscale"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (365 > 100 characters) (auto-generated noqa)

import os
import sys

import nidaqmx
import numpy as np  # noqa: F401 - 'numpy as np' imported but unused (auto-generated noqa)

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

parent_folder = os.getcwd()
utils_folder = os.path.join(parent_folder, "Utils")
sys.path.append(utils_folder)


"""Note to run with Hardware: Update the Terminal Channel names based on NI MAX
   in the below initialize step"""

# Default channels
OUTPUT_TERMINAL = "Simulated_Power/power"

INPUT_TERMINAL = "TP_TH2"
# Physical channel name is "Simulated_TS1_AI/ai0"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Thermistor_test_TestScale.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
def setup(
    output_terminal=OUTPUT_TERMINAL, input_terminal=INPUT_TERMINAL, file_path=DEFAULT_FILEPATH
):
    """Creates the necessary objects for voltage generation
    and the Temprature Measurement"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (330 > 100 characters) (auto-generated noqa)
    # Create the instances of generation class required for the test
    pssm = nipcbatt.PowerSupplySourceAndMeasure()

    """Initializes the channels for the pssm module to prepare 
       for voltage generation"""
    pssm.initialize(output_terminal)
    # Creates the necessary instances of measurement class required for the test
    ttr = nipcbatt.TemperatureMeasurementUsingThermistor()
    """Initializes the channels of ttr module to prepare for temprature
       measuremnt"""
    ttr.initialize(input_terminal)

    # Sets the logger Function
    logger = PcbattLogger(file_path)
    logger.attach(pssm)
    logger.attach(ttr)
    # returns initialized objects
    return pssm, ttr


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    pssm: nipcbatt.PowerSupplySourceAndMeasure,
    ttr: nipcbatt.TemperatureMeasurementUsingThermistor,
    input_terminal=INPUT_TERMINAL,
):
    results_map = {}  # this structure will hold results in key-value pairs

    """Sets up the volatge and current to be generated and whether
    to enable the output or not"""
    terminal_parameters = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
        voltage_setpoint_volts=5.0,
        current_setpoint_amperes=0.1,
        power_sense=nidaqmx.constants.Sense.LOCAL,
        idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED,  # Disable power output when idle
        enable_output=True,
    )

    measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )
    # Set the Sampling rate and the Number of Samples to per channel as required
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

    pssm.configure_and_measure(configuration=pssm_config)

    # region TTR configure and measure

    # Set the parameters for Thermistor
    coefficients_steinhart_hart_parameters = nipcbatt.CoefficientsSteinhartHartParameters(
        coefficient_steinhart_hart_a=0,
        coefficient_steinhart_hart_b=0,
        coefficient_steinhart_hart_c=0,
    )

    beta_coefficient_and_sensor_resistance_parameters = (
        nipcbatt.BetaCoefficientAndSensorResistanceParameters(
            coefficient_steinhart_hart_beta_kelvins=3720, sensor_resistance_ohms=10000
        )
    )

    global_channel_parameters = nipcbatt.TemperatureThermistorRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        temperature_minimum_value_celsius_degrees=0,
        temperature_maximum_value_celsius_degrees=100,
        voltage_excitation_value_volts=5,
        thermistor_resistor_ohms=1000,
        steinhart_hart_equation_option=nipcbatt.SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE,
        coefficients_steinhart_hart_parameters=coefficients_steinhart_hart_parameters,
        beta_coefficient_and_sensor_resistance_parameters=beta_coefficient_and_sensor_resistance_parameters,
    )

    # region specific_channels_parameters
    specific_channels_parameters = []

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
    ####################################################################################################  # noqa: W505 - doc line too long (104 > 100 characters) (auto-generated noqa)

    ttr_result_data = ttr.configure_and_measure(configuration=ttr_config)

    print("TTR result :\n")
    print(ttr_result_data)
    # close region
    # record results
    results_map["Thermistor data"] = ttr_result_data

    # return results
    return results_map


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    ttr: nipcbatt.TemperatureMeasurementUsingThermistor, pssm: nipcbatt.PowerSupplySourceAndMeasure
):
    ttr.close()
    pssm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def thermistor_test_testscale(
    generation_output_channel=OUTPUT_TERMINAL, measurement_input_channel=INPUT_TERMINAL
):
    """Execute all the steps in sequence"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)
    # Runs the Setup function
    pssm, ttr = setup(
        output_terminal=generation_output_channel,
        input_terminal=measurement_input_channel,
    )
    # Runs the main function
    main(pssm, ttr, input_terminal=measurement_input_channel)
    # Runs the cleanup function
    cleanup(ttr, pssm)


# endregion
