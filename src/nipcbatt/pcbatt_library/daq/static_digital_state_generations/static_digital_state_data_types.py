""" Static Digital State Generation data types"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (160 > 100 characters) (auto-generated noqa)

from typing import List

from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class StaticDigitalStateGenerationConfiguration(PCBATestToolkitData):
    """Defines the values used in the creation of Static Digital State Configuration"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)

    def __init__(self, data_to_write: List[bool]) -> None:
        """Initializes an instance of 'StaticDigitalStateGenerationConfiguration
           with specific values.

        Args:
            data_to_write (array of boolean):
                The boolean state of each channel to write to the hardware
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # Input validation
        Guard.is_not_none(data_to_write, nameof(data_to_write))
        Guard.is_not_empty(data_to_write, nameof(data_to_write))

        # generate states
        self._data_to_write = data_to_write

    @property
    def data_to_write(self) -> List[bool]:
        """
        :type: array of 'bool': Holds the state of the write values to the DO channels
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._data_to_write


class StaticDigitalStateGenerationData(PCBATestToolkitData):
    """Defines the values used in the production of Static Digital State Generation Data"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (202 > 100 characters) (auto-generated noqa)

    def __init__(self, channel_identifiers: List[str]) -> None:
        """Initializes an instance of StaticDigitalStateGenerationData with specific values.

        Args:
            channel_identifiers (array of string):
                The list of channels to which the data to write is written
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        # Input validation
        Guard.is_not_none(channel_identifiers, nameof(channel_identifiers))
        Guard.is_not_empty(channel_identifiers, nameof(channel_identifiers))

        # generate states
        self._channel_identifiers = channel_identifiers

    @property
    def channel_identifiers(self) -> List[str]:
        """
        :type: array of 'str': Holds the names of the digital output channels to write to
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._channel_identifiers
