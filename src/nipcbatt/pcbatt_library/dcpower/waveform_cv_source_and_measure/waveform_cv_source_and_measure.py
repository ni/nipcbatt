"""Defines class used for DC constant voltage source and measurement on PCB points."""

import math

import nidcpower

from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure_data_types import (
    WaveformVoltageSourceAndMeasureParameters,
    WaveformVoltageSourceAndMeasureResultData,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)

_APERTURE_TIME_UNSUPPORTED_MODELS = frozenset(
    {"NI PXI-4110", "NI PXI-4130", "NI PXI-4131A", "NI PXIe-4154"}
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDCPower,
)


class WaveformVoltageSourceAndMeasure(BuildingBlockUsingNIDCPower):
    """Defines a way that allows you to source DC voltage waveform and perform measurements on PCB points."""

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
        self.session.channels[self._channel_name].source_mode = nidcpower.SourceMode.SEQUENCE
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
        self, configuration: WaveformVoltageSourceAndMeasureParameters
    ) -> WaveformVoltageSourceAndMeasureResultData:
        """Configures and/or measures DC voltage. Behavior is set by ``execution_settings``.

        Behavior is controlled by the ``execution_settings`` :
        To source and measure all in one function call:
        - CONFIGURE_SOURCE_AND_MEASURE

        Or use separated steps calls to execute the same flow but sequentially with:
        - CONFIGURE_ONLY
        - START_SOURCE_ONLY
        - MEASURE_ONLY


        Args:
            configuration (WaveformVoltageSourceAndMeasureParameters): Channel, timing,
                trigger, and execution settings.

        Returns:
            WaveformVoltageSourceAndMeasureResultData: Hardware execution settings and
                measurement results held in instance state (``_execution_settings`` and
                ``_measurement_results``). Fields not populated by the current execution
                type retain the values set during ``initialize`` (``NaN`` by default).
        """
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
                timing_parameters=configuration.timing_parameters
            )
            # self.configure_trigger_settings(trigger_parameters=configuration.trigger_parameters)
            self.session.set_sequence(values=configuration.voltage_setpoints)
            self.session.commit()
            self._execution_settings.update(
                {
                    "Transient Response": self.session.channels[
                        self._channel_name
                    ].transient_response.name,
                    "Voltage Gain Bandwidth": self.session.channels[
                        self._channel_name
                    ].voltage_gain_bandwidth,
                    "Voltage Compensation Frequency": self.session.channels[
                        self._channel_name
                    ].voltage_compensation_frequency,
                    "Voltage Pole Zero Ratio": self.session.channels[
                        self._channel_name
                    ].voltage_pole_zero_ratio,
                    "Current Gain Bandwidth": self.session.channels[
                        self._channel_name
                    ].current_gain_bandwidth,
                    "Current Compensation Frequency": self.session.channels[
                        self._channel_name
                    ].current_compensation_frequency,
                    "Current Pole Zero Ratio": self.session.channels[
                        self._channel_name
                    ].current_pole_zero_ratio,
                    "Device Model": self.session.instrument_model,
                    "Output Function": self.session.channels[
                        self._channel_name
                    ].output_function.name,
                }
            )
           
            # For CONFIGURE_SOURCE_AND_MEASURE — initiate source immediately after commit
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
            # self.session.wait_for_event(nidcpower.Event.SOURCE_COMPLETE)

        # Perform measurement for CONFIGURE_SOURCE_AND_MEASURE or MEASURE_ONLY
        if configuration.execution_settings.execution_type in [
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ]:
            
            # Calculate the number of measurements to fetch based on the aperture time and step size
            measure_record_dt = self.session.channels[self._channel_name].measure_record_dt
            step_record_length = int(abs(configuration.timing_parameters.aperture_time / configuration.timing_parameters.step_size))
            count = len(configuration.voltage_setpoints) * step_record_length

            # Fetch measurements from the instrument
            measurements = self.session.channels[self._channel_name].fetch_multiple(count=count, timeout=10.0)

            # Extract voltage, current, and compliance status from the measurements
            voltages = [m.voltage for m in measurements]
            currents = [m.current for m in measurements]
            in_compliance = [m.in_compliance for m in measurements]

            # Store the measurement results in the instance state
            self._measurement_results["waveform_measurements"] = {
                "x_data": voltages,
                "y_data": currents,
                "dt": measure_record_dt
            }
            self._measurement_results["raw_measurements"] = {
                "Voltage Measurement (V)": float(voltages[0]),
                "Current Measurement (A)": float(currents[0]),
                "In Compliance": bool(in_compliance[0])
            }
            self._measurement_results["Measure Record Delta Time"] = measure_record_dt
            self._measurement_results["Sample Rate (Hz)"] = 1.0 / measure_record_dt
            self._measurement_results["Step Record Length"] = step_record_length
            self._measurement_results["Effective Step Time (Sec)"] = measure_record_dt * self._measurement_results["Step Record Length"]
            self._measurement_results["Total Sequence Time (Sec)"] = self._measurement_results["Effective Step Time (Sec)"] * len(configuration.voltage_setpoints)
            return WaveformVoltageSourceAndMeasureResultData(
                execution_settings=self._execution_settings,
                measurement_results=self._measurement_results,
            )

        # Return the execution settings and measurement results
        return WaveformVoltageSourceAndMeasureResultData(
            execution_settings=self._execution_settings,
            measurement_results=self._measurement_results,
        )


    def configure_range_and_terminal(
        self, voltage_channel_settings: VoltageChannelSettings
    ) -> None:
        """Configures the voltage level, current limit, and their respective ranges on the channel.

        Args:
            voltage_channel_settings (VoltageChannelSettings): Channel settings to apply.
        """
        self.session.channels[self._channel_name].current_limit = (
            voltage_channel_settings.current_limit
        )
        self.session.channels[self._channel_name].voltage_level_range = (
            voltage_channel_settings.voltage_level_range
        )
        self.session.channels[self._channel_name].current_limit_range = (
            voltage_channel_settings.current_limit_range
        )


    def configure_timing_settings(
        self, timing_parameters: TimingParameters, 
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
        self.session.channels[self._channel_name].source_delay = (
            timing_parameters.source_delay
        )
        self.session.channels[self._channel_name].aperture_time = (
            timing_parameters.aperture_time
        )
        self.session.channels[self._channel_name].aperture_time_units = (
            nidcpower.ApertureTimeUnits.SECONDS
        )
        self.session.channels[self._channel_name].measure_record_length = (
            timing_parameters.measure_record_length
        )
        self.session.channels[self._channel_name].measure_when = (
            timing_parameters.measure_when
        )
        self.session.channels[self._channel_name].transient_response = (
            timing_parameters.transient_response
        )
        self.session.channels[self._channel_name].voltage_gain_bandwidth = (
            timing_parameters.voltage_gain_bandwidth
        )
        self.session.channels[self._channel_name].voltage_compensation_frequency = (
            timing_parameters.voltage_compensation_frequency
        )
        
        self.session.channels[self._channel_name].current_gain_bandwidth = (
            timing_parameters.current_gain_bandwidth    
        )
        self.session.channels[self._channel_name].current_compensation_frequency = (
            timing_parameters.current_compensation_frequency
        )
        self.session.channels[self._channel_name].current_pole_zero_ratio = (
            timing_parameters.current_pole_zero_ratio
        )
        self.session.channels[self._channel_name].voltage_pole_zero_ratio = (
            timing_parameters.voltage_pole_zero_ratio
        )


'''
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
'''
