""" Performs unit tests ensuring the integrity of the datatypes used in 
    DMM-based DC-RMS voltage measurements """

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt import dmm

class TestDMMDcRmsVoltage(unittest.TestCase):
    """Defines a test fixture that ensures the enums are created 
        correctly
        
        Args:
            unittest.TestCase: Base class from which this class inherits
        """
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidmm_version = importlib.metadata.version("nidmm")
        logging.debug("%s = %s", nameof(used_nidmm_version), used_nidmm_version)
        
    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    
    def test_enum_members_shape_and_types(self):
        "Tests the creation of different type and shapes of enums"

        range_values = [member.value for member in dmm.VoltageRangeAndFunctions]

        for value in range_values:
            data = dmm.VoltageRangeAndFunctions(value)
            self.assertEqual(value, data.value)


    def test_properties_are_effectively_read_only(self):
        """Attempting to assign to properties should raise AttributeError."""
        RESOLUTION = 5.5

        initial_member = dmm.VoltageRangeAndFunctions.AC_200mV
        resolution = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=initial_member,
            resolution_in_digits=resolution,
        )

        # The class exposes read-only properties (no setters). Direct assignment should fail.
        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.VoltageRangeAndFunctions.AC_50mV)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        # Confirm original values unchanged
        self.assertIs(params.measurement_function, initial_member)
        self.assertIs(params.resolution_in_digits, resolution)


    def test_basic_construction_and_properties(self):
        """Create params and verify properties return the same objects."""

        RESOLUTION = 6.5

        member = dmm.VoltageRangeAndFunctions.DC_100mV
        res = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)
        self.assertEqual(params.resolution_in_digits.value, RESOLUTION)


    def test_construct_for_every_voltage_range_enum_value(self):
        """Iterate all VoltageRangeAndFunctions, instantiate params, and verify."""
       
        res = dmm.ResolutionInDigits(5.5)

        for member in dmm.VoltageRangeAndFunctions:
            params = dmm.DcRmsVoltageMeasurementFunctionParameters(
                measurement_function=member,
                resolution_in_digits=res,
            )
            self.assertIs(params.measurement_function, member)
            self.assertIs(params.resolution_in_digits, res)


    def test_dcrms_meas_config_properties_are_read_only(self):

        "Ensure all function properties are read only"

        member = dmm.VoltageRangeAndFunctions.AC_200mV
        res = dmm.ResolutionInDigits(6.5)

        params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.VoltageRangeAndFunctions.DC_1V)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)


    def test_identity_of_references(self):

        "Make sure the same object is returned, not a copy"

        member = dmm.VoltageRangeAndFunctions.DC_1V
        res = dmm.ResolutionInDigits(7.5)

        params = dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)