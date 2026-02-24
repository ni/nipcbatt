""" Constants data types for serial communications."""

import dataclasses

import pyvisa.constants


@dataclasses.dataclass
class ConstantsForSerialCommunication:
    """Constants used for serial communication."""

    DEFAULT_PARITY = pyvisa.constants.Parity.none
    DEFAULT_DELAY_BEFORE_RECEIVE_RESPONSE_MILLISECONDS = 500
    DEFAULT_STOP_BITS = pyvisa.constants.StopBits.one
    DEFAULT_FLOW_CONTROL_MODE = pyvisa.constants.ControlFlow.none
