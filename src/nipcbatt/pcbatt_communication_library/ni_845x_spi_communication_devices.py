"""Provides SPI communication with NI-845x devices."""

import numpy

from nipcbatt.pcbatt_communication_library._ni_845x_internal import _ni_845x_functions
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_communication_library.ni_845x_devices import Ni845xDevicesHandler
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)


class Ni845xSpiDevicesHandler(Ni845xDevicesHandler):
    """Defines handler on SPI devices."""

    def __init__(self) -> None:
        """Default initialization of new `Ni845xSpiDevicesHandler` object"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)
        super().__init__()
        self._configuration_handle = _ni_845x_functions.ni_845x_spi_configuration_open_impl()

    def close(self):
        """Closes a previously opened device.

        Raises:
            PCBATTCommunicationException:
                Raised when an error occured while calling `ni845xClose` function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_spi_configuration_close_impl(self._configuration_handle)
        super().close()

    @property
    def configuration(self):
        """Gets an instance of `` used to configure I2C communication.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before.
        """
        return Ni845xSpiConfiguration(self._configuration_handle)

    def write_and_read_data(
        self,
        data_bytes_to_be_written: numpy.ndarray[numpy.ubyte],
        number_of_bytes_to_read: int,
    ) -> numpy.ndarray[numpy.ubyte]:
        """Performs a write followed by read (combined format) on an SPI slave device.

        Args:
            data_bytes_to_be_written (numpy.ndarray[numpy.ubyte]): The number of bytes to write.
            number_of_bytes_to_read (int): The number of bytes to read.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiWriteRead` function from `ni845x.dll`

        Returns:
            numpy.ndarray[numpy.ubyte]: A `numpy.ndarray`
            of bytes containing data that have been read.
        """
        if self._devices_handler is None:
            raise PCBATTCommunicationException(
                PCBATTCommunicationExceptionMessages.OPEN_METHOD_MUST_BE_CALLED_FIRST
            )

        data_bytes_array = numpy.zeros(
            shape=(number_of_bytes_to_read),
            dtype=numpy.ubyte,
        )

        _ni_845x_functions.ni_845x_spi_write_read_impl(
            device_handle=self._devices_handler,
            configuration_handle=self._configuration_handle,
            write_data_array=data_bytes_to_be_written,
            read_data_array=data_bytes_array,
        )

        return data_bytes_array


class Ni845xSpiConfiguration:
    """Defines methods used to configure SPI communication on a SPI device."""

    def __init__(self, configuration_handle: int) -> None:
        """Initializes an instance of
        `Ni845xI2cConfiguration` with specific values.

        Args:
            configuration_handle (int): The configuration handle.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._configuration_handle = configuration_handle

    @property
    def chip_select(self) -> int:
        """Gets the chip select value for SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationSetChipSelect`
                function from `ni845x.dll`

        Returns:
            int: The configuration address.
        """
        return _ni_845x_functions.ni_845x_spi_configuration_get_chip_select_impl(
            configuration_handle=self._configuration_handle
        )

    @chip_select.setter
    def chip_select(self, val: int):
        """Sets the chip select value for SPI configuration.

        Args:
            val (int): the chip select value for SPI configuration.
        """
        _ni_845x_functions.ni_845x_spi_configuration_set_chip_select_impl(
            configuration_handle=self._configuration_handle, chip_select=val
        )

    @property
    def clock_rate_kilohertz(self) -> int:
        """Gets the clock rate of the SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationGetClockRate`
                function from `ni845x.dll`

        Returns:
            int: the clock rate of the SPI configuration.
        """
        return _ni_845x_functions.ni_845x_spi_configuration_get_clock_rate_impl(
            configuration_handle=self._configuration_handle
        )

    @clock_rate_kilohertz.setter
    def clock_rate_kilohertz(self, val: int):
        """Sets the clock rate of the SPI configuration.

        Args:
            val (int): the clock rate of the SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationSetClockRate`
                function from `ni845x.dll`
        """
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_rate_impl(
            configuration_handle=self._configuration_handle, clock_rate_kilohertz=val
        )

    @property
    def clock_phase(self) -> SpiConfigurationClockPhase:
        """Gets the clock phase value for SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationGetClockPhase`
                function from `ni845x.dll`

        Returns:
            SpiConfigurationClockPhase: The configuration address.
        """
        return _ni_845x_functions.ni_845x_spi_configuration_get_clock_phase_impl(
            configuration_handle=self._configuration_handle
        )

    @clock_phase.setter
    def clock_phase(self, val: SpiConfigurationClockPhase):
        """Sets the clock phase value for SPI configuration.

        Args:
            val (int): the clock phase value for SPI configuration.
        """
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_phase_impl(
            configuration_handle=self._configuration_handle, clock_phase=val
        )

    @property
    def clock_polarity(self) -> SpiConfigurationClockPolarity:
        """Gets the clock polarity value for SPI configuration.

        Raises:
            PCBATTCommunicationException:
                Raised when
                the method `open` was nor called before or
                an error occured while calling `ni845xSpiConfigurationGetClockPolarity`
                function from `ni845x.dll`

        Returns:
            int: The clock polarity value for SPI configuration.
        """
        return _ni_845x_functions.ni_845x_spi_configuration_get_clock_polarity_impl(
            configuration_handle=self._configuration_handle
        )

    @clock_polarity.setter
    def clock_polarity(self, val: SpiConfigurationClockPolarity):
        """Sets the clock polarity value for SPI configuration.

        Args:
            val (int): the clock polarity value for SPI configuration.
        """
        _ni_845x_functions.ni_845x_spi_configuration_set_clock_polarity_impl(
            configuration_handle=self._configuration_handle, clock_polarity=val
        )
