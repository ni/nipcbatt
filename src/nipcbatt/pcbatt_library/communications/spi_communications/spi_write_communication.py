""" Defines class used for SPI write communication on PCB points. """

import time

import numpy

from nipcbatt.pcbatt_library.common.communication_data_types import (
    MemoryAddressParameters,
)
from nipcbatt.pcbatt_library.common.communication_functions import (
    compute_pages_characteristics,
    create_command_for_spi_write_communication,
)
from nipcbatt.pcbatt_library.spi_communications.spi_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library.spi_communications.spi_write_data_types import (
    SpiWriteCommunicationConfiguration,
    SpiWriteParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import (
    BuildingBlockUsingNi845xSpiDevice,
)


class SpiWriteCommunication(BuildingBlockUsingNi845xSpiDevice):
    """Defines a way that allows you to perform a write operation to SPI device,"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)

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

    def configure_and_write_data(self, configuration: SpiWriteCommunicationConfiguration) -> None:
        """Defines class used for SPI write communication on PCB points.

        Args:
            configuration (SpiWriteCommunicationConfiguration):
                An instance of `SpiWriteCommunicationConfiguration`,
                encapsulating parameters used to configure communication.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        # Configuration of the device for SPI communications.
        self.configure_device_for_spi_communications(parameters=configuration.device_parameters)

        # Configuration of SPI communication.
        self.configure_spi_communication(parameters=configuration.communication_parameters)

        # Write of data bytes to SPI device.
        self.write_data(parameters=configuration.write_parameters)

    def configure_device_for_spi_communications(self, parameters: SpiDeviceParameters) -> None:
        """Configures the device for SPI communications.

        Args:
            parameters (SpiDeviceParameters):
                A `SpiDeviceParameters` object used to configure the device for SPI communications.
        """
        self.devices_handler.set_input_output_voltage_level(parameters.voltage_level)

    def configure_spi_communication(self, parameters: SpiCommunicationParameters) -> None:
        """Configures the SPI communication.

        Args:
            parameters (SpiCommunicationParameters):
                A `SpiCommunicationParameters` object used to configure SPI communications.
        """
        self.devices_handler.configuration.chip_select = parameters.chip_select
        self.devices_handler.configuration.clock_rate_kilohertz = parameters.clock_rate_kilohertz
        self.devices_handler.configuration.clock_phase = parameters.clock_phase
        self.devices_handler.configuration.clock_polarity = parameters.clock_polarity

    def write_data(self, parameters: SpiWriteParameters) -> None:
        """Reads data bytes from an SPI device.

        Args:
            parameters (SpiWriteParameters):
                A `SpiWriteParameters` object used
                to perform read operations on SPI device.
        """
        pages_characteristics = compute_pages_characteristics(
            data_memory_start_address=parameters.memory_address_parameters.memory_address,
            number_of_bytes_to_write=parameters.data_to_be_written.size,
            number_of_bytes_per_page=parameters.number_of_bytes_per_page,
        )

        for page_characteristics in pages_characteristics:
            # Compute the address of the page as a data bytes collection.
            address_parameters = MemoryAddressParameters(
                memory_address=page_characteristics.data_memory_address,
                address_type=parameters.memory_address_parameters.address_type,
                address_endianness=parameters.memory_address_parameters.address_endianness,
            )

            data_to_be_written = create_command_for_spi_write_communication(
                address_parameters=address_parameters,
                number_of_bytes_to_write=page_characteristics.number_of_bytes_in_page,
            )

            # After the address where data will be stored, append the data bytes themselves.
            source_start_index = page_characteristics.index_in_data_bytes_array
            source_end_index = source_start_index + page_characteristics.number_of_bytes_in_page
            destination_start_index = (
                numpy.dtype(numpy.ubyte).itemsize + address_parameters.address_type.value
            )
            destination_end_index = (
                destination_start_index + page_characteristics.number_of_bytes_in_page
            )

            # Copy the data bytes of page to buffer
            numpy.put(
                data_to_be_written,
                range(destination_start_index, destination_end_index),
                parameters.data_to_be_written[source_start_index:source_end_index],
            )

            # Write the data.
            self.devices_handler.write_and_read_data(
                data_bytes_to_be_written=data_to_be_written,
                number_of_bytes_to_read=data_to_be_written.size,
            )

            time.sleep(parameters.delay_between_page_write_operations_milliseconds / 1000.0)
