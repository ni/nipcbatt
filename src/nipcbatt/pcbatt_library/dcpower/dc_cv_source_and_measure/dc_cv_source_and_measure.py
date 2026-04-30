"""Defines class used for DC constant voltage source and measurement on PCB points."""

from typing import Union
import math

import nidcpower

from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)

class DCVoltageSourceAndMeasure:
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
        self._session = nidcpower.Session(resource_name=self._resource_name)

        self._channel_name = self._session.get_channel_names(0)[0]
        self._session.channels[self._channel_name].reset()
        self._session.channels[self._channel_name].source_mode = nidcpower.SourceMode.SINGLE_POINT
        self._session.channels[self._channel_name].output_function = nidcpower.OutputFunction.DC_VOLTAGE

    def close(self):
        """Closes the NI DC Power session and releases internal resources.

        Resets the specified channel(s) to a known state before closing the session.
        """
        self._session.channels[self._channel_name].reset()
        self._session.close()

    def configure_and_measure(
            self,
            configuration: DCVoltageSourceAndMeasureParameters
        ) -> Union[tuple, None]:
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
            tuple: A two-element tuple ``(execution_settings, measurement_results)``
                where:

                - ``execution_settings`` (dict): Applied hardware settings including
                  voltage level, ranges, aperture time, device model, and output function.
                  Fields are ``math.nan`` when configuration is not performed.
                - ``measurement_results`` (dict): Measured values including voltage,
                  current, compliance state, power and resistance. Fields are 
                  ``math.nan``/``False`` when measurement is not performed.
        """
        execution_settings = {
            "Voltage Level Setting (V)": math.nan,
            "Voltage Level Range (V)": math.nan,
            "Current Limit Setting (A)": math.nan,
            "Current Limit Range (A)": math.nan,
            "Aperture Time (Sec)": math.nan,
            "Output Function": self._session.channels[self._channel_name].output_function.name,
        }
        measurement_results = {
            "Voltage Measurement (V)": math.nan,
            "Current Measurement (A)": math.nan,
            "Power (W)": math.nan,
            "Resistance (Ohm)": math.nan,
            "Compliance/Limit Reached": False,
        }

        # Apply channel, timing, and trigger settings for CONFIGURE_ONLY or CONFIGURE_SOURCE_AND_MEASURE
        if configuration.execution_settings.execution_type in [MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE, MeasurementExecutionType.CONFIGURE_ONLY]:
            self.configure_range_and_terminal(voltage_channel_settings=configuration.voltage_channel_settings)
            self._session.channels[self._channel_name].source_delay = configuration.timing_parameters.source_delay
            self._session.channels[self._channel_name].sense = configuration.voltage_channel_settings.sensing
            self._session.channels[self._channel_name].output_enabled = configuration.voltage_channel_settings.enable_output
            self.configure_timing_settings(
                timing_parameters=configuration.timing_parameters, 
                execution_settings=execution_settings
                )
            self.configure_trigger_settings(
                trigger_parameters=configuration.trigger_parameters
                )
            self._session.commit()
            execution_settings.update({
                "Voltage Level Setting (V)":self._session.channels[self._channel_name].voltage_level,
                "Voltage Level Range (V)":self._session.channels[self._channel_name].voltage_level_range,
                "Current Limit Setting (A)":self._session.channels[self._channel_name].current_limit,
                "Current Limit Range (A)":self._session.channels[self._channel_name].current_limit_range,
                "Device Model":self._session.instrument_model,
                "Output Function": self._session.channels[self._channel_name].output_function.name,
            })
            if self._session.instrument_model not in ["NI PXI-4110", "NI PXI-4130", "NI PXI-4131A", "NI PXIe-4154"]:
                execution_settings.update({
                    "Aperture Time (Sec)": self._session.channels[self._channel_name].aperture_time
                })
            # For CONFIGURE_SOURCE_AND_MEASURE, initiate after commit
            if configuration.execution_settings.execution_type == MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE:
                self._session.initiate()
                self._session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

        # For START_SOURCE_ONLY, initiate and wait for event completion
        if configuration.execution_settings.execution_type == MeasurementExecutionType.START_SOURCE_ONLY:
            self._session.initiate()
            self._session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

        # Perform measurement for CONFIGURE_SOURCE_AND_MEASURE or MEASURE_ONLY
        if configuration.execution_settings.execution_type in [MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE, MeasurementExecutionType.MEASURE_ONLY]:
            measured_value = self._session.measure_multiple()
            in_compliance = self._session.query_in_compliance()
            measurement_results["Compliance/Limit Reached"] = in_compliance
            
            if configuration.execution_settings.skip_analysis:
                measurement_results.update({
                    "Voltage Measurement (V)": measured_value[0].voltage,
                    "Current Measurement (A)": measured_value[0].current,
                })
                return execution_settings, measurement_results
            
            # Calculate power from the measured voltage and current
            power = measured_value[0].voltage * measured_value[0].current
            # Calculate Resistance from the measured voltage and current. Avoid division by zero if current is zero.
            resistance = abs(measured_value[0].voltage / measured_value[0].current) if measured_value[0].current != 0 else math.inf
            measurement_results.update({
                "Voltage Measurement (V)": measured_value[0].voltage,
                "Current Measurement (A)": measured_value[0].current,
                "Power (W)": power,
                "Resistance (Ohm)": resistance,
            })

        return execution_settings, measurement_results

    def configure_range_and_terminal(
        self,
        voltage_channel_settings: VoltageChannelSettings
    ) -> None:
        """Configures the voltage level, current limit, and their respective ranges on the channel.

        Args:
            voltage_channel_settings (VoltageChannelSettings):
                An instance of ``VoltageChannelSettings`` containing the voltage level,
                voltage level range, current limit, and current limit range to apply.
        """
        self._session.channels[self._channel_name].voltage_level = voltage_channel_settings.voltage_level
        self._session.channels[self._channel_name].current_limit = voltage_channel_settings.current_limit
        self._session.channels[self._channel_name].voltage_level_range = voltage_channel_settings.voltage_level_range
        self._session.channels[self._channel_name].current_limit_range = voltage_channel_settings.current_limit_range

    def configure_timing_settings(
        self,
        timing_parameters: TimingParameters,
        execution_settings: dict 
    ) -> None:
        """Configures aperture time and transient response settings based on the instrument model.

        Args:
            timing_parameters (TimingParameters):
                An instance of ``TimingParameters`` containing the aperture time (in seconds)
                and transient response setting to apply.
            execution_settings (dict):
                The execution settings dictionary to update with the aperture time value.
                Set to ``math.nan`` for models that do not support aperture time.
        """
        match self._session.instrument_model:
            case "NI PXIe-4112" | "NI PXIe-4113":
                self._session.channels[self._channel_name].aperture_time = timing_parameters.aperture_time
                self._session.channels[self._channel_name].aperture_time_units = nidcpower.ApertureTimeUnits.SECONDS
            case "NI PXI-4110" | "NI PXI-4130" | "NI PXI-4131A" | "NI PXIe-4154":
                execution_settings.update({
                    "Aperture Time (Sec)": math.nan
                })
            case _:
                self._session.channels[self._channel_name].aperture_time = timing_parameters.aperture_time
                self._session.channels[self._channel_name].aperture_time_units = nidcpower.ApertureTimeUnits.SECONDS
                self._session.channels[self._channel_name].transient_response = timing_parameters.transient_response
                
        
    def configure_trigger_settings(
            self,
            trigger_parameters: TriggerParameters
    ) -> None:
        """Configures source trigger input and event signal routing for the channel.

        Args:
            trigger_parameters (TriggerParameters):
                An instance of ``TriggerParameters`` containing the source trigger behavior, start 
                source name, export event, event signal to export, and output event signal terminal.
        """
        # Configure digital-edge source trigger if enabled
        if trigger_parameters.source_trigger_behavior == SourceTriggerBehavior.Start_Source_Trigger:
            self._session.channels[self._channel_name].source_trigger_type = nidcpower.TriggerType.DIGITAL_EDGE
            self._session.channels[self._channel_name].digital_edge_source_trigger_input_terminal = trigger_parameters.start_source_name

        # Route the selected event signal to the specified output terminal
        if trigger_parameters.export_event == ExportEvent.Route_Event:
            setattr(
                self._session.channels[self._channel_name],
                trigger_parameters.event_signal_to_export.value,
                trigger_parameters.output_event_signal_terminal,
            )