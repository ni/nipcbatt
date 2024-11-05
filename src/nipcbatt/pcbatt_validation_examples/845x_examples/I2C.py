""" This example demonstrates use of LM75 I2C Temperature sensor for taking 
 temperature measurements using USB-8452 device """

### Ensure correct hardware and corresponding trigger names before running this example

import time
import numpy
import nipcbatt
import nipcbatt.pcbatt_communication_library
import nipcbatt.pcbatt_communication_library.ni_845x_data_types
import nipcbatt.pcbatt_communication_library.ni_845x_devices
import nipcbatt.pcbatt_communication_library.ni_845x_i2c_communication_devices
import nipcbatt.pcbatt_library
import nipcbatt.pcbatt_communication_library._ni_845x_internal
import nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions
from ctypes import c_uint8
import threading

# Flag to control the loop
running = True


def check_input():
    global running
    input("Press Enter to exit...\n")
    running = False


# Start a thread to listen for Enter key
input_thread = threading.Thread(target=check_input)
input_thread.start()

# Initialize
i2c = (
    nipcbatt.pcbatt_communication_library.ni_845x_i2c_communication_devices.Ni845xI2cDevicesHandler()
)
i2c.open(device_name="USB-8452")

# pylint: disable=protected-access
handle_type = (
    nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions._get_handle_type()
)

# begin I2C Configure
nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions.invoke_ni_845x_function(
    nipcbatt.pcbatt_communication_library._ni_845x_internal._ni_845x_functions._Ni845xFunctionsNames.NI_845X_SET_IO_VOLTAGE_LEVEL,
    handle_type(i2c._devices_handler),
    c_uint8(nipcbatt.pcbatt_communication_library.ni_845x_data_types.Ni845xVoltageLevel(33)),
)
# region manual call
i2c.enable_pullup_resistors(enable=False)
i2c.set_timeout(timeout_milliseconds=40000)

i2c.configuration.address = 73
seven_bits = nipcbatt.pcbatt_communication_library.ni_845x_data_types.Ni845xI2cAddressingType(0)
i2c.configuration.addressing_type = seven_bits
i2c.configuration.clock_rate_kilohertz = 400

data_bytes_to_be_written = numpy.ndarray(shape=[0], dtype=numpy.ubyte)
i2c_write_read = i2c.write_and_read_data(
    data_bytes_to_be_written=data_bytes_to_be_written, number_of_bytes_to_read=2
)
# end region I2C configure

# Region infinite Loop

# Click on the terminal and press Enter to exit this infinite loop
while running:
    i2c_read = i2c.read_data(number_of_bytes_to_read=2)

    # region temperature measure
    lsb = i2c_read[1]
    msb = i2c_read[0]
    joined = hex((msb << 8) + lsb)

    joined_ubyte = int(joined, 16)

    five_shifted = numpy.right_shift(joined_ubyte, 5)

    if numpy.right_shift(joined_ubyte, 15) != 0:
        five_shifted = numpy.add(five_shifted, numpy.int8(63488), dtype=numpy.int8)

    temp = five_shifted * 0.125
    print("Temperature : " + str(temp) + "°C\n")
    time.sleep(0.5)
    # endregion temperature measure

# Wait for the input thread to finish before exiting
input_thread.join()
