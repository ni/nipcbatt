"""This example resets all configured Digital output channels voltage to 0 Volts"""  

import nipcbatt

# Note to run with Hardware: Update Virtual/Physical Channels Info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
DIGITAL_OUT_CHANNELS = "Sim_PC_basedDAQ/port0/line0:7"


def power_down_all_do_channels():
    """Set digital state to LOW on all digital output channels"""  
    
    # declare list to hold boolean false values
    low_values = [False, False, False, False, False, False, False, False]

    # Static Digital State Generation -- Initialize DO channels
    generation = nipcbatt.StaticDigitalStateGeneration()
    generation.initialize(channel_expression=DIGITAL_OUT_CHANNELS)

    # create configuration for output
    output_config = nipcbatt.StaticDigitalStateGenerationConfiguration(data_to_write=low_values)

    # set digital state LOW for all Digital Output channels
    generation.configure_and_generate(configuration=output_config)

    # closes the Static Digital State Generation Task for Digital output module
    generation.close()
