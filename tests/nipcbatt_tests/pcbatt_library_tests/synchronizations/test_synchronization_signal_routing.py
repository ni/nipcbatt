"""This module provides SynchronizationSignalsRouting check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

from nipcbatt.pcbatt_library.synchronizations.synchronization_signal_routing import (
    SynchronizationSignalRouting,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestSynchronizationSignalRouting(unittest.TestCase):
    """Defines a test fixture that checks
    `SynchronizationSignalRouting` class is ready to use.

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
        _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_route_sample_clock_signal_to_terminal_fails_when_terminal_name_is_none(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_sample_clock_signal_to_terminal(terminal_name=None)

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_sample_clock_signal_to_terminal_fails_when_terminal_name_is_empty(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_sample_clock_signal_to_terminal(terminal_name="")

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_sample_clock_signal_to_terminal_fails_when_terminal_name_is_whitespace(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_sample_clock_signal_to_terminal(terminal_name=" ")

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_sample_clock_signal_to_terminal(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_sample_clock_signal_to_terminal."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (192 > 100 characters) (auto-generated noqa)
        # Arrange
        with SynchronizationSignalRouting() as synchronization_signal_routing:
            # Act
            synchronization_signal_routing.route_sample_clock_signal_to_terminal(
                terminal_name="/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
            )
            # Assert

    def test_route_start_trigger_signal_to_terminal_fails_when_terminal_name_is_none(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (270 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_start_trigger_signal_to_terminal(
                terminal_name=None
            )

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_start_trigger_signal_to_terminal_fails_when_terminal_name_is_empty(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal."""  # noqa: D202, D403, W505 - No blank lines allowed after function docstring (auto-generated noqa), First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (270 > 100 characters) (auto-generated noqa)

        # Arrange
        synchronization_signal_routing = SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_start_trigger_signal_to_terminal(terminal_name="")

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_start_trigger_signal_to_terminal_fails_when_terminal_name_is_whitespace(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)
        synchronization_signal_routing = SynchronizationSignalRouting()

        # Act
        with self.assertRaises(ValueError) as ctx:
            synchronization_signal_routing.route_start_trigger_signal_to_terminal(terminal_name=" ")

        # Assert
        self.assertEqual(
            "The string value terminal_name is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_route_start_trigger_signal_to_terminal(
        self,
    ):
        """unit test of SynchronizationSignalRouting.route_start_trigger_signal_to_terminal."""  # noqa: D403, W505 - First word of the first line should be properly capitalized (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)
        # Arrange
        with SynchronizationSignalRouting() as synchronization_signal_routing:
            # Act
            synchronization_signal_routing.route_start_trigger_signal_to_terminal(
                terminal_name="/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
            )
            # Assert


if __name__ == "__main__":
    unittest.main()
