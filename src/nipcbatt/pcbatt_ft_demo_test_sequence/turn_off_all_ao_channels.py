"""Turn Off all AO Channels"""

import nipcbatt

# pylint: disable=C0115,C0116,C0103


class TurnOffAllAOChannels:
    def __init__(self) -> None:
        self.dc_voltage_gen_task = None

        self.setup()
        self.main()
        self.cleanup()

    def setup(self) -> None:
        self.dc_voltage_generation_initialize_ao_channels()

    def dc_voltage_generation_initialize_ao_channels(self) -> None:
        self.dc_voltage_gen_task = nipcbatt.DcVoltageGeneration()
        self.dc_voltage_gen_task.initialize("Sim_PC_basedDAQ/ao0:3")

    def main(self) -> None:
        self.dc_voltage_generation_configure_initiate_and_sources_dc_voltage()

    def dc_voltage_generation_configure_initiate_and_sources_dc_voltage(self) -> None:
        voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=-10, range_max_volts=10
        )

        configuration = nipcbatt.DcVoltageGenerationConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            output_voltages=[0.0, 0.0, 0.0, 0.0],
        )

        self.dc_voltage_gen_task.configure_and_generate(configuration=configuration)

    def cleanup(self) -> None:
        self.dc_voltage_generation_close_ao_channels()

    def dc_voltage_generation_close_ao_channels(self) -> None:
        self.dc_voltage_gen_task.close()
