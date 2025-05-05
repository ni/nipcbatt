"""Demonstrates Analog PWM Signal Generation and Time Domain Measurement using 
   AO and AI channels or Modules""" 

import os
import sys

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
OUTPUT_TERMINAL = "TS_PWM_LED0"

INPUT_TERMINAL = "TP_PWM_LED0"

DIGITAL_TRIGGER_SOURCE = "/Sim_PC_basedDAQ/ao/StartTrigger"

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\Analog_PWM_Test.txt"


# Initialize Region
########################################   INITIALIZATION FUNCTION   ################################################################  # noqa: W505 - doc line too long (133 > 100 characters) (auto-generated noqa)
# Initialize region
def setup(
    output_terminal=OUTPUT_TERMINAL,
    input_terminal=INPUT_TERMINAL,
    file_path=DEFAULT_FILEPATH,
):
    """Creates necessary objects for the generation of Analog PWM siganl and
    Time Domain Measurement"""  
    # Creates instance of the generation class required for the test
    svg = nipcbatt.SignalVoltageGeneration()
    """Initializes the channels for signal volatge generaion"""
    svg.initialize(channel_expression=output_terminal)
    # Creates instance for the measurement class required for the test
    tdvm = nipcbatt.TimeDomainMeasurement()
    """Initializes the channels for tdvm module to prepare for measurement"""
    tdvm.initialize(analog_input_channel_expression=input_terminal)

    # Sets up the logger function
    logger = PcbattLogger(file_path)
    logger.attach(svg)
    logger.attach(tdvm)
    # returns the initialized objects
    return svg, tdvm


###############################################################################################################################################  # noqa: W505 - doc line too long (143 > 100 characters) (auto-generated noqa)
# end region initialize


# Region to configure and Generate/Measure
###################  MAIN TEST FUNCTION : CONFIGURE AND GENERATE/MEASURE ###########################
def main(  
    svg: nipcbatt.SignalVoltageGeneration,
    tdvm: nipcbatt.TimeDomainMeasurement,
    digital_trigger_source=DIGITAL_TRIGGER_SOURCE,
):
    results_map = {}  # this structure will hold results in key-value pairs

    # Set the maximum and minimum range for tdvm measurement
    global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )
    # Set the Sampling rate and the Number of Samples per Channel as required
    meas_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=1000,
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    specific_channels_parameters = []

    # Specify the Measurement Execution Type
    meas_config_configure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )
    # Set the Digital Trigger Type, Digital Trigger Source and Digital Trigger Edge
    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source=digital_trigger_source,
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    tdvm_config = nipcbatt.TimeDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=meas_config_configure_only,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion tdvm configure only
    tdvm.configure_and_measure(configuration=tdvm_config)

    # region configure SVG

    # Set the Signal Voltage generation range
    voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
        range_min_volts=-10, range_max_volts=10
    )
    # Set the Sampling rate hertz and the generated siganl duration
    gen_timing_parameters = nipcbatt.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100000,
        generated_signal_duration_seconds=0.1,
    )

    gen_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    # Set the PWM signal parameters
    waveform_parameters = nipcbatt.SignalVoltageGenerationSquareWaveParameters(
        generated_signal_amplitude_volts=0.5,
        generated_signal_duty_cycle_percent=80.00,
        generated_signal_frequency_hertz=100,
        generated_signal_phase_radians=0,
        generated_signal_offset_volts=0.5,
    )

    svg_config = nipcbatt.SignalVoltageGenerationSquareWaveConfiguration(
        voltage_generation_range_parameters=voltage_generation_range_parameters,
        waveform_parameters=waveform_parameters,
        timing_parameters=gen_timing_parameters,
        digital_start_trigger_parameters=gen_trigger_parameters,
    )

    # endregion
    svg.configure_and_generate_square_waveform(svg_config)

    # region tdvm measure only
    meas_options_measure_only = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    meas_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    tdvm_config = nipcbatt.TimeDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=meas_options_measure_only,
        sample_clock_timing_parameters=meas_timing_parameters,
        digital_start_trigger_parameters=meas_trigger_parameters,
    )

    # endregion tdvm configure and measure
    #################################################################################################### 
    # end region configure and measure
    tdvm_result_data = tdvm.configure_and_measure(configuration=tdvm_config)

    print("TDVM result :\n")
    print(tdvm_result_data)
    # record results
    results_map["TDVM data"] = tdvm_result_data

    # return results
    return results_map


# region close


############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################
# Close all tasks
def cleanup(  
    svg: nipcbatt.SignalVoltageGeneration,
    tdvm: nipcbatt.TimeDomainMeasurement,
):
    svg.close()
    tdvm.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def analog_pwm_test(
    generation_output_channel=OUTPUT_TERMINAL,
    measurement_input_channel=INPUT_TERMINAL,
    trigger_source=DIGITAL_TRIGGER_SOURCE,
):
    """Executes all steps in the sequence"""  

    # Runs the Setup Function
    svg, tdvm = setup(
        output_terminal=generation_output_channel,
        input_terminal=measurement_input_channel,
    )
    # Runs the Main Function
    main(svg, tdvm, digital_trigger_source=trigger_source)
    # Runs the cleanup Function
    cleanup(svg, tdvm)


# endregion test
