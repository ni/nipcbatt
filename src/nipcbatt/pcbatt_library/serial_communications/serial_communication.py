""" Defines class used for serial communication on serial devices. """

from nipcbatt.pcbatt_library.serial_communications.serial_data_types import (
    SerialCommunicationConfiguration,
    SerialCommunicationData,
    SerialCommunicationParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingVisa


class SerialCommunication(BuildingBlockUsingVisa):
    """Defines a way that allows you to perform operations on serial device."""

    def initialize(self, serial_device_name: str):
        """Initializes the communication with the specific serial device.

        Args:
            serial_device_name (str): The name of a serial device.
        """
        if self.is_serial_device_handler_initialized:
            return

        self.open_serial_device(serial_device_name=serial_device_name)

    def close(self):
        """Closes communication procedure and releases internal resources."""
        if not self.is_serial_device_handler_initialized:
            return

        self.close_serial_device()

    def configure_then_send_command_and_receive_response(
        self, configuration: SerialCommunicationConfiguration
    ) -> SerialCommunicationData:
        """Configures then performs serial communication operations
        according to specific configuration parameters.

        Args:
            configuration (SerialCommunicationConfiguration):
                An instance of `SerialCommunicationConfiguration`,
                encapsulating parameters used to configure communication.

        Returns:
            SerialCommunicationData:
                An instance of `SerialCommunicationData`
                encapsulating the received response.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Configuration of the device for serial communications.
        self.configure_serial_communication(parameters=configuration.communication_parameters)

        # Send command and receive response.
        return SerialCommunicationData(
            received_response=self.send_command_and_receive_response(configuration.command_to_send)
        )

    def configure_serial_communication(self, parameters: SerialCommunicationParameters):
        """Configures the serial communication.

        Args:
            parameters (SerialCommunicationParameters):
                A `SerialCommunicationParameters` object used
                to configure the device for serial communications.
        """
        self.serial_device_handler.baud_rate = parameters.data_rate_bauds
        self.serial_device_handler.data_bits = parameters.number_of_bits_in_data_frame

        self.serial_device_handler.query_delay = (
            parameters.delay_before_receive_response_milliseconds / 1000.0
        )

        self.serial_device_handler.parity = parameters.parity
        self.serial_device_handler.stop_bits = parameters.stop_bits
        self.serial_device_handler.flow_control = parameters.flow_control

    def send_command_and_receive_response(self, command_to_send: str) -> str:
        """Sends a command to a serial device and receive response from it.

        Args:
            command_to_send (str): The string representing the command to send.

        Returns:
            str: The response sent back by the serial communication.
        """
        return self.serial_device_handler.query(message=command_to_send)
