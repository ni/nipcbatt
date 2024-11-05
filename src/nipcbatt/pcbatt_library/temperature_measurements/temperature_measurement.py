"""Defines class with common methods used for temperature measurements on PCB points."""

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementData,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_constants import (
    ConstantsForTemperatureMeasurement,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_data_types import (
    TemperatureMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class TemperatureMeasurement(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to perform Temperature measurements on PCB points."""

    def close(self):
        """Closes measurement procedure and releases internal resources."""
        if not self.is_task_initialized:
            return

        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()

    def configure_timing(self, parameters: SampleClockTimingParameters):
        """Configures the timing characteristics used for temperature measurements.

        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        self.task.timing.cfg_samp_clk_timing(
            rate=parameters.sampling_rate_hertz,
            sample_mode=nidaqmx.constants.AcquisitionType.FINITE,
            samps_per_chan=parameters.number_of_samples_per_channel,
            source=parameters.sample_clock_source,
        )

        # if the current timing engine setting is Auto
        # then delete the previous timing engine property
        # and let the task revert to the default setting of DAQmx
        # to automatically set the value of the timing engine
        if parameters.sample_timing_engine == SampleTimingEngine.AUTO:
            # Sample timing engine is auto selected
            ...
        else:
            self.task.timing.samp_timing_engine = parameters.sample_timing_engine.value

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for temperature measurements.

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

    def acquire_data_for_measurement_analysis(self) -> MeasurementData:
        """Acquires Data from DAQ channel for measurement of temperature.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

        # Builds the shape of numpy array (number of channels, number of samples per channel)
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan

        # Build the numpy array.
        data_to_read = numpy.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=numpy.float64,
        )

        # Reads data and fill numpy array.
        reader = nidaqmx.stream_readers.AnalogMultiChannelReader(self.task.in_stream)
        reader.read_many_sample(
            data=data_to_read,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        return MeasurementData(data_to_read)

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
    ) -> TemperatureMeasurementResultData:
        """Proceeds to the analysis of temperatures from the measurement.

        Args:
            measurement_data (MeasurementData): An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.

        Returns:
            TemperatureMeasurementResultData:
            An instance of `TemperatureMeasurementResultData`
            that specifies the measurement results.
        """
        # Check if sampling rate is 0 and raise error to avoid divide by 0 error.
        Guard.is_greater_than_zero(
            self.task.timing.samp_clk_rate, nameof(self.task.timing.samp_clk_rate)
        )
        delta_time_seconds = invert_value(self.task.timing.samp_clk_rate)

        # Initialization for TemperatureMeasurementResultData instance creation.
        waveform = []
        avg_temps_celsius_degrees = []
        avg_temps_kelvin = []
        acq_duration_seconds = 0.0

        for samples_per_channel, channel_name in zip(
            measurement_data.samples_per_channel,
            self.task.in_stream.channels_to_read.channel_names,
        ):
            # samples_per_channel contains samples captured
            # from the channel which name is channel_name.
            # Assures that the samples array is not empty and contain only float values.

            Guard.all_elements_are_of_same_type(samples_per_channel, float)
            Guard.is_not_empty(samples_per_channel, nameof(samples_per_channel))

            acq_duration_seconds = delta_time_seconds * len(samples_per_channel)

            # Creates an instance of AnalogWaveform and add it to waveforms.
            waveform.append(
                AnalogWaveform(
                    channel_name=channel_name,
                    delta_time_seconds=delta_time_seconds,
                    samples=samples_per_channel,
                )
            )

            mean_temperature_celsius_degrees = numpy.mean(samples_per_channel)
            avg_temps_celsius_degrees.append(mean_temperature_celsius_degrees)
            avg_temps_kelvin.append(
                mean_temperature_celsius_degrees
                - ConstantsForTemperatureMeasurement.ABSOLUTE_ZERO_CELSIUS_DEGREES
            )

        return TemperatureMeasurementResultData(
            waveforms=waveform,
            acquisition_duration_seconds=acq_duration_seconds,
            average_temperatures_celsius_degrees=avg_temps_celsius_degrees,
            average_temperatures_kelvin=avg_temps_kelvin,
        )
