""" Static Digital State Generation data types"""

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateGenerationConfiguration(PCBATestToolkitData):
    """Defines the values used in the creation of Static Digital State Configuration"""

    def __init__(self, data_to_write: List[bool]) -> None:
        """Initializes an instance of 'StaticDigitalStateGenerationConfiguration
           with specific values.

        Args:
            data_to_write (array of boolean):
                The boolean state of each channel to write to the hardware
        """

        # Input validation
        Guard.is_not_none(data_to_write, nameof(data_to_write))
        Guard.is_not_empty(data_to_write, nameof(data_to_write))

        # generate states
        self._data_to_write = data_to_write

    @property
    def data_to_write(self) -> List[bool]:
        """
        :type: array of 'bool': Holds the state of the write values to the DO channels
        """
        return self._data_to_write


class StaticDigitalStateGenerationData(PCBATestToolkitData):
    """Defines the values used in the production of Static Digital State Generation Data"""

    def __init__(self, channel_identifiers: List[str]) -> None:
        """Initializes an instance of StaticDigitalStateGenerationData with specific values.

        Args:
            channel_identifiers (array of string):
                The list of channels to which the data to write is written
        """

        # Input validation
        Guard.is_not_none(channel_identifiers, nameof(channel_identifiers))
        Guard.is_not_empty(channel_identifiers, nameof(channel_identifiers))

        # generate states
        self._channel_identifiers = channel_identifiers

    @property
    def channel_identifiers(self) -> List[str]:
        """
        :type: array of 'str': Holds the names of the digital output channels to write to
        """
        return self._channel_identifiers
