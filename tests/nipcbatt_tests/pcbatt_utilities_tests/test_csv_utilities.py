"""Provides unit tests related to functional_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

from varname import nameof

from nipcbatt.pcbatt_utilities import (
    csv_utilities,
    file_utilities,
    functional_utilities,
)


class TestCsvUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.csv_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        self.counter = 0

    def tearDown(self):
        self.counter = 0

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        repository_dir_path = Path(__file__).parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestCsvUtilities),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_export_signal_to_csv_file(self):
        """Unit test of csv_utilities.export_signal_to_csv_file"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (177 > 100 characters) (auto-generated noqa)
        # Arrange
        signal_samples = [1, 4, 9, 16]
        csv_file_ouput_path = os.path.join(
            TestCsvUtilities.tests_output_folder_path,
            "test_export_signal_to_csv_file.csv",
        )

        # Act
        csv_utilities.export_signal_to_csv_file(
            signal_csv_file_path=csv_file_ouput_path,
            signal_samples=signal_samples,
            signal_sampling_rate=1,
            x_axis_name="Time (s)",
            y_axis_name="Amplitude (V)",
        )

        # Assert
        self.assertTrue(os.path.exists(path=csv_file_ouput_path))
        csv_lines_list = list(file_utilities.read_lines(csv_file_ouput_path, "utf8"))

        logging.debug("%s = %s", nameof(csv_lines_list), csv_lines_list)
        self.assertEqual(first=1 + len(signal_samples), second=len(csv_lines_list))

    @functional_utilities.repeat(2)
    def test_export_columns_to_csv_file(self):
        """Unit test of csv_utilities.export_to_csv_file_columns"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (178 > 100 characters) (auto-generated noqa)
        # Arrange
        x_samples = [1, 2, 3, 4]
        y_samples = [1, 4, 9, 16]
        csv_file_ouput_path = os.path.join(
            TestCsvUtilities.tests_output_folder_path,
            "test_export_columns_to_csv_file.csv",
        )

        # Act
        csv_utilities.export_columns_to_csv_file(
            csv_file_path=csv_file_ouput_path,
            column1_data=x_samples,
            column2_data=y_samples,
            column1_name="X",
            column2_name="X^2",
        )

        # Assert
        self.assertTrue(os.path.exists(path=csv_file_ouput_path))

    @functional_utilities.repeat(2)
    def test_import_from_csv_file_2d_array(self):
        """Unit test of csv_utilities.import_from_csv_file_2d_array"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (258 > 100 characters) (auto-generated noqa)

        # Arrange
        expected_csv_lines_count = 14001
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent

        logging.debug("%s = %s", nameof(repository_dir_path), repository_dir_path)

        emv_csv_file_path = os.path.join(
            repository_dir_path, "pcbatt.testdata", "EMV_Waveform_TA121.csv"
        )
        logging.debug("%s = %s", nameof(emv_csv_file_path), emv_csv_file_path)

        # Act
        (column_1_array, column_2_array) = csv_utilities.import_from_csv_file_2d_array(
            csv_file_path=emv_csv_file_path, header_is_present=False
        )
        logging.debug(
            "%s[%s] = %s",
            nameof(column_1_array),
            "Time (s)",
            column_1_array,
        )

        logging.debug(
            "%s[%s] = %s",
            nameof(column_2_array),
            "Ampltiude (V)",
            column_2_array,
        )

        # Assert
        self.assertIsNotNone(column_1_array)
        self.assertIsNotNone(column_2_array)

        self.assertEqual(first=expected_csv_lines_count, second=column_1_array.size)
        self.assertEqual(first=expected_csv_lines_count, second=column_2_array.size)


if __name__ == "__main__":
    unittest.main()
