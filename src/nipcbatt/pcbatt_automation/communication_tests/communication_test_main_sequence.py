"""Main sequence for executing communication test sequence"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (172 > 100 characters) (auto-generated noqa)

# pylint: disable=W0105

# import functions
from nipcbatt.pcbatt_automation.communication_tests.i2c_comm_test import i2c_comm_test
from nipcbatt.pcbatt_automation.communication_tests.serial_comm_test import (
    serial_comm_test,
)
from nipcbatt.pcbatt_automation.communication_tests.spi_comm_test import spi_comm_test

"""Note to run with simulation: Test sequence cannot be executed in simulation mode"""

############# MAIN ####################

# Example demonstrates simple read and write data operations through I2C protocol
# communication using NI 845x Device

i2c_comm_test()

# Example demonstrates simple read and write data operations through SPI protocol
# communication using NI 845x Device

spi_comm_test()

## Example demonstrates simple read and write data operations through Serial COM port

serial_comm_test()
