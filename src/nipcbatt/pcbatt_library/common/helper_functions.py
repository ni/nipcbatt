"""Various helper functions usable by any module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (162 > 100 characters) (auto-generated noqa)


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
