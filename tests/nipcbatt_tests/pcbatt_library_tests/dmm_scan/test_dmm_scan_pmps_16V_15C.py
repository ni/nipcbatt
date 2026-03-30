# pylint: disable=C0301
"""This module provides comprehensive unit tests for DmmScanPMPS class and data types."""

import importlib.metadata
import logging
import sys
import unittest
from typing import NamedTuple
from unittest.mock import MagicMock, patch

from varname import nameof

from nipcbatt.pcbatt_library.dmm_scan.dmm_scan_pmps_16V_15C import (
    DmmScanPMPS,
    ScanResources,
    MeasurementResult,
)


class TestScanResources(unittest.TestCase):
    """Defines a test fixture that checks `ScanResources` NamedTuple is correctly structured.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        pass

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestScanResources")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestScanResources")

    def test_scan_resources_is_named_tuple(self):
        """Unit test verifying that ScanResources is a NamedTuple."""
        self.assertTrue(issubclass(ScanResources, tuple))

    def test_scan_resources_has_required_fields(self):
        """Unit test verifying that ScanResources has all required fields."""
        expected_fields = ("mux_generation", "shunt_generation", "dmm_generation")
        self.assertEqual(ScanResources._fields, expected_fields)

    def test_scan_resources_field_access(self):
        """Unit test verifying that ScanResources fields can be accessed correctly."""
        scan_resources = ScanResources(
            mux_generation=None,
            shunt_generation=None,
            dmm_generation=None
        )

        self.assertIsNone(scan_resources.mux_generation)
        self.assertIsNone(scan_resources.shunt_generation)
        self.assertIsNone(scan_resources.dmm_generation)


class TestMeasurementResult(unittest.TestCase):
    """Defines a test fixture that checks `MeasurementResult` NamedTuple is correctly structured.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505

    def setUp(self):
        """Set up test fixtures."""
        pass

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    @classmethod
    def setUpClass(cls):
        """Set up class-level fixtures."""
        print("Setup test fixture: TestMeasurementResult")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestMeasurementResult")

    def test_measurement_result_is_named_tuple(self):
        """Unit test verifying that MeasurementResult is a NamedTuple."""
        self.assertTrue(issubclass(MeasurementResult, tuple))

    def test_measurement_result_has_required_fields(self):
        """Unit test verifying that MeasurementResult has all required fields."""
        expected_fields = (
            "sessions",
            "scan_time",
            "formatted_measurements",
            "execution_settings",
            "raw_measurements",
        )
        self.assertEqual(MeasurementResult._fields, expected_fields)

    def test_measurement_result_field_access(self):
        """Unit test verifying that MeasurementResult fields can be accessed correctly."""
        scan_resources = ScanResources(
            mux_generation=None,
            shunt_generation=None,
            dmm_generation=None
        )

        measurement_result = MeasurementResult(
            sessions=scan_resources,
            scan_time=0.5,
            formatted_measurements=[],
            execution_settings=[],
            raw_measurements=[]
        )

        self.assertEqual(measurement_result.sessions, scan_resources)
        self.assertEqual(measurement_result.scan_time, 0.5)
        self.assertEqual(measurement_result.formatted_measurements, [])
        self.assertEqual(measurement_result.execution_settings, [])
        self.assertEqual(measurement_result.raw_measurements, [])

    def test_measurement_result_with_sample_data(self):
        """Unit test verifying MeasurementResult with realistic sample data."""
        scan_resources = ScanResources(
            mux_generation=None,
            shunt_generation=None,
            dmm_generation=None
        )

        formatted_measurements = [
            ("ch0", "5.125V (dc)", 0.015),
            ("ch1", "10.25V (dc)", 0.018),
        ]
        execution_settings = [
            {"Function": "DC_VOLTS", "Range": 10, "Digits_Resolution": 5.5},
            {"Function": "DC_VOLTS", "Range": 10, "Digits_Resolution": 5.5},
        ]
        raw_measurements = [
            ("ch0", {"Measured_Value": 5.125, "Unit": "V (dc)"}, "DC_VOLTS"),
            ("ch1", {"Measured_Value": 10.25, "Unit": "V (dc)"}, "DC_VOLTS"),
        ]

        measurement_result = MeasurementResult(
            sessions=scan_resources,
            scan_time=0.045,
            formatted_measurements=formatted_measurements,
            execution_settings=execution_settings,
            raw_measurements=raw_measurements
        )

        self.assertEqual(len(measurement_result.formatted_measurements), 2)
        self.assertEqual(len(measurement_result.execution_settings), 2)
        self.assertEqual(len(measurement_result.raw_measurements), 2)
        self.assertEqual(measurement_result.scan_time, 0.045)


class TestDmmScanPMPSInitialization(unittest.TestCase):
    """Defines a test fixture that checks DmmScanPMPS initialization.

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
        print("Setup test fixture: TestDmmScanPMPSInitialization")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestDmmScanPMPSInitialization")

    def test_dmm_scan_pmps_can_be_instantiated(self):
        """Unit test verifying that DmmScanPMPS can be instantiated."""
        self.assertIsNotNone(self.dmm_scan)

    def test_dmm_scan_pmps_is_instance_of_building_blocks(self):
        """Unit test verifying that DmmScanPMPS inherits from building block classes."""
        from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
            BuildingBlockUsingNIDMM,
            BuildingBlockUsingNISWITCH,
        )
        self.assertIsInstance(self.dmm_scan, BuildingBlockUsingNIDMM)
        self.assertIsInstance(self.dmm_scan, BuildingBlockUsingNISWITCH)

    def test_dmm_scan_pmps_has_initialize_method(self):
        """Unit test verifying that DmmScanPMPS has initialize method."""
        self.assertTrue(hasattr(self.dmm_scan, "initialize"))
        self.assertTrue(callable(getattr(self.dmm_scan, "initialize")))

    def test_dmm_scan_pmps_has_configure_and_measure_method(self):
        """Unit test verifying that DmmScanPMPS has configure_and_measure method."""
        self.assertTrue(hasattr(self.dmm_scan, "configure_and_measure"))
        self.assertTrue(callable(getattr(self.dmm_scan, "configure_and_measure")))

    def test_dmm_scan_pmps_has_close_method(self):
        """Unit test verifying that DmmScanPMPS has close method."""
        self.assertTrue(hasattr(self.dmm_scan, "close"))
        self.assertTrue(callable(getattr(self.dmm_scan, "close")))


class TestDmmScanPMPSInitializeMethod(unittest.TestCase):
    """Defines a test fixture for testing DmmScanPMPS.initialize() method.

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
        print("Setup test fixture: TestDmmScanPMPSInitializeMethod")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestDmmScanPMPSInitializeMethod")

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_initialize_returns_scan_resources(self, mock_dmm, mock_switch):
        """Unit test verifying that initialize() returns ScanResources."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm.return_value = mock_dmm_instance

        result = self.dmm_scan.initialize(
            mux_resource_name="Sim_MUX",
            mux_topology_name="2527/2-Wire Dual 16x1 Mux",
            shunt_resource_name="Sim_SHUNT",
            shunt_topology_name="2568/31-SPST",
            dmm_resource_name="Sim_DMM",
            powerline_freq=50,
            close_all_shunts=True
        )

        self.assertIsInstance(result, ScanResources)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_initialize_with_default_parameters(self, mock_dmm, mock_switch):
        """Unit test verifying initialize() works with default parameters."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm.return_value = mock_dmm_instance

        result = self.dmm_scan.initialize()

        self.assertIsInstance(result, ScanResources)
        self.assertIsNotNone(result.mux_generation)
        self.assertIsNotNone(result.shunt_generation)
        self.assertIsNotNone(result.dmm_generation)

    @patch("nipcbatt.switch.StaticDigitalPathGeneration")
    @patch("nipcbatt.dmm.MixedMeasurement")
    def test_initialize_with_close_all_shunts_false(self, mock_dmm, mock_switch):
        """Unit test verifying initialize() with close_all_shunts=False."""
        mock_mux_instance = MagicMock()
        mock_shunt_instance = MagicMock()
        mock_dmm_instance = MagicMock()

        mock_switch.side_effect = [mock_mux_instance, mock_shunt_instance]
        mock_dmm.return_value = mock_dmm_instance

        result = self.dmm_scan.initialize(close_all_shunts=False)

        self.assertIsInstance(result, ScanResources)


class TestDmmScanPMPSCloseMethod(unittest.TestCase):
    """Defines a test fixture for testing DmmScanPMPS.close() method.

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
        print("Setup test fixture: TestDmmScanPMPSCloseMethod")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level fixtures."""
        print("Teardown fixture: TestDmmScanPMPSCloseMethod")

    def test_close_method_calls_close_on_all_resources(self):
        """Unit test verifying close() calls close on all resource handles."""
        mock_mux = MagicMock()
        mock_shunt = MagicMock()
        mock_dmm = MagicMock()

        scan_resources = ScanResources(
            mux_generation=mock_mux,
            shunt_generation=mock_shunt,
            dmm_generation=mock_dmm
        )

        self.dmm_scan.close(scan_resources)

        mock_mux.close.assert_called_once()
        mock_shunt.close.assert_called_once()
        mock_dmm.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()
