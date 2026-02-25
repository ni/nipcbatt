"""Helper functions and classes for DMM measurement operations."""

import math
from enum import Enum

import nidmm


# Helper Class to extract nidmm.Function and range value from enum
class RangeAndMeasurementFunctionParameters:
    """Extracts measurement function and range from enum values with tuple format."""

    def __init__(self, range_function: Enum):
        """Initialize with an enum that has tuple values (function, range).

        Args:
            range_function: Enum with value as (nidmm.Function, float)
        """
        measurement_function, rangevalue = range_function.value
        self._measurement_function = measurement_function
        self._range_value = rangevalue

    @property
    def measurement_function(self) -> nidmm.Function:
        """Returns the measurement function extracted from the enum.

        Returns:
            nidmm.Function: The measurement function
        """
        return self._measurement_function

    @property
    def range_value(self) -> float:
        """Returns the range value extracted from the enum.

        Returns:
            float: The measurement range value
        """
        return self._range_value


# Helper Class to format measurement results after the readings are fetched from the DMM
class FormatMeasurement:
    """Formats measurement results based on resolution in digits."""

    # Mapping of nidmm.Function to measurement units
    UNIT_MAP = {
        nidmm.Function.DC_VOLTS: "V",
        nidmm.Function.AC_VOLTS: "V",
        nidmm.Function.DC_CURRENT: "A",
        nidmm.Function.AC_CURRENT: "A",
        nidmm.Function.TWO_WIRE_RES: "Ohm",
        nidmm.Function.FOUR_WIRE_RES: "Ohm",
        nidmm.Function.FREQ: "Hz",
        nidmm.Function.PERIOD: "s",
    }

    @staticmethod
    def format_with_si_prefix(measured_value: float, total_digits: int) -> tuple[str, str]:
        """Formats a value in engineering notation with SI prefix.

        Args:
            measured_value: The numerical value to format
            total_digits: Total number of significant digits to display

        Returns:
            tuple: (formatted_number, si_prefix)
                - formatted_number: The scaled value as a string with appropriate decimal places
                - si_prefix: The SI prefix symbol (e.g., 'k', 'M', 'µ', 'm') or exponential notation

        How it works:
            1. Convert measured_value to scientific notation
            2. Transform to engineering notation (exponent divisible by 3)
            3. Scale the mantissa accordingly to match engineering exponent
            4. Determine decimal places needed to maintain significant figures
            5. Map engineering exponent to SI prefix (m, k, M, G, etc.)
            6. Return formatted number and SI prefix
        """
        # Convert to scientific notation string and parse
        sci_str = f"{measured_value:.{total_digits-1}e}"
        mantissa_str, exp_str = sci_str.split("e")
        mantissa = float(mantissa_str)
        exponent = int(exp_str)

        # Convert to engineering notation (exponent divisible by 3)
        eng_exponent = 3 * (exponent // 3)
        scaled_value = mantissa * (10 ** (exponent - eng_exponent))

        # Calculate decimal places
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
            -6: "µ",
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

    @staticmethod
    def measurement(
        range_in_digits: float, measured_value: float, measurement_function: nidmm.Function = None
    ) -> dict:
        """Formats the measurement value according to the specified resolution.

        Args:
            range_in_digits: Resolution in digits (e.g., 6.5 for 6.5 digit resolution)
            measured_value: The measured value to format
            measurement_function: Optional nidmm.Function to append appropriate unit

        Returns:
            dict: Dictionary containing:
                - 'Formatted_Measurement': Human-readable string with SI prefix and unit
                - 'Measured_Value': Original raw measured value
                - 'Unit': Base unit symbol
        """
        # Handle NaN and infinite values
        if math.isnan(measured_value):
            return {
                "Formatted_Measurement": "NaN",
                "Measured_Value": measured_value,
                "Unit": FormatMeasurement.UNIT_MAP.get(measurement_function, ""),
            }
        if math.isinf(measured_value):
            sign = "+" if measured_value > 0 else "-"
            unit = FormatMeasurement.UNIT_MAP.get(measurement_function, "")
            return {
                "Formatted_Measurement": f"{sign}Inf{unit}",
                "Measured_Value": measured_value,
                "Unit": unit,
            }
        if measured_value == 0:
            unit = FormatMeasurement.UNIT_MAP.get(measurement_function, "")
            return {
                "Formatted_Measurement": f"0{unit}",
                "Measured_Value": measured_value,
                "Unit": unit,
            }

        total_digits = int(range_in_digits) + 1
        formatted_number, prefix = FormatMeasurement.format_with_si_prefix(
            measured_value, total_digits
        )
        unit = FormatMeasurement.UNIT_MAP.get(measurement_function, "")
        measurement = f"{formatted_number}{prefix}{unit}"
        return {
            "Formatted_Measurement": measurement,
            "Measured_Value": measured_value,
            "Unit": unit,
        }
