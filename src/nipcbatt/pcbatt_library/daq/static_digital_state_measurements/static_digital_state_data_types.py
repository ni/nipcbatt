"""Static digital state  data types"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (149 > 100 characters) (auto-generated noqa)

from typing import Dict, List

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateMeasurementResultData(PCBATestToolkitData):
    """Defines parameters used for configuration of static digital state measurements"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (199 > 100 characters) (auto-generated noqa)

    def __init__(self, digital_states: List[bool], channel_identifiers: List[str]) -> None:
        """Initializes an instance of `StaticDigitalStateMeasurementResultData'
        with specific values

        Args:
            digital_states (array of boolean):
                The boolean state of each corresponding channel in the measurement
            channel_identifiers (array of string):
                The channel ID of each channel in the measurement
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input verification
        Guard.is_not_none(digital_states, nameof(digital_states))
        Guard.is_not_none(channel_identifiers, nameof(channel_identifiers))
        Guard.have_same_size(
            digital_states,
            nameof(digital_states),
            channel_identifiers,
            nameof(channel_identifiers),
        )

        # generate states_per_channels
        state_map: Dict[str, bool] = {}
        for i, state in enumerate(digital_states):
            state_map[channel_identifiers[i]] = state

        # class properties
        self._digital_states = digital_states
        self._channel_identifiers = channel_identifiers
        self._states_per_channels = state_map

    @property
    def digital_states(self) -> List[bool]:
        """
        :type: array of 'bool': Holds the state of each channel
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._digital_states

    @property
    def channel_identifiers(self) -> List[str]:
        """:type: array of 'str': Identifies each channel"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return self._channel_identifiers

    @property
    def states_per_channels(self) -> Dict[str, bool]:
        """:type: dictionary of 'str', 'bool' pairs
            maps each channel to its current state

        Returns:
            Dict[str, bool]: mapping of channel to digital state
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self._states_per_channels
