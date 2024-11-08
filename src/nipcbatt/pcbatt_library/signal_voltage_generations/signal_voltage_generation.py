"""Defines class used for generation of signal voltage on PCB points."""

import math

import nidaqmx.constants
import nidaqmx.stream_writers
import numpy as np

from nipcbatt.pcbatt_analysis.waveform_creation import (
    multitones_waveform,
    sine_waveform,
    square_waveform,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
)
from nipcbatt.pcbatt_library.signal_voltage_generations.signal_voltage_data_types import (
    SignalVoltageGenerationMultipleTonesConfiguration,
    SignalVoltageGenerationMultipleTonesWaveParameters,
    SignalVoltageGenerationSineWaveConfiguration,
    SignalVoltageGenerationSineWaveParameters,
    SignalVoltageGenerationSquareWaveConfiguration,
    SignalVoltageGenerationSquareWaveParameters,
    SignalVoltageGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.signal_voltage_generations.signal_voltage_generation_constants import (
    ConstantsForSignalVoltageGeneration,
)
from nipcbatt.pcbatt_library.synchronizations.synchronization_signal_routing import (
    SynchronizationSignalRouting,
)
from nipcbatt.pcbatt_utilities import numeric_utilities


class SignalVoltageGeneration(SynchronizationSignalRouting):
    """Provides a way that allows you to generate signal voltage and apply it into PCB points."""

    def initialize(self, channel_expression: str):
        """Initializes the analog output channels and obtains
        the Daqmx Task for signal voltage generation.

        Args:
            channel_expression (str):
                Expression representing the name of an analog output physical channel,
                or a global channel in DAQ System.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for analog output voltage.
        if self.contains_only_global_virtual_channels(channel_expression=channel_expression):
            self.add_global_channels(global_channel_expression=channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_generation_type(nidaqmx.constants.UsageTypeAO.VOLTAGE)
        else:
            # Add the channel_expression to analog output channel of the Daqmx task
            self.task.ao_channels.add_ao_voltage_chan(
                physical_channel=channel_expression,
                min_val=ConstantsForSignalVoltageGeneration.INITIAL_RANGE_MIN_VOLTS,
                max_val=ConstantsForSignalVoltageGeneration.INITIAL_RANGE_MAX_VOLTS,
                units=ConstantsForSignalVoltageGeneration.INITIAL_AO_VOLTAGE_UNITS,
            )

    def configure_all_channels(
        self,
        parameters: VoltageGenerationChannelParameters,
    ) -> None:
        """Configures all analog output channels for Signal Voltage generation.

        Args:
            parameters (VoltageGenerationChannelParameters):
            An instance of `VoltageGenerationChannelParameters` used
            to configure the analog output channels.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        for channel in self.task.ao_channels:
            channel.ao_min = parameters.range_min_volts
            channel.ao_max = parameters.range_max_volts
            # channel.ao_term_cfg = nidaqmx.constants.TerminalConfiguration.RSE

    def configure_timing(self, parameters: SignalVoltageGenerationTimingParameters):
        """Configures the timing characteristics used for Current measurements.

        Args:
            parameters (SampleClockTimingParameters): An instance of `SampleClockTimingParameters`
                used to configure the timing.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=self._get_generated_signal_samples_count(
                sampling_rate_hertz=parameters.sampling_rate_hertz,
                generated_signal_duration_seconds=parameters.generated_signal_duration_seconds,
            ),
            source=parameters.sample_clock_source,
        )

    def _get_generated_signal_samples_count(
        self, sampling_rate_hertz, generated_signal_duration_seconds
    ) -> int:
        """Calculates the number of samples that will be in the generated signal"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (194 > 100 characters) (auto-generated noqa)
        return math.ceil(sampling_rate_hertz * generated_signal_duration_seconds)

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for Current measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def generate_voltage_sine_waveform(
        self,
        signal_parameters: SignalVoltageGenerationSineWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
    ) -> None:
        """Generates a signal that is a sine wave according to `signal_parameters`.

        Args:
            signal_parameters (SignalVoltageGenerationSineWaveParameters):
                An instance of `SignalVoltageGenerationSineWaveParameters`
                used to configure the signal to generate.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` used
                to configure the sample rate and duration of the signal to be generated.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        waveform_samples_count = self._get_generated_signal_samples_count(
            sampling_rate_hertz=timing_parameters.sampling_rate_hertz,
            generated_signal_duration_seconds=timing_parameters.generated_signal_duration_seconds,
        )

        samples_to_write = sine_waveform.create_sine_waveform(
            amplitude=signal_parameters.generated_signal_tone_parameters.tone_amplitude_volts,
            frequency=signal_parameters.generated_signal_tone_parameters.tone_frequency_hertz,
            phase=signal_parameters.generated_signal_tone_parameters.tone_phase_radians,
            offset=signal_parameters.generated_signal_offset_volts,
            samples_count=waveform_samples_count,
            sampling_rate=timing_parameters.sampling_rate_hertz,
        )

        # build a numpy 2D array (number of row is the number of output channels)
        # from the numpy 1D array
        samples_to_write = np.tile(samples_to_write, (self.task.out_stream.num_chans, 1))

        writer = nidaqmx.stream_writers.AnalogMultiChannelWriter(
            self.task.out_stream, auto_start=True
        )
        writer.write_many_sample(samples_to_write)

    def generate_voltage_square_waveform(
        self,
        signal_parameters: SignalVoltageGenerationSquareWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
    ) -> None:
        """Creates a signal that is a square wave.

        Args:
            signal_parameters (SignalVoltageGenerationSquareWaveParameters):
                An instance of `SignalVoltageGenerationSquareWaveParameters`
                used to configure the signal to generate.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` used
                to configure the sample rate and duration of the signal to be generated.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        waveform_samples_count = self._get_generated_signal_samples_count(
            sampling_rate_hertz=timing_parameters.sampling_rate_hertz,
            generated_signal_duration_seconds=timing_parameters.generated_signal_duration_seconds,
        )

        samples_to_write = square_waveform.create_square_waveform(
            amplitude=signal_parameters.generated_signal_amplitude_volts,
            frequency=signal_parameters.generated_signal_frequency_hertz,
            duty_cycle=numeric_utilities.from_percent_to_decimal_ratio(
                percent=signal_parameters.generated_signal_duty_cycle_percent
            ),
            phase=signal_parameters.generated_signal_phase_radians,
            offset=signal_parameters.generated_signal_offset_volts,
            samples_count=waveform_samples_count,
            sampling_rate=timing_parameters.sampling_rate_hertz,
        )

        # build a numpy 2D array (number of row is the number of output channels)
        # from the numpy 1D array
        samples_to_write = np.tile(samples_to_write, (self.task.out_stream.num_chans, 1))

        writer = nidaqmx.stream_writers.AnalogMultiChannelWriter(
            self.task.out_stream, auto_start=True
        )
        writer.write_many_sample(data=samples_to_write)

    def generate_voltage_multi_tones_waveform(
        self,
        signal_parameters: SignalVoltageGenerationMultipleTonesWaveParameters,
        timing_parameters: SignalVoltageGenerationTimingParameters,
    ) -> None:
        """Generates a signal that contains sum of multiple sine waves at different tones
        (amplitudes and frequencies).

        Args:
            signal_parameters (SignalVoltageGenerationMultipleTonesWaveParameters):
                An instance of `SignalVoltageGenerationMultipleTonesWaveParameters`
                    used to configure the signal to generate.
            timing_parameters (SignalVoltageGenerationTimingParameters):
                An instance of `SignalVoltageGenerationTimingParameters` used
                to configure the sample rate and duration of the signal to be generated.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        waveform_samples_count = self._get_generated_signal_samples_count(
            sampling_rate_hertz=timing_parameters.sampling_rate_hertz,
            generated_signal_duration_seconds=timing_parameters.generated_signal_duration_seconds,
        )

        waveform_tones_input = list(
            map(
                lambda tone_parameters: multitones_waveform.WaveformTone(
                    frequency=tone_parameters.tone_frequency_hertz,
                    amplitude=tone_parameters.tone_amplitude_volts,
                    phase_radians=tone_parameters.tone_phase_radians,
                ),
                signal_parameters.multiple_tones_parameters,
            )
        )

        samples_to_write = multitones_waveform.create_multitones_waveform(
            multitones_amplitude=signal_parameters.generated_signal_amplitude_volts,
            waveform_tones=waveform_tones_input,
            samples_count=waveform_samples_count,
            sampling_rate=timing_parameters.sampling_rate_hertz,
        )

        # build a numpy 2D array (number of row is the number of output channels)
        # from the numpy 1D array
        samples_to_write = np.tile(samples_to_write, (self.task.out_stream.num_chans, 1))

        writer = nidaqmx.stream_writers.AnalogMultiChannelWriter(
            self.task.out_stream, auto_start=True
        )
        writer.write_many_sample(data=samples_to_write)

    def configure_and_generate_sine_waveform(
        self,
        configuration: SignalVoltageGenerationSineWaveConfiguration,
    ) -> None:
        """Configures and generates the Sine wave according to the specific configuration.

        Args:
            configuration (SignalVoltageGenerationSineWaveConfiguration):
                An instance of `SignalVoltageGenerationSineWaveConfiguration`
                used to configure the generation of single tone sine voltage signal at the channel.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        self.configure_all_channels(parameters=configuration.voltage_generation_range_parameters)

        self.configure_timing(
            parameters=SignalVoltageGenerationTimingParameters(
                sample_clock_source=configuration.timing_parameters.sample_clock_source,
                sampling_rate_hertz=configuration.timing_parameters.sampling_rate_hertz,
                generated_signal_duration_seconds=(
                    configuration.timing_parameters.generated_signal_duration_seconds
                ),
            )
        )
        self.configure_trigger(parameters=configuration.digital_start_trigger_parameters)

        self.generate_voltage_sine_waveform(
            signal_parameters=configuration.waveform_parameters,
            timing_parameters=configuration.timing_parameters,
        )

    def configure_and_generate_square_waveform(
        self,
        configuration: SignalVoltageGenerationSquareWaveConfiguration,
    ) -> None:
        """Configures and generates a Square wave voltage signal according
        to the specific configuration.

        Args:
            configuration (SignalVoltageGenerationSquareWaveConfiguration):
                An instance of `SignalVoltageGenerationSquareWaveConfiguration`
                used to configure the generation of square wave voltage signal at the channel.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        self.configure_all_channels(parameters=configuration.voltage_generation_range_parameters)

        self.configure_timing(
            parameters=SignalVoltageGenerationTimingParameters(
                sample_clock_source=configuration.timing_parameters.sample_clock_source,
                sampling_rate_hertz=configuration.timing_parameters.sampling_rate_hertz,
                generated_signal_duration_seconds=(
                    configuration.timing_parameters.generated_signal_duration_seconds
                ),
            )
        )
        self.configure_trigger(parameters=configuration.digital_start_trigger_parameters)

        self.generate_voltage_square_waveform(
            signal_parameters=configuration.waveform_parameters,
            timing_parameters=configuration.timing_parameters,
        )

    def configure_and_generate_multiple_tones_waveform(
        self,
        configuration: SignalVoltageGenerationMultipleTonesConfiguration,
    ) -> None:
        """Configures and generates a multi-tone sine wave voltage signal according
        to the specific configuration.

        Args:
            configuration (SignalVoltageGenerationMultipleTonesConfiguration):
                An instance of `SignalVoltageGenerationMultipleTonesConfiguration`
                used to configure the generation of multi-tones voltage waveform at the channel.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        self.configure_all_channels(parameters=configuration.voltage_generation_range_parameters)

        self.configure_timing(
            parameters=SignalVoltageGenerationTimingParameters(
                sample_clock_source=configuration.timing_parameters.sample_clock_source,
                sampling_rate_hertz=configuration.timing_parameters.sampling_rate_hertz,
                generated_signal_duration_seconds=(
                    configuration.timing_parameters.generated_signal_duration_seconds
                ),
            )
        )
        self.configure_trigger(parameters=configuration.digital_start_trigger_parameters)

        self.generate_voltage_multi_tones_waveform(
            signal_parameters=configuration.waveform_parameters,
            timing_parameters=configuration.timing_parameters,
        )

    def close(self):
        """Closes generation procedure and releases internal resources."""
        if not self.is_task_initialized:
            return
        # Wait until done
        self.task.wait_until_done()
        super().close()
        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()
