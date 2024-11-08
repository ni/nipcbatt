"""This example resets all configured Analog output channels to 0 volts"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (185 > 100 characters) (auto-generated noqa)

import nipcbatt

# Note to run with hardware: update virtual/physical channels info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
ANALOG_OUT_CHANNELS = "Sim_PC_basedDAQ/ao0:3"

# Assign the Range Parameters for all configured AO Channels
RANGE_PARAMETERS = nipcbatt.DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS


def power_down_all_ao_channels(
    channel_names=ANALOG_OUT_CHANNELS,
    parameters=RANGE_PARAMETERS,
):
    """Turn off configured AO channels by configuring to 0V"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (250 > 100 characters) (auto-generated noqa)

    # declare constant to hold output voltage of 0V
    off_voltages = [0.0, 0.0, 0.0, 0.0]

    # DC Voltage Generation - Initialize AO Channels
    generation = nipcbatt.DcVoltageGeneration()
    generation.initialize(analog_output_channel_expression=channel_names)

    # Create configuration for analog output
    output_configuration = nipcbatt.DcVoltageGenerationConfiguration(
        voltage_generation_range_parameters=parameters, output_voltages=off_voltages
    )

    # Sources DC Voltage at 0V to Analog Output channels
    generation.configure_and_generate(configuration=output_configuration)

    # Close the DC Voltage Generation Task for Analog output module
    generation.close()
