"""Defines a set of exceptions that can be raised by pcbatt communication module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)


class PCBATTCommunicationException(  # noqa: N818 - exception name 'PCBATTCommunicationException' should be named with an Error suffix (auto-generated noqa)
    Exception
):
    """Defines base class for all exception raised by
    nipcatt.pcbatt_communication_library package."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (345 > 100 characters) (auto-generated noqa)

    def __init__(  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self, message: str
    ):
        super().__init__(message)
