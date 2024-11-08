""" Serial communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (150 > 100 characters) (auto-generated noqa)

import pyvisa.constants
from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SerialCommunicationParameters(PCBATestToolkitData):
    """Defines the parameters used to configure serial device for communications."""

    def __init__(
        self,
        data_rate_bauds: int,
        number_of_bits_in_data_frame: int,
        delay_before_receive_response_milliseconds: int,
        parity: pyvisa.constants.Parity,
        stop_bits: pyvisa.constants.StopBits,
        flow_control: pyvisa.constants.ControlFlow,
    ):
        """Initializes an instance of
        `SerialCommunicationParameters` with specific values.

        Args:
            data_rate_bauds (int):
                The baud rate of the communication.
            number_of_bits_in_data_frame (int):
                The number of data bits contained in each frame
                (4, 5, 6, 7, or 8).
            delay_before_receive_response (int):
                The delay time that occurs after the send of command
                and before the reception of response.
            parity (pyvisa.constants.Parity):
                The `pyvisa.constants.Parity` value representing
                the parity used with every frame transmitted and received.
            stop_bits (pyvisa.constants.StopBits):
                The `pyvisa.constants.StopBits` value representing
                the number of stop bits used to indicate the end of a frame.
            flow_control (pyvisa.constants.ControlFlow):
                The `pyvisa.constants.ControlFlow` value representing
                the flow control mechanism(s) used by the serial communication.

        Raises:
            ValueError:
                Raised when
                `data_rate_bauds` is negative or equal to zero,
                `number_of_bits_in_data_frame` is lower than 4 or greater than 8,
                `delay_before_receive_response_milliseconds` is negative or equal to zero.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(data_rate_bauds, nameof(data_rate_bauds))
        Guard.is_within_limits_included(
            number_of_bits_in_data_frame,
            4,
            8,
            nameof(number_of_bits_in_data_frame),
        )
        Guard.is_greater_than_zero(
            delay_before_receive_response_milliseconds,
            nameof(delay_before_receive_response_milliseconds),
        )

        self._data_rate_bauds = data_rate_bauds
        self._number_of_bits_in_data_frame = number_of_bits_in_data_frame
        self._delay_before_receive_response_milliseconds = (
            delay_before_receive_response_milliseconds
        )
        self._parity = parity
        self._stop_bits = stop_bits
        self._flow_control = flow_control

    @property
    def data_rate_bauds(self) -> int:
        """Gets the baud rate of the communication."""
        return self._data_rate_bauds

    @property
    def number_of_bits_in_data_frame(self) -> int:
        """Gets the number of data bits contained in each frame
        (4, 5, 6, 7, or 8)."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (323 > 100 characters) (auto-generated noqa)
        return self._number_of_bits_in_data_frame

    @property
    def delay_before_receive_response_milliseconds(self) -> int:
        """Gets the delay time that occurs after the send of command
        and before the reception of response."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (341 > 100 characters) (auto-generated noqa)
        return self._delay_before_receive_response_milliseconds

    @property
    def parity(self) -> pyvisa.constants.Parity:
        """Gets the `pyvisa.constants.Parity` value representing
        the parity used with every frame transmitted and received."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (362 > 100 characters) (auto-generated noqa)
        return self._parity

    @property
    def stop_bits(self) -> pyvisa.constants.StopBits:
        """Gets the `pyvisa.constants.StopBits` value representing
        the number of stop bits used to indicate the end of a frame."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (364 > 100 characters) (auto-generated noqa)
        return self._stop_bits

    @property
    def flow_control(self) -> pyvisa.constants.ControlFlow:
        """Gets the `pyvisa.constants.ControlFlow` value representing
        the flow control mechanism(s) used by the serial communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (367 > 100 characters) (auto-generated noqa)
        return self._flow_control


class SerialCommunicationConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of the serial communication."""

    def __init__(
        self,
        communication_parameters: SerialCommunicationParameters,
        command_to_send: str,
    ):
        """Initializes an instance of
        `SerialCommunicationConfiguration` with specific values.

        Args:
            communication_parameters (SerialCommunicationParameters):
                An instance of `SerialCommunicationParameters`
                that represents the parameters used for settings of serial communication.
            command_to_send (str):
                The string representing the command to send.

        Raises:
            ValueError:
                Raised when
                `communication_parameters` is None,
                `command_to_send` is None or empty or whitespace.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(communication_parameters, nameof(communication_parameters))
        Guard.is_not_none_nor_empty_nor_whitespace(command_to_send, nameof(command_to_send))

        self._communication_parameters = communication_parameters
        self._command_to_send = command_to_send

    @property
    def communication_parameters(self) -> SerialCommunicationParameters:
        """Gets the instance of `SerialCommunicationParameters`
        that represents the parameters used for settings of serial communication."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (377 > 100 characters) (auto-generated noqa)
        return self._communication_parameters

    @property
    def command_to_send(self) -> str:
        """Gets the string representing the command to send."""
        return self._command_to_send


class SerialCommunicationData(PCBATestToolkitData):
    """Defines data obtained after serial communication on serial device."""

    def __init__(self, received_response: str):
        """Initializes an instance of
        `SerialCommunicationData` with specific values.

        Args:
            received_response (str):
                The received response after serial communication.

        Raises:
            ValueError:
                Raised when
                `received_response` is None or empty or whitespace.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_not_none_nor_empty_nor_whitespace(received_response, nameof(received_response))

        self._received_response = received_response

    @property
    def received_response(self) -> str:
        """Gets the received response after serial communication."""
        return self._received_response
