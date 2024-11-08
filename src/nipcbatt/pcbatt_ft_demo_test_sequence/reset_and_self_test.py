"""Reset and Self-Test"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (136 > 100 characters) (auto-generated noqa)

# pylint: disable=C0413,E0401,C0115,W0611,C0116,C0103

import os  # noqa: F401 - 'os' imported but unused (auto-generated noqa)
import sys
from time import sleep, time

import nidaqmx.constants  # noqa: F401 - 'nidaqmx.constants' imported but unused (auto-generated noqa)

import nipcbatt


class ResetAndSelfTest:  # noqa: D101 - Missing docstring in public class (auto-generated noqa)
    def __init__(self) -> None:  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self.digital_state_meas_task = None
        self.digital_state_gen_task = None

        self.start_time = None
        self.elasped_time = 0

        self.led = [False]

        self.setup()
        self.main()
        self.cleanup()

    def setup(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.initialize_reset_button()
        self.initialize_led_status()

    def initialize_reset_button(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.digital_state_gen_task = nipcbatt.StaticDigitalStateGeneration()
        self.digital_state_gen_task.initialize("TS_RESET0")

    def initialize_led_status(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.digital_state_meas_task = nipcbatt.StaticDigitalStateMeasurement()
        self.digital_state_meas_task.initialize("TP_ACT_LED0")

    def main(self) -> None:  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self.turn_on_dut_reset_button()
        self.wait_for_100_ms_seconds_in_reset_enabled_state()
        self.turn_off_dut_reset_button()
        self.get_start_time()
        while self.led[0] is False and self.elasped_time < 30:
            self.wait_led_activity()
            self.led_state_status()
            self.get_current_time()
        self.dut_elasped_time_validation_or_timeout()

    def turn_on_dut_reset_button(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        configuration = nipcbatt.StaticDigitalStateGenerationConfiguration(data_to_write=[True])

        self.digital_state_gen_task.configure_and_generate(configuration=configuration)

    def wait_for_100_ms_seconds_in_reset_enabled_state(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        sleep(0.1)

    def turn_off_dut_reset_button(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        configuration = nipcbatt.StaticDigitalStateGenerationConfiguration(data_to_write=[False])

        self.digital_state_gen_task.configure_and_generate(configuration=configuration)

    def get_start_time(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.start_time = time()

    def wait_led_activity(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        sleep(0.1)

    def led_state_status(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        result_data = self.digital_state_meas_task.configure_and_measure()
        self.led = result_data.digital_states

    def get_current_time(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.elasped_time = time() - self.start_time

    def dut_elasped_time_validation_or_timeout(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        if self.elasped_time >= 30:
            # Gather the name of the class and the method where the exception was raised
            exception_message = (
                "Sequence : "
                + self.__class__.__name__
                + ", Method : "
                + sys._getframe().f_code.co_name
                + "\n"
            )
            exception_message += "DUT wasn't able to start in 30 seconds"
            raise ValueError(exception_message)
        else:
            print("Status: Pass -- Elapsed time: ", self.elasped_time)

    def cleanup(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.close_led_status()
        self.close_reset_button()

    def close_led_status(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.digital_state_meas_task.close()

    def close_reset_button(  # noqa: D102 - Missing docstring in public method (auto-generated noqa)
        self,
    ) -> None:
        self.digital_state_gen_task.close()
