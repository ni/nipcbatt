"""Defines class used for waveform DC constant voltage source and measurement on PCB points."""

import math

import nidcpower

from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure_data_types import (
    WaveformTimingParameters,
    WaveformVoltageSourceAndMeasureParameters,
    WaveformVoltageSourceAndMeasureResultData,
    WaveformVoltageChannelSettings,
    WaveformExecutionSettings,
    MeasurementExecutionType,
    EventSignalToExport,
    ExportEvent,
    TriggerParameters,
    SourceTriggerBehavior,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
)

_APERTURE_TIME_UNSUPPORTED_MODELS = frozenset(
    {"NI PXI-4110", "NI PXI-4130", "NI PXI-4131A", "NI PXIe-4154"}
)
_TRANSIENT_RESPONSE_UNSUPPORTED_MODELS = frozenset(
    {"NI PXI-4110", "NI PXI-4130", "NI PXI-4131A", "NI PXIe-4154", "NI PXIe-4112", "NI PXIe-4113"}
)
from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
    BuildingBlockUsingNIDCPower,
)


class WaveformVoltageSourceAndMeasure(BuildingBlockUsingNIDCPower):
    """Defines a way that allows you to source DC voltage waveform and perform measurements on PCB points."""

    def initialize(self, resource_name: str):
        """Initializes the NI DC Power session with the specified resource.

        Opens a new NI-DCPower session, resets the channel, configures
        the source mode to sequence (for stepping through the waveform's voltage
        setpoints), and sets the output function to DC voltage.

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
        # Initialize the execution settings as instance state so values persist across
        # the separated CONFIGURE_ONLY, START_SOURCE_ONLY, and MEASURE_ONLY calls
        self._execution_settings = {
            "Voltage Level Range (V)": math.nan,
            "Current Limit (A)": math.nan,
            "Current Limit Range (A)": math.nan,
            "Measure Record Delta Time": math.nan,
            "Sample Rate (Hz)": math.nan,
            "Step Record Length": math.nan,
            "Effective Step Time (Sec)": math.nan,
            "Total Sequence Time (Sec)": math.nan,
            "Device Model": "",
            "Transient Response": "",
            "Voltage Gain Bandwidth (Hz)": math.nan,
            "Voltage Compensation Frequency (Hz)": math.nan,
            "Voltage Pole Zero Ratio": math.nan,
            "Current Gain Bandwidth (Hz)": math.nan,
            "Current Compensation Frequency (Hz)": math.nan,
            "Current Pole Zero Ratio": math.nan,
        }

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
        """Configures and/or measures DC voltage waveform. Behavior is set by ``execution_settings``.

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
            WaveformVoltageSourceAndMeasureResultData: Hardware execution settings held in
                instance state (``_execution_settings``), plus the measured voltage and
                current waveforms. Execution settings not populated by the current execution
                type retain the values set during ``initialize`` (``NaN`` by default), and
                the waveforms are empty when measurement is not performed.
        """
        step_record_length = 0
        voltage_waveform = []
        current_waveform = []
        # Apply channel, timing, and trigger settings for CONFIGURE_ONLY or
        # CONFIGURE_SOURCE_AND_MEASURE
        if configuration.execution_settings.execution_type in [
            MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ]:
            self.configure_range_and_terminal(
                voltage_channel_settings=configuration.voltage_channel_settings
            )
            self.session.channels[self._channel_name].source_delay = configuration.timing_parameters.source_delay
            self.session.channels[self._channel_name].sense = (
                configuration.voltage_channel_settings.sensing
            )
            self.session.channels[self._channel_name].output_enabled = (
                configuration.voltage_channel_settings.enable_output
            )

            if self.session.instrument_model not in _APERTURE_TIME_UNSUPPORTED_MODELS:
                try:
                    step_record_length = int(abs(configuration.voltage_channel_settings.step_time / configuration.timing_parameters.aperture_time))
                except ZeroDivisionError as error:
                    raise ValueError(
                        "Failed to compute step_record_length: aperture_time is zero."
                    ) from error
            else:   
                # If aperture time is unsupported by the instrument model, 
                # use a default value of 16.66666 ms to compute step_record_length
                step_record_length = int(abs(configuration.voltage_channel_settings.step_time / 0.01666666))

            self.session.channels[self._channel_name].measure_record_length = step_record_length
            self.session.channels[self._channel_name].measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE

            self.configure_timing_settings(
                timing_parameters=configuration.timing_parameters
            )

            self.configure_trigger_settings(
                trigger_parameters=configuration.trigger_parameters
            )

            # Apply the same source delay to every voltage setpoint in the sequence
            source_delays = [configuration.timing_parameters.source_delay] * len(configuration.voltage_channel_settings.voltage_setpoints)
            self.session.set_sequence(values=configuration.voltage_channel_settings.voltage_setpoints, source_delays=source_delays)
            self.session.commit()

            if configuration.timing_parameters.transient_response is nidcpower.TransientResponse.CUSTOM and self.session.instrument_model not in _TRANSIENT_RESPONSE_UNSUPPORTED_MODELS:
                self._execution_settings.update(
                    {
                        "Transient Response": self.session.channels[
                            self._channel_name
                        ].transient_response.name,
                        "Voltage Gain Bandwidth (Hz)": self.session.channels[
                            self._channel_name
                        ].voltage_gain_bandwidth,
                        "Voltage Compensation Frequency (Hz)": self.session.channels[
                            self._channel_name
                        ].voltage_compensation_frequency,
                        "Voltage Pole Zero Ratio": self.session.channels[
                            self._channel_name
                        ].voltage_pole_zero_ratio,
                        "Current Gain Bandwidth (Hz)": self.session.channels[
                            self._channel_name
                        ].current_gain_bandwidth,
                        "Current Compensation Frequency (Hz)": self.session.channels[
                            self._channel_name
                        ].current_compensation_frequency,
                        "Current Pole Zero Ratio": self.session.channels[
                            self._channel_name
                        ].current_pole_zero_ratio,
                    }
                )
            else:
                if self.session.instrument_model not in _TRANSIENT_RESPONSE_UNSUPPORTED_MODELS:
                    self._execution_settings.update(
                        {
                            "Transient Response": self.session.channels[
                                self._channel_name 
                            ].transient_response.name,
                        }
                    )
            
            self._execution_settings.update(
                {
                    "Voltage Level Range (V)": self.session.channels[self._channel_name].voltage_level_range,
                    "Current Limit (A)": self.session.channels[self._channel_name].current_limit,
                    "Current Limit Range (A)": self.session.channels[self._channel_name].current_limit_range,
                    "Device Model": self.session.instrument_model,
                }
            )
           
            # For CONFIGURE_SOURCE_AND_MEASURE — initiate source and wait for event completion after commit
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
            measure_record_dt = self.session.channels[self._channel_name].measure_record_delta_time.total_seconds()
            sample_rate = 1.0 / measure_record_dt # measure_record_delta_time is read from the instrument in seconds
            effective_step_time = measure_record_dt * step_record_length
            total_sequence_time = effective_step_time * len(configuration.voltage_channel_settings.voltage_setpoints)
            self._execution_settings.update(
                {
                    "Measure Record Delta Time": measure_record_dt,
                    "Sample Rate (Hz)": sample_rate,
                    "Step Record Length": step_record_length,
                    "Effective Step Time (Sec)": effective_step_time,
                    "Total Sequence Time (Sec)": total_sequence_time,
                }
            )

            count = len(configuration.voltage_channel_settings.voltage_setpoints) * step_record_length
            timeout_padding_multiplier = 2
            timeout = count * measure_record_dt * timeout_padding_multiplier

            # Fetch measurements from the instrument
            measurements = self.session.channels[self._channel_name].fetch_multiple(count=count, timeout=timeout)

            # Extract voltage and current from the measurements
            voltages = [m.voltage for m in measurements]
            currents = [m.current for m in measurements]
            voltage_waveform.append(
                AnalogWaveform(
                    channel_name=self._channel_name,
                    delta_time_seconds=measure_record_dt,
                    samples=voltages,
                )
            )
            current_waveform.append(
                AnalogWaveform(
                    channel_name=self._channel_name,
                    delta_time_seconds=measure_record_dt,
                    samples=currents,
                )
            )
            return WaveformVoltageSourceAndMeasureResultData(
                execution_settings=self._execution_settings,
                voltage_waveform=voltage_waveform,
                current_waveform=current_waveform,
            )

        # Return the execution settings and measurement results
        return WaveformVoltageSourceAndMeasureResultData(
            execution_settings=self._execution_settings,
            voltage_waveform=voltage_waveform,
            current_waveform=current_waveform,
        )

    def configure_range_and_terminal(
        self, voltage_channel_settings: WaveformVoltageChannelSettings
    ) -> None:
        """Configures the voltage level, current limit, and their respective ranges on the channel.

        Args:
            voltage_channel_settings (WaveformVoltageChannelSettings): Channel settings to apply.
        """
        self.session.channels[self._channel_name].voltage_level_range = (
            voltage_channel_settings.voltage_level_range
        )
        self.session.channels[self._channel_name].current_limit = (
            voltage_channel_settings.current_limit
        )
        self.session.channels[self._channel_name].current_limit_range = (
            voltage_channel_settings.current_limit_range
        )


    def configure_timing_settings(
        self, timing_parameters: WaveformTimingParameters, 
    ) -> None:
        """Configures aperture time and transient response settings based on the instrument model.

        Args:
            timing_parameters (WaveformTimingParameters):
                An instance of ``WaveformTimingParameters`` containing the aperture time (in seconds)
                and transient response setting to apply.
        """

        match self.session.instrument_model:
            case "NI PXIe-4112" | "NI PXIe-4113":
                self.session.channels[self._channel_name].aperture_time = (
                    timing_parameters.aperture_time
                )
                self.session.channels[self._channel_name].aperture_time_units = (
                    nidcpower.ApertureTimeUnits.SECONDS
                )
            case _ if self.session.instrument_model in _APERTURE_TIME_UNSUPPORTED_MODELS:
                pass # Do not set aperture time and transient response for unsupported models
            case _:
                self.session.channels[self._channel_name].aperture_time = (
                    timing_parameters.aperture_time
                )
                self.session.channels[self._channel_name].aperture_time_units = (
                    nidcpower.ApertureTimeUnits.SECONDS
                )
                if timing_parameters.transient_response is nidcpower.TransientResponse.CUSTOM and self.session.instrument_model not in _TRANSIENT_RESPONSE_UNSUPPORTED_MODELS:
                    self.session.channels[self._channel_name].transient_response = (
                        timing_parameters.transient_response
                    )
                    self.session.channels[self._channel_name].voltage_gain_bandwidth = (
                        timing_parameters.voltage_gain_bandwidth
                    )
                    self.session.channels[self._channel_name].voltage_compensation_frequency = (
                        timing_parameters.voltage_compensation_frequency
                    )
                    self.session.channels[self._channel_name].voltage_pole_zero_ratio = (
                        timing_parameters.voltage_pole_zero_ratio
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
                else:
                    if self.session.instrument_model not in _TRANSIENT_RESPONSE_UNSUPPORTED_MODELS:
                        self.session.channels[self._channel_name].transient_response = (
                            timing_parameters.transient_response
                        )

    def configure_trigger_settings(self, trigger_parameters: TriggerParameters) -> None:
        """Configures source trigger input and event signal routing.

        - ``Start_Source_Trigger``: source waits for a digital edge on ``start_source_name``.
        - ``Route_Event``: exports ``event_signal_to_export`` to ``output_event_signal_terminal``.
        - Not supported on all devices (e.g. NI PXI-4110 raises ``DriverError``).

        Args:
            trigger_parameters (TriggerParameters): Trigger and event routing settings.
        """
        # Configure digital-edge source trigger if enabled
        if trigger_parameters.source_trigger_behavior == SourceTriggerBehavior.Start_Source_Trigger:
            self.session.channels[self._channel_name].source_trigger_type = (
                nidcpower.TriggerType.DIGITAL_EDGE
            )
            self.session.channels[self._channel_name].digital_edge_source_trigger_input_terminal = (
                trigger_parameters.start_source_name
            )

        # Route the selected event signal to the specified output terminal
        if trigger_parameters.export_event == ExportEvent.Route_Event:
            setattr(
                self.session.channels[self._channel_name],
                trigger_parameters.event_signal_to_export.value,
                trigger_parameters.output_event_signal_terminal,
            )