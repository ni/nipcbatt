"""This module provides test of integration of SignalVoltageGeneration."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_interpreters import (
    _MockInterpreter,
)
from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_utilities import (
    _replace_daqmx,
)


class TestIntegrationSignalVoltageGeneration(unittest.TestCase):
    """Defines a test fixture that checks the integration of
    `SignalVoltageGeneration` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)
        _replace_daqmx(_MockInterpreter)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_signal_voltage_generation_generate_only(self):
        """Checks if class `SignalVoltageGeneration' can generate
        with just the initial configurations"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (417 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.generate_voltage_sine_waveform(
            signal_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
            timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.generate_voltage_square_waveform(
            signal_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS,
            timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.generate_voltage_multi_tones_waveform(
            signal_parameters=nipcbatt.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
            timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.close()

    def test_signal_voltage_generation_configure_and_generate_in_loop(self):
        """Checks if class `SignalVoltageGeneration' can configure and generate
        when they are called one after the other."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (345 > 100 characters) (auto-generated noqa)
        generation_channel_parameters_1 = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=-5.0,
            range_max_volts=5.0,
        )
        sine_wave_parameters_1 = nipcbatt.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=0.01,
            generated_signal_tone_parameters=nipcbatt.ToneParameters(
                tone_frequency_hertz=100,
                tone_amplitude_volts=1.0,
                tone_phase_radians=0,
            ),
        )

        generation_channel_parameters_2 = nipcbatt.VoltageGenerationChannelParameters(
            range_min_volts=-8.0,
            range_max_volts=8.0,
        )
        sine_wave_parameters_2 = nipcbatt.SignalVoltageGenerationSineWaveParameters(
            generated_signal_offset_volts=0.02,
            generated_signal_tone_parameters=nipcbatt.ToneParameters(
                tone_frequency_hertz=1000,
                tone_amplitude_volts=2.0,
                tone_phase_radians=0.3,
            ),
        )

        test_parameter_list = []
        test_parameter_list.append((generation_channel_parameters_1, sine_wave_parameters_1))
        test_parameter_list.append((generation_channel_parameters_2, sine_wave_parameters_2))

        generation = nipcbatt.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )

        for generation_parameters, sine_wave_parameters in test_parameter_list:
            generation.configure_all_channels(parameters=generation_parameters)
            generation.configure_timing(
                parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS
            )
            generation.generate_voltage_sine_waveform(
                signal_parameters=sine_wave_parameters,
                timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
            )
        generation.close()

    def test_signal_voltage_generation_for_configure_and_generate_sine_wave(self):
        """Checks if class `SignalVoltageGeneration' can configure and generate sine wave."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (179 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_and_generate_sine_waveform(
            configuration=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION
        )
        generation.close()

    def test_signal_voltage_generation_for_configure_and_generate_square_wave(self):
        """Checks if class `SignalVoltageGeneration' can configure and generate square wave."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (181 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_and_generate_square_waveform(
            configuration=nipcbatt.DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION
        )
        generation.close()

    def test_signal_voltage_generation_for_configure_and_generate_multiple_tones_sine_signal(
        self,
    ):
        """Checks if class `SignalVoltageGeneration' can configure and generate
        multiple tones signal."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (403 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_and_generate_multiple_tones_waveform(
            configuration=nipcbatt.DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION
        )
        generation.close()

    def test_signal_voltage_generation_route_sample_clock_signal_to_terminal(self):
        """Checks if class `SignalVoltageGeneration' can configure and export the
        sample clock signal to the specified terminal"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (349 > 100 characters) (auto-generated noqa)
        generation = nipcbatt.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_all_channels(
            parameters=nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
        )
        generation.configure_timing(
            parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS
        )
        generation.configure_trigger(parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS)
        generation.route_sample_clock_signal_to_terminal(
            terminal_name="/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
        )
        generation.generate_voltage_multi_tones_waveform(
            signal_parameters=nipcbatt.DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
            timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.close()

    def test_signal_voltage_generation_route_digital_trigger_signal_to_terminal(self):
        """Checks if class `SignalVoltageGeneration' can configure and export the
        digital trigger signal to the specified terminal"""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (429 > 100 characters) (auto-generated noqa)

        generation = nipcbatt.SignalVoltageGeneration()
        generation.initialize(
            channel_expression="NI_PCBA_Measurement_Simulated_TestScale_TS1Mod3/ao0:1"
        )
        generation.configure_all_channels(
            parameters=nipcbatt.DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS
        )
        generation.configure_timing(
            parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS
        )
        generation.route_start_trigger_signal_to_terminal(
            terminal_name="/NI_PCBA_Measurement_Simulated_TestScale_TS1Mod1/PFI0"
        )
        generation.configure_trigger(parameters=nipcbatt.DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS)
        generation.generate_voltage_square_waveform(
            signal_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS,
            timing_parameters=nipcbatt.DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
        )
        generation.close()


if __name__ == "__main__":
    unittest.main()
