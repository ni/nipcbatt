"""Various helper functions usable by any module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)


def format_with_si_prefix(measured_value: float, total_digits: int) -> tuple[str, str]:
    """Formats a value in engineering notation with an SI prefix.

    Args:
        measured_value: The numerical value to format.
        total_digits: Total number of significant digits to display.

    Returns:
        tuple: (formatted_number, si_prefix)
            - formatted_number: The scaled value as a string with appropriate decimal places.
            - si_prefix: The SI prefix symbol (e.g., 'k', 'M', 'u', 'm') or exponential notation.

    How it works:
        1. Convert measured_value to scientific notation.
        2. Transform to engineering notation (exponent divisible by 3).
        3. Scale the mantissa accordingly to match engineering exponent.
        4. Determine decimal places needed to maintain significant figures.
        5. Map engineering exponent to SI prefix (m, k, M, G, etc.).
        6. Return formatted number and SI prefix.
    """
    sci_str = f"{measured_value:.{total_digits-1}e}"
    mantissa_str, exp_str = sci_str.split("e")
    mantissa = float(mantissa_str)
    exponent = int(exp_str)

    eng_exponent = 3 * (exponent // 3)
    scaled_value = mantissa * (10 ** (exponent - eng_exponent))

    decimal_places = total_digits - len(str(int(abs(scaled_value))))
    decimal_places = max(0, decimal_places)
    formatted_number = f"{scaled_value:.{decimal_places}f}"

    si_prefixes = {
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
        21: "Z",
        24: "Y",
    }
    prefix = si_prefixes.get(eng_exponent, f"e{eng_exponent}")

    return (formatted_number, prefix)


# Helper function to generate ramp data
def digital_ramp_pattern_generator(
    number_of_samples: int = None, number_of_digital_lines: int = None
):
    """Generates Ramp based Digital Output Data couting from 0 upto (2^N)-1 where "N" represents the
    Number of Digital Lines."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (324 > 100 characters) (auto-generated noqa)
    if number_of_samples is (0 or None):
        raise ValueError("number_of_samples must be >= 1")
    if number_of_digital_lines is (0 or None):
        raise ValueError("number_of_digital lines must be >= 1")

    # create variables for holding data
    total_lines = 2**number_of_digital_lines
    port_digital_data = [0] * number_of_samples

    # populate array with values
    for i in range(number_of_samples):
        port_digital_data[i] = i % total_lines

    return port_digital_data
