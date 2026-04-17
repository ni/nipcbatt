from typing import Union
import math

import nidcpower

from nipcbatt.pcbatt_library.smu.dc_voltage_source_and_measure.dc_voltage_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    EventSignalToExport,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)

class DCVoltageSourceAndMeasure:

    def BuildTerminalName(self, fully_qualified_channel_name: str, local_terminal_name: str) -> str:
        _channel_name = fully_qualified_channel_name[:fully_qualified_channel_name.rfind("/")]
        _channel_number = fully_qualified_channel_name[fully_qualified_channel_name.rfind("/") + 1:]

        if self._session.instrument_model ==  "NI PXI-4132" :
            return f"/{_channel_name}/{local_terminal_name}"          
        else:
            return f"/{_channel_name}/Engine{_channel_number}/{local_terminal_name}"          


    def initialize(self, resource_name: str):
        """Initializes the NI DC Power session with the specified resource.

        Args:
            resource_name (str):
                The resource name of the NI-DCPower instrument (e.g., "Dev1").
        """
        self._resource_name = resource_name
        self._session = nidcpower.Session(resource_name=self._resource_name)

        self._channel_name = self._session.get_channel_names(0)[0]

        self._session.channels[self._channel_name].reset()

        self._session.output_enabled = False

        self._session.channels[self._channel_name].source_mode = nidcpower.SourceMode.SINGLE_POINT

        self._session.channels[self._channel_name].output_function = nidcpower.OutputFunction.DC_VOLTAGE

        self.BuildTerminalName(self._channel_name, "SourceTrigger")
        self.BuildTerminalName(self._channel_name, "SourceCompleteEvent")

    def close(self):
        """Closes the NI DC Power session."""
        self._session.close()

    def configure_and_measure(
            self, 
            configuration:DCVoltageSourceAndMeasureParameters
        ) -> Union[list, None]:
        
        execution_settings = []

        if configuration.execution_type == MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE:

            self.configure_range_and_terminal(voltage_channel_settings=configuration.voltage_channel_settings)
            self._session.channels[self._channel_name].source_delay = configuration.timing_parameters.source_delay
            self._session.channels[self._channel_name].sense = configuration.voltage_channel_settings.sensing
            self._session.channels[self._channel_name].output_enabled = configuration.voltage_channel_settings.enable_output

            self.configure_timing_settings(timing_parameters=configuration.timing_parameters)
            self.configure_trigger_settings(trigger_parameters=configuration.trigger_parameters)

            self._session.commit()

            execution_settings = [
                self._session.channels[self._channel_name].voltage_level,
                self._session.channels[self._channel_name].voltage_level_range,
                self._session.channels[self._channel_name].current_limit,
                self._session.channels[self._channel_name].current_limit_range,
                self._session.channels[self._channel_name].output_function,
                self._session.channels[self._channel_name].aperture_time,
                self._session.instrument_model,
            ]

            self._session.initiate()

            self._session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)
        
        if configuration.execution_type in [MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE, MeasurementExecutionType.MEASURE_ONLY]:
            meaured_value = self._session.measure_multiple()
            in_complaince = self._session.query_in_compliance()
            print(f"Measured Value: {meaured_value}, In Compliance: {in_complaince}")

        return execution_settings if execution_settings else None


    def configure_range_and_terminal(
        self, 
        voltage_channel_settings: VoltageChannelSettings
    ) -> None:
        self._session.channels[self._channel_name].voltage_level = voltage_channel_settings.voltage_level
        self._session.channels[self._channel_name].current_limit = voltage_channel_settings.current_limit
        self._session.channels[self._channel_name].voltage_level_range = voltage_channel_settings.voltage_level_range
        self._session.channels[self._channel_name].current_limit_range = voltage_channel_settings.current_limit_range
        

    def configure_timing_settings(
        self,
        timing_parameters: TimingParameters,
    ) -> None:
        match self._session.instrument_model:
            case "NI PXIe-4112" | "NI PXIe-4113":
                self._session.channels[self._channel_name].aperture_time = timing_parameters.aperture_time
                self._session.channels[self._channel_name].aperture_time_units = nidcpower.ApertureTimeUnits.SECONDS
            case "NI PXI-4110" | "NI PXI-4130" | "NI PXI-4131A" | "NI PXIe-4154":
                self._session.channels[self._channel_name].transient_response = math.nan
            case _:
                self._session.channels[self._channel_name].aperture_time = timing_parameters.aperture_time
                self._session.channels[self._channel_name].aperture_time_units = nidcpower.ApertureTimeUnits.SECONDS
                self._session.channels[self._channel_name].transient_response = timing_parameters.transient_response
        
    def configure_trigger_settings(
            self,
            trigger_parameters: TriggerParameters
    ) -> None:
        if trigger_parameters.source_trigger_behavior.value == "Start_Source_Trigger":
            self._session.channels[self._channel_name].source_trigger_type = nidcpower.TriggerType.DIGITAL_EDGE
            self._session.channels[self._channel_name].digital_edge_source_trigger_input_terminal = trigger_parameters.start_source_name

        if trigger_parameters.export_event.value == "Route_Event":
            # switch case
            _signal = trigger_parameters.output_event_signal_terminal
            match trigger_parameters.event_signal_to_export:
                case EventSignalToExport.Source_Complete_Event:
                    self._session.channels[self._channel_name].source_complete_event_output_terminal = _signal
                case EventSignalToExport.Measure_Complete_Event:
                    self._session.channels[self._channel_name].measure_complete_event_output_terminal = _signal
                case EventSignalToExport.Sequence_Iteration_Complete_Event:
                    self._session.channels[self._channel_name].sequence_iteration_complete_event_output_terminal = _signal
                case EventSignalToExport.Sequence_Engine_Done_Event:
                    self._session.channels[self._channel_name].sequence_engine_done_event_output_terminal = _signal
                case EventSignalToExport.Pulse_Complete_Event:
                    self._session.channels[self._channel_name].pulse_complete_event_output_terminal = _signal
                case EventSignalToExport.Ready_for_Pulse_Trigger_Event:
                    self._session.channels[self._channel_name].ready_for_pulse_trigger_event_output_terminal = _signal
                case EventSignalToExport.Start_Trigger:
                    self._session.channels[self._channel_name].exported_start_trigger_output_terminal = _signal
                case EventSignalToExport.Source_Trigger:
                    self._session.channels[self._channel_name].exported_source_trigger_output_terminal = _signal
                case EventSignalToExport.Measure_Trigger:
                    self._session.channels[self._channel_name].exported_measure_trigger_output_terminal = _signal
                case EventSignalToExport.Sequence_Advance_Trigger:
                    self._session.channels[self._channel_name].exported_sequence_advance_trigger_output_terminal = _signal
                case EventSignalToExport.Pulse_Trigger:
                    self._session.channels[self._channel_name].exported_pulse_trigger_output_terminal = _signal