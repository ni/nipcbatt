# pylint: disable=C0301
# remove it when arguments of initialize are used.
"""Defines class used for temperature measurement using Thermistor on PCB points."""

import math

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.temperature_measurements.temperature_constants import (
    ConstantsForTemperatureMeasurement,
    ConstantsForTemperatureMeasurementUsingThermistor,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_data_types import (
    CoefficientsSteinhartHartParameters,
    SteinhartHartEquationOption,
    TemperatureThermistorChannelRangeAndTerminalParameters,
    TemperatureThermistorMeasurementConfiguration,
    TemperatureThermistorRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement import (
    TemperatureMeasurement,
)
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class TemperatureMeasurementUsingThermistor(TemperatureMeasurement):
    """Defines a way that allows you to perform Temperature measurements
    using Thermistor on PCB points."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (331 > 100 characters) (auto-generated noqa)

    def initialize(self, channel_expression: str):
        """Initializes the measurement with the specific channels
        Args:
            channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for current measurement.
        if self.contains_only_global_virtual_channels(channel_expression=channel_expression):
            self.add_global_channels(global_channel_expression=channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMISTOR)
        else:
            # Add the channel_expression to analog input current channel of the Daqmx task
            self.task.ai_channels.add_ai_thrmstr_chan_vex(
                physical_channel=channel_expression,
                name_to_assign_to_channel="",
                min_val=(
                    ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                ),
                max_val=(
                    ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                ),
                units=ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS,
                resistance_config=(
                    ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_RESISTANCE_CONFIGURATION
                ),
                voltage_excit_source=(
                    ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_EXCITATION_SOURCE
                ),
                voltage_excit_val=(
                    ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_VOLTAGE_EXCITATION_VALUE_VOLTS
                ),
                a=ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_COEFFICIENT_STAINHART_HART_A,
                b=ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_COEFFICIENT_STAINHART_HART_B,
                c=ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_COEFFICIENT_STAINHART_HART_C,
                r_1=ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_RESISTOR_OHMS,
            )

    def configure_and_measure(self, configuration: TemperatureThermistorMeasurementConfiguration):
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (TemperatureRtdMeasurementConfiguration):
            A instance of `TemperatureRtdMeasurementConfiguration`
            used to configure the measurement.

        Returns:
            TemperatureMeasurementResultData | None:
            An instance of `TemperatureMeasurementResultData`
            or `None` if no measure was performed.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if configuration.measurement_execution_type in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.configure_all_channels(configuration.global_channel_parameters)
            for specific_channel_parameters in configuration.specific_channels_parameters:
                self.configure_specific_channel(specific_channel_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_execution_type in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(data)

        return None

    def configure_all_channels(self, parameters: TemperatureThermistorRangeAndTerminalParameters):
        """Configures all channels used for temperature measurements using a Thermistor.

        Args:
            parameters (TemperatureThermistorRangeAndTerminalParameters):
            An instance of `TemperatureThermistorRangeAndTerminalParameters`
            used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        for channel in self.task.ai_channels:
            channel.ai_min = parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.temperature_maximum_value_celsius_degrees
            channel.ai_term_cfg = parameters.terminal_configuration
            channel.ai_thrmstr_r1 = parameters.thermistor_resistor_ohms
            channel.ai_excit_val = parameters.voltage_excitation_value_volts
            stainhart_hart_coefficients = self._compute_steinhart_hart_coefficients_from_parameters(
                parameters
            )
            channel.ai_thrmstr_a = stainhart_hart_coefficients.coefficient_steinhart_hart_a
            channel.ai_thrmstr_b = stainhart_hart_coefficients.coefficient_steinhart_hart_b
            channel.ai_thrmstr_c = stainhart_hart_coefficients.coefficient_steinhart_hart_c

    def configure_specific_channel(
        self, parameters: TemperatureThermistorChannelRangeAndTerminalParameters
    ):
        """Configures the specific channels used for temperature measurements using a Thermistor.

        Args:
            parameters (TemperatureThermistorChannelRangeAndTerminalParameters):
            An instance of `TemperatureThermistorChannelRangeAndTerminalParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        stainhart_hart_coefficients = self._compute_steinhart_hart_coefficients_from_parameters(
            parameters.channel_parameters
        )
        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # updates the voltage parameters of the channel
            channel = self.task.ai_channels[parameters.channel_name]
            channel.ai_min = parameters.channel_parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.channel_parameters.temperature_maximum_value_celsius_degrees
            channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
            channel.ai_excit_val = parameters.channel_parameters.voltage_excitation_value_volts
            channel.ai_thrmstr_r1 = parameters.channel_parameters.thermistor_resistor_ohms
            channel.ai_thrmstr_a = stainhart_hart_coefficients.coefficient_steinhart_hart_a
            channel.ai_thrmstr_b = stainhart_hart_coefficients.coefficient_steinhart_hart_b
            channel.ai_thrmstr_c = stainhart_hart_coefficients.coefficient_steinhart_hart_c
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMISTOR)
                for channel in self.task.ai_channels:
                    channel.ai_min = (
                        parameters.channel_parameters.temperature_minimum_value_celsius_degrees
                    )
                    channel.ai_max = (
                        parameters.channel_parameters.temperature_maximum_value_celsius_degrees
                    )
                    channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
                    channel.ai_thrmstr_r1 = parameters.channel_parameters.thermistor_resistor_ohms
                    channel.ai_excit_val = (
                        parameters.channel_parameters.voltage_excitation_value_volts
                    )
                    channel.ai_thrmstr_a = stainhart_hart_coefficients.coefficient_steinhart_hart_a
                    channel.ai_thrmstr_b = stainhart_hart_coefficients.coefficient_steinhart_hart_b
                    channel.ai_thrmstr_c = stainhart_hart_coefficients.coefficient_steinhart_hart_c

            else:
                # physical channel
                channel = self.task.ai_channels.add_ai_thrmstr_chan_vex(
                    physical_channel=parameters.channel_name,
                    name_to_assign_to_channel="",
                    min_val=(
                        parameters.channel_parameters.temperature_minimum_value_celsius_degrees
                    ),
                    max_val=(
                        parameters.channel_parameters.temperature_maximum_value_celsius_degrees
                    ),
                    units=ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS,
                    resistance_config=(
                        ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_RESISTANCE_CONFIGURATION
                    ),
                    voltage_excit_source=(
                        ConstantsForTemperatureMeasurementUsingThermistor.INITIAL_THERMISTOR_EXCITATION_SOURCE
                    ),
                    voltage_excit_val=(
                        parameters.channel_parameters.voltage_excitation_value_volts
                    ),
                    a=stainhart_hart_coefficients.coefficient_steinhart_hart_a,
                    b=stainhart_hart_coefficients.coefficient_steinhart_hart_b,
                    c=stainhart_hart_coefficients.coefficient_steinhart_hart_c,
                    r_1=parameters.channel_parameters.thermistor_resistor_ohms,
                )
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration

    def _compute_steinhart_hart_coefficients_from_parameters(
        self, parameters: TemperatureThermistorRangeAndTerminalParameters
    ) -> CoefficientsSteinhartHartParameters:
        if (
            parameters.steinhart_hart_equation_option
            == SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS
        ):
            return parameters.coefficients_steinhart_hart_parameters

        return self._compute_steinhart_hart_coefficients(
            parameters.beta_coefficient_and_sensor_resistance_parameters.coefficient_steinhart_hart_beta_kelvins,
            parameters.beta_coefficient_and_sensor_resistance_parameters.sensor_resistance_ohms,
        )

    def _compute_steinhart_hart_coefficients(
        self,
        coefficient_steinhart_hart_beta_kelvins: float,
        sensor_resistance_ohms: float,
    ) -> CoefficientsSteinhartHartParameters:
        """Computes coefficients of Steinhart-Hart equation."""
        return CoefficientsSteinhartHartParameters(
            coefficient_steinhart_hart_a=invert_value(
                ConstantsForTemperatureMeasurementUsingThermistor.THERMISTOR_REFERENCE_TEMPERATURE_KELVINS
            )
            - invert_value(coefficient_steinhart_hart_beta_kelvins)
            * math.log(sensor_resistance_ohms),
            coefficient_steinhart_hart_b=invert_value(coefficient_steinhart_hart_beta_kelvins),
            coefficient_steinhart_hart_c=0,
        )
