"""Helper functions for DC power instrument operations."""

import math

import nidcpower

_SI_PREFIXES = {
    -24: "y",
    -21: "z",
    -18: "a",
    -15: "f",
    -12: "p",
    -9: "n",
    -6: "u",
    -3: "m",
    0: "",
    3: "k",
    6: "M",
    9: "G",
    12: "T",
    15: "P",
    18: "E",
}


def format_si_fixed_decimals(value: float, unit: str, decimal_places: int = 3) -> str:
    """Formats a numeric value in SI engineering notation with a fixed number of decimal places.

    Scales the value to engineering notation (exponent divisible by 3),
    applies the matching SI prefix, and appends the unit directly without a space.

    Args:
        value (float):
            The numeric value to format.
        unit (str):
            The unit string to append (e.g., ``"A"``, ``"W"``, ``"Ohm"``).
        decimal_places (int):
            Number of digits after the decimal point. Defaults to ``3``.

    Returns:
        str: Formatted string with SI prefix and unit attached.

    Examples:
        ``format_si_fixed_decimals(0.000958775, "A")`` → ``"958.775uA"``

        ``format_si_fixed_decimals(9.696e-5, "W")`` → ``"96.960uW"``

        ``format_si_fixed_decimals(105.477, "Ohm")`` → ``"105.477Ohm"``

        ``format_si_fixed_decimals(0.0, "V")`` → ``"0.000V"``
    """
    if math.isnan(value):
        return f"NaN{unit}"
    if math.isinf(value):
        sign = "+" if value > 0 else "-"
        return f"{sign}Inf{unit}"
    if value == 0.0:
        return f"0.{'0' * decimal_places}{unit}"

    exp = math.floor(math.log10(abs(value)))
    eng_exp = 3 * (exp // 3)
    scaled = value / (10**eng_exp)
    prefix = _SI_PREFIXES.get(eng_exp, f"e{eng_exp}")
    return f"{scaled:.{decimal_places}f}{prefix}{unit}"


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
