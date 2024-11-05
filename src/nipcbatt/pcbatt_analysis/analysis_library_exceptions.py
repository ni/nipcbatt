"""Defines a set of exceptions that can be raised by analysis module."""


class PCBATTAnalysisException(  # noqa: N818 - exception name 'PCBATTAnalysisException' should be named with an Error suffix (auto-generated noqa)
    Exception
):
    """Defines base class for all exception raised by nipcatt.pcbatt_analysis modules."""

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, message: str
    ):
        super().__init__(message)


class PCBATTAnalysisLoadNativeLibraryFailedException(  # noqa: N818 - exception name 'PCBATTAnalysisLoadNativeLibraryFailedException' should be named with an Error suffix (auto-generated noqa)
    PCBATTAnalysisException
):
    """Defines exception raised by nipcatt.pcbatt_analysis modules,
    when loading native library file fails for any reason."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (354 > 100 characters) (auto-generated noqa)


class PCBATTAnalysisCallNativeLibraryFailedException(  # noqa: N818 - exception name 'PCBATTAnalysisCallNativeLibraryFailedException' should be named with an Error suffix (auto-generated noqa)
    PCBATTAnalysisException
):
    """Defines exception raised by nipcatt.pcbatt_analysis modules,
    when calling native library function fails for any reason."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
