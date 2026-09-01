"""This module provides format_si_fixed_decimals unit tests."""
 
import unittest
 
from nipcbatt.pcbatt_library.dcpower.common.helper_function import (
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
            (0.9999999274781265, "V", 3, "1.000V"),  # value just below 1, must not drop to mV
            (0.000958775, "A", 3, "958.775uA"),
            (958.775, "A", 3, "958.775A"),
            (9.696e-5, "W", 3, "96.960uW"),
            (105.477, "Ohm", 3, "105.477Ohm"),
            (0.0, "V", 3, "0.000V"),
            (-0.000958775, "A", 3, "-958.775uA"),
            (1000.0, "V", 3, "1.000kV"),
            (999.9996, "V", 3, "1.000kV"),  # rounds up and carries to next SI prefix
            (float("nan"), "V", 3, "NaNV"),
            (float("inf"), "V", 3, "+InfV"),
            (float("-inf"), "V", 3, "-InfV"),
            (1e-30, "V", 3, "1.000e-30V"),  # below yocto, falls back to eN notation
            (1e25, "V", 3, "10.000e24V"),  # above exa, falls back to eN notation
        ]
 
        for value, unit, decimal_places, expected in cases:
            with self.subTest(value=value, unit=unit, decimal_places=decimal_places):
                self.assertEqual(
                    format_si_fixed_decimals(value, unit, decimal_places), expected
                )
 
 
if __name__ == "__main__":
    unittest.main()
print("all pass")