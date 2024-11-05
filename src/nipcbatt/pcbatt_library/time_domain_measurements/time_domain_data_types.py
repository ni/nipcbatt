# pylint: disable=C0301
""" Time Domain data types """

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


class TimeDomainMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Time domain measurement."""

    def __init__(
        self,
        global_channel_parameters: VoltageRangeAndTerminalParameters,
        specific_channels_parameters: List[VoltageMeasurementChannelAndTerminalRangeParameters],
        measurement_options: MeasurementOptions,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `TimeDomainMeasurementConfiguration` with specific values.

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
                contains objects that are not type of VoltageMeasurementChannelAndTerminalRangeParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
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


class TimeDomainMeasurementResultData(PCBATestToolkitData):
    """Defines voltage Time domain measurement results obtained after waveform analysis."""

    def __init__(
        self,
        waveforms: List[AnalogWaveform],
        acquisition_duration_seconds: float,
        mean_dc_voltage_values_volts: List[float],
        vpp_amplitudes_volts: List[float],
        voltage_waveforms_frequencies_hertz: List[float],
        voltage_waveforms_periods_seconds: List[float],
        voltage_waveforms_duty_cycles_percent: List[float],
    ) -> None:
        """Initializes an instance of
        `TimeDomainMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement and used to compute DC-RMS voltage.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            mean_dc_voltage_values_volts (List[float]):
                The list of mean DC voltages computed for all configured channels, expressed in Volts.
            vpp_amplitudes_volts (List[float]):
                The list of peak to peak voltage amplitudes computed for all configured channels, expressed in Volts.
            voltage_waveforms_frequencies_hertz (List[float]):
                The list of voltage waveforms frequencies computed for all configured channels, expressed in Hertz.
            voltage_waveforms_periods_seconds (List[float]):
                The list of voltage waveforms periods computed for all configured channels, expressed in seconds.
            voltage_waveforms_duty_cycles_percent (List[float]):
                The list of voltage waveforms duty cycles computed for all configured channels, expressed in %.

        Raises:
            TypeError:
                Raised when `waveforms` contains objects that are not `AnalogWaveform`,
                `mean_dc_voltage_values_volts` contains objects that are not `float`,
                `vpp_amplitudes_volts` contains objects that are not `float`,
                `voltage_waveforms_frequencies_hertz` contains objects that are not `float`,
                `voltage_waveforms_periods_seconds` contains objects that are not `float`,
                `voltage_waveforms_duty_cycles_percent` contains objects that are not `float`.
            ValueError:
                Raised when `waveforms` is None or empty.
        """
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))

        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(
            input_list=mean_dc_voltage_values_volts, expected_type=float
        )
        Guard.all_elements_are_of_same_type(input_list=vpp_amplitudes_volts, expected_type=float)
        Guard.all_elements_are_of_same_type(
            input_list=voltage_waveforms_frequencies_hertz, expected_type=float
        )
        Guard.all_elements_are_of_same_type(
            input_list=voltage_waveforms_periods_seconds, expected_type=float
        )
        Guard.all_elements_are_of_same_type(
            input_list=voltage_waveforms_duty_cycles_percent, expected_type=float
        )

        self._waveforms = waveforms
        self._acquisition_duration_seconds = acquisition_duration_seconds
        self._mean_dc_voltage_values_volts = mean_dc_voltage_values_volts
        self._vpp_amplitudes_volts = vpp_amplitudes_volts
        self._voltage_waveforms_frequencies_hertz = voltage_waveforms_frequencies_hertz
        self._voltage_waveforms_periods_seconds = voltage_waveforms_periods_seconds
        self._voltage_waveforms_duty_cycles_percent = voltage_waveforms_duty_cycles_percent

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute time domain results.
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
    def mean_dc_voltage_values_volts(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of mean DC voltages computed for all configured channels, expressed in Volts.
        """
        return self._mean_dc_voltage_values_volts

    @property
    def vpp_amplitudes_volts(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of peak to peak voltage amplitudes computed for all configured channels, expressed in Volts.
        """
        return self._vpp_amplitudes_volts

    @property
    def voltage_waveforms_frequencies_hertz(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of voltage waveforms frequencies computed for all configured channels, expressed in Hertz.
        """
        return self._voltage_waveforms_frequencies_hertz

    @property
    def voltage_waveforms_periods_seconds(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of voltage waveforms periods computed for all configured channels, expressed in seconds.
        """
        return self._voltage_waveforms_periods_seconds

    @property
    def voltage_waveforms_duty_cycles_percent(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of voltage waveforms duty cycles computed for all configured channels, expressed in %.
        """
        return self._voltage_waveforms_duty_cycles_percent
