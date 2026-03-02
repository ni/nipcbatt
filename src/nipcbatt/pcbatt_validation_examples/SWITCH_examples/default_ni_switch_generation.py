""" NI-SWITCH generation with default input parameters """

from nipcbatt import switch
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

def main():
    """Configures and executes default NI SWITCH generation with logging."""

    generation = switch.StaticDigitalPathGeneration()

    logger = PcbattLogger(file="c:\\Temp\\switch_logger.txt")
    logger.attach(generation)

    # declare all parameters necessary for path generaton
    resource_name = "Sim_MUX"
    topology = "2527/2-Wire Dual 16x1 Mux"
    p1, p2 = "ch0", "com0"
    max_wait_debounce = 100
    connect = True
    simulate = False #Change to True to simulate

    # instantiate parameters and settings objects
    channel_params = switch.StaticDigitalPathGenerationChannelParameters(p1, p2)
    state = switch.StaticDigitalPathGenerationStateParameters(connect)
    ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
    timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
    configuration = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)
    

    # ======================= Initialize the Switch ============================ #
    generation.initialize(resource_name, topology, connect, simulate)

    # =============== Configure and generate nominal configuration ============= #
    generation.configure_and_generate(configuration)

    # ======================== Close the DMM Session =========================== #
    generation.close()

    print('SUCCESS: Connected ' + p1 + ' to ' + p2)

if __name__ == "__main__":
    main()
