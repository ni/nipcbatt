"""Helper functions for DC power instrument operations."""

import math

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


def generate_pulse_current_sequence(
    start_current,
    end_current,
    step_size,
    source_delay,
    max_points=10000
):
    """
    Replicates the LabVIEW sequence generation logic.
    """

    # Protect against zero step
    if step_size == 0:
        raise ValueError("Step size cannot be zero")

    # Allow reverse sweeps
    if end_current < start_current:
        step = -abs(step_size)
    else:
        step = abs(step_size)

    # Calculate number of points
    num_points = int(
        math.floor(abs(end_current - start_current) / abs(step))
    ) + 1

    # Limit for SMU
    num_points = min(num_points, max_points)

    # Generate sequence
    pulse_current_sequence = [
        start_current + i * step
        for i in range(num_points)
    ]

    # Protect against overshoot
    if step > 0:
        pulse_current_sequence = [
            min(v, end_current)
            for v in pulse_current_sequence
        ]
    else:
        pulse_current_sequence = [
            max(v, end_current)
            for v in pulse_current_sequence
        ]

    last_point_current = pulse_current_sequence[-1]

    # Create delay array
    source_delays = [source_delay] * num_points

    return {
        "source_delays": source_delays,
        "number_of_points": num_points,
        "pulse_current_sequence": pulse_current_sequence,
        "last_point_current": last_point_current,
    }