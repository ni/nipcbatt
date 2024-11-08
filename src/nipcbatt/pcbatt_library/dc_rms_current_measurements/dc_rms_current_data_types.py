""" DC-RMS current data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (144 > 100 characters) (auto-generated noqa)

from typing import List

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementOptions,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcRmsCurrentMeasurementTerminalRangeParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal of all channels for DC-RMS Current measurement"""  # noqa: W505, D415 - doc line too long (106 > 100 characters) (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa)

    # The minimum value of shunt resitor value that Daqmx allows is 100e-9
    MINIMUM_ALLOWED_SHUNT_RESISTOR_VALUE_OHMS = 100e-9

    def __init__(
        self,
        terminal_configuration: nidaqmx.constants.TerminalConfiguration,
        range_min_amperes: float,
        range_max_amperes: float,
        shunt_resistor_ohms: float,
    ) -> None:
        """Initializes an instance of `DcRmsCurrentMeasurementTerminalRangeParameters` with specific values.

        Args:
            terminal_configuration (nidaqmx.constants.TerminalConfiguration):
                The settings of the terminal for all the current channels.
            range_min_amperes (float):
                The minimum current value im amperes expected for the measurement on the channel.
            range_max_amperes (float):
                The maximum current value in amperes expected for the measurement on the channel.
            shunt_resistor_ohms (float):
                The value in ohms of the external shunt resistor.

        Raises:
            ValueError when,
                    the value of `terminal_configuration` is set to None,
                    when `range_min_amperes` is greater or equal to `range_max_amperes`,
                    when `shunt_resistor_ohms` value is less than 'MINIMUM_ALLOWED_SHUNT_RESISTOR_VALUE_OHMS'.
        """  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(terminal_configuration, nameof(terminal_configuration))
        Guard.is_greater_than(
            value=range_max_amperes,
            expected_smaller_value=range_min_amperes,
            value_name=nameof(range_max_amperes),
        )
        Guard.is_greater_than_or_equal_to(
            value=shunt_resistor_ohms,
            expected_smaller_value=DcRmsCurrentMeasurementTerminalRangeParameters.MINIMUM_ALLOWED_SHUNT_RESISTOR_VALUE_OHMS,
            value_name=nameof(shunt_resistor_ohms),
        )

        self._terminal_configuration = terminal_configuration
        self._range_min_amperes = range_min_amperes
        self._range_max_amperes = range_max_amperes
        self._shunt_resistor_ohms = shunt_resistor_ohms

    @property
    def terminal_configuration(self) -> nidaqmx.constants.TerminalConfiguration:
        """
        :class:`nidaqmx.constants.TerminalConfiguration`:
            Gets the input terminal configuration parameter.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._terminal_configuration

    @property
    def range_min_amperes(self) -> float:
        """
        :type:`float`: Gets the minimum value expected for the measurement on the channel.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._range_min_amperes

    @property
    def range_max_amperes(self) -> float:
        """
        :type:`float`: Gets the maximum value expected for the measurement on the channel.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._range_max_amperes

    @property
    def shunt_resistor_ohms(self) -> float:
        """
        :type:`float`: Gets the value in ohms of an external shunt resistor.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._shunt_resistor_ohms


class DcRmsCurrentMeasurementChannelAndTerminalRangeParameters(PCBATestToolkitData):
    """Defines the parameters used to configure channels for DC-RMS Current measurement."""

    def __init__(
        self,
        channel_name: str,
        channel_parameters: DcRmsCurrentMeasurementTerminalRangeParameters,
    ) -> None:
        """Initializes an instance of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`
           with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (DcRmsCurrentMeasurementTerminalRangeParameters):
                An instance of `DcRmsCurrentMeasurementTerminalRangeParameters` that specifies
                the parameters used to configure the channel.

        Raises:
            ValueError when,
                    the value of `channel_name` is set to None or empty or whitespace,
                    when `channel_parameters` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_not_none(channel_parameters, nameof(channel_parameters))

        self._channel_name = channel_name
        self._channel_parameters = channel_parameters

    @property
    def channel_name(self) -> str:
        """
        :type:`str`: Gets the name of the channel to configure.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return self._channel_name

    @property
    def channel_parameters(self) -> DcRmsCurrentMeasurementTerminalRangeParameters:
        """
        :class:`DcRmsCurrentMeasurementTerminalRangeParameters`:
            Gets an instance of `DcRmsCurrentMeasurementTerminalRangeParameters` that specifies
            the parameters used to configure the channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._channel_parameters


class DcRmsCurrentMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the DC-RMS current measurement."""

    def __init__(
        self,
        global_channel_parameters: DcRmsCurrentMeasurementTerminalRangeParameters,
        specific_channels_parameters: List[
            DcRmsCurrentMeasurementChannelAndTerminalRangeParameters
        ],
        measurement_options: MeasurementOptions,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `DcRmsCurrentMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (DcRmsCurrentMeasurementTerminalRangeParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (DcRmsCurrentMeasurementChannelAndTerminalRangeParameters):
                The list of instances of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` used to configure channels.
            measurement_options (MeasurementOptions):
                An instance of `MeasurementOptions` that represents the settings of options used for execution.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `measurement_options` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (127 > 100 characters) (auto-generated noqa)

        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=DcRmsCurrentMeasurementChannelAndTerminalRangeParameters,
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_options = measurement_options
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> DcRmsCurrentMeasurementTerminalRangeParameters:
        """
        :class:`DcRmsCurrentMeasurementTerminalRangeParameters`:
            Gets the settings of terminal for all channels."""  # noqa: D205, D209, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (444 > 100 characters) (auto-generated noqa)
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[DcRmsCurrentMeasurementChannelAndTerminalRangeParameters]:
        """
        :class:`List[DcRmsCurrentMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters` used to configure channels.
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


class DcRmsCurrentMeasurementResultData(PCBATestToolkitData):
    """Defines the result values computed during analysis procedure for DC-RMS Current measurement."""  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        waveforms: list[AnalogWaveform],
        acquisition_duration_seconds: float,
        dc_values_amperes: list[float],
        rms_values_amperes: list[float],
    ) -> None:
        """Initializes an instance of
        `DcRmsCurrentMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement and used to compute DC-RMS current.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            dc_values_amperes (List[float]):
                The list of DC value of the current computed for all configured channels, expressed in amperes.
            rms_values_amperes (List[float]):
                The list of RMS value of the current computed for all configured channels, expressed in amperes.

        Raises:
            TypeError when,
                `waveforms` containes objects that are not `AnalogWaveform',
                `dc_values_amperes` contains objects that are not `float',
                `rms_values_amperes` contains objects that are not `float'.
            ValueError when,
                `waveforms` is None.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (120 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(input_list=dc_values_amperes, expected_type=float)
        Guard.all_elements_are_of_same_type(input_list=rms_values_amperes, expected_type=float)

        self._waveforms = waveforms
        self._acquisition_duration_seconds = acquisition_duration_seconds
        self._dc_values_amperes = dc_values_amperes
        self._rms_values_amperes = rms_values_amperes

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets the list of waveforms acquired from channels defined
            for measurement and used to compute DC-RMS current.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._waveforms

    @property
    def acquisition_duration_seconds(self) -> float:
        """
        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._acquisition_duration_seconds

    @property
    def dc_values_amperes(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of DC current computed for all configured channels, expressed in amperes.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._dc_values_amperes

    @property
    def rms_values_amperes(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of RMS current computed for all configured channels, expressed in amperes.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._rms_values_amperes
