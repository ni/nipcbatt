"""Defines class used for resistance measurement on PCB points."""

from typing import Union

import nidmm

from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingNIDMM

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.common.helper_functions import (
    FormatMeasurement,
    RangeAndMeasurementFunctionParameters,
)
from nipcbatt.pcbatt_library.dmm.resistance_measurements.resistance_data_types import (
    ResistanceMeasurementFunctionParameters,
    ResistanceMeasurementConfiguration,
    ResistanceMeasurementResultData,
)


class DcRmsResistanceMeasurement(BuildingBlockUsingNIDMM):
    """Defines a way that allows you to perform resistance measurements on PCB points."""

    def initialize(self, dmm_resource_name: str, powerline_frequency: float):
        """Initializes the DMM session with the specific resource name and powerline frequency.

        Args:
            dmm_resource_name (str):
                The resource name of the DMM device to use for measurements.
            powerline_frequency (float):
                The powerline frequency in Hz (typically 50.0 or 60.0).
        """
        self._dmm_resource_name = dmm_resource_name
        self._powerline_frequency = powerline_frequency
        self._instrument = nidmm.Session(resource_name=self._dmm_resource_name)
        self.session.powerline_freq = self._powerline_frequency

    def configure_and_measure(
        self, configuration: ResistanceMeasurementConfiguration
    ) -> Union[ResistanceMeasurementResultData, None]:
        """Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (ResistanceMeasurementConfiguration):
                An instance of `ResistanceMeasurementConfiguration` used to configure
                the measurement.

        Returns:
            ResistanceMeasurementResultData | None: An instance of
                `ResistanceMeasurementResultData` containing DMM execution settings
                 and the measured resistance value,or None if only configuration was performed.
        """
        if configuration.execution_type in (
            MeasurementExecutionType.CONFIGURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            self.configure_measurement_function(
                parameters=configuration.measurement_function_parameters
            )
            self.configure_trigger(parameters=configuration.trigger_parameters)
            self.configure_timing(parameters=configuration.timing_parameters)
            if self.session.function == nidmm.Function.AC_VOLTS:
                self.session.ac_min_freq = configuration.ac_min_frequency

        if configuration.execution_type in (
            MeasurementExecutionType.MEASURE_ONLY,
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        ):
            return self.acquire_measurement(
                configuration.measurement_function_parameters.resolution_in_digits.value
            )
        return None

    def close(self):
        """Closes measurement procedure and releases internal resources."""
        if self.is_session_initialized:
            self.session.close()
            self._instrument = None

    def configure_measurement_function(self, parameters: ResistanceMeasurementFunctionParameters):
        """Configures the measurement function settings for the DMM.

        Args:
            parameters (ResistanceMeasurementFunctionParameters):
                An instance of `ResistanceMeasurementFunctionParameters` containing the measurement
                function type (2-wire/4-wire resistance) and resolution in digits to configure.
        """
        measurement_function_and_range = RangeAndMeasurementFunctionParameters(
            parameters.measurement_function
        )
        resolution_in_digits = parameters.resolution_in_digits.value
        self.session.configure_measurement_digits(
            measurement_function=measurement_function_and_range.measurement_function,
            range=measurement_function_and_range.range_value,
            resolution_digits=resolution_in_digits,
        )

    def configure_trigger(self, parameters: TriggerParameters):
        """Configure the characteristics of triggers used for resistance measurements.

        Args:
            parameters (TriggerParameters):
                An instance of `TriggerParameters` containing trigger source,
                trigger delay, and enable/disable flag.
        """
        if not parameters.enable_trigger:
            self.session.configure_trigger(
                trigger_source=nidmm.TriggerSource.IMMEDIATE, trigger_delay=-1.0
            )
            return
        self.session.configure_trigger(
            trigger_source=nidmm.TriggerSource[parameters.trigger_source.name],
            trigger_delay=parameters.trigger_delay,
        )
        # Configure Slope if trigger is enabled
        nidmm_trigger_slope_attribute_id = 1250334
        self.session._set_attribute_vi_int32(
            nidmm_trigger_slope_attribute_id, parameters.trigger_slope.value
        )

    def configure_timing(self, parameters: TimingParameters):
        """Configures the timing characteristics used for resistance measurements.

        Args:
            parameters (TimingParameters):
                An instance of `TimingParameters` containing aperture time and
                settle time settings.
        """
        self.session.aperture_time = parameters.aperture_time_seconds
        self.session.settle_time = parameters.settle_time_seconds

    def acquire_measurement(
        self, resolution_in_digits: float
    ) -> ResistanceMeasurementResultData:
        """Acquires and formats the measurement result data.

        Args:
            resolution_in_digits (float):
                The resolution in digits used for formatting the measured value.

        Returns:
            ResistanceMeasurementResultData:
                An instance of `ResistanceMeasurementResultData` containing:
                - dmm_execution_settings: Dictionary with keys 'Function', 'Range',
                  'Resolution_in_Digits', 'Aperture_Time', and 'Settle_Time'
                - measurement: Dictionary with keys 'Measured_Value', 'Unit', and
                  'Formatted_Measurement'
        """
        measurement = FormatMeasurement.measurement(
            resolution_in_digits=resolution_in_digits,
            measured_value=self.session.read(),
            measurement_function=self.session.function,
        )
        aperture_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.aperture_time, 3)
        )
        settle_time = "{}{}".format(
            *FormatMeasurement.format_with_si_prefix(self.session.settle_time.total_seconds(), 3)
        )
        dmm_execution_settings = {
            "Function": self.session.function.name,
            "Range": self.session.range,
            "Digits_Resolution": self.session.resolution_digits,
            "Aperture_Time(s)": aperture_time,
            "Settle_Time(s)": settle_time,
            "Minimum_Frequency(Hz)": self.session.ac_min_freq,
            "Absolute_Resolution": self.session.resolution_absolute,
            "Input_Resistance(Ohm)": self.session.input_resistance,
            "Auto_Range_Value": self.session.auto_range_value,
        }
        return ResistanceMeasurementResultData(
            dmm_execution_settings=dmm_execution_settings, measurement=measurement
        )
