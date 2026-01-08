# pylint: disable=C0301
""" Constants data types for Temperature measurements."""
import dataclasses

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    MeasurementExecutionType,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_data_types import (
    BetaCoefficientAndSensorResistanceParameters,
    CoefficientsSteinhartHartParameters,
    SteinhartHartEquationOption,
    TemperatureRtdMeasurementConfiguration,
    TemperatureRtdMeasurementTerminalParameters,
    TemperatureThermistorMeasurementConfiguration,
    TemperatureThermistorRangeAndTerminalParameters,
    TemperatureThermocoupleMeasurementConfiguration,
    TemperatureThermocoupleMeasurementTerminalParameters,
)


@dataclasses.dataclass
class ConstantsForTemperatureMeasurement:
    """Constants used for Temperature measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)

    INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES = 0.0
    INITIAL_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES = 100.0
    INITIAL_AI_TEMPERATURE_UNITS = nidaqmx.constants.TemperatureUnits.DEG_C

    DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES = 0.0
    DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES = 100.0

    DEFAULT_SAMPLE_CLOCK_SOURCE = "OnboardClock"
    DEFAULT_SAMPLING_RATE_HERTZ = 100
    DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL = 10
    DEFAULT_SAMPLE_TIMING_ENGINE = SampleTimingEngine.AUTO

    DEFAULT_TRIGGER_TYPE = StartTriggerType.NO_TRIGGER
    DEFAULT_DIGITAL_START_TRIGGER_SOURCE = ""
    DEFAULT_DIGITAL_START_TRIGGER_EDGE = nidaqmx.constants.Edge.RISING

    ABSOLUTE_ZERO_CELSIUS_DEGREES = -273.15


@dataclasses.dataclass
class ConstantsForTemperatureMeasurementUsingRtd:
    """Constants used for Temperature measurement using RTD"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

    INITIAL_CURRENT_EXCITATION_VALUE_AMPERES = 0.0025
    INITIAL_SENSOR_RESISTANCE_OHMS = 100.0
    INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES = 0.0
    INITIAL_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES = 100.0
    INITIAL_RTD_RESISTANCE_CONFIGURATION = nidaqmx.constants.ResistanceConfiguration.THREE_WIRE
    INITIAL_AI_TEMPERATURE_UNITS = nidaqmx.constants.TemperatureUnits.DEG_C
    INITIAL_RTD_EXCITATION_SOURCE = nidaqmx.constants.ExcitationSource.INTERNAL
    INITIAL_RTD_TYPE = nidaqmx.constants.RTDType.PT_3750

    DEFAULT_RTD_TYPE = nidaqmx.constants.RTDType.PT_3750
    DEFAULT_SENSOR_RESISTANCE_OHMS = 100.0
    DEFAULT_RESISTANCE_CONFIGURATION = nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE
    DEFAULT_EXCITATION_SOURCE = nidaqmx.constants.ExcitationSource.INTERNAL
    DEFAULT_CURRENT_EXCITATION_VALUE_AMPERES = 0.001
    DEFAULT_ADC_TIMING_MODE = nidaqmx.constants.ADCTimingMode.AUTOMATIC


@dataclasses.dataclass
class ConstantsForTemperatureMeasurementUsingThermistor:
    """Constants used for Temperature measurement using Thermistor"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)

    INITIAL_VOLTAGE_EXCITATION_VALUE_VOLTS = 2.5
    INITIAL_THERMISTOR_RESISTANCE_CONFIGURATION = (
        nidaqmx.constants.ResistanceConfiguration.FOUR_WIRE
    )
    INITIAL_THERMISTOR_EXCITATION_SOURCE = nidaqmx.constants.ExcitationSource.EXTERNAL

    INITIAL_COEFFICIENT_STAINHART_HART_A = 0.001295361
    INITIAL_COEFFICIENT_STAINHART_HART_B = 0.0002343159
    INITIAL_COEFFICIENT_STAINHART_HART_C = 1.018703e-7
    INITIAL_THERMISTOR_RESISTOR_OHMS = 5000.0

    DEFAULT_VOLTAGE_EXCITATION_VALUE_VOLTS = 5.0
    DEFAULT_THERMISTOR_RESISTOR_OHMS = 1000.0
    DEFAULT_AI_TERMINAL_CONFIGURATION = nidaqmx.constants.TerminalConfiguration.RSE
    DEFAULT_STEINHART_HART_EQUATION_OPTION = (
        SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS
    )

    DEFAULT_COEFFICIENT_STAINHART_HART_A = 0.0
    DEFAULT_COEFFICIENT_STAINHART_HART_B = 0.0
    DEFAULT_COEFFICIENT_STAINHART_HART_C = 0.0

    DEFAULT_COEFFICIENT_STAINHART_HART_BETA_KELVINS = 0
    DEFAULT_THERMISTOR_SENSOR_RESISTANCE_OHMS = 0.0

    THERMISTOR_REFERENCE_TEMPERATURE_KELVINS = 298.15


@dataclasses.dataclass
class ConstantsForTemperatureMeasurementUsingThermocouple:
    """Constants used for Temperature measurement using Thermocouple"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (182 > 100 characters) (auto-generated noqa)

    DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES = 0.0
    DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES = 100.0

    DEFAULT_THERMOCOUPLE_TYPE = nidaqmx.constants.ThermocoupleType.J
    DEFAULT_COLD_JUNCTION_COMPENSATION_TEMPERATURE = 25.00
    DEFAULT_COLD_JUNCTION_COMPENSATION_SOURCE = nidaqmx.constants.CJCSource.BUILT_IN
    INITIAL_COLD_JUNCTION_COMPENSATION_CHANNEL_NAME = ""

    DEFAULT_ENABLE_AUTOZERO = False
    DEFAULT_AUTOZERO_MODE = nidaqmx.constants.AutoZeroType.NONE


DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS = TemperatureRtdMeasurementTerminalParameters(
    temperature_minimum_value_celsius_degrees=(
        ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
    ),
    temperature_maximum_value_celsius_degrees=(
        ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
    ),
    current_excitation_value_amperes=(
        ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_CURRENT_EXCITATION_VALUE_AMPERES
    ),
    sensor_resistance_ohms=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_SENSOR_RESISTANCE_OHMS,
    rtd_type=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_RTD_TYPE,
    excitation_source=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_EXCITATION_SOURCE,
    resistance_configuration=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_RESISTANCE_CONFIGURATION,
    adc_timing_mode=ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_ADC_TIMING_MODE,
)

DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS = SampleClockTimingParameters(
    sample_clock_source=ConstantsForTemperatureMeasurement.DEFAULT_SAMPLE_CLOCK_SOURCE,
    sampling_rate_hertz=ConstantsForTemperatureMeasurement.DEFAULT_SAMPLING_RATE_HERTZ,
    number_of_samples_per_channel=(
        ConstantsForTemperatureMeasurement.DEFAULT_NUMBER_OF_SAMPLES_PER_CHANNEL
    ),
    sample_timing_engine=ConstantsForTemperatureMeasurement.DEFAULT_SAMPLE_TIMING_ENGINE,
)

DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS = DigitalStartTriggerParameters(
    trigger_select=ConstantsForTemperatureMeasurement.DEFAULT_TRIGGER_TYPE,
    digital_start_trigger_source=(
        ConstantsForTemperatureMeasurement.DEFAULT_DIGITAL_START_TRIGGER_SOURCE
    ),
    digital_start_trigger_edge=(
        ConstantsForTemperatureMeasurement.DEFAULT_DIGITAL_START_TRIGGER_EDGE
    ),
)

DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION = TemperatureRtdMeasurementConfiguration(
    global_channel_parameters=DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS,
    specific_channels_parameters=[],
    measurement_execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    sample_clock_timing_parameters=DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
    digital_start_trigger_parameters=DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
)

DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS = CoefficientsSteinhartHartParameters(
    coefficient_steinhart_hart_a=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_A
    ),
    coefficient_steinhart_hart_b=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_B
    ),
    coefficient_steinhart_hart_c=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_C
    ),
)

DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS = BetaCoefficientAndSensorResistanceParameters(
    coefficient_steinhart_hart_beta_kelvins=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_COEFFICIENT_STAINHART_HART_BETA_KELVINS
    ),
    sensor_resistance_ohms=(
        ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_THERMISTOR_SENSOR_RESISTANCE_OHMS
    ),
)

DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS = (
    TemperatureThermistorRangeAndTerminalParameters(
        terminal_configuration=(
            ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_AI_TERMINAL_CONFIGURATION
        ),
        temperature_minimum_value_celsius_degrees=(
            ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
        ),
        temperature_maximum_value_celsius_degrees=(
            ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
        ),
        voltage_excitation_value_volts=(
            ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_VOLTAGE_EXCITATION_VALUE_VOLTS
        ),
        thermistor_resistor_ohms=(
            ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_THERMISTOR_RESISTOR_OHMS
        ),
        steinhart_hart_equation_option=(
            ConstantsForTemperatureMeasurementUsingThermistor.DEFAULT_STEINHART_HART_EQUATION_OPTION
        ),
        coefficients_steinhart_hart_parameters=(DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS),
        beta_coefficient_and_sensor_resistance_parameters=(
            DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS
        ),
    )
)

DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION = (
    TemperatureThermistorMeasurementConfiguration(
        global_channel_parameters=(DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS),
        specific_channels_parameters=[],
        measurement_execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=(DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS),
        digital_start_trigger_parameters=(DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS),
    )
)

DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS = TemperatureThermocoupleMeasurementTerminalParameters(
    temperature_minimum_value_celsius_degrees=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
    ),
    temperature_maximum_value_celsius_degrees=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
    ),
    thermocouple_type=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_THERMOCOUPLE_TYPE
    ),
    cold_junction_compensation_temperature=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_COLD_JUNCTION_COMPENSATION_TEMPERATURE
    ),
    perform_auto_zero_mode=(
        ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_ENABLE_AUTOZERO
    ),
    auto_zero_mode=(ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_AUTOZERO_MODE),
)


DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION = (
    TemperatureThermocoupleMeasurementConfiguration(
        global_channel_parameters=DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS,
        specific_channels_parameters=[],
        measurement_execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        sample_clock_timing_parameters=DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
        digital_start_trigger_parameters=DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
    )
)
