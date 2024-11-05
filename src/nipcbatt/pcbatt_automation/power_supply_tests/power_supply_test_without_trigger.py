"""This example demonstrates Power Supply source and Voltage Measurement without trigger"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (202 > 100 characters) (auto-generated noqa)

# pylint: disable=W0105,E0401

import nidaqmx.constants

import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

## Setup: Get the physical channels required for the test.

"""Note to run with Hardware: Update Virtual/Physical Channels Info based on 
   NI MAX in the below Initialize Steps"""

# Default channels
POWER_CHANNEL = "Simulated_power/power"
ANALOG_INPUT_CHANNEL = "TP_Power0:2"  # physical channel = Simulated_AI/ai0:2

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\power_supply_test_without_trigger_results.txt"


# region initialize
############################### INITIALIZATION FUNCTION ############################################


def setup(
    power_channel=POWER_CHANNEL,
    voltage_channel=ANALOG_INPUT_CHANNEL,
):
    """Creates the necessary objects for the generation and measurement of the power supply"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (282 > 100 characters) (auto-generated noqa)

    # Create the instances of generation and measurement classes required for the test.
    power_supply_test_source_instance = nipcbatt.PowerSupplySourceAndMeasure()
    analog_input_test_point_instance = nipcbatt.DcRmsVoltageMeasurement()

    # Initialize Power Supply
    """Initializes the configured channels of Power supply module"""
    power_supply_test_source_instance.initialize(power_channel_name=power_channel)

    # Initialize Test Point
    """Initializes the configured channels of AI module to perform Voltage measuerement"""
    analog_input_test_point_instance.initialize(analog_input_channel_expression=voltage_channel)

    return power_supply_test_source_instance, analog_input_test_point_instance


####################################################################################################
# endregion initialize


# region configure_and_measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(
    power_supply_test_source_instance: nipcbatt.PowerSupplySourceAndMeasure,
    analog_input_test_point_instance: nipcbatt.DcRmsVoltageMeasurement,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Note to run with Hardware: Review the configurations and update the trigger configurations"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (288 > 100 characters) (auto-generated noqa)

    """ If write_to_file is True, the Logger is used to output the results to a file.
        The Logger can be used to store configurations and outputs in a .txt or .csv file.
        The default file path is C:\\Windows\\Temp\\power_supply_test_with_trigger_results.txt"""
    if write_to_file:
        logger = PcbattLogger(filepath)
        logger.attach(power_supply_test_source_instance)
        logger.attach(analog_input_test_point_instance)

    ### Configure and measure VDD using 'PowerSupplySourceAndMeasureConfiguration'

    # initialize an instance of 'PowerSupplySourceAndMeasureTerminalParameters'
    gen_terminal_parameters = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
        voltage_setpoint_volts=5,
        current_setpoint_amperes=1,
        power_sense=nidaqmx.constants.Sense.LOCAL,
        idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE,
        enable_output=True,
    )

    # initialize an instance of 'MeasurementOptions'
    gen_measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # initialize an instance of 'SampleClockTimingParameters'
    gen_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    gen_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'PowerSupplySourceAndMeasureConfiguration'
    gen_result_data_after_configure_and_measure = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
        terminal_parameters=gen_terminal_parameters,
        measurement_options=gen_measurement_options,
        sample_clock_timing_parameters=gen_sample_clock_timing_parameters,
        digital_start_trigger_parameters=gen_digital_start_trigger_parameters,
    )

    # use the config object to execute configure_and_measure
    gen_result_data_after_configure_and_measure = (
        power_supply_test_source_instance.configure_and_measure(
            configuration=gen_result_data_after_configure_and_measure
        )
    )

    """Storing results -- create both a Python dictionary (hashmap)
    A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record intermediate result
    results_map["pssm_configure_and_measure"] = gen_result_data_after_configure_and_measure

    #### Configure and measure an instance of 'DcRmsVoltageMeasurementConfiguration'

    # initialize an an instance of 'MeasurementOptions'
    meas_measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    # intialize an instance of 'VoltageRangeAndTerminalParameters'
    meas_global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )

    # initialize an instance of 'List[VoltageMeasurementChannelAndTerminalRangeParameters]'
    meas_specific_channels_parameters = []

    # initialize an instance of 'SampleClockTimingParameters'
    meas_sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    # initialize an instance of 'DigitalStartTriggerParameters'
    meas_digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # initialize an instance of 'DcRmsVoltageMeasurementConfiguration'
    meas_measurement_config = nipcbatt.DcRmsVoltageMeasurementConfiguration(
        global_channel_parameters=meas_global_channel_parameters,
        specific_channels_parameters=meas_specific_channels_parameters,
        measurement_options=meas_measurement_options,
        sample_clock_timing_parameters=meas_sample_clock_timing_parameters,
        digital_start_trigger_parameters=meas_digital_start_trigger_parameters,
    )

    # use the config object to execute configure_and_measure
    meas_result_data_after_configuring = analog_input_test_point_instance.configure_and_measure(
        configuration=meas_measurement_config
    )

    # record intermediate result
    results_map["drvm_configure_and_measure"] = meas_result_data_after_configuring

    # return results
    return results_map


####################################################################################################
# endregion configure_and_generate

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    power_supply_test_source_instance: nipcbatt.PowerSupplySourceAndMeasure,
    analog_input_test_point_instance: nipcbatt.DcRmsVoltageMeasurement,
):
    """Closes out the created objects used in the generation and measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (190 > 100 characters) (auto-generated noqa)
    power_supply_test_source_instance.close()  # Close TS
    analog_input_test_point_instance.close()  # Close TP


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def power_supply_test_without_trigger(
    power_channel=POWER_CHANNEL,
    voltage_channel=ANALOG_INPUT_CHANNEL,
    write_to_file=True,
    filepath=DEFAULT_FILEPATH,
):
    """Execute all steps in the sequence"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (231 > 100 characters) (auto-generated noqa)

    # Run setup function
    gen, meas = setup(power_channel, voltage_channel)

    # Run main function
    main(gen, meas, write_to_file, filepath)

    # Run cleanup function
    cleanup(gen, meas)


####################################################################################################
# endregion test
