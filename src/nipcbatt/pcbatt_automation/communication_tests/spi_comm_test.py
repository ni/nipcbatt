"""Example demonstrates simple read and write data operations through SPI 
   protocol communication using NI 845x Device """ 


import numpy as np

# import functions
import nipcbatt
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# Note to run with Hardware: Update Device ID of the connected SPI Interface Device
# (Ex: NI USB-8452 Device)

DEVICE_ID = "DeviceA"
SESSION_NUMBER = 0

# Set the default file path to save the acquired waveforms and measurement analysis results.
DEFAULT_FILEPATH = "C:\\Windows\\Temp\\spi_comm_test_results.txt"


# region initialize
######## INITIALIZE ################################################################################
def setup():
    """Creates and initializes SPI communication objects"""  

    reader = nipcbatt.SpiReadCommunication()
    reader.initialize(device_name=DEVICE_ID)

    writer = nipcbatt.SpiWriteCommunication()
    writer.initialize(device_name=DEVICE_ID)

    return reader, writer


# endregion initialize


# region configure
####### CONFIGURE/READ & CONFIGURE/WRITE DATA ######################################################
def main(
    reader: nipcbatt.SpiReadCommunication,
    writer: nipcbatt.SpiWriteCommunication,
    write_to_file: bool,
):
    """If you wish to write your results to a file use the following commands
    Make sure the write_to_file option is set to True when calling spi_comm_test()
    Change the file path to desired location on your drive
    The default file path is C:\\Windows\\Temp\\spi_comm_test_results.txt""" 

    # if write_to_file is True, call write_results_to_file in order to output the results to a file
    if write_to_file:
        logger = PcbattLogger(file=DEFAULT_FILEPATH)
        logger.attach(reader)
        logger.attach(writer)

    """Note to run with Hardware: Update Read data settings for SPI communication"""
    read_dev_params = nipcbatt.SpiDeviceParameters(
        voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    )

    read_comm_params = nipcbatt.SpiCommunicationParameters(
        chip_select=0,
        clock_rate_kilohertz=1000,
        clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE,
        clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
    )

    read_mem_params = nipcbatt.MemoryAddressParameters(
        memory_address=0,  # 0x00
        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
        address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
    )

    read_params = nipcbatt.SpiReadParameters(
        number_of_bytes_to_read=32, memory_address_parameters=read_mem_params
    )

    read_config = nipcbatt.SpiReadCommunicationConfiguration(
        device_parameters=read_dev_params,
        communication_parameters=read_comm_params,
        read_parameters=read_params,
    )

    read_data = reader.configure_and_read_data(configuration=read_config)

    # Note to run with Hardware: Update Write data settings for SPI communication
    write_dev_params = nipcbatt.SpiDeviceParameters(
        voltage_level=nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_33
    )

    write_comm_params = nipcbatt.SpiCommunicationParameters(
        chip_select=0,
        clock_rate_kilohertz=1000,
        clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_FIRST_EDGE,
        clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
    )

    data = [np.ubyte(0xAB), np.ubyte(0x1D), np.ubyte(0x11), np.ubyte(0xFF)]
    data_to_write = np.array(data)

    write_mem_params = nipcbatt.MemoryAddressParameters(
        memory_address=0,  # 0x00
        address_type=nipcbatt.DataMemoryAddressType.ADDRESS_ENCODED_ON_TWO_BYTES,
        address_endianness=nipcbatt.DataMemoryAddressEndianness.BIG_ENDIAN,
    )

    write_params = nipcbatt.SpiWriteParameters(
        number_of_bytes_per_page=32,
        delay_between_page_write_operations_milliseconds=5,
        data_to_be_written=data_to_write,
        memory_address_parameters=write_mem_params,
    )

    write_config = nipcbatt.SpiWriteCommunicationConfiguration(
        device_parameters=write_dev_params,
        communication_parameters=write_comm_params,
        write_parameters=write_params,
    )

    writer.configure_and_write_data(configuration=write_config)

    """Storing results -- create both a Python dictionary (hashmap) 
       A dictionary will store values with a key provided by the user"""
    results_map = {}  # this structure will hold results in key-value pairs

    # record result
    results_map["SPI DATA"] = read_data

    return read_data


# endregion configure

# region close
############################# CLEAN UP FUNCTION: CLOSE ALL TASKS ###################################


# Close all tasks
def cleanup(
    reader: nipcbatt.SpiReadCommunication,
    writer: nipcbatt.SpiWriteCommunication,
):
    """Closes out the created objects used in the communication""" 
    reader.close()
    writer.close()


####################################################################################################
# endregion close


# region test
############# USE THIS FUNCTION TO CALL THE WHOLE SEQUENCE #########################################
def spi_comm_test():
    """Execute all steps in the sequence"""  

    # Run setup function
    spi_reader, spi_writer = setup()

    # Run main function
    main(reader=spi_reader, writer=spi_writer, write_to_file=True)

    # run cleanup
    cleanup(spi_reader, spi_writer)


####################################################################################################
# endregion test  