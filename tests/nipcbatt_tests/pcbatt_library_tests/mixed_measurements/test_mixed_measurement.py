# pylint: disable=C0301
"""This module provides MixedMeasurement check."""

import importlib.metadata
import logging
from pathlib import Path
import sys
import unittest

# Force using local source tree instead of installed package in venv.
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "src"))

import nipcbatt
from nipcbatt import dmm


class TestMixedMeasurement(unittest.TestCase):
    """Defines a test fixture that checks
    `MixedMeasurement` class is ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (201 > 100 characters) (auto-generated noqa)

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
        logging.debug("used_nidaqmx_version = %s", used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_mixed_measurement(self):
        """Checks if class MixedMeasurement is ready to use"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)
        measurement = dmm.MixedMeasurement()
        try:
            measurement.initialize(dmm_resource_name="Sim_DMM", powerline_frequency=50)

            measurement.configure_and_measure(
                configuration=dmm.DEFAULT_MIXED_MEASUREMENT_CONFIGURATION
            )
        finally:
            measurement.close()


if __name__ == "__main__":
    unittest.main()
