""" Defines class used for I2C read communication on PCB points. """

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import Ni845xPullupStatus
from nipcbatt.pcbatt_library.common.communication_functions import (
    create_command_for_i2c_communications,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types import (
    I2cReadCommunicationConfiguration,
    I2cReadCommunicationData,
    I2cReadParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import (
    BuildingBlockUsingNi845xI2cDevice,
)


class I2cReadCommunication(BuildingBlockUsingNi845xI2cDevice):
    """Defines a way that allows you to perform a read operation from I2C device."""

    def initialize(self, device_name: str):
        """Initializes the communication with the specific NI 845x device.

        Args:
            device_name (str): The name of a communication device.
        """
        if self.is_devices_handler_initialized:
            return

        self.devices_handler.open(device_name=device_name)

    def close(self):
        """Closes communication procedure and releases internal resources."""
        if not self.is_devices_handler_initialized:
            return

        self.devices_handler.close()

    def configure_and_read_data(
        self,
        configuration: I2cReadCommunicationConfiguration,
    ) -> I2cReadCommunicationData:
        """Configures and performs read operation according to specific configuration parameters.

        Args:
            configuration (I2cReadCommunicationConfiguration):
                An instance of `I2cReadCommunicationConfiguration`,
                encapsulating parameters used to configure communication.

        Returns:
            I2cReadCommunicationData:
                An instance of `I2cReadCommunicationData`, encapsulating the data bytes read.
        """
        # Configuration of the device for I2C communications.
        self.configure_device_for_i2c_communications(parameters=configuration.device_parameters)

        # Configuration of I2C communication.
        self.configure_i2c_communication(parameters=configuration.communication_parameters)

        # Read of data bytes from I2C device.
        return self.read_data(parameters=configuration.read_parameters)

    def configure_device_for_i2c_communications(self, parameters: I2cDeviceParameters) -> None:
        """Configures the device for I2C communications.

        Args:
            parameters (I2cDeviceParameters):
                A `I2cDeviceParameters` object used to configure the device for I2C communications.
        """
        self.devices_handler.set_input_output_voltage_level(voltage_level=parameters.voltage_level)
        self.devices_handler.enable_pullup_resistors = (
            Ni845xPullupStatus.PULLUP_ENABLE
            if parameters.enable_i2c_pullup_resistor
            else Ni845xPullupStatus.PULLUP_DISABLE
        )

    def configure_i2c_communication(self, parameters: I2cCommunicationParameters) -> None:
        """Configures the I2C communication.

        Args:
            parameters (I2cCommunicationParameters):
                A `I2cCommunicationParameters` object used to configure I2C communications.
        """
        self.devices_handler.configuration.address = parameters.device_address
        self.devices_handler.configuration.addressing_type = parameters.addressing_type
        self.devices_handler.configuration.clock_rate_kilohertz = parameters.clock_rate_kilohertz
        self.devices_handler.configuration.ack_poll_timeout_milliseconds = (
            parameters.ack_poll_timeout_milliseconds
        )

    def read_data(self, parameters: I2cReadParameters) -> I2cReadCommunicationData:
        """Reads data bytes from an I2C device.

        Args:
            parameters (I2cReadParameters):
                A `I2cReadParameters` object used
                to perform read operations on I2C device.

        Returns:
            I2cReadCommunicationData:
                An instance of `I2cReadCommunicationData`, encapsulating the data bytes read.
        """
        data_to_be_writtten = create_command_for_i2c_communications(
            address_parameters=parameters.memory_address_parameters
        )
        data_bytes_read = self.devices_handler.write_and_read_data(
            data_bytes_to_be_written=data_to_be_writtten,
            number_of_bytes_to_read=parameters.number_of_bytes_to_read,
        )
        return I2cReadCommunicationData(data_bytes_read=data_bytes_read)
