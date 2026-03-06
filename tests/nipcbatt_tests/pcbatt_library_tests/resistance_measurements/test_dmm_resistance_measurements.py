""" Performs unit tests ensuring the integrity of the datatypes used in 
    DMM-based resistance measurements """

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt import dmm


class TestDmmResistance(unittest.TestCase):
    """Defines a test fixture that ensures the data types of the 
        dmm.Resistance class are created correctly
        
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

        range_values = [member.value for member in dmm.ResistanceRangeAndFunctions]

        for value in range_values:
            data = dmm.ResistanceRangeAndFunctions(value)
            self.assertEqual(value, data.value)

    def test_function_params_basic_construction_and_properties(self):
        """Create a ResistanceMeasurementFunctionParameters and verify properties."""

        RESOLUTION = 6.5

        target_member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm
        resolution = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=target_member,
            resolution_in_digits=resolution,
        )

        # Verify properties return exactly what we passed in
        self.assertIs(params.measurement_function, target_member)
        self.assertIs(params.resolution_in_digits, resolution)
        self.assertEqual(params.resolution_in_digits.value, RESOLUTION)


    def test_properties_are_effectively_read_only(self):
        """Attempting to assign to properties should raise AttributeError."""
        RESOLUTION = 5.5

        initial_member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm
        resolution = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=initial_member,
            resolution_in_digits=resolution,
        )

        # The class exposes read-only properties (no setters). Direct assignment should fail.
        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.ResistanceRangeAndFunctions.TWO_W_RES_10k_Ohm)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        # Confirm original values unchanged
        self.assertIs(params.measurement_function, initial_member)
        self.assertIs(params.resolution_in_digits, resolution)

    
    def test_basic_construction_and_properties(self):
        """Create params and verify properties return the same objects."""

        RESOLUTION = 6.5

        member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm
        res = dmm.ResolutionInDigits(RESOLUTION)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)
        self.assertEqual(params.resolution_in_digits.value, RESOLUTION)


    def test_construct_for_every_current_range_enum_value(self):
        """Iterate all CurrentRangeAndFunctions, instantiate params, and verify."""
       
        res = dmm.ResolutionInDigits(5.5)

        for member in dmm.ResistanceRangeAndFunctions:
            params = dmm.ResistanceMeasurementFunctionParameters(
                measurement_function=member,
                resolution_in_digits=res,
            )
            self.assertIs(params.measurement_function, member)
            self.assertIs(params.resolution_in_digits, res)


    def test_dcrms_meas_config_properties_are_read_only(self):

        "Ensure all function properties are read only"

        member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_1k_Ohm
        res = dmm.ResolutionInDigits(6.5)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "measurement_function", dmm.ResistanceRangeAndFunctions.TWO_W_RES_10k_Ohm)

        with self.assertRaises(AttributeError):
            # type: ignore[attr-defined]
            setattr(params, "resolution_in_digits", dmm.ResolutionInDigits(4.5))

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)


    def test_identity_of_references(self):

        "Make sure the same object is returned, not a copy"

        member = dmm.ResistanceRangeAndFunctions.TWO_W_RES_100k_Ohm
        res = dmm.ResolutionInDigits(7.5)

        params = dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=member,
            resolution_in_digits=res,
        )

        self.assertIs(params.measurement_function, member)
        self.assertIs(params.resolution_in_digits, res)