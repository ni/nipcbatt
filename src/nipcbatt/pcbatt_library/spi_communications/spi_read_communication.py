""" Defines class used for SPI read communication on PCB points. """

from nipcbatt.pcbatt_library.common.communication_functions import (
    create_command_for_spi_read_communication,
)
from nipcbatt.pcbatt_library.spi_communications.spi_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library.spi_communications.spi_read_data_types import (
    SpiReadCommunicationConfiguration,
    SpiReadCommunicationData,
    SpiReadParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import (
    BuildingBlockUsingNi845xSpiDevice,
)


class SpiReadCommunication(BuildingBlockUsingNi845xSpiDevice):
    """Defines a way that allows you to perform a read operation from SPI device."""

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
        configuration: SpiReadCommunicationConfiguration,
    ) -> SpiReadCommunicationData:
        """Configures and performs read operation according to specific configuration parameters.

        Args:
            configuration (SpiReadCommunicationConfiguration):
                An instance of `SpiReadCommunicationConfiguration`,
                encapsulating parameters used to configure communication.

        Returns:
            SpiReadCommunicationData:
                An instance of `SpiReadCommunicationData`, encapsulating the data bytes read.
        """
        # Configuration of the device for SPI communications.
        self.configure_device_for_spi_communications(parameters=configuration.device_parameters)

        # Configuration of SPI communication.
        self.configure_spi_communication(parameters=configuration.communication_parameters)

        # Read of data bytes from SPI device.
        return self.read_data(parameters=configuration.read_parameters)

    def configure_device_for_spi_communications(self, parameters: SpiDeviceParameters) -> None:
        """Configures the device for SPI communications.

        Args:
            parameters (SpiDeviceParameters):
                A `SpiDeviceParameters` object used to configure the device for SPI communications.
        """
        self.devices_handler.set_input_output_voltage_level(voltage_level=parameters.voltage_level)

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

    def read_data(self, parameters: SpiReadParameters) -> SpiReadCommunicationData:
        """Reads data bytes from an SPI device.

        Args:
            parameters (SpiReadParameters):
                A `SpiReadParameters` object used
                to perform read operations on Spi device.

        Returns:
            SpiReadCommunicationData:
                An instance of `SpiReadCommunicationData`, encapsulating the data bytes read.
        """
        data_to_be_written = create_command_for_spi_read_communication(
            address_parameters=parameters.memory_address_parameters,
            number_of_bytes_to_read=parameters.number_of_bytes_to_read,
        )
        data_bytes_read = self.devices_handler.write_and_read_data(
            data_bytes_to_be_written=data_to_be_written,
            number_of_bytes_to_read=parameters.number_of_bytes_to_read,
        )

        if data_bytes_read.size > parameters.number_of_bytes_to_read:
            data_bytes_read.resize(
                new_shape=(data_bytes_read.size - parameters.number_of_bytes_to_read)
            )

        return SpiReadCommunicationData(data_bytes_read=data_bytes_read)
