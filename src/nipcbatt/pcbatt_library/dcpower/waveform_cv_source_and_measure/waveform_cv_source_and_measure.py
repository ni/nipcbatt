"""Defines class used for DC constant voltage source and measurement on PCB points."""

import math

import nidcpower

from nipcbatt.pcbatt_library.common.helper_functions import (
    format_with_si_prefix as _si_notation,
)

from nipcbatt.pcbatt_library.dcpower.common.helper_functions import (
    generate_pulse_current_sequence,
)

from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    DCVoltageSourceAndMeasureResultData,
    EffectiveExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDCPower,
)


class DCVoltageSourceAndMeasure(BuildingBlockUsingNIDCPower):
    """Defines a way that allows you to source DC voltage and perform measurements on PCB points."""

    def initialize(self, resource_name: str):
        """Initializes the NI DC Power session with the specified resource.

        Opens a new NI-DCPower session, resets the channel, configures
        the source mode to single-point, and sets the output function to DC voltage.

        Args:
            resource_name (str):
                The resource name of the NI-DCPower instrument (e.g., "PPS1/0").
        """
        self._resource_name = resource_name
        # Open the NI-DCPower session for the given resource
        self._instrument = nidcpower.Session(resource_name=self._resource_name)

        self._channel_name = self.session.get_channel_names(0)[0]
        self.session.channels[self._channel_name].reset()
        self.session.channels[self._channel_name].source_mode = nidcpower.SourceMode.SINGLE_POINT
        self.session.channels[self._channel_name].output_function = (
            nidcpower.OutputFunction.DC_VOLTAGE
        )

    def close(self):
        """Closes the NI DC Power session and releases internal resources.

        Resets the specified channel(s) to a known state before closing the session.
        """
        if self.is_session_initialized:
            self.session.channels[self._channel_name].reset()
            self.session.close()
            self._instrument = None

    def configure_and_measure(
        self, configuration: DCVoltageSourceAndMeasureParameters
    ) -> DCVoltageSourceAndMeasureResultData:
        """Configures and/or performs a DC voltage source and measurement operation.

        Behavior is controlled by the ``execution_settings`` :
        - CONFIGURE_ONLY
        - CONFIGURE_SOURCE_AND_MEASURE
        - START_SOURCE_ONLY
        - MEASURE_ONLY

        Args:
            configuration (DCVoltageSourceAndMeasureParameters):
                An instance of ``DCVoltageSourceAndMeasureParameters`` containing
                voltage channel settings, timing parameters, trigger parameters,
                and the execution settings.

        Returns:
            DCVoltageSourceAndMeasureResultData: An instance containing the applied
                hardware execution settings and measurement results.
        """
        effective_execution_settings = {
            "Pulse On Time": math.nan,
            "Pulse Off Time": math.nan,
            "Pulse Bias Delay": math.nan,
            "Pulse Current Level Range": math.nan,
            "Pulse Bias Current Level": math.nan,
            "Pulse Voltage Limit": math.nan,
            "Pulse Voltage Limit Range": math.nan,
            "Pulse Bias Voltage Limit": math.nan,
            "Output Function": self.session.channels[self._channel_name].output_function.name,
            "Aperture Time (Sec)": math.nan,
            "Transient Response": self.session.channels[self._channel_name].transient_response.name,
            "Voltage Gain Bandwidth": math.nan,
            "Voltage Compensation Frequency": math.nan,
            "Voltage Pole Zero Ratio": math.nan,
            "Current Gain Bandwidth": math.nan,
            "Current Compensation Frequency": math.nan,
            "Current Pole Zero Ratio": math.nan,
            "Last Point Current (A)": math.nan,
            "Number of Points": math.nan,
            "Device Model": ""            
        }
        measurement_results = {
            "In Compliance": list(bool()),
            "Current Measurements": list(float()),
            "Voltage Measurements": list(float()),
            "Power Measurements": list(float()),
        }

        # Apply channel, timing, and trigger settings for CONFIGURE_ONLY or
        # CONFIGURE_SOURCE_AND_MEASURE
        if configuration.execution_settings.execution_type in [
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ]:
            self.configure_range_and_terminal(
                voltage_channel_settings=configuration.voltage_channel_settings
            )
            
            self.configure_timing_settings(
                timing_parameters=configuration.timing_parameters,
                effective_execution_settings=effective_execution_settings,
            )
            self.configure_trigger_settings(trigger_parameters=configuration.trigger_parameters, timing_parameters=configuration.timing_parameters)
            self.session.commit()
            effective_execution_settings.update(
                {
                    "Voltage Level Setting (V)": self.session.channels[
                        self._channel_name
                    ].voltage_level,
                    "Voltage Level Range (V)": self.session.channels[
                        self._channel_name
                    ].voltage_level_range,
                    "Current Limit Setting (A)": self.session.channels[
                        self._channel_name
                    ].current_limit,
                    "Current Limit Range (A)": self.session.channels[
                        self._channel_name
                    ].current_limit_range,
                    "Device Model": self.session.instrument_model,
                    "Output Function": self.session.channels[
                        self._channel_name
                    ].output_function.name,
                }
            )
            if self.session.instrument_model not in [
                "NI PXI-4110",
                "NI PXI-4130",
                "NI PXI-4131A",
                "NI PXIe-4154",
            ]:
                effective_execution_settings.update(
                    {
                        "Aperture Time (Sec)": self.session.channels[
                            self._channel_name
                        ].aperture_time
                    }
                )
            # For CONFIGURE_SOURCE_AND_MEASURE, initiate after commit
            if (
                configuration.execution_settings.execution_type
                == MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE
            ):
                self.session.initiate()
                self.session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

        # For START_SOURCE_ONLY, initiate and wait for event completion
        if (
            configuration.execution_settings.execution_type
            == MeasurementExecutionType.START_SOURCE_ONLY
        ):
            self.session.initiate()
            self.session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

        # Perform measurement for CONFIGURE_SOURCE_AND_MEASURE or MEASURE_ONLY
        if configuration.execution_settings.execution_type in [
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ]:
            measured_value = self.session.measure_multiple()
            in_compliance = self.session.query_in_compliance()
            measurement_results["Compliance/Limit Reached"] = in_compliance

            if configuration.execution_settings.skip_analysis:
                measurement_results["formatted_measurements"].update(
                    {
                        "Voltage Measurement (V)": "".join(
                            _si_notation(measured_value[0].voltage, 6)
                        ),
                        "Current Measurement (A)": "".join(
                            _si_notation(measured_value[0].current, 5)
                        ),
                    }
                )
                measurement_results["raw_measurements"].update(
                    {
                        "Voltage Measurement (V)": float(measured_value[0].voltage),
                        "Current Measurement (A)": float(measured_value[0].current),
                    }
                )
                return DCVoltageSourceAndMeasureResultData(
                    execution_settings=effective_execution_settings,
                    measurement_results=measurement_results,
                )

            # Calculate power from the measured voltage and current
            power = measured_value[0].voltage * measured_value[0].current
            # Calculate Resistance from the measured voltage and current.
            # Avoid division by zero if current is zero.
            resistance = (
                abs(measured_value[0].voltage / measured_value[0].current)
                if measured_value[0].current != 0
                else math.inf
            )
            measurement_results["formatted_measurements"].update(
                {
                    "Voltage Measurement (V)": "".join(_si_notation(measured_value[0].voltage, 6)),
                    "Current Measurement (A)": "".join(_si_notation(measured_value[0].current, 5)),
                    "Power (W)": "".join(_si_notation(power, 5)),
                    "Resistance (Ohm)": "".join(_si_notation(resistance, 5)),
                }
            )
            measurement_results["raw_measurements"].update(
                {
                    "Voltage Measurement (V)": float(measured_value[0].voltage),
                    "Current Measurement (A)": float(measured_value[0].current),
                    "Power (W)": float(power),
                    "Resistance (Ohm)": float(resistance),
                }
            )

        return DCVoltageSourceAndMeasureResultData(
            execution_settings=effective_execution_settings,
            measurement_results=measurement_results,
        )

    def configure_range_and_terminal(
        self, voltage_channel_settings: VoltageChannelSettings
    ) -> None:
        """Configures the voltage level, current limit, and their respective ranges on the channel.

        Args:
            voltage_channel_settings (VoltageChannelSettings):
                An instance of ``VoltageChannelSettings`` containing the voltage level,
                voltage level range, current limit, and current limit range to apply.
        """

        source_delays, number_of_points, pulse_current_sequence, last_point_current = generate_pulse_current_sequence(
            start_current=voltage_channel_settings.start_current,
            end_current=voltage_channel_settings.end_current,
            step_size=voltage_channel_settings.step_size,
            source_delay=voltage_channel_settings.source_delay,
        )

        self.session.channels.source_delay = source_delays
        self.session.channels.number_of_points = number_of_points
        self.session.channels.pulse_current_sequence = pulse_current_sequence
        self.session.channels.last_point_current = last_point_current

        self.session.channels[self._channel_name].pulse_current_level_range = (
            voltage_channel_settings.pulse_current_level_range
        )

        self.session.channels[self._channel_name].pulse_bias_current_level = (
            voltage_channel_settings.pulse_bias_current_level
        )

        self.session.channels[self._channel_name].pulse_voltage_limit = (
            voltage_channel_settings.pulse_voltage_limit
        )

        self.session.channels[self._channel_name].pulse_voltage_limit_range = (
            voltage_channel_settings.pulse_voltage_limit_range
        )

        self.session.channels[self._channel_name].pulse_bias_voltage_limit = (
            voltage_channel_settings.pulse_bias_voltage_limit
        )

        

    def configure_timing_settings(
        self, timing_parameters: TimingParameters, effective_execution_settings: EffectiveExecutionSettings
    ) -> None:
        """Configures aperture time and transient response settings based on the instrument model.

        Args:
            timing_parameters (TimingParameters):
                An instance of ``TimingParameters`` containing the aperture time (in seconds)
                and transient response setting to apply.
            effective_execution_settings (EffectiveExecutionSettings):
                The execution settings dictionary to update with the aperture time value.
                Set to ``math.nan`` for models that do not support aperture time.
        """
        self.session.channels[self._channel_name].pulse_on_time = (
            timing_parameters.pulse_on_time
        )
        self.session.channels[self._channel_name].pulse_off_time = (
            timing_parameters.pulse_off_time
        )
        self.session.channels[self._channel_name].pulse_bias_delay = (
            timing_parameters.pulse_bias_delay
        )
        self.session.channels[self._channel_name].aperture_time = (
            timing_parameters.aperture_time
        )
        self.session.channels[self._channel_name].aperture_time_units = (
            nidcpower.ApertureTimeUnits.SECONDS
        )

    def configure_trigger_settings(self, trigger_parameters: TriggerParameters, timing_parameters: TimingParameters) -> None:
        """Configures source trigger input and event signal routing for the channel.

        Args:
            trigger_parameters (TriggerParameters):
                An instance of ``TriggerParameters`` containing the source trigger behavior, start
                source name, export event, event signal to export, and output event signal terminal.
        """
        # Configure digital-edge source trigger if enabled
        if trigger_parameters.source_trigger_behavior == SourceTriggerBehavior.No_Synchronization_Events:

            if trigger_parameters.export_event == ExportEvent.Route_Event:
                self.session.channels[self._channel_name].event_signal_to_export = (
                    trigger_parameters.event_signal_to_export.value
                )
            elif trigger_parameters.export_event == ExportEvent.NONE:
                pass

            self.session.commit_with_channel(self._channel_name)

        elif trigger_parameters.source_trigger_behavior == SourceTriggerBehavior.Primary_Configuration_Events:

            self.session.channels[self._channel_name].source_delay = timing_parameters.source_delay
            self.session.channels[self._channel_name].disable_source_trigger = True
            self.session.channels[self._channel_name].measure_trigger_behavior = nidcpower.MeasureTriggerBehavior.SOURCE_COMPLETE
            self.session.channels[self._channel_name].measure_complete_event_delay = timing_parameters.measure_complete_event_delay

            if trigger_parameters.export_event == ExportEvent.Route_Event:
                self.session.channels[self._channel_name].event_signal_to_export = (
                    trigger_parameters.event_signal_to_export.value
                )
            elif trigger_parameters.export_event == ExportEvent.NONE:
                pass

            self.session.commit_with_channel(self._channel_name)


        elif trigger_parameters.source_trigger_behavior == SourceTriggerBehavior.Secondary_Configuration_Events:

            self.session.channels[self._channel_name].source_delay = 0.00003
            self.session.channels[self._channel_name].source_digital_edge_source_trigger_input_terminal = trigger_parameters.start_source_name
            self.session.channels[self._channel_name].measure_trigger_behavior = nidcpower.MeasureTriggerBehavior.ON_MEASURE_TRIGGER
            self.session.channels[self._channel_name].measure_digital_edge_source_trigger_input_terminal = timing_parameters.start_measure_name

            if trigger_parameters.export_event == ExportEvent.Route_Event:
                self.session.channels[self._channel_name].event_signal_to_export = (
                    trigger_parameters.event_signal_to_export.value
                )
            elif trigger_parameters.export_event == ExportEvent.NONE:
                pass

            self.session.commit_with_channel(self._channel_name)


    def build_effective_execution_settings(self, channel_name, last_point_current, number_of_poimts, instrument_model):
        """Builds a dictionary of effective execution settings based on the current configuration.

        Args:
            channel_name (str): The name of the channel being configured.
            last_point_current (float): The last point current value.
            number_of_points (int): The number of points in the pulse sequence.
            instrument_model (str): The model of the instrument being used.

        Returns:
            dict: A dictionary containing the effective execution settings.
        """
        effective_execution_settings = {
            "Pulse On Time": self.session.channels[self._channel_name].pulse_on_time,
            "Pulse Off Time": self.session.channels[self._channel_name].pulse_off_time,
            "Pulse Bias Delay": self.session.channels[self._channel_name].pulse_bias_delay,
            "Pulse Current Level Range": self.session.channels[self._channel_name].pulse_current_level_range,
            "Pulse Bias Current Level": self.session.channels[self._channel_name].pulse_bias_current_level,
            "Pulse Voltage Limit": self.session.channels[self._channel_name].pulse_voltage_limit,
            "Pulse Voltage Limit Range": self.session.channels[self._channel_name].pulse_voltage_limit_range,
            "Pulse Bias Voltage Limit": self.session.channels[self._channel_name].pulse_bias_voltage_limit,
            "Output Function": self.session.channels[self._channel_name].output_function.name,
            "Aperture Time (Sec)": self.session.channels[self._channel_name].aperture_time,
            "Transient Response": self.session.channels[self._channel_name].transient_response.name,
            "Voltage Gain Bandwidth": self.session.channels[self._channel_name].voltage_gain_bandwidth,
            "Voltage Pole Zero Ratio": self.session.channels[self._channel_name].voltage_pole_zero_ratio,
            "Current Gain Bandwidth": self.session.channels[self._channel_name].current_gain_bandwidth,
            "Current Pole Zero Ratio": self.session.channels[self._channel_name].current_pole_zero_ratio,
            "Last Point Current (A)": self.session.channels[self._channel_name].last_point_current,
            "Number of Points": self.session.channels[self._channel_name].number_of_points,
            "Device Model": self.session.channels[self._channel_name].instrument_model,
        }
        return effective_execution_settings
