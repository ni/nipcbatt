"""Defines a set of exceptions that can be raised by analysis module."""


class PCBATTAnalysisException(Exception):
    """Defines base class for all exception raised by nipcatt.pcbatt_analysis modules."""

    def __init__(self, message: str):
        super().__init__(message)


class PCBATTAnalysisLoadNativeLibraryFailedException(PCBATTAnalysisException):
    """Defines exception raised by nipcatt.pcbatt_analysis modules,
    when loading native library file fails for any reason."""


class PCBATTAnalysisCallNativeLibraryFailedException(PCBATTAnalysisException):
    """Defines exception raised by nipcatt.pcbatt_analysis modules,
    when calling native library function fails for any reason."""
