"""Defines unit tests related to nipcbatt.pcbatt_analysis.library_info module."""

import logging
import platform
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_analysis import analysis_library_info
from nipcbatt.pcbatt_utilities import functional_utilities


class TestAnalysisLibraryInfo(unittest.TestCase):
    """Defines a test fixture that checks function of module
    `pcbatt_analysis.library_info`.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        analysis_library_info.enable_traces(False)

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")
        analysis_library_info.enable_traces(False)

    def test_get_labview_analysis_traces_folder_path(self):
        """Test of pcbatt_analysis.library_info.get_labview_analysis_traces_folder_path"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (201 > 100 characters) (auto-generated noqa)
        # Arrange
        analysis_library_info.enable_traces(True)

        # Act
        folder_path = analysis_library_info.get_labview_analysis_traces_folder_path()

        logging.debug("%s = %s", nameof(folder_path), folder_path)

        # Assert
        self.assertIsNotNone(folder_path)
        self.assertTrue(folder_path)

    @functional_utilities.repeat(10)
    def test_enable_traces(self):
        """Test of pcbatt_analysis.library_info.enable_traces"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)
        analysis_library_info.enable_traces(True)
        traces_are_enabled = analysis_library_info.are_traces_enabled()

        self.assertTrue(traces_are_enabled)

        analysis_library_info.enable_traces(False)
        traces_are_enabled = analysis_library_info.are_traces_enabled()
        self.assertFalse(traces_are_enabled)

    @functional_utilities.repeat(10)
    def test_are_traces_enabled(self):
        """Test of pcbatt_analysis.library_info.are_traces_enabled"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)
        traces_are_enabled = analysis_library_info.are_traces_enabled()
        self.assertFalse(traces_are_enabled)

    @functional_utilities.repeat(10)
    def test_is_labview_runtime_available(self):
        """Test of pcbatt_analysis.library_info.is_labview_runtime_available"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (190 > 100 characters) (auto-generated noqa)
        runtime_is_available = analysis_library_info.is_labview_runtime_available()
        self.assertIsNotNone(runtime_is_available)

    @functional_utilities.repeat(10)
    def test_get_labview_analysis_library_version_numbers(self):
        """Test of pcbatt_analysis.library_info.get_labview_analysis_library_version"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        library_version_numbers = (
            analysis_library_info.get_labview_analysis_library_version_numbers()
        )

        logging.debug("%s = %s", nameof(library_version_numbers), library_version_numbers)

        self.assertIsNotNone(library_version_numbers)
        self.assertEqual(4, len(library_version_numbers))
        self.assertGreater(library_version_numbers[0], 0)
        self.assertGreater(library_version_numbers[3], 0)

    @functional_utilities.repeat(10)
    def test_get_labview_analysis_available_functions_names_list(self):
        """Test of pcbatt_analysis.library_info.get_supported_labview_functions_names_list"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (204 > 100 characters) (auto-generated noqa)
        labview_function_names = (
            analysis_library_info.get_labview_analysis_available_functions_names_list()
        )

        self.assertIsNotNone(labview_function_names)
        self.assertTrue(len(labview_function_names) >= 1)


if __name__ == "__main__":
    unittest.main()
