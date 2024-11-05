# pylint: disable=C0301
""" DC-RMS Voltage data types """

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcRmsVoltageMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of DC-RMS voltage measurement."""

    def __init__(
        self,
        global_channel_parameters: VoltageRangeAndTerminalParameters,
        specific_channels_parameters: List[VoltageMeasurementChannelAndTerminalRangeParameters],
        measurement_options: MeasurementOptions,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `DcRmsVoltageMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (VoltageRangeAndTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[VoltageMeasurementChannelAndTerminalRangeParameters]):
                The list of instances of `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of `VoltageMeasurementChannelAndTerminalRangeParameters`.
            ValueError:
                Raised when
                `specific_channels_parameters` is None,
                `global_channel_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None.
        """
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=VoltageMeasurementChannelAndTerminalRangeParameters,
        )
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_options = measurement_options
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> VoltageRangeAndTerminalParameters:
        """
        :class:`VoltageRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels."""
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[VoltageMeasurementChannelAndTerminalRangeParameters]:
        """
        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        """
        return self._specific_channels_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        """
        return self._measurement_options

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """
        return self._digital_start_trigger_parameters


class DcRmsVoltageMeasurementResultData(PCBATestToolkitData):
    """Defines voltage DC-RMS results obtained after waveform analysis."""

    def __init__(
        self,
        waveforms: List[AnalogWaveform],
        acquisition_duration_seconds: float,
        dc_values_volts: List[float],
        rms_values_volts: List[float],
    ) -> None:
        """Initializes an instance of
        `DcRmsVoltageMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement and used to compute DC-RMS voltage.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            dc_values_volts (List[float]):
                The list of DC voltages computed for all configured channels, expressed in Volts.
            rms_values_volts (List[float]):
                The list of RMS voltages computed for all configured channels, expressed in Volts.

        Raises:
            ValueError:
                Raised when `waveforms` is None or empty.
            TypeError:
                Raised when `waveforms` contains objects that are not `AnalogWaveform`,
                `dc_values_volts` contains objects that are not `float`,
                `rms_values_volts` contains objects that are not `float`
        """
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))
        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(input_list=dc_values_volts, expected_type=float)
        Guard.all_elements_are_of_same_type(input_list=rms_values_volts, expected_type=float)

        self._waveforms = waveforms
        self._acquisition_duration_seconds = acquisition_duration_seconds
        self._dc_values_volts = dc_values_volts
        self._rms_values_volts = rms_values_volts

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute DC-RMS voltage.
        """
        return self._waveforms

    @property
    def acquisition_duration_seconds(self) -> float:
        """
        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        """
        return self._acquisition_duration_seconds

    @property
    def dc_values_volts(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of DC voltages computed for all configured channels, expressed in Volts.
        """
        return self._dc_values_volts

    @property
    def rms_values_volts(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of RMS voltages computed for all configured channels, expressed in Volts.
        """
        return self._rms_values_volts
