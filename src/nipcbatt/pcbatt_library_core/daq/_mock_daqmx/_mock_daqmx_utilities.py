"""Provides a set of higher order function utilities related to daqmx."""

import logging
from typing import Type

import nidaqmx
import nidaqmx.errors
import nidaqmx.system.system

from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_task import (
    _MockSystem,
    _MockTask,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.reflection_utilities import substitute_method


def _replace_daqmx(interpreter_class: Type):
    """Substitutes mock version of nidaqmx in Building block class.

    Args:
        interpreter_class (Type): Class of interpreter to use in mock version.
    """

    def _instrument_factory() -> _MockTask:
        logging.debug("Using mock version of nidaqmx.Task")
        return _MockTask(interpreter=interpreter_class())

    def _daqmx_local_system() -> _MockSystem:
        return _MockSystem.local(interpreter=interpreter_class())

    substitute_method(
        cls=BuildingBlockUsingDAQmx,
        method=_instrument_factory,
        method_name="_instrument_factory",
    )

    substitute_method(
        cls=BuildingBlockUsingDAQmx,
        method=_daqmx_local_system,
        method_name="_daqmx_local_system",
    )


def _replace_daqmx_if_not_installed(interpreter_class: Type):
    """Substitutes mock version of nidaqmx in Building block class
    if nidaqmx in not installed on local system.
    Args:
        interpreter_class (Type): Class of interpreter to use in mock version.
    """  # noqa: D202, D205, D411, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

    def _instrument_factory() -> nidaqmx.Task:
        try:
            task = nidaqmx.Task()
            logging.debug("Using nidaqmx.Task")
            return task
        except nidaqmx.errors.DaqNotFoundError:
            logging.debug("Using mock version of nidaqmx.Task")
            return _MockTask(interpreter=interpreter_class())

    def _daqmx_local_system() -> nidaqmx.system.system.System:
        try:
            print(nidaqmx.system.system.System.local().driver_version)
            return nidaqmx.system.system.System.local()
        except nidaqmx.errors.DaqNotFoundError:
            return _MockSystem.local(interpreter=interpreter_class())

    substitute_method(
        cls=BuildingBlockUsingDAQmx,
        method=_instrument_factory,
        method_name="_instrument_factory",
    )

    substitute_method(
        cls=BuildingBlockUsingDAQmx,
        method=_daqmx_local_system,
        method_name="_daqmx_local_system",
    )
