"""Constants for default values for Power Supply Source Measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementExecutionType,
    MeasurementOptions,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_data_types import (
    PowerSupplySourceAndMeasureConfiguration,
    PowerSupplySourceAndMeasureTerminalParameters,
)


class ConstantsForPowerSupplySourceMeasurement:
    """Constants used for Power Supply measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

    INITIAL_VOLTAGE_SETPOINT_VOLTS = 0.0
    INITIAL_CURRENT_SETPOINT_AMPERES = 0.03
    INITIAL_OUTPUT_ENABLE = False

    DEFAULT_VOLTAGE_SETPOINT_VOLTS = 1.0
    DEFAULT_CURRENT_SETPOINT_AMPERES = 0.1
    DEFAULT_REMOTE_SENSE = nidaqmx.constants.Sense.LOCAL
    DEFAULT_IDLE_OUTPUT_BEHAVIOUR = nidaqmx.constants.PowerIdleOutputBehavior.OUTPUT_DISABLED
    DEFAULT_OUTPUT_ENABLE = True

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_AND_MEASURE
    DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT = MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 1000
    DEFAULT_SAMPLE_TIMING_ENGINE = SampleTimingEngine.AUTO

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING


DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS = PowerSupplySourceAndMeasureTerminalParameters(
    voltage_setpoint_volts=ConstantsForPowerSupplySourceMeasurement.DEFAULT_VOLTAGE_SETPOINT_VOLTS,
    current_setpoint_amperes=ConstantsForPowerSupplySourceMeasurement.DEFAULT_CURRENT_SETPOINT_AMPERES,
    power_sense=ConstantsForPowerSupplySourceMeasurement.DEFAULT_REMOTE_SENSE,
    idle_output_behaviour=ConstantsForPowerSupplySourceMeasurement.DEFAULT_IDLE_OUTPUT_BEHAVIOUR,
    enable_output=ConstantsForPowerSupplySourceMeasurement.DEFAULT_OUTPUT_ENABLE,
)

DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS = MeasurementOptions(
    execution_option=ConstantsForPowerSupplySourceMeasurement.DEFAULT_EXECUTION_TYPE,
    measurement_analysis_requirement=ConstantsForPowerSupplySourceMeasurement.DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT,
)

DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForPowerSupplySourceMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForPowerSupplySourceMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=ConstantsForPowerSupplySourceMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL,
    sample_timing_engine=ConstantsForPowerSupplySourceMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForPowerSupplySourceMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=ConstantsForPowerSupplySourceMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE,
    digital_start_trigger_edge=ConstantsForPowerSupplySourceMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE,
)

DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION = PowerSupplySourceAndMeasureConfiguration(
    terminal_parameters=DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS,
    measurement_options=DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS,
    sample_clock_timing_parameters=DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS,
)
