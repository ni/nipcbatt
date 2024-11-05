"""Defines a set of exceptions that can be raised by pcbatt communication module"""


class PCBATTCommunicationException(Exception):
    """Defines base class for all exception raised by
    nipcatt.pcbatt_communication_library package."""

    def __init__(self, message: str):
        super().__init__(message)
