# pylint: disable=W0707, W0719, W0702, W0212
"""Defines the base classes used by PCBA Test Toolkit data types"""

import json

from nipcbatt.pcbatt_utilities.reflection_utilities import (
    convert_for_json_serialization,
    enumerate_properties,
)


class PCBATestToolkitData:
    """Base class that defines methods for all building block data."""

    def __repr__(self) -> str:
        """Called when repr() is invoked on the `PCBATestToolkitData`object

        Returns:
            str: The string representing the object.
        """
        return self._to_json_representation()

    def __str__(self) -> str:
        """Called when str() is invoked on the `PCBATestToolkitData`object

        Returns:
            str: The string representing the object.
        """
        return self._to_json_representation()

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `PCBATestToolkitData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`
                (e.g. all properties defined in self object are equal to those of value_to_compare).
        """
        if isinstance(value_to_compare, self.__class__):
            return all(
                property_value == property_value_of_value_to_compare
                for (_, property_value), (_, property_value_of_value_to_compare) in zip(
                    enumerate_properties(self), enumerate_properties(value_to_compare)
                )
            )

        return False

    def _to_json_representation(self) -> str:
        return json.dumps(
            convert_for_json_serialization(self),
            indent=4,
        ).replace("\\n", "\n")
