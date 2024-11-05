""" Defines class used for I2C write communication on PCB points. """

import time

import numpy

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import Ni845xPullupStatus
from nipcbatt.pcbatt_library.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.common.communication_functions import (
    compute_pages_characteristics,
    create_command_for_i2c_communications,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types import (
    I2cWriteCommunicationConfiguration,
    I2cWriteParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import (
    BuildingBlockUsingNi845xI2cDevice,
)


class I2cWriteCommunication(BuildingBlockUsingNi845xI2cDevice):
    """Defines a way that allows you to perform a write operation to I2C device,"""

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

    def configure_and_write_data(self, configuration: I2cWriteCommunicationConfiguration) -> None:
        """Defines class used for I2C write communication on PCB points.

        Args:
            configuration (I2cWriteCommunicationConfiguration):
                An instance of `I2cWriteCommunicationConfiguration`,
                encapsulating parameters used to configure communication.
        """

        # Configuration of the device for I2C communications.
        self.configure_device_for_i2c_communications(parameters=configuration.device_parameters)

        # Configuration of I2C communication.
        self.configure_i2c_communication(parameters=configuration.communication_parameters)

        # Write of data bytes to I2C device.
        self.write_data(parameters=configuration.write_parameters)

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

    def write_data(self, parameters: I2cWriteParameters) -> None:
        """Reads data bytes from an I2C device.

        Args:
            parameters (I2cWriteParameters):
                A `I2cWriteParameters` object used
                to perform read operations on I2C device.
        """
        pages_characteristics = compute_pages_characteristics(
            data_memory_start_address=parameters.memory_address_parameters.memory_address,
            number_of_bytes_to_write=len(parameters.data_to_be_written),
            number_of_bytes_per_page=parameters.number_of_bytes_per_page,
        )

        for page_characteristics in pages_characteristics:
            # Compute the address of the page as a data bytes collection.
            address_parameters = MemoryAddressParameters(
                memory_address=page_characteristics.data_memory_address,
                address_type=parameters.memory_address_parameters.address_type,
                address_endianness=parameters.memory_address_parameters.address_endianness,
            )

            data_to_be_written = create_command_for_i2c_communications(
                address_parameters=address_parameters
            )

            # After the address where data will be stored, append the data bytes themselves.
            numpy.append(
                data_to_be_written,
                parameters.data_to_be_written[
                    page_characteristics.index_in_data_bytes_array : (
                        page_characteristics.index_in_data_bytes_array
                        + page_characteristics.number_of_bytes_in_page
                    )
                ],
            )

            # Write the data.
            self.devices_handler.write_data(data_bytes_to_be_written=data_to_be_written)

            time.sleep(seconds=parameters.delay_between_page_write_operations_milliseconds / 1000.0)
