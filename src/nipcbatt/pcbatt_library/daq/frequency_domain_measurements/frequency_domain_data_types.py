""" Frequency domain data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (146 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AmplitudeSpectrum,
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


class FrequencyDomainMeasurementConfiguration(PCBATestToolkitData):
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
        `FrequencyDomainMeasurementConfiguration` with specific values.

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
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (101 > 100 characters) (auto-generated noqa)
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
            Gets the settings of terminal for all channels."""  # noqa: D205, D209, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (444 > 100 characters) (auto-generated noqa)
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[VoltageMeasurementChannelAndTerminalRangeParameters]:
        """
        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `VoltageMeasurementChannelAndTerminalRangeParameters` used to configure channels.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._specific_channels_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementOptions`:
            Gets a `MeasurementOptions` instance
            that represents the settings of options used for execution.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class MultipleTonesMeasurementResultData(PCBATestToolkitData):
    """Defines multiple tones measurement results obtained after waveform analysis."""

    def __init__(
        self,
        tones_frequencies_hertz: List[float],
        tones_amplitudes_volts: List[float],
    ) -> None:
        """Initializes an instance of "MultipleTonesMeasurementResultData" with specific values.

        Args:
            tones_frequencies_hertz (List[float]):
                A list of frequencies of detected tones for all analyzed waveforms.
            tones_amplitudes_volts (List[float]):
                A list of voltage peak amplitudes of detected tones for all analyzed waveforms.

        Raises:
            TypeError: Raised when,
                `tones_frequencies_hertz` containes objects that are not `float',
                `tones_amplitudes_volts` contains objects that are not `float'.

            ValueError: Raised when,
                `tones_frequencies_hertz` is None,
                `tones_amplitudes_volts` is None,
                `tones_frequencies_hertz` and `tones_amplitudes_volts` lists have different lengths.
        """
        Guard.is_not_none(tones_frequencies_hertz, nameof(tones_frequencies_hertz))
        Guard.is_not_none(tones_amplitudes_volts, nameof(tones_amplitudes_volts))
        Guard.all_elements_are_of_same_type(input_list=tones_frequencies_hertz, expected_type=float)
        Guard.all_elements_are_of_same_type(input_list=tones_amplitudes_volts, expected_type=float)
        Guard.have_same_size(
            first_iterable_instance=tones_amplitudes_volts,
            first_iterable_name=nameof(tones_amplitudes_volts),
            second_iterable_instance=tones_frequencies_hertz,
            second_iterable_name=nameof(tones_frequencies_hertz),
        )

        self._tones_frequencies_hertz = tones_frequencies_hertz
        self._tones_amplitudes_volts = tones_amplitudes_volts

    @property
    def tones_frequencies_hertz(self) -> List[float]:
        """
        :class:`List[float]`:
        Gets a List containing detected tones frequencies of all analyzed waveform.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._tones_frequencies_hertz

    @property
    def tones_amplitudes_volts(self) -> List[float]:
        """
        :class:`List[float]`:
        Gets a list containing detected tones peak amplitudes of all analyzed waveform.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._tones_amplitudes_volts


class FrequencyDomainMeasurementResultData(PCBATestToolkitData):
    """Defines frequency domain measurement results obtained after waveform analysis."""

    def __init__(
        self,
        waveforms: List[AnalogWaveform],
        magnitude_rms: List[AmplitudeSpectrum],
        magnitude_peak: List[AmplitudeSpectrum],
        detected_tones: List[MultipleTonesMeasurementResultData],
    ) -> None:
        """Initializes an instance of "FrequencyDomainMeasurementResultData" with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                A list of `AnalogWaveform` acquired from channels defined for measurement.
            magnitude_rms (List[AmplitudeSpectrum]):
                A list of `AmplitudeSpectrum` representing the frequency domain measurement RMS computed on all channels.
            magnitude_peak (List[AmplitudeSpectrum]):
                A list of `AmplitudeSpectrum` representing the frequency domain measurement Peak to Peak computed on all channels.
            detected_tones (List[MultipleTonesMeasurementResultData]):
                A list of `MultipleTonesMeasurementResultData` representing the detected tones in the waveform.

        Raises:
            TypeError: Raised when,
                `waveforms` contains objects that are not `AnalogWaveform`,
                `magnitude_rms' contains objects that are not 'AmplitudeSpectrum`,
                `magnitude_peak` contains objects that are not 'AmplitudeSpectrum`,
                `detected_tones` contains objects that are not `MultipleTonesMeasurementResultData`

            ValueError: Raised when,
                `waveforms` is None or empty.
        """  # noqa: W505 - doc line too long (121 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))

        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(
            input_list=magnitude_peak, expected_type=AmplitudeSpectrum
        )
        Guard.all_elements_are_of_same_type(
            input_list=magnitude_rms, expected_type=AmplitudeSpectrum
        )
        Guard.all_elements_are_of_same_type(
            input_list=detected_tones, expected_type=MultipleTonesMeasurementResultData
        )

        self._waveforms = waveforms
        self._magnitude_rms = magnitude_rms
        self._magnitude_peak = magnitude_peak
        self._detected_tones = detected_tones

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute frequency domain results.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveforms

    @property
    def magnitude_rms(self) -> List[AmplitudeSpectrum]:
        """
        :calss: List[AmplitudeSpectrum]:
            Gets an array of RMS based spectrums computed for each channel waveform in `waveforms`.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._magnitude_rms

    @property
    def magnitude_peak(self) -> List[AmplitudeSpectrum]:
        """
        :calss: List[AmplitudeSpectrum]:
            Gets an array of Peak to Peak based spectrums computed for each channel waveform in `waveforms`.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (108 > 100 characters) (auto-generated noqa)
        return self._magnitude_peak

    @property
    def detected_tones(self) -> List[MultipleTonesMeasurementResultData]:
        """
        :calss: List[MultipleTonesMeasurementResultData]:
            Gets an array of multiple tones analysis results for each waveform contained in `waveforms`.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)
        return self._detected_tones
