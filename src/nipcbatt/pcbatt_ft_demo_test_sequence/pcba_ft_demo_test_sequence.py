"""
PCBA FT Demo Test Sequences demonstrates testing of PCBA DUTs using PCIe DAQ and TestScale Hardware. 
These example sequences can be executed in hardware simulation using the Python pcbatt 
measurement libraries and can be built off of for a custom sequencer.

Limits suggested will return a FAIL test with DAQ simulation and they need to be changed 
to match your physical hardware.
"""  

from animation_and_sound_user_input_test import AnimationAndSoundUserInputTest
from audio_filter_test import AudioFilterTest
from limit_exception import LimitException
from power_diagnostics import PowerDiagnostics
from reset_and_self_test import ResetAndSelfTest
from turn_off_all_ao_channels import TurnOffAllAOChannels


class MainSequence:
    """Sequence for testing different systems"""  

    def __init__(self) -> None:  
        self.main()
        self.cleanup()

    def main(self) -> None:
        """Main method"""  
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
        """turn everything off"""  
        t = TurnOffAllAOChannels()
        t.cleanup()


MainSequence()
