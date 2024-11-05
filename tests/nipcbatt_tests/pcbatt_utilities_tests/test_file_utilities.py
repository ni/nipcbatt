"""Provides unit tests related to file_utilities.py module"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)

import logging
import os
import platform
import sys
import unittest
from pathlib import Path

from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_utilities import (
    file_utilities,
    functional_utilities,
    iterable_utilities,
)


class TestFileUtilities(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_utilities.file_utilities`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

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
            nameof(TestFileUtilities),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    @functional_utilities.repeat(2)
    def test_write_lines(self):
        """Unit test of file_utilities.write_lines"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (164 > 100 characters) (auto-generated noqa)
        # Arrange
        file_output_path = os.path.join(
            TestFileUtilities.tests_output_folder_path,
            "test_write_lines.txt",
        )
        file_lines = ["a", "b", "c"]

        # Act
        file_utilities.write_lines(
            text_file_path=file_output_path,
            text_file_encoding="utf8",
            text_lines=file_lines,
        )

        # Assert
        self.assertTrue(os.path.exists(path=file_output_path))

    @functional_utilities.repeat(2)
    def test_read_lines(self):
        """Unit test of file_utilities.read_lines"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (163 > 100 characters) (auto-generated noqa)
        # Arrange
        file_input_path = os.path.join(
            TestFileUtilities.tests_output_folder_path,
            "test_read_lines.txt",
        )

        file_lines = ["a", "b", "c"]

        file_utilities.write_lines(
            text_file_path=file_input_path,
            text_file_encoding="utf8",
            text_lines=file_lines,
        )

        # Act
        read_lines = file_utilities.read_lines(
            text_file_path=file_input_path, text_file_encoding="utf8"
        )

        count, iterable_reset = iterable_utilities.count(read_lines)
        # Assert
        self.assertIsNotNone(read_lines)
        self.assertEqual(first=3, second=count)

        read_lines_list = list(iterable_reset)
        self.assertEqual(first=3, second=len(read_lines_list))
        self.assertEqual(first="a", second=read_lines_list[0])
        self.assertEqual(first="b", second=read_lines_list[1])
        self.assertEqual(first="c", second=read_lines_list[2])

    @parameterized.expand([("C:/windows/explorer.exe"), ("C:/windows/system32/kernel32.dll")])
    def test_file_exists_should_not_fail(self, file_path: str):
        """Unit test of nipcbatt.pcbatt_utilities.file_utilities.file_exists"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (267 > 100 characters) (auto-generated noqa)

        self.assertTrue(file_utilities.file_exists(file_path))


if __name__ == "__main__":
    unittest.main()
