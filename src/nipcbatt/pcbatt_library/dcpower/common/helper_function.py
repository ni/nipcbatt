"""Helper functions for DC power instrument operations."""

import nidcpower


def set_output_enabled(
    session: nidcpower.Session,
    channel_name: str,
    enable_output: bool,
) -> None:
    """Enables or disables the output of a DC power channel.

    Accepts an existing DCPower session resource, retrieves 
    the channel name, and sets the ``output_enabled`` 
    property.

    Args:
        session (nidcpower.Session):
            An already-open NI-DCPower session.
        channel_name (str):
            The name of the channel to configure (e.g. ``"0"``).
        enable_output (bool):
            When ``True``, enables the channel output.
            When ``False``, disables the channel output.
    """
    session.channels[channel_name].output_enabled = enable_output
