""" I2C communication data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (147 > 100 characters) (auto-generated noqa)

from varname import nameof

from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    Ni845xI2cAddressingType,
    Ni845xVoltageLevel,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class I2cDeviceParameters(PCBATestToolkitData):
    """Defines the parameters used to configure I2C device for communications."""

    def __init__(self, enable_i2c_pullup_resistor: bool, voltage_level: Ni845xVoltageLevel):
        """Initializes an instance of
        `I2cDeviceParameters` with specific values.

        Args:
            enable_i2c_pullup_resistor (bool):
                A boolean value that indicates whether
                the on-board pullup resistors for I2C operations are enabled.
            voltage_level (Ni845xVoltageLevel):
                The `Ni845xVoltageLevel` value
                representing the voltage level of signal
                sent or received during I2C communications.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._enable_i2c_pullup_resistor = enable_i2c_pullup_resistor
        self._voltage_level = voltage_level

    @property
    def enable_i2c_pullup_resistor(self) -> bool:
        """Gets whether the on-board pullup resistors for I2C operations are enabled."""
        return self._enable_i2c_pullup_resistor

    @property
    def voltage_level(self) -> Ni845xVoltageLevel:
        """Gets the `Ni845xVoltageLevel` value."""
        return self._voltage_level


class I2cCommunicationParameters(PCBATestToolkitData):
    """Defines the parameters used to configure I2C communications."""

    def __init__(
        self,
        device_address: int,
        addressing_type: Ni845xI2cAddressingType,
        clock_rate_kilohertz: int,
        ack_poll_timeout_milliseconds: int,
    ):
        """Initializes an instance of
        `I2cCommunicationParameters` with specific values.

        Args:
            device_address (int):
                The address of the device.
            addressing_type (Ni845xI2cAddressingType):
                The addressing type used for configuration of I2C communication.
            clock_rate_kilohertz (int):
                The clock rate to apply to the device communication, in kilohertz.
            ack_poll_timeout_milliseconds (int):
                The I2C ACK (acknowledge) polling timeout
                to apply to the device communication, in milliseconds.

        Raises:
            ValueError:
                Raised when
                `device_address` is negative,
                `clock_rate_kilohertz` is negative or equal to zero,
                `ack_poll_timeout_milliseconds` is negative.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        Guard.is_greater_than_or_equal_to_zero(device_address, nameof(device_address))
        Guard.is_greater_than_zero(clock_rate_kilohertz, nameof(clock_rate_kilohertz))
        Guard.is_greater_than_or_equal_to_zero(
            ack_poll_timeout_milliseconds, nameof(ack_poll_timeout_milliseconds)
        )

        self._device_address = device_address
        self._addressing_type = addressing_type
        self._clock_rate_kilohertz = clock_rate_kilohertz
        self._ack_poll_timeout_milliseconds = ack_poll_timeout_milliseconds

    @property
    def device_address(self) -> int:
        """Gets the address of the device."""
        return self._device_address

    @property
    def addressing_type(self) -> Ni845xI2cAddressingType:
        """Gets the addressing type used for configuration of I2C communication."""
        return self._addressing_type

    @property
    def clock_rate_kilohertz(self) -> int:
        """Gets the clock rate to apply to the device communication."""
        return self._clock_rate_kilohertz

    @property
    def ack_poll_timeout_milliseconds(self) -> int:
        """Gets the I2C ACK (acknowledge) polling timeout
        to apply to the device communication, in milliseconds."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (358 > 100 characters) (auto-generated noqa)
        return self._ack_poll_timeout_milliseconds
