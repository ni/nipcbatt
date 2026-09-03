"""This module provides format_si_fixed_decimals unit tests."""
 
import unittest
 
from nipcbatt.pcbatt_library.dcpower.common.helper_functions import (
    format_si_fixed_decimals,
)
 
 
class TestFormatSiFixedDecimals(unittest.TestCase):
    """Defines a test fixture that checks
    `format_si_fixed_decimals` formats values correctly.
 
    Args:
        unittest.TestCase: Base class from which this class inherits.
    """
 
    def test_format_si_fixed_decimals_cases(self):
        """Checks formatting across the documented examples and boundary/edge values."""  # noqa: D415, W505
        cases = [
            (0.9999999274781265, "V", 3, "1.000 V"),  # value just below 1, must not drop to mV
            (0.000958775, "A", 3, "958.775 uA"),
            (958.775, "A", 3, "958.775 A"),
            (9.696e-5, "W", 3, "96.960 uW"),
            (105.477, "Ohm", 3, "105.477 Ohm"),
            (0.0, "V", 3, "0.000 V"),
            (-0.000958775, "A", 3, "-958.775 uA"),
            (1000.0, "V", 3, "1.000 kV"),
            (999.9996, "V", 3, "1.000 kV"),  # rounds up and carries to next SI prefix
            (float("nan"), "V", 3, "NaN"),
            (float("inf"), "V", 3, "+Inf"),
            (float("-inf"), "V", 3, "-Inf"),
        ]
 
        for value, unit, decimal_places, expected in cases:
            with self.subTest(value=value, unit=unit, decimal_places=decimal_places):
                self.assertEqual(
                    format_si_fixed_decimals(value, unit, decimal_places), expected
                )
 
 
if __name__ == "__main__":
    unittest.main()
print("all pass")