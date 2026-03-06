""" Defines class used for routing of synchronization signal."""

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SynchronizationSignalRouting(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to route synchronization signal
    (sample clock or start trigger) to specific terminal."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (353 > 100 characters) (auto-generated noqa)

    def route_sample_clock_signal_to_terminal(self, terminal_name: str):
        """Routes sample clock signal to the specified terminal.

        Args:
            terminal_name (str):
            The name of the terminal where the signal is routed.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(terminal_name, nameof(terminal_name))

        self.task.export_signals.export_signal(
            signal_id=nidaqmx.constants.Signal.SAMPLE_CLOCK,
            output_terminal=terminal_name,
        )

    def route_start_trigger_signal_to_terminal(self, terminal_name: str):
        """Routes start trigger signal to the specified terminal.

        Args:
            terminal_name (str):
            The name of the terminal where the signal is routed.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(terminal_name, nameof(terminal_name))

        self.task.export_signals.export_signal(
            signal_id=nidaqmx.constants.Signal.START_TRIGGER,
            output_terminal=terminal_name,
        )

    def close(self):
        """Closes signal routing procedure."""
