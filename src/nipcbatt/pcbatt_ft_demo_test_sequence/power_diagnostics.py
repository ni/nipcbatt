"""Power Diagnostics"""  

import os  
import sys  
from time import sleep 

import nidaqmx.constants
from limit_exception import ( 
    LimitException,
)

import nipcbatt


class PowerDiagnostics:  
    def __init__(self):  
        self.ps_task = None
        self.dc_voltage_meas_task = None

        self.setup()
        self.main()
        self.cleanup()

    def setup( 
        self,
    ) -> None:
        # Power up and Validate Start-up, Transition Max Current, Idle Power Consumption and DC Regulators  
        self.initialize_power_supply()
        self.initialize_dc_regulator_tps()

    def initialize_power_supply(  
        self,
    ) -> None:
        self.ps_task = nipcbatt.PowerSupplySourceAndMeasure()
        self.ps_task.initialize("Simulated_Power/power")

    def initialize_dc_regulator_tps( 
        self,
    ) -> None:
        self.dc_voltage_meas_task = nipcbatt.DcRmsVoltageMeasurement()
        self.dc_voltage_meas_task.initialize("TP_REG0:1")

    def main(self) -> None:   
        self.power_on_and_measure_startup_max_current()
        self.measure_idle_power_consumption()
        self.measure_dc_regulator_voltages()

    def power_on_and_measure_startup_max_current(   
        self,
    ) -> None:
        terminal_parameters = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
            voltage_setpoint_volts=6,
            current_setpoint_amperes=3,
            power_sense=nidaqmx.constants.Sense.REMOTE,
            idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE,
            enable_output=True,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
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

        configuration = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
            terminal_parameters=terminal_parameters,
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.ps_task.configure_and_measure(configuration=configuration)

        lower_limit = 0
        upper_limit = 1
        tested_value = result_data.max_current_level_amperes

        print("\n\n1. Power On & Maximum Current Measurement")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Fail  -- Measured current:", tested_value)
            print("Maximum current must be between 0.0 and 1.0 ", "\n")
        else:
            print("Status: Pass", "\n")

    def measure_idle_power_consumption(   
        self,
    ) -> None:
        terminal_parameters = nipcbatt.PowerSupplySourceAndMeasureTerminalParameters(
            voltage_setpoint_volts=6,
            current_setpoint_amperes=3,
            power_sense=nidaqmx.constants.Sense.REMOTE,
            idle_output_behaviour=nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE,
            enable_output=True,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
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

        configuration = nipcbatt.PowerSupplySourceAndMeasureConfiguration(
            terminal_parameters=terminal_parameters,
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.ps_task.configure_and_measure(configuration=configuration)

        lower_limit = 4.5
        upper_limit = 5.5
        tested_value = result_data.average_power_value_watts

        print("2. Measure Idle Power Consumption")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Fail -- Measured power:", tested_value)
            print("Average power value must be between 4.5 and 5.5 watts", "\n")
        else:
            print("Status: Pass", "\n")

    def measure_dc_regulator_voltages( 
        self,
    ) -> None:
        global_channel_parameters = nipcbatt.VoltageRangeAndTerminalParameters(
            terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
            range_min_volts=-10,
            range_max_volts=10,
        )

        measurement_options = nipcbatt.MeasurementOptions(
            execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
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

        configuration = nipcbatt.DcRmsVoltageMeasurementConfiguration(
            global_channel_parameters=global_channel_parameters,
            specific_channels_parameters=[],
            measurement_options=measurement_options,
            sample_clock_timing_parameters=sample_clock_timing_parameters,
            digital_start_trigger_parameters=digital_start_trigger_parameters,
        )

        result_data = self.dc_voltage_meas_task.configure_and_measure(configuration=configuration)

        lower_limit = 4.9
        upper_limit = 5.2
        tested_value = result_data.dc_values_volts[0]

        print("\n\n3. Measure DC Regulator Voltages")

        print("TP_REG0:")
        if tested_value < lower_limit or tested_value > upper_limit:
            print("Status: Fail -- Measured voltage:", tested_value)
            print("TP_REG0 must be between 4.9 and 5.2 volts", "\n")
        else:
            print("Status: Pass", "\n")

        lower_limit = 3.1
        upper_limit = 3.4
        tested_value = result_data.dc_values_volts[1]

        print("TP_REG1:")
        if tested_value < lower_limit or tested_value > upper_limit:
            if tested_value < lower_limit or tested_value > upper_limit:
                print("Status: Fail -- Measured voltage:", tested_value)
                print("TP_REG1 must be between 3.1 and 3.4 volts", "\n")
            else:
                print("Status: Pass", "\n")

    def cleanup(   
        self,
    ) -> None:
        self.close_power_supply()
        self.close_dc_regulators_meas()

    def close_power_supply(   
        self,
    ) -> None:
        self.ps_task.close()

    def close_dc_regulators_meas(   
        self,
    ) -> None:
        self.dc_voltage_meas_task.close()
