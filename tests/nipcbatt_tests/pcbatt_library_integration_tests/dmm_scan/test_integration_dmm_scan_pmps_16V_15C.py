# pylint: disable=C0301
"""This module provides comprehensive integration tests for DmmScanPMPS complete workflow."""

import importlib.metadata
import logging
import sys
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from varname import nameof

from nipcbatt.pcbatt_library.dmm_scan.dmm_scan_pmps_16V_15C import (
    DmmScanPMPS,
    ScanResources,
    MeasurementResult,
)


class TestIntegrationDmmScanPMPSWorkflow(unittest.TestCase):
    """Defines a test fixture that checks the complete DmmScanPMPS workflow.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSWorkflow")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSWorkflow")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_complete_scan_workflow_with_single_measurement(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying complete scan workflow with single measurement."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 5.125,
            "Unit": "V (dc)",
            "Formatted_Measurement": "5.125V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 10,
            "Digits_Resolution": 5.5,
            "Aperture_Time(s)": "1m",
            "Settle_Time(s)": "1m",
            "Minimum_Frequency(Hz)": 40.0,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize(
            mux_resource_name="Sim_MUX",
            dmm_resource_name="Sim_DMM",
            powerline_freq=50,
        )

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            close_all_shunts=False,
            verbose=False,
        )

        self.assertIsInstance(result, MeasurementResult)
        self.assertEqual(len(result.formatted_measurements), 1)
        self.assertEqual(len(result.raw_measurements), 1)
        self.assertEqual(len(result.execution_settings), 1)
        self.assertGreater(result.scan_time, 0)

        self.dmm_scan.close(scan_resources)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_multiple_channels(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying scan with multiple channels."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 0.0,
            "Unit": "V (dc)",
            "Formatted_Measurement": "0V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 10,
            "Digits_Resolution": 5.5,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize(powerline_freq=50)

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [i, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5]
            for i in range(5)
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            close_all_shunts=False,
            verbose=False,
        )

        self.assertEqual(len(result.formatted_measurements), 5)
        self.assertEqual(len(result.raw_measurements), 5)
        self.assertEqual(len(result.execution_settings), 5)

        self.dmm_scan.close(scan_resources)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_voltage_measurement(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying scan with voltage measurements."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 5.0,
            "Unit": "V (dc)",
            "Formatted_Measurement": "5V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 100,
            "Digits_Resolution": 5.5,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize()

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_100V, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [1, dmm_module.MixedRangeAndFunctions.DC_100V, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            close_all_shunts=False,
            verbose=False,
        )

        self.assertEqual(len(result.formatted_measurements), 2)
        self.assertGreater(result.scan_time, 0)

        self.dmm_scan.close(scan_resources)


class TestIntegrationDmmScanPMPSScanConfiguration(unittest.TestCase):
    """Defines a test fixture for testing scan configuration handling.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSScanConfiguration")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSScanConfiguration")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_configuration_with_mixed_ranges(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test with mixed voltage ranges in single scan."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 0.0,
            "Unit": "V (dc)",
            "Formatted_Measurement": "0V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 10,
            "Digits_Resolution": 5.5,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize()

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_1V, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [1, dmm_module.MixedRangeAndFunctions.DC_10V, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [2, dmm_module.MixedRangeAndFunctions.DC_100V, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            close_all_shunts=False,
            verbose=False,
        )

        self.assertEqual(len(result.formatted_measurements), 3)
        self.assertGreaterEqual(mock_dmm_instance.configure_measurement_function.call_count, 1)

        self.dmm_scan.close(scan_resources)


class TestIntegrationDmmScanPMPSWithVerboseOutput(unittest.TestCase):
    """Defines a test fixture for testing DmmScanPMPS with verbose output.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSWithVerboseOutput")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSWithVerboseOutput")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_verbose_output(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying verbose output during scan."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 5.125,
            "Unit": "V (dc)",
            "Formatted_Measurement": "5.125V (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_VOLTS",
            "Range": 10,
            "Digits_Resolution": 5.5,
            "Aperture_Time(s)": "1m",
            "Settle_Time(s)": "1m",
            "Minimum_Frequency(Hz)": 40.0,
            "Absolute_Resolution": 0.0001,
            "Input_Resistance(Ohm)": 10000000.0,
            "Auto_Range_Value": -1.0,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize()

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [1, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        captured_output = StringIO()
        sys.stdout = captured_output

        try:
            result = self.dmm_scan.configure_and_measure(
                resource_handles=scan_resources,
                scan_configuration=scan_configuration,
                close_all_shunts=False,
                verbose=True,
            )

            sys.stdout = sys.__stdout__
            output_string = captured_output.getvalue()

            self.assertIsInstance(result, MeasurementResult)
            self.assertEqual(len(result.formatted_measurements), 2)

            self.assertIn("SCAN TIME", output_string)
            self.assertIn("FORMATTED MEASUREMENTS", output_string)
            self.assertIn("EXECUTION SETTINGS", output_string)
            self.assertIn("RAW MEASUREMENTS", output_string)

            self.dmm_scan.close(scan_resources)

        finally:
            sys.stdout = sys.__stdout__


class TestIntegrationDmmScanPMPSWithShuntHandling(unittest.TestCase):
    """Defines a test fixture for testing DmmScanPMPS with shunt handling.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSWithShuntHandling")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSWithShuntHandling")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_current_channels_and_shunt_handling(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying shunt handling for current channels (16+)."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 0.5,
            "Unit": "A (dc)",
            "Formatted_Measurement": "500mA (dc)"
        }
        mock_measurement.dmm_execution_settings = {
            "Function": "DC_CURRENT",
            "Range": 1.0,
            "Digits_Resolution": 5.5,
        }

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize(close_all_shunts=True)

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [16, dmm_module.MixedRangeAndFunctions.DC_Current_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [17, dmm_module.MixedRangeAndFunctions.DC_Current_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            close_all_shunts=True,
            verbose=False,
        )

        self.assertGreater(mock_shunt_instance.configure_and_generate.call_count, 0)
        self.assertEqual(len(result.formatted_measurements), 2)

        self.dmm_scan.close(scan_resources)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_with_mixed_voltage_and_current_channels(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test with mixed voltage and current channels in one scan."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.dmm_execution_settings = {}

        def measurement_side_effect(*args, **kwargs):
            result_copy = MagicMock()
            result_copy.measurement = {
                "Measured_Value": 0.0,
                "Unit": "V (dc)",
                "Formatted_Measurement": "0V (dc)"
            }
            result_copy.dmm_execution_settings = {
                "Function": "DC_VOLTS",
                "Range": 10,
            }
            return result_copy

        mock_dmm_instance.acquire_measurement.side_effect = measurement_side_effect

        scan_resources = self.dmm_scan.initialize(close_all_shunts=True)

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [16, dmm_module.MixedRangeAndFunctions.DC_Current_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [1, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
            [17, dmm_module.MixedRangeAndFunctions.DC_Current_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            close_all_shunts=True,
            verbose=False,
        )

        self.assertEqual(len(result.formatted_measurements), 4)
        self.assertEqual(len(result.raw_measurements), 4)

        self.dmm_scan.close(scan_resources)


class TestIntegrationDmmScanPMPSPerformance(unittest.TestCase):
    """Defines a test fixture for performance characteristics of DmmScanPMPS.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        self.dmm_scan = DmmScanPMPS()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestIntegrationDmmScanPMPSPerformance")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestIntegrationDmmScanPMPSPerformance")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_integration_scan_returns_valid_timing_information(
        self, mock_dmm_class, mock_switch_class
    ):
        """Integration test verifying scan returns valid timing information."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch_class.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm_class.return_value = mock_dmm_instance

        mock_measurement = MagicMock()
        mock_measurement.measurement = {
            "Measured_Value": 0.0,
            "Unit": "V (dc)",
            "Formatted_Measurement": "0V (dc)"
        }
        mock_measurement.dmm_execution_settings = {}

        mock_dmm_instance.acquire_measurement.return_value = mock_measurement

        scan_resources = self.dmm_scan.initialize()

        from nipcbatt import dmm as dmm_module
        scan_configuration = [
            [0, dmm_module.MixedRangeAndFunctions.DC_Voltage_Auto_Range, dmm_module.ResolutionInDigits.DIGITS_5_5],
        ]

        result = self.dmm_scan.configure_and_measure(
            resource_handles=scan_resources,
            scan_configuration=scan_configuration,
            close_all_shunts=False,
            verbose=False,
        )

        self.assertGreater(result.scan_time, 0)
        self.assertIsInstance(result.scan_time, float)
        self.assertLess(result.scan_time, 60)

        self.dmm_scan.close(scan_resources)


if __name__ == "__main__":
    unittest.main()
