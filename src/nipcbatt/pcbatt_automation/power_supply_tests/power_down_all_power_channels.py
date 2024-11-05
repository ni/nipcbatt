"""This example resets and closes configured Power channels"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

import nipcbatt

# Note to run with hardware: update virtual/physical channels info based
# on NI MAX in the below Initialize Steps

# Local constant for channel name
POWER_CHANNEL = "Simulated_power/power"

# Default configuration for Power channel
CONFIGURATION = nipcbatt.DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION


def power_down_all_power_channels(
    channel_name=POWER_CHANNEL,
    config: nipcbatt.PowerSupplySourceAndMeasureConfiguration = CONFIGURATION,
):
    """Configure power channel with default parameters and close"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (255 > 100 characters) (auto-generated noqa)

    # Initialize Power Channels
    generation = nipcbatt.PowerSupplySourceAndMeasure()
    generation.initialize(power_channel_name=channel_name)

    # Use the configure_and_measure method for power channel with default configuration
    generation.configure_and_measure(configuration=config)

    # Close the 'PowerSupplySourceAndMeasure' Task for power channel
    generation.close()
