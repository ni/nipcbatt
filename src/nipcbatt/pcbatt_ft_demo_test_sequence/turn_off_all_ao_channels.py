"""Turn Off all AO Channels"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (141 > 100 characters) (auto-generated noqa)

import nipcbatt

# pylint: disable=C0115,C0116,C0103


class TurnOffAllAOChannels:  # noqa: D101 - Missing docstring in public class (auto-generated noqa)
    def __init__(self) -> None:  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self.dc_voltage_gen_task = None

        self.setup()
        self.main()
        self.cleanup()

    def setup(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.dc_voltage_generation_initialize_ao_channels()

    def dc_voltage_generation_initialize_ao_channels(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.dc_voltage_gen_task = nipcbatt.DcVoltageGeneration()
        self.dc_voltage_gen_task.initialize("Sim_PC_basedDAQ/ao0:3")

    def main(self) -> None:  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self.dc_voltage_generation_configure_initiate_and_sources_dc_voltage()

    def dc_voltage_generation_configure_initiate_and_sources_dc_voltage(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=-10, range_max_volts=10
        )

        configuration = nipcbatt.DcVoltageGenerationConfiguration(
            voltage_generation_range_parameters=voltage_generation_range_parameters,
            output_voltages=[0.0, 0.0, 0.0, 0.0],
        )

        self.dc_voltage_gen_task.configure_and_generate(configuration=configuration)

    def cleanup(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.dc_voltage_generation_close_ao_channels()

    def dc_voltage_generation_close_ao_channels(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.dc_voltage_gen_task.close()
