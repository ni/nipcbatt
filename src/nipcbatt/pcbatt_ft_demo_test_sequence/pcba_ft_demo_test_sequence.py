"""
PCBA FT Demo Test Sequences demonstrates testing of PCBA DUTs using PCIe DAQ and TestScale Hardware. 
These example sequences can be executed in hardware simulation using the Python pcbatt 
measurement libraries and can be built off of for a custom sequencer.

Limits suggested will return a FAIL test with DAQ simulation and they need to be changed 
to match your physical hardware.
"""  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (101 > 100 characters) (auto-generated noqa)

from animation_and_sound_user_input_test import AnimationAndSoundUserInputTest
from audio_filter_test import AudioFilterTest
from limit_exception import LimitException
from power_diagnostics import PowerDiagnostics
from reset_and_self_test import ResetAndSelfTest
from turn_off_all_ao_channels import TurnOffAllAOChannels


class MainSequence:
    """Sequence for testing different systems"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (159 > 100 characters) (auto-generated noqa)

    def __init__(self) -> None:  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self.main()
        self.cleanup()

    def main(self) -> None:
        """Main method"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (136 > 100 characters) (auto-generated noqa)
        try:
            print("\n\n------Power Diagnostics------\n")
            PowerDiagnostics()
            print("\n\n------Reset and Self Test------\n\n")
            ResetAndSelfTest()
            print("\n\n------Animation and Sound User Input Test------\n")
            AnimationAndSoundUserInputTest()
            print("\n\n------Audio Filter Test------\n")
            AudioFilterTest()
        except LimitException as e:
            print(e.caller)
            print(e.message)
        except ValueError as e:
            print(e)

    def cleanup(self) -> None:
        """turn everything off"""  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (233 > 100 characters) (auto-generated noqa)
        t = TurnOffAllAOChannels()
        t.cleanup()


MainSequence()
