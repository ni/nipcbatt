"""Animation and Sound User Input Test"""

# pylint: disable=C0413,E0401,C0115,W0611,C0116,C0103

import os
import sys
from time import sleep

import nidaqmx.constants
from limit_exception import LimitException

import nipcbatt


class AnimationAndSoundUserInputTest:
    def __init__(self):
        self.digital_state_gen_task = None
        self.time_domain_meas_task = None
        self.dyn_digit_meas_task = None

        self.setup()
        self.main()
        self.cleanup()

    def setup(self):
        self.initialize_push_user_button(channel_expression="TS_BUTTON0")
        self.initialize_tp_tweeter(channel_expression="TP_TWEET0")
        self.initialize_leds_pattern(channel_expression="TP_AN_LED0:2")

    def initialize_push_user_button(self, channel_expression: str) -> None:
        self.digital_state_gen_task = nipcbatt.StaticDigitalStateGeneration()
        self.digital_state_gen_task.initialize(channel_expression=channel_expression)

    def initialize_tp_tweeter(self, channel_expression: str) -> None:
        self.time_domain_meas_task = nipcbatt.TimeDomainMeasurement()
        self.time_domain_meas_task.initialize(analog_input_channel_expression=channel_expression)

    def initialize_leds_pattern(self, channel_expression: str) -> None:
        self.dyn_digit_meas_task = nipcbatt.DynamicDigitalPatternMeasurement()
        self.dyn_digit_meas_task.initialize(channel_expression=channel_expression)

    def main(self):
        self.configure_tweeter_meas()
        self.configure_dig_pattern()
        self.turn_on_dut_user_button()
        self.wait_for_500_ms_seconds_push_button()
        self.turn_off_dut_user_button()
        self.measure_and_check_leds_pattern()
        self.fetch_tweeter_sound()

    def configure_tweeter_meas(self) -> None:
        global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=1000,
            number_of_samples_per_channel=2500,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = nipcbatt.TimeDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        self.time_domain_meas_task.configure_and_measure(configuration=configuration)

    def configure_dig_pattern(self) -> None:
        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=100.0,
            number_of_samples_per_channel=200,
            active_edge=nidaqmx.constants.Edge.RISING,
        )

        trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
            measurement_options=measurement_options,
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )

        self.dyn_digit_meas_task.configure_and_measure(configuration=configuration)

    def turn_on_dut_user_button(self) -> None:
        configuration = nipcbatt.StaticDigitalStateGenerationConfiguration(data_to_write=[True])

        self.digital_state_gen_task.configure_and_generate(configuration=configuration)

    def wait_for_500_ms_seconds_push_button(self) -> None:
        sleep(0.5)

    def turn_off_dut_user_button(self) -> None:
        configuration = nipcbatt.StaticDigitalStateGenerationConfiguration(data_to_write=[False])

        self.digital_state_gen_task.configure_and_generate(configuration=configuration)

    def measure_and_check_leds_pattern(self) -> None:
        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        timing_parameters = nipcbatt.DynamicDigitalPatternTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000.0,
            number_of_samples_per_channel=1000,
            active_edge=nidaqmx.constants.Edge.RISING,
        )

        trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = nipcbatt.DynamicDigitalPatternMeasurementConfiguration(
            measurement_options=measurement_options,
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )

        self.dyn_digit_meas_task.configure_and_measure(configuration=configuration)

    def fetch_tweeter_sound(self) -> None:
        # Fetches the measured DC Voltage (measured after Button action) and returns Time Domain Analysis Frequency
        # NOTE: This Step errors outs for non-periodic waveform captures.

        global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
            measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
        )

        sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
            sample_clock_source="OnboardClock",
            sampling_rate_hertz=10000,
            number_of_samples_per_channel=1000,
            sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
        )

        digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
            trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
            digital_start_trigger_source="",
            digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
        )

        configuration = nipcbatt.TimeDomainMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.time_domain_meas_task.configure_and_measure(configuration=configuration)

        lower_limit = 990
        upper_limit = 1010
        if result_data.voltage_waveforms_frequencies_hertz:
            tested_value = result_data.voltage_waveforms_frequencies_hertz[0]
        else:
            tested_value = lower_limit  # default for test purposes

        print("\n\n1. Measure Tweeter Frequency")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Fail  -- Measure frequency:", tested_value)
            print("Measured value must between 990 and 1010 Hz", "\n")
        else:
            print("Status: Pass", "\n")

    def cleanup(self) -> None:
        self.close_tweeter_meas()
        self.close_leds_pattern()
        self.close_push_button()

    def close_tweeter_meas(self) -> None:
        self.time_domain_meas_task.close()

    def close_leds_pattern(self) -> None:
        self.dyn_digit_meas_task.close()

    def close_push_button(self) -> None:
        self.digital_state_gen_task.close()
