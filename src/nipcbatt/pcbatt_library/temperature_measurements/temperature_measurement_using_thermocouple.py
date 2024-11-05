"""Defines class used for temperature measurement using Thermocouple on PCB points."""

import nidaqmx.constants

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.temperature_measurements.temperature_constants import (
    ConstantsForTemperatureMeasurement,
    ConstantsForTemperatureMeasurementUsingThermocouple,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_data_types import (
    TemperatureThermocoupleChannelRangeAndTerminalParameters,
    TemperatureThermocoupleMeasurementConfiguration,
    TemperatureThermocoupleMeasurementTerminalParameters,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement import (
    TemperatureMeasurement,
)


class TemperatureMeasurementUsingThermocouple(TemperatureMeasurement):
    """Defines a way that allows you to perform Temperature measurements
    using Thermocouple on PCB points."""

    def initialize(
        self,
        channel_expression: str,
        cold_junction_compensation_channel: str,
        cold_junction_compensation_source=nidaqmx.constants.CJCSource.BUILT_IN,
    ):
        """Initializes the measurement with the specific channels
        Args:
            channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
            cold_junction_compensation_channel (str):
                Expression representing channel for cold junction compensation when 'cold_junction_compensation_source'
                is specified as 'nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL'.
            cold_junction_compensation_source (nidaqmx.constants.CJCSource):
                Specify the source for cold junction compensation: [CONSTANT_USER_VALUE, SCANNABLE_CHANNEL, BUILT_IN]
                Default value is set as BUILT_IN.
        """
        if self.is_task_initialized:
            return
        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for temperature measurement.
        if self.contains_only_global_virtual_channels(channel_expression=channel_expression):
            self.add_global_channels(global_channel_expression=channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMOCOUPLE)
        else:
            # Add the channel_expression to analog input temperature channel of the Daqmx task
            self.task.ai_channels.add_ai_thrmcpl_chan(
                physical_channel=channel_expression,
                name_to_assign_to_channel="",
                min_val=(
                    ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                ),
                max_val=(
                    ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                ),
                units=(ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS),
                thermocouple_type=(
                    ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_THERMOCOUPLE_TYPE
                ),
                cjc_source=cold_junction_compensation_source,
                cjc_val=(
                    ConstantsForTemperatureMeasurementUsingThermocouple.DEFAULT_COLD_JUNCTION_COMPENSATION_TEMPERATURE
                ),
                cjc_channel=cold_junction_compensation_channel,
            )

    def configure_and_measure(self, configuration: TemperatureThermocoupleMeasurementConfiguration):
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (TemperatureThermocoupleMeasurementConfiguration):
            A instance of `TemperatureThermocoupleMeasurementConfiguration`
            used to configure the measurement.

        Returns:
            TemperatureMeasurementResultData | None:
            An instance of `TemperatureMeasurementResultData`
            or `None` if no measure was performed.
        """
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

    def configure_all_channels(
        self, parameters: TemperatureThermocoupleMeasurementTerminalParameters
    ):
        """Configures all channels used for temperature measurements using a Thermocouple.

        Args:
            parameters (TemperatureThermocoupleMeasurementTerminalParameters):
            An instance of `TemperatureThermocoupleMeasurementTerminalParameters`
            used to configure the channels.
        """
        for channel in self.task.ai_channels:
            channel.ai_min = parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.temperature_maximum_value_celsius_degrees
            channel.ai_thrmcpl_type = parameters.thermocouple_type
            channel.ai_thrmcpl_cjc_val = parameters.cold_junction_compensation_temperature
            if parameters.perform_auto_zero_mode is True:
                channel.ai_auto_zero_mode = parameters.auto_zero_mode

    def configure_specific_channel(
        self, parameters: TemperatureThermocoupleChannelRangeAndTerminalParameters
    ):
        """Configures the specific channels used for temperature measurements using a Thermocouple.

        Args:
            parameters (TemperatureThermocoupleChannelRangeAndTerminalParameters):
            An instance of `TemperatureThermocoupleChannelRangeAndTerminalParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """

        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # updates the thermocouple parameters of the channel
            channel = self.task.ai_channels[parameters.channel_name]
            channel.ai_min = parameters.channel_parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.channel_parameters.temperature_maximum_value_celsius_degrees
            channel.ai_thrmcpl_type = parameters.channel_parameters.thermocouple_type
            channel.ai_thrmcpl_cjc_val = (
                parameters.channel_parameters.cold_junction_compensation_temperature
            )
            if parameters.channel_parameters.perform_auto_zero_mode is True:
                channel.ai_auto_zero_mode = parameters.channel_parameters.auto_zero_mode
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMOCOUPLE)
                for channel in self.task.ai_channels:
                    channel.ai_min = (
                        parameters.channel_parameters.temperature_minimum_value_celsius_degrees
                    )
                    channel.ai_max = (
                        parameters.channel_parameters.temperature_maximum_value_celsius_degrees
                    )
                    channel.ai_thrmcpl_type = parameters.channel_parameters.thermocouple_type
                    channel.ai_thrmcpl_cjc_val = (
                        parameters.channel_parameters.cold_junction_compensation_temperature
                    )
                    if parameters.channel_parameters.perform_auto_zero_mode is True:
                        channel.ai_auto_zero_mode = parameters.channel_parameters.auto_zero_mode
            else:
                # Physical channel
                channel = self.task.ai_channels.add_ai_thrmcpl_chan(
                    physical_channel=parameters.channel_name,
                    name_to_assign_to_channel="",
                    min_val=(
                        parameters.channel_parameters.temperature_minimum_value_celsius_degrees
                    ),
                    max_val=(
                        parameters.channel_parameters.temperature_maximum_value_celsius_degrees
                    ),
                    units=(ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS),
                    thermocouple_type=(parameters.channel_parameters.thermocouple_type),
                    cjc_source=parameters.channel_parameters.cold_junction_compensation_source,
                    cjc_val=(parameters.channel_parameters.cold_junction_compensation_temperature),
                    cjc_channel=parameters.channel_parameters.cold_junction_compensation_channel_name,
                )
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
