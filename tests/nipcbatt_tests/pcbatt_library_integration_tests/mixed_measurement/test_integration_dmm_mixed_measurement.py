"""This module provides integration tests for DMM mixed measurement."""

import importlib.metadata
import logging
import sys
import unittest

import nidmm
import nipcbatt
from nipcbatt import dmm


class TestIntegrationMixedMeasurement(unittest.TestCase):
	"""Defines integration checks for `dmm.MixedMeasurement`."""

	RESOURCE_NAME = "Sim_DMM"
	POWERLINE_FREQUENCY = 60.0

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

		try:
			used_nidmm_version = importlib.metadata.version("nidmm")
		except importlib.metadata.PackageNotFoundError:
			used_nidmm_version = "not installed"
		logging.debug("used_nidmm_version = %s", used_nidmm_version)

	@classmethod
	def tearDownClass(cls):
		print("Teardown fixture")

	def _create_initialized_uut(self) -> dmm.MixedMeasurement:
		uut = dmm.MixedMeasurement()
		try:
			uut.initialize(self.RESOURCE_NAME, self.POWERLINE_FREQUENCY)
		except nidmm.errors.DriverError as error:
			self.skipTest(f"NI-DMM resource '{self.RESOURCE_NAME}' not available: {error}")
		return uut

	def test_initialize_configure_measure_close_dc_voltage(self):
		"""Happy path: DC voltage mixed measurement configure and measure."""
		uut = self._create_initialized_uut()

		cfg = dmm.MixedMeasurementConfiguration(
			execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
			measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
				dmm.MixedRangeAndFunctions.DC_10V,
				dmm.ResolutionInDigits.DIGITS_5_5,
			),
			trigger_parameters=dmm.TriggerParameters(
				trigger_source=nidmm.TriggerSource.IMMEDIATE,
				trigger_delay=0.0,
				slope=dmm.Slope.RISING_EDGE,
				enable_trigger=True,
			),
			timing_parameters=dmm.TimingParameters(0.001, 0.01),
			ac_min_frequency=10.0,
		)

		try:
			result = uut.configure_and_measure(cfg)

			self.assertIsNotNone(result)
			self.assertIsInstance(result, dmm.MixedMeasurementResultData)
			self.assertIn("Measured_Value", result.measurement)
		finally:
			uut.close()

	def test_configure_only_returns_none(self):
		"""Ensures CONFIGURE_ONLY execution returns None."""
		uut = self._create_initialized_uut()

		cfg = dmm.MixedMeasurementConfiguration(
			execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
			measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
				dmm.MixedRangeAndFunctions.TWO_W_RES_1k_Ohm,
				dmm.ResolutionInDigits.DIGITS_4_5,
			),
			trigger_parameters=dmm.TriggerParameters(
				trigger_source=nidmm.TriggerSource.IMMEDIATE,
				trigger_delay=0.0,
				slope=dmm.Slope.RISING_EDGE,
				enable_trigger=False,
			),
			timing_parameters=dmm.TimingParameters(0.001, 0.01),
			ac_min_frequency=10.0,
		)

		try:
			result = uut.configure_and_measure(cfg)
			self.assertIsNone(result)
		finally:
			uut.close()

	def test_measure_only_reads_and_wraps_result(self):
		"""Ensures MEASURE_ONLY returns mixed measurement result data."""
		uut = self._create_initialized_uut()

		cfg = dmm.MixedMeasurementConfiguration(
			execution_type=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
			measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
				dmm.MixedRangeAndFunctions.DC_100mA,
				dmm.ResolutionInDigits.DIGITS_5_5,
			),
			trigger_parameters=dmm.TriggerParameters(
				trigger_source=nidmm.TriggerSource.IMMEDIATE,
				trigger_delay=0.0,
				slope=dmm.Slope.RISING_EDGE,
				enable_trigger=True,
			),
			timing_parameters=dmm.TimingParameters(0.001, 0.01),
			ac_min_frequency=10.0,
		)

		try:
			result = uut.configure_and_measure(cfg)
			self.assertIsNotNone(result)
			self.assertIsInstance(result.dmm_execution_settings, dict)
			self.assertIsInstance(result.measurement, dict)
		finally:
			uut.close()

	def test_ac_measurement_applies_ac_min_frequency(self):
		"""AC measurement path should apply configured AC minimum frequency."""
		uut = self._create_initialized_uut()

		cfg = dmm.MixedMeasurementConfiguration(
			execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
			measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
				dmm.MixedRangeAndFunctions.AC_20V,
				dmm.ResolutionInDigits.DIGITS_4_5,
			),
			trigger_parameters=dmm.TriggerParameters(
				trigger_source=nidmm.TriggerSource.IMMEDIATE,
				trigger_delay=0.0,
				slope=dmm.Slope.RISING_EDGE,
				enable_trigger=True,
			),
			timing_parameters=dmm.TimingParameters(0.001, 0.01),
			ac_min_frequency=55.0,
		)

		try:
			result = uut.configure_and_measure(cfg)
			self.assertIsNotNone(result)
			self.assertEqual(result.dmm_execution_settings["Minimum_Frequency(Hz)"], 55.0)
		finally:
			uut.close()

	def test_multiple_mixed_ranges(self):
		"""Verifies mixed measurement with multiple function/range settings."""
		uut = self._create_initialized_uut()

		test_ranges = [
			dmm.MixedRangeAndFunctions.DC_1V,
			dmm.MixedRangeAndFunctions.DC_10mA,
			dmm.MixedRangeAndFunctions.TWO_W_RES_10k_Ohm,
			dmm.MixedRangeAndFunctions.FOUR_W_RES_1k_Ohm,
		]

		try:
			for mixed_range in test_ranges:
				cfg = dmm.MixedMeasurementConfiguration(
					execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
					measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
						mixed_range,
						dmm.ResolutionInDigits.DIGITS_4_5,
					),
					trigger_parameters=dmm.TriggerParameters(
						trigger_source=nidmm.TriggerSource.IMMEDIATE,
						trigger_delay=0.0,
						slope=dmm.Slope.RISING_EDGE,
						enable_trigger=True,
					),
					timing_parameters=dmm.TimingParameters(0.001, 0.01),
					ac_min_frequency=10.0,
				)

				result = uut.configure_and_measure(cfg)
				self.assertIsNotNone(result)
				self.assertIn("Function", result.dmm_execution_settings)
				self.assertIn("Measured_Value", result.measurement)
		finally:
			uut.close()


if __name__ == "__main__":
	unittest.main()
