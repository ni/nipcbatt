"""Defines class used for temperature measurement using RTD on PCB points."""

import nidaqmx
import nidaqmx.constants
import nidaqmx.stream_readers

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.temperature_measurements.temperature_constants import (
    ConstantsForTemperatureMeasurement,
    ConstantsForTemperatureMeasurementUsingRtd,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_data_types import (
    TemperatureRtdMeasurementChannelParameters,
    TemperatureRtdMeasurementConfiguration,
    TemperatureRtdMeasurementTerminalParameters,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement import (
    TemperatureMeasurement,
)


class TemperatureMeasurementUsingRtd(TemperatureMeasurement):
    """Defines a way that allows you to perform Temperature measurements using RTD on PCB points."""

    def initialize(self, channel_expression: str):
        """Initializes the measurement with the specific channels

        Args:
            channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for current measurement.
        if self.contains_only_global_virtual_channels(channel_expression=channel_expression):
            self.add_global_channels(global_channel_expression=channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_RTD)
        else:
            # Add the channel_expression to analog input current channel of the Daqmx task
            self.task.ai_channels.add_ai_rtd_chan(
                physical_channel=channel_expression,
                name_to_assign_to_channel="",
                min_val=(
                    ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                ),
                max_val=(
                    ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                ),
                units=ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS,
                rtd_type=ConstantsForTemperatureMeasurementUsingRtd.INITIAL_RTD_TYPE,
                resistance_config=(
                    ConstantsForTemperatureMeasurementUsingRtd.INITIAL_RTD_RESISTANCE_CONFIGURATION
                ),
                current_excit_source=(
                    ConstantsForTemperatureMeasurementUsingRtd.INITIAL_RTD_EXCITATION_SOURCE
                ),
                current_excit_val=(
                    ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_CURRENT_EXCITATION_VALUE_AMPERES
                ),
                r_0=ConstantsForTemperatureMeasurementUsingRtd.INITIAL_SENSOR_RESISTANCE_OHMS,
            )

    def configure_and_measure(self, configuration: TemperatureRtdMeasurementConfiguration):
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

    def configure_all_channels(self, parameters: TemperatureRtdMeasurementTerminalParameters):
        """Configures all channels used for temperature measurements using RTD.

        Args:
            parameters (TemperatureRtdMeasurementTerminalParameters):
            An instance of `TemperatureRtdMeasurementTerminalParameters`
            used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        self.task.ai_channels.all.ai_adc_timing_mode = parameters.adc_timing_mode
        for channel in self.task.ai_channels:
            channel.ai_min = parameters.temperature_minimum_value_celsius_degrees
            channel.ai_max = parameters.temperature_maximum_value_celsius_degrees
            channel.ai_rtd_type = parameters.rtd_type
            channel.ai_rtd_r0 = parameters.sensor_resistance_ohms
            channel.ai_excit_src = parameters.excitation_source
            channel.ai_excit_val = parameters.current_excitation_value_amperes
            channel.ai_excit_voltage_or_current = (
                nidaqmx.constants.ExcitationVoltageOrCurrent.USE_CURRENT
            )
            channel.ai_resistance_cfg = parameters.resistance_configuration

    def configure_specific_channel(self, parameters: TemperatureRtdMeasurementChannelParameters):
        """Configures the specific channels used for temperature measurements using RTD.

        Args:
            parameters (TemperatureRtdMeasurementChannelParameters):
            An instance of `TemperatureRtdMeasurementChannelParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # updates the voltage parameters of the channel
            self.task.ai_channels[parameters.channel_name].ai_rtd_type = parameters.rtd_type
            self.task.ai_channels[
                parameters.channel_name
            ].ai_rtd_r0 = parameters.sensor_resistance_ohms
            self.task.ai_channels[
                parameters.channel_name
            ].ai_resistance_cfg = parameters.resistance_configuration
            self.task.ai_channels[
                parameters.channel_name
            ].ai_excit_src = parameters.excitation_source
            self.task.ai_channels[
                parameters.channel_name
            ].ai_excit_val = parameters.current_excitation_value_amperes
            self.task.ai_channels[
                parameters.channel_name
            ].ai_excit_voltage_or_current = nidaqmx.constants.ExcitationVoltageOrCurrent.USE_CURRENT
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.TEMPERATURE_RTD)
                for channel in self.task.ai_channels:
                    channel.ai_min = (
                        ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                    )
                    channel.ai_max = (
                        ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                    )
                    channel.ai_rtd_type = parameters.rtd_type
                    channel.ai_rtd_r0 = parameters.sensor_resistance_ohms
                    channel.ai_excit_src = parameters.excitation_source
                    channel.ai_excit_val = parameters.current_excitation_value_amperes
                    channel.ai_excit_voltage_or_current = (
                        nidaqmx.constants.ExcitationVoltageOrCurrent.USE_CURRENT
                    )
                    channel.ai_resistance_cfg = parameters.resistance_configuration
                    channel.ai_adc_timing_mode = (
                        ConstantsForTemperatureMeasurementUsingRtd.DEFAULT_ADC_TIMING_MODE
                    )

            else:
                # Physical channel
                self.task.ai_channels.add_ai_rtd_chan(
                    physical_channel=parameters.channel_name,
                    name_to_assign_to_channel="",
                    min_val=(
                        ConstantsForTemperatureMeasurement.INITIAL_TEMPERATURE_MINIMUM_VALUE_CELSIUS_DEGREES
                    ),
                    max_val=(
                        ConstantsForTemperatureMeasurement.DEFAULT_TEMPERATURE_MAXIMUM_VALUE_CELSIUS_DEGREES
                    ),
                    units=ConstantsForTemperatureMeasurement.INITIAL_AI_TEMPERATURE_UNITS,
                    rtd_type=parameters.rtd_type,
                    resistance_config=parameters.resistance_configuration,
                    current_excit_source=parameters.excitation_source,
                    current_excit_val=parameters.current_excitation_value_amperes,
                    r_0=parameters.sensor_resistance_ohms,
                )
