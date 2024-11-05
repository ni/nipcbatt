""" Constants data types for Voltage Measurements."""

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (
    MeasurementAnalysisRequirement,
    MeasurementExecutionType,
    SampleTimingEngine,
    StartTriggerType,
)


class ConstantsForVoltageMeasurement:
    """Constants used for Voltage measurement"""

    INITIAL_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.DEFAULT
    INITIAL_VOLTAGE_MINIMUM_VALUE_VOLTS = -10.0
    INITIAL_VOLTAGE_MAXIMUM_VALUE_VOLTS = 10.0
    INITIAL_AI_VOLTAGE_UNITS = nidaqmx.constants.VoltageUnits.VOLTS

    DEFAULT_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_VOLTAGE_MINIMUM_VALUE_VOLTS = -10.0
    DEFAULT_VOLTAGE_MAXIMUM_VALUE_VOLTS = 10.0

    DEFAULT_EXECUTION_TYPE = MeasurementExecutionType.CONFIGURE_AND_MEASURE
    DEFAULT_MEASUREMENT_ANALYSIS_REQUIREMENT = MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 10000
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 1000
    DEFAULT_SAMPLE_TIMING_ENGINE = SampleTimingEngine.AUTO

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING
