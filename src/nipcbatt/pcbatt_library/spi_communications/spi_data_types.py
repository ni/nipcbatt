""" SPI communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

from varname import nameof

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    Ni845xVoltageLevel,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SpiDeviceParameters(PCBATestToolkitData):
    """Defines the parameters used to configure SPI device for communications."""

    def __init__(self, voltage_level: Ni845xVoltageLevel):
        """Initializes an instance of
        `SpiDeviceParameters` with specific values.

        Args:
            voltage_level (Ni845xVoltageLevel):
                The `Ni845xVoltageLevel` value
                representing the voltage level of signal
                sent or received during SPI communications.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._voltage_level = voltage_level

    @property
    def voltage_level(self) -> Ni845xVoltageLevel:
        """Gets the `Ni845xVoltageLevel` value."""
        return self._voltage_level


class SpiCommunicationParameters(PCBATestToolkitData):
    """Defines the parameters used to configure SPI communications."""

    def __init__(
        self,
        chip_select: int,
        clock_rate_kilohertz: int,
        clock_phase: SpiConfigurationClockPhase,
        clock_polarity: SpiConfigurationClockPolarity,
    ):
        """Initializes an instance of
        `SpiCommunicationParameters` with specific values.

        Args:
            chip_select (int):
                The chip select value for SPI configuration.
            clock_rate_kilohertz (int):
                The clock rate to apply to the device communication, in kilohertz.
            clock_phase (SpiConfigurationClockPhase):
                The SpiConfigurationClockPhase value representing
                the clock phase value for SPI configuration.
            clock_polarity (SpiConfigurationClockPolarity):
                The SpiConfigurationClockPolarity value representing
                the clock polarity value for SPI configuration.

        Raises:
            ValueError:
                Raised when
                `chip_select` is negative,
                `clock_rate_kilohertz` is negative or equal to zero,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_zero(clock_rate_kilohertz, nameof(clock_rate_kilohertz))

        self._chip_select = chip_select
        self._clock_rate_kilohertz = clock_rate_kilohertz
        self._clock_phase = clock_phase
        self._clock_polarity = clock_polarity

    @property
    def chip_select(self) -> int:
        """Gets the chip select value for SPI configuration."""
        return self._chip_select

    @property
    def clock_rate_kilohertz(self) -> int:
        """Gets the clock rate to apply to the device communication."""
        return self._clock_rate_kilohertz

    @property
    def clock_phase(self) -> SpiConfigurationClockPhase:
        """Gets the SpiConfigurationClockPhase value representing
        the clock phase value for SPI configuration."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (348 > 100 characters) (auto-generated noqa)
        return self._clock_phase

    @property
    def clock_polarity(self) -> SpiConfigurationClockPolarity:
        """Gets the SpiConfigurationClockPhase value representing
        the clock polarity value for SPI configuration."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (351 > 100 characters) (auto-generated noqa)
        return self._clock_polarity
