"""Static digital state  data types"""

from typing import Dict, List

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateMeasurementResultData(PCBATestToolkitData):
    """Defines parameters used for configuration of static digital state measurements"""

    def __init__(self, digital_states: List[bool], channel_identifiers: List[str]) -> None:
        """Initializes an instance of `StaticDigitalStateMeasurementResultData'
        with specific values

        Args:
            digital_states (array of boolean):
                The boolean state of each corresponding channel in the measurement
            channel_identifiers (array of string):
                The channel ID of each channel in the measurement
        """

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
        """
        return self._digital_states

    @property
    def channel_identifiers(self) -> List[str]:
        """:type: array of 'str': Identifies each channel"""
        return self._channel_identifiers

    @property
    def states_per_channels(self) -> Dict[str, bool]:
        """:type: dictionary of 'str', 'bool' pairs
            maps each channel to its current state

        Returns:
            Dict[str, bool]: mapping of channel to digital state
        """
        return self._states_per_channels
