"""Defines datatypes related to NI-845x modules."""

from collections import namedtuple
from enum import IntEnum


class DataMemoryAddressType(IntEnum):
    """Defines on which the size, in bytes,
    the memory address of the communication device is addressed."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (360 > 100 characters) (auto-generated noqa)

    ADDRESS_ENCODED_ON_ONE_BYTE = 1
    """The address is encoded on 1 byte."""

    ADDRESS_ENCODED_ON_TWO_BYTES = 2
    """The address is encoded on 2 bytes."""


class DataMemoryAddressEndianness(IntEnum):
    """Defines the endianness of the memory address
    in a device communication using I2C/SPI protocols."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (350 > 100 characters) (auto-generated noqa)

    LITTLE_ENDIAN = 0
    """Little Endian."""

    BIG_ENDIAN = 1
    """Big Endian."""


class Ni845xPullupStatus(IntEnum):
    """Defines the status of pullup resistor."""

    PULLUP_DISABLE = 0
    """Pullups are disabled."""

    PULLUP_ENABLE = 1
    """Pullups are enabled."""


class Ni845xI2cAddressingType(IntEnum):
    """Defines the addressing type used for configuration of I2C communication."""

    ADDRESSING_7_BIT = 0
    """The NI 845x hardware uses the standard 7-bit
    addressing when communicating with the I2C slave device."""

    ADDRESSING_10_BIT = 1
    """The NI 845x hardware uses the extended 10-bit 
    addressing when communicating with the I2C slave device."""


class Ni845xVoltageLevel(IntEnum):
    """Defines the voltage levels supported by NI-845x devices."""

    VOLTAGE_LEVEL_33 = 33
    """The output I/O high level is 3.3 V."""

    VOLTAGE_LEVEL_25 = 25
    """The output I/O high level is 2.5 V."""

    VOLTAGE_LEVEL_18 = 18
    """The output I/O high level is 1.8 V."""

    VOLTAGE_LEVEL_15 = 15
    """The output I/O high level is 1.5 V."""

    VOLTAGE_LEVEL_12 = 12
    """The output I/O high level is 1.2 V."""


class SpiConfigurationClockPhase(IntEnum):
    """Defines the clock phase used for configuration of SPI communication."""

    CLOCK_PHASE_FIRST_EDGE = 0
    """Data is centered on the first edge of the clock period."""

    CLOCK_PHASE_SECOND_EDGE = 1
    """Data is centered on the second edge of the clock period."""


class SpiConfigurationClockPolarity(IntEnum):
    """Defines the clock polarity used for configuration of SPI communication."""

    CLOCK_POLARITY_IDLE_LOW = 0
    """Clock is low in the idle state."""

    CLOCK_POLARITY_IDLE_HIGH = 1
    """Clock is high in the idle state."""


DevicesFindResultData = namedtuple(
    "DevicesFindResultData", ("device_name", "device_handle", "number_of_devices_found")
)
