# pylint: disable=C0301
"""This module provides PowerSupplySourceAndMeasure check."""
import importlib.metadata
import logging
import sys
import unittest

import numpy as np
from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _InterpreterPowerSupplySourceAndMeasure,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestPowerSupplySourceAndMeasure(unittest.TestCase):
    """Defines a test fixture that checks
    `PowerSupplySourceAndMeasure` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_InterpreterPowerSupplySourceAndMeasure)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_power_supply_source_and_measure(self):
        """Checks if class PowerSupplySourceAndMeasure is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)
        measurement = nipcbatt.PowerSupplySourceAndMeasure()

        measurement.initialize(power_channel_name="TS1Mod1_pwr/power")

        measurement.configure_and_measure(
            configuration=nipcbatt.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION
        )

        measurement.close()

    def test_analyze_measurement_data_results_when_providing_valid_data(self):
        """unit test of PowerSupplySourceAndMeasureData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (157 > 100 characters) (auto-generated noqa)
        ############ ARRANGE ######################################
        # create data objects for test
        voltage_samples1 = np.asarray([-2.0, -1.0, 0.0, 1.0, 2.0])
        voltage_samples2 = np.asarray([0.0, 0.0, 0.0, 0.0, 0.0])
        voltage_samples4 = np.asarray([-99.0, 0.0, 99.0, 0.0, -99.0])

        current_samples1 = np.asarray([-2.0, -1.0, 0.0, 1.0, 2.0])
        current_samples2 = np.asarray([0.0, 0.0, 0.0, 0.0, 0.0])
        current_samples4 = np.asarray([-99.0, 0.0, 99.0, 0.0, -99.0])

        sample_rate1 = 1000000000  # 1 GHz
        sample_rate2 = 100000000  # 100 MHz
        sample_rate4 = 1000000  # 1 MHz

        data_1 = nipcbatt.PowerSupplySourceAndMeasureData(
            "data1", voltage_samples1, current_samples1, sample_rate1
        )

        data_2 = nipcbatt.PowerSupplySourceAndMeasureData(
            "data2", voltage_samples2, current_samples2, sample_rate2
        )

        data_4 = nipcbatt.PowerSupplySourceAndMeasureData(
            "data4", voltage_samples4, current_samples4, sample_rate4
        )

        #################### ACT ######################################################
        # generate result objects
        res_data_1 = nipcbatt.PowerSupplySourceAndMeasure.analyze_measurement_data(self, data_1)
        res_data_2 = nipcbatt.PowerSupplySourceAndMeasure.analyze_measurement_data(self, data_2)
        res_data_4 = nipcbatt.PowerSupplySourceAndMeasure.analyze_measurement_data(self, data_4)

        #################### ASSERT ###################################################
        # test max voltage
        self.assertAlmostEqual(res_data_1.max_voltage_level_volts, 2.0, places=5)
        self.assertAlmostEqual(res_data_2.max_voltage_level_volts, 0.0, places=5)
        self.assertAlmostEqual(res_data_4.max_voltage_level_volts, 99.0, places=5)

        # test max current
        self.assertAlmostEqual(res_data_1.max_current_level_amperes, 2.0, places=5)
        self.assertAlmostEqual(res_data_2.max_current_level_amperes, 0.0, places=5)
        self.assertAlmostEqual(res_data_4.max_current_level_amperes, 99.0, places=5)

        # test max power
        self.assertAlmostEqual(res_data_1.max_power_level_watts, 4.0, places=5)
        self.assertAlmostEqual(res_data_2.max_power_level_watts, 0.0, places=5)
        self.assertAlmostEqual(res_data_4.max_power_level_watts, 9801.0, places=5)

        # test average power
        self.assertAlmostEqual(res_data_1.average_power_value_watts, 2.0, places=5)
        self.assertAlmostEqual(res_data_2.average_power_value_watts, 0.0, places=5)
        self.assertAlmostEqual(res_data_4.average_power_value_watts, 5880.6, places=5)

        # test acquisition duration
        self.assertAlmostEqual(res_data_1.acquisition_duration_seconds, 5e-09, places=5)
        self.assertAlmostEqual(res_data_2.acquisition_duration_seconds, 5e-08, places=5)
        self.assertAlmostEqual(res_data_4.acquisition_duration_seconds, 5e-06, places=5)

    def test_analyze_measurement_data_results_when_providing_undefined_data(self):
        """unit test of PowerSupplySourceAndMeasureData."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (157 > 100 characters) (auto-generated noqa)
        ############ ARRANGE ######################################
        # create data objects for test
        voltage_samples1 = None
        voltage_samples2 = np.asarray([-2.0, -1.0, 0.0, 1.0, 2.0])

        current_samples1 = None
        current_samples2 = np.asarray([-2.0, -1.0, 0.0, 1.0, 2.0])

        sample_rate1 = None
        sample_rate2 = 1000000  # 1 MHz

        #################### ACT & ASSERT ###################################################
        # test PowerSupplySourceAndMeasureData constructor
        with self.assertRaises(ValueError):
            print(
                nipcbatt.PowerSupplySourceAndMeasureData(
                    "data1", voltage_samples1, current_samples2, sample_rate2
                )
            )

            print(
                nipcbatt.PowerSupplySourceAndMeasureData(
                    "data2", voltage_samples2, current_samples1, sample_rate2
                )
            )

            print(
                nipcbatt.PowerSupplySourceAndMeasureData(
                    "data3", voltage_samples2, current_samples2, sample_rate1
                )
            )


if __name__ == "__main__":
    unittest.main()
