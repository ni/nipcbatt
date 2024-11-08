"""Holds base types of the package nipcbatt.pcbatt_analysis"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

import json

from nipcbatt.pcbatt_utilities.reflection_utilities import (
    convert_for_json_serialization,
)


class AnalysisLibraryElement:
    """Defines base class of analysis library elements."""

    def __repr__(self) -> str:
        """Called when repr() is invoked on the `AnalysisLibraryElement`object

        Returns:
            str: JSON string representing the object.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        return json.dumps(
            convert_for_json_serialization(self),
            indent=4,
        ).replace("\\n", "\n")

    def __str__(self) -> str:
        """Called when str() is invoked on the `AnalysisLibraryElement`object

        Returns:
            str: line string representing the object.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        cls = self.__class__
        return f"<{cls.__module__}.{cls.__qualname__} object at {id(self)}>"
