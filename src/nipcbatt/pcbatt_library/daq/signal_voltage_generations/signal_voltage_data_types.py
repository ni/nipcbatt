""" Signal Voltage Generation data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (155 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class ToneParameters(PCBATestToolkitData):
    """Defines the settings of a tone used to generate a signal."""

    def __init__(
        self,
        tone_frequency_hertz: float,
        tone_amplitude_volts: float,
        tone_phase_radians: float,
    ) -> None:
        """Initializes an instance of `ToneParameters` with specific values.

        Args:
            tone_frequency_hertz (float):
                The frequency value of the tone, in Hertz
            tone_amplitude_volts (float):
                The amplitude value of the tone, in Volts
            tone_phase_radians (float):
                The phase value of the tone, in Radians
        """
        Guard.is_greater_than_zero(tone_frequency_hertz, nameof(tone_frequency_hertz))
        Guard.is_greater_than_zero(tone_amplitude_volts, nameof(tone_amplitude_volts))

        self._tone_frequency_hertz = tone_frequency_hertz
        self._tone_amplitude_volts = tone_amplitude_volts
        self._tone_phase_radians = tone_phase_radians

    @property
    def tone_frequency_hertz(self) -> float:
        """Gets the frequency value of the tone, in Hertz."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

        return self._tone_frequency_hertz

    @property
    def tone_amplitude_volts(self) -> float:
        """Gets the amplitude value of the tone, in Volts"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (248 > 100 characters) (auto-generated noqa)

        return self._tone_amplitude_volts

    @property
    def tone_phase_radians(self) -> float:
        """Gets the phase value of the tone, in Radians."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (145 > 100 characters) (auto-generated noqa)

        return self._tone_phase_radians


class SignalVoltageGenerationTimingParameters(PCBATestToolkitData):
    """Defines the settings of sample clock timing for signal voltage generation."""

    def __init__(
        self,
        sample_clock_source: str,
        sampling_rate_hertz: int,
        generated_signal_duration_seconds: float,
    ) -> None:
        """Used to initialize an instance of `SampleClockTimingParameters`.

        Args:
            sample_clock_source (str): The source of the clock.
            sampling_rate_hertz (int): The sampling rate (in Hz).
            generated_signal_duration_seconds (float):
                The duration in seconds for which the signal needs to be generated.

        Raises:
            ValueError:
                Raised if `sample_clock_source` is None or empty or white space,
                if `sampling_rate_hertz` is less than or equal to zero.
                If the `generated_signal_duration_seconds' is less than or equal to zero.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(sample_clock_source, nameof(sample_clock_source))
        Guard.is_greater_than_zero(sampling_rate_hertz, nameof(sampling_rate_hertz))
        Guard.is_greater_than_zero(
            generated_signal_duration_seconds, nameof(generated_signal_duration_seconds)
        )

        self._sample_clock_source = sample_clock_source
        self._sampling_rate_hertz = sampling_rate_hertz
        self._generated_signal_duration_seconds = generated_signal_duration_seconds

    @property
    def sample_clock_source(self) -> str:
        """Gets the source of the clock."""
        return self._sample_clock_source

    @property
    def sampling_rate_hertz(self) -> int:
        """Gets the sampling rate (in Hz)."""
        return self._sampling_rate_hertz

    @property
    def generated_signal_duration_seconds(self) -> float:
        """Gets the duration of the generated signal voltage."""
        return self._generated_signal_duration_seconds


class SignalVoltageGenerationSineWaveParameters(PCBATestToolkitData):
    """Defines the parameters used to configure generation of sine wave signal voltage."""

    def __init__(
        self,
        generated_signal_offset_volts: float,
        generated_signal_tone_parameters: ToneParameters,
    ) -> None:
        """Initializes an instance of `SignalVoltageGenerationSineWaveParameters` with specific values.

        Args:
            generated_signal_offset_volts (float):
                The offset of the generated signal voltage.
            generated_signal_tone_parameters (ToneParameters):
                The tone settings of the generated signal.

        Raises:
            ValueError:
                if the `generated_signal_tone_parameters' is None
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            generated_signal_tone_parameters, nameof(generated_signal_tone_parameters)
        )

        self._generated_signal_offset_volts = generated_signal_offset_volts
        self._generated_signal_tone_parameters = generated_signal_tone_parameters

    @property
    def generated_signal_offset_volts(self) -> float:
        """Gets the offset of the generated signal voltage."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (148 > 100 characters) (auto-generated noqa)

        return self._generated_signal_offset_volts

    @property
    def generated_signal_tone_parameters(self) -> ToneParameters:
        """Gets the tone settings of the generated signal"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (248 > 100 characters) (auto-generated noqa)

        return self._generated_signal_tone_parameters


class SignalVoltageGenerationSquareWaveParameters(PCBATestToolkitData):
    """Defines the parameters used to configure generation of square wave signal voltage."""

    def __init__(
        self,
        generated_signal_offset_volts: float,
        generated_signal_frequency_hertz: float,
        generated_signal_amplitude_volts: float,
        generated_signal_duty_cycle_percent: float,
        generated_signal_phase_radians: float,
    ) -> None:
        """Initializes an instance of `SignalVoltageGenerationSquareWaveParameters` with specific values.

        Args:
            generated_signal_offset_volts (float):
                The offset of the generated signal voltage in volts.
            generated_signal_frequency_hertz (float):
                The frequency value of the square wave, in Hertz
            generated_signal_amplitude_volts (float):
                The amplitude value of the square wave, in volts
            generated_signal_duty_cycle_percent (float):
                The duty cycle of the square wave, in percent.
            generated_signal_phase_radians(float):
                The phase value of the square wave, in radians

        Raises:
            ValueError:
                If the value of `generated_signal_frequency_hertz` is less than or equal to 0
                If the value of `generated_signal_amplitude_volts` is less than or equal to 0
                If the value of `generated_signal_duty_cycle_percent` is not between 0 and 100
        """  # noqa: W505 - doc line too long (105 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(
            generated_signal_frequency_hertz, nameof(generated_signal_frequency_hertz)
        )
        Guard.is_greater_than_zero(
            generated_signal_amplitude_volts, nameof(generated_signal_amplitude_volts)
        )
        Guard.is_within_limits_excluded(
            value=generated_signal_duty_cycle_percent,
            lower_limit=0,
            upper_limit=100,
            value_name=nameof(generated_signal_duty_cycle_percent),
        )

        self._generated_signal_offset_volts = generated_signal_offset_volts
        self._generated_signal_frequency_hertz = generated_signal_frequency_hertz
        self._generated_signal_amplitude_volts = generated_signal_amplitude_volts
        self._generated_signal_duty_cycle_percent = generated_signal_duty_cycle_percent
        self._generated_signal_phase_radians = generated_signal_phase_radians

    @property
    def generated_signal_offset_volts(self) -> float:
        """Gets the offset of the generated signal voltage."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (148 > 100 characters) (auto-generated noqa)

        return self._generated_signal_offset_volts

    @property
    def generated_signal_frequency_hertz(self) -> float:
        """Gets the frequency value of the square wave, in Hertz."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)

        return self._generated_signal_frequency_hertz

    @property
    def generated_signal_amplitude_volts(self) -> float:
        """Gets the amplitude value of the square wave, in Volts."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)

        return self._generated_signal_amplitude_volts

    @property
    def generated_signal_duty_cycle_percent(self) -> float:
        """Gets the duty cycle of the square wave, in percent."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (151 > 100 characters) (auto-generated noqa)

        return self._generated_signal_duty_cycle_percent

    @property
    def generated_signal_phase_radians(self) -> float:
        """Gets the phase value of the square wave, in radians."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (152 > 100 characters) (auto-generated noqa)

        return self._generated_signal_phase_radians


class SignalVoltageGenerationMultipleTonesWaveParameters(PCBATestToolkitData):
    """Defines the parameters used to configure generation of (multi-tone)
    signal voltage with one or more sine waves (sum of sinusoid)."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (361 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        generated_signal_offset_volts: float,
        generated_signal_amplitude_volts: float,
        multiple_tones_parameters: List[ToneParameters],
    ) -> None:
        """Initializes an instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
         with specific values.

        Args:
            generated_signal_offset_volts (float):
                The offset of the generated signal voltage.
            generated_signal_amplitude_volts (float):
                The Amplitude value used to rescale the resulted sine wave.
            multiple_tones_parameters (List[ToneParameters]):
                The List of `ToneParameters` representing the settings of each
                 sine wave in generated signal voltage.

        Raises:
            ValueError:
                If the `generated_signal_amplitude_volts' is less than or equal to zero.
                if the `generated_signal_tone_parameters' is None or empty List
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        Guard.is_greater_than_zero(
            generated_signal_amplitude_volts, nameof(generated_signal_amplitude_volts)
        )

        Guard.is_not_none(multiple_tones_parameters, nameof(multiple_tones_parameters))
        Guard.is_not_empty(multiple_tones_parameters, nameof(multiple_tones_parameters))

        self._generated_signal_offset_volts = generated_signal_offset_volts
        self._generated_signal_amplitude_volts = generated_signal_amplitude_volts
        self._multiple_tones_parameters = multiple_tones_parameters

    @property
    def generated_signal_offset_volts(self) -> float:
        """Gets the offset of the generated signal voltage."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (148 > 100 characters) (auto-generated noqa)

        return self._generated_signal_offset_volts

    @property
    def generated_signal_amplitude_volts(self) -> float:
        """Gets the Amplitude value used to rescale the resulted sine wave."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)

        return self._generated_signal_amplitude_volts

    @property
    def multiple_tones_parameters(self) -> List[ToneParameters]:
        """Gets the List `ToneSettings` representing the settings of
        each sine wave in generated signal voltage."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (424 > 100 characters) (auto-generated noqa)

        return self._multiple_tones_parameters


class SignalVoltageGenerationSineWaveConfiguration(PCBATestToolkitData):
    """Defines the parameters used for configuration of sine wave signal generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (197 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_generation_range_parameters: VoltageGenerationChannelParameters,
        waveform_parameters: SignalVoltageGenerationSineWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `SignalVoltageGenerationSineWaveConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
            waveform_parameters (SignalVoltageGenerationSineWaveParameters):
                An instance of `SignalVoltageGenerationSineWaveParameters`
                used to configure the generation of sine wave signal voltage.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of SignalVoltageGenerationTimingParameters that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            voltage_generation_range_parameters,
            nameof(voltage_generation_range_parameters),
        )
        Guard.is_not_none(
            waveform_parameters,
            nameof(waveform_parameters),
        )
        Guard.is_not_none(
            timing_parameters,
            nameof(timing_parameters),
        )
        Guard.is_not_none(
            digital_start_trigger_parameters,
            nameof(digital_start_trigger_parameters),
        )

        self._voltage_generation_range_parameters = voltage_generation_range_parameters
        self._waveform_parameters = waveform_parameters
        self._timing_parameters = timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters:
        """
        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for signal voltage generation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_generation_range_parameters

    @property
    def waveform_parameters(
        self,
    ) -> SignalVoltageGenerationSineWaveParameters:
        """
        :class:`SignalVoltageGenerationSineWaveParameters`:
            Gets an instance of `SignalVoltageGenerationSineWaveParameters`
            used to configure the generation of sine wave signal voltage.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveform_parameters

    @property
    def timing_parameters(self) -> SignalVoltageGenerationTimingParameters:
        """
        :class:`SignalVoltageGenerationTimingParameters`:
            Gets a `SignalVoltageGenerationTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class SignalVoltageGenerationSquareWaveConfiguration(PCBATestToolkitData):
    """Defines the parameters used for configuration of square wave signal generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_generation_range_parameters: VoltageGenerationChannelParameters,
        waveform_parameters: SignalVoltageGenerationSquareWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `SignalVoltageGenerationSquareWaveConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
            waveform_parameters (SignalVoltageGenerationSquareWaveParameters):
                An instance of `SignalVoltageGenerationSquareWaveParameters`
                used to configure the generation of square wave signal voltage.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of SignalVoltageGenerationTimingParameters that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            voltage_generation_range_parameters,
            nameof(voltage_generation_range_parameters),
        )
        Guard.is_not_none(
            waveform_parameters,
            nameof(waveform_parameters),
        )
        Guard.is_not_none(
            timing_parameters,
            nameof(timing_parameters),
        )
        Guard.is_not_none(
            digital_start_trigger_parameters,
            nameof(digital_start_trigger_parameters),
        )

        self._voltage_generation_range_parameters = voltage_generation_range_parameters
        self._waveform_parameters = waveform_parameters
        self._timing_parameters = timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters:
        """
        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for signal voltage generation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_generation_range_parameters

    @property
    def waveform_parameters(
        self,
    ) -> SignalVoltageGenerationSquareWaveParameters:
        """
        :class:`SignalVoltageGenerationSquareWaveParameters`:
            Gets an instance of `SignalVoltageGenerationSquareWaveParameters`
            used to configure the generation of square wave signal voltage.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveform_parameters

    @property
    def timing_parameters(self) -> SignalVoltageGenerationTimingParameters:
        """
        :class:`SignalVoltageGenerationTimingParameters`:
            Gets a `SignalVoltageGenerationTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters


class SignalVoltageGenerationMultipleTonesConfiguration(PCBATestToolkitData):
    """Defines the parameters used for configuration of multi-tone sine wave signal generation"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (208 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        voltage_generation_range_parameters: VoltageGenerationChannelParameters,
        waveform_parameters: SignalVoltageGenerationMultipleTonesWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `SignalVoltageGenerationMultipleTonesConfiguration` with specific values.

        Args:
            voltage_generation_range_parameters (VoltageGenerationChannelParameters):
                An instance of `VoltageGenerationChannelParameters' used to configure the channels.
            waveform_parameters (SignalVoltageGenerationMultipleTonesWaveParameters):
                An instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
                used to configure the generation of sine wave signal voltage.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (112 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(
            voltage_generation_range_parameters,
            nameof(voltage_generation_range_parameters),
        )
        Guard.is_not_none(
            waveform_parameters,
            nameof(waveform_parameters),
        )
        Guard.is_not_none(
            timing_parameters,
            nameof(timing_parameters),
        )
        Guard.is_not_none(
            digital_start_trigger_parameters,
            nameof(digital_start_trigger_parameters),
        )

        self._voltage_generation_range_parameters = voltage_generation_range_parameters
        self._waveform_parameters = waveform_parameters
        self._timing_parameters = timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def voltage_generation_range_parameters(self) -> VoltageGenerationChannelParameters:
        """
        :class:`VoltageGenerationChannelParameters`:
            Gets an instance of `VoltageGenerationChannelParameters'
            that represents the terminal settings for all channel for signal voltage generation.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._voltage_generation_range_parameters

    @property
    def waveform_parameters(
        self,
    ) -> SignalVoltageGenerationMultipleTonesWaveParameters:
        """
        :class:`SignalVoltageGenerationMultipleTonesWaveParameters`:
            Gets an instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
            used to configure the generation of multi-tone sine wave signal voltage.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveform_parameters

    @property
    def timing_parameters(self) -> SignalVoltageGenerationTimingParameters:
        """
        :class:`SignalVoltageGenerationTimingParameters`:
            Gets a `SignalVoltageGenerationTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._digital_start_trigger_parameters
