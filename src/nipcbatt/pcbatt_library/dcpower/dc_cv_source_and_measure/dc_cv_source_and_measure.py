"""Defines class used for DC constant voltage source and measurement on PCB points."""

import math

import nidcpower

from nipcbatt.pcbatt_library.dcpower.common.helper_function import (
    format_si_fixed_decimals as _si_fixed,
)
from nipcbatt.pcbatt_library.dcpower.dc_cv_source_and_measure.dc_cv_source_and_measure_data_types import (
    DCVoltageSourceAndMeasureParameters,
    DCVoltageSourceAndMeasureResultData,
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
            resource_name (str): NI-DCPower resource name, e.g. ``"PPS1/0"``.
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
        """Resets the channel and closes the NI-DCPower session, releasing all resources."""
        if self.is_session_initialized:
            self.session.channels[self._channel_name].reset()
            self.session.close()
            self._instrument = None

    def configure_and_measure(
        self, configuration: DCVoltageSourceAndMeasureParameters
    ) -> DCVoltageSourceAndMeasureResultData:
        """Configures and/or measures DC voltage. Behavior is set by ``execution_settings``.

        Behavior is controlled by the ``execution_settings`` :
        To source and measure all in one function call:
        - CONFIGURE_SOURCE_AND_MEASURE 

        Or use separated steps calls to execute the same flow but sequentially with:	
        - CONFIGURE_ONLY
        - START_SOURCE_ONLY
        - MEASURE_ONLY


        Args:
            configuration (DCVoltageSourceAndMeasureParameters): Channel, timing,
                trigger, and execution settings.

        Returns:
            DCVoltageSourceAndMeasureResultData: Hardware execution settings and
                measurement results. Unused fields contain ``NaN``.
        """
        execution_settings = {
            "Voltage Level Setting (V)": math.nan,
            "Voltage Level Range (V)": math.nan,
            "Current Limit Setting (A)": math.nan,
            "Current Limit Range (A)": math.nan,
            "Aperture Time (Sec)": math.nan,
            "Output Function": self.session.channels[self._channel_name].output_function.name,
        }
        measurement_results = {
            "formatted_measurements": {
                "Voltage Measurement": math.nan,
                "Current Measurement": math.nan,
                "Power": math.nan,
                "Resistance": math.nan,
            },
            "raw_measurements": {
                "Voltage Measurement (V)": math.nan,
                "Current Measurement (A)": math.nan,
                "Power (W)": math.nan,
                "Resistance (Ohm)": math.nan,
            },
            "Compliance/Limit Reached": False,
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
            self.session.channels[self._channel_name].source_delay = (
                configuration.timing_parameters.source_delay
            )
            self.session.channels[self._channel_name].sense = (
                configuration.voltage_channel_settings.sensing
            )
            self.session.channels[self._channel_name].output_enabled = (
                configuration.voltage_channel_settings.enable_output
            )
            self.configure_timing_settings(
                timing_parameters=configuration.timing_parameters,
                execution_settings=execution_settings,
            )
            self.configure_trigger_settings(trigger_parameters=configuration.trigger_parameters)
            self.session.commit()
            execution_settings.update(
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
                execution_settings.update(
                    {
                        "Aperture Time (Sec)": self.session.channels[
                            self._channel_name
                        ].aperture_time
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
                        "Voltage Measurement": _si_fixed(measured_value[0].voltage, "V"),
                        "Current Measurement": _si_fixed(measured_value[0].current, "A"),
                    }
                )
                measurement_results["raw_measurements"].update(
                    {
                        "Voltage Measurement (V)": float(measured_value[0].voltage),
                        "Current Measurement (A)": float(measured_value[0].current),
                    }
                )
                return DCVoltageSourceAndMeasureResultData(
                    execution_settings=execution_settings,
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
                    "Voltage Measurement": _si_fixed(measured_value[0].voltage, "V"),
                    "Current Measurement": _si_fixed(measured_value[0].current, "A"),
                    "Power": _si_fixed(power, "W"),
                    "Resistance": _si_fixed(resistance, "Ohm"),
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
            execution_settings=execution_settings,
            measurement_results=measurement_results,
        )

    def configure_range_and_terminal(
        self, voltage_channel_settings: VoltageChannelSettings
    ) -> None:
        """Configures the voltage level, current limit, and their respective ranges on the channel.

        Args:
            voltage_channel_settings (VoltageChannelSettings): Channel settings to apply.
        """
        self.session.channels[self._channel_name].voltage_level = (
            voltage_channel_settings.voltage_level
        )
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
        self, timing_parameters: TimingParameters, execution_settings: dict
    ) -> None:
        """Configures aperture time and transient response based on the instrument model.

        PXIe-4112/4113: aperture time only. PXI-4110/4130/4131A/4154: neither supported
        (``Aperture Time (Sec)`` set to ``NaN``). All other models: both supported.

        Args:
            timing_parameters (TimingParameters): Aperture time and transient response to apply.
            execution_settings (dict): Updated in-place; ``NaN`` set for unsupported models.
        """
        match self.session.instrument_model:
            case "NI PXIe-4112" | "NI PXIe-4113":
                self.session.channels[self._channel_name].aperture_time = (
                    timing_parameters.aperture_time
                )
                self.session.channels[self._channel_name].aperture_time_units = (
                    nidcpower.ApertureTimeUnits.SECONDS
                )
            case "NI PXI-4110" | "NI PXI-4130" | "NI PXI-4131A" | "NI PXIe-4154":
                execution_settings.update({"Aperture Time (Sec)": math.nan})
            case _:
                self.session.channels[self._channel_name].aperture_time = (
                    timing_parameters.aperture_time
                )
                self.session.channels[self._channel_name].aperture_time_units = (
                    nidcpower.ApertureTimeUnits.SECONDS
                )
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
