# pylint: disable=W0231, W0221
"""Simulation of DAQmx implementation."""
import nidaqmx
import nidaqmx.constants
import nidaqmx.system.system
import nidaqmx.utils


class _MockSystem(nidaqmx.system.system.System):
    """Defines methods used to discover mock instruments."""

    def __init__(self, interpreter):
        self._interpreter = interpreter

    @staticmethod
    def local(interpreter):
        """
        nidaqmx.system.system.System: Represents the local DAQmx system.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        return _MockSystem(interpreter=interpreter)


class _MockTask(nidaqmx.Task):
    """Defines methods used to simulate instruments though DAQmx tasks."""

    def __init__(self, new_task_name="", *, interpreter=None):
        self._close_on_exit = False
        self._saved_name = new_task_name  # _initialize sets this to the name assigned by DAQmx.
        self._grpc_options = None
        self._event_handlers = {}

        # assign a custom interpreter.
        self._interpreter = interpreter
        self._handle, self._close_on_exit = self._interpreter.create_task(new_task_name)

        self._initialize(self._handle, self._interpreter)

    def close(self):
        """
        Clears the task.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if self._handle is None:
            return

        self._interpreter.clear_task(self._handle)
        self._handle = None
