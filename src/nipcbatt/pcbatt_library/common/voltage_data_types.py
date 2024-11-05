"""Defines datatypes that are common to DC-RMS Voltage,
   Frequency Domain and Time Domain Measurements."""

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class VoltageRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for DC-RMS Voltage measurement."""

    def __init__(
        self,
        terminal_configuration: nidaqmx.constants.TerminalConfiguration,
        range_min_volts: float,
        range_max_volts: float,
    ) -> None:
        """Initializes an instance of `VoltageRangeAndTerminalParameters` with specific values.

        Args:
            terminal_configuration (nidaqmx.constants.TerminalConfiguration):
                The input terminal configuration parameter.
            range_min_volts (float):
                The minimum value expected for the measurement on the channel.
            range_max_volts (float):
                The maximum value expected for the measurement on the channel.
        """
        self._terminal_configuration = terminal_configuration
        self._range_min_volts = range_min_volts
        self._range_max_volts = range_max_volts

    @property
    def terminal_configuration(self) -> nidaqmx.constants.TerminalConfiguration:
        """
        :class:`nidaqmx.constants.TerminalConfiguration`:
            Gets the input terminal configuration parameter.
        """
        return self._terminal_configuration

    @property
    def range_min_volts(self) -> float:
        """
        :type:`float`: Gets the minimum value expected for the measurement on the channel.
        """
        return self._range_min_volts

    @property
    def range_max_volts(self) -> float:
        """
        :type:`float`: Gets the maximum value expected for the measurement on the channel.
        """
        return self._range_max_volts


class VoltageMeasurementChannelAndTerminalRangeParameters(PCBATestToolkitData):
    """Defines the parameters used to configure channels for DC-RMS Voltage measurement."""

    def __init__(
        self,
        channel_name: str,
        channel_parameters: VoltageRangeAndTerminalParameters,
    ) -> None:
        """Initializes an instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
           with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (VoltageRangeAndTerminalParameters):
                An instance of `VoltageRangeAndTerminalParameters` that specifies
                the parameters used to configure the channel.
        """
        self._channel_name = channel_name
        self._channel_parameters = channel_parameters

    @property
    def channel_name(self) -> str:
        """
        :type:`str`: Gets the name of the channel to configure.
        """
        return self._channel_name

    @property
    def channel_parameters(self) -> VoltageRangeAndTerminalParameters:
        """
        :class:`VoltageRangeAndTerminalParameters`:
            Gets an instance of `VoltageRangeAndTerminalParameters` that specifies
            the parameters used to configure the channel.
        """
        return self._channel_parameters


class VoltageGenerationChannelParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal of all channels for Voltage Generation"""

    def __init__(
        self,
        range_min_volts: float,
        range_max_volts: float,
    ) -> None:
        """Initializes an instance of `VoltageGenerationChannelParameters` with specific values.

        Args:
            range_min_volts (float):
                Specifies the minimum voltage you expect to generate.
            range_max_volts (float):
                Specifies the maximum voltage you expect to generate.

        Raises:
            ValueError:
                Raised when `range_min_volts' is greater than or equal to `range_max_volts`.
        """
        Guard.is_less_than(range_min_volts, range_max_volts, nameof(range_min_volts))

        self._range_min_volts = range_min_volts
        self._range_max_volts = range_max_volts

    @property
    def range_min_volts(self) -> float:
        """
        :type:`float`: Gets the minimum voltage you expect to generate on the channels.
        """
        return self._range_min_volts

    @property
    def range_max_volts(self) -> float:
        """
        :type:`float`: Gets the maximum voltage you expect to generate on the channels.
        """
        return self._range_max_volts
