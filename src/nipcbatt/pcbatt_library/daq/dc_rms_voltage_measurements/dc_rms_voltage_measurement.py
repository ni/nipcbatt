# pylint: disable=W0613, C0301
# remove it when arguments of initialize are used.
""" Defines class used for DC-RMS Voltage measurement on PCB points."""

from typing import Union

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import LabViewBasicDcRms
from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementData,
    MeasurementExecutionType,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.common.voltage_constants import (
    ConstantsForVoltageMeasurement,
)
from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_constants import (
    ConstantsForDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
    DcRmsVoltageMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class DcRmsVoltageMeasurement(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to perform DC-RMS voltage measurements on PCB points."""

    def initialize(self, analog_input_channel_expression: str):
        """Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)
        if self.is_task_initialized:
            return

        # If the input channel_expression contains global channel, then add them as global channels
        # and verify if the global channels are configured for current measurement.
        if self.contains_only_global_virtual_channels(
            channel_expression=analog_input_channel_expression
        ):
            self.add_global_channels(global_channel_expression=analog_input_channel_expression)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.VOLTAGE)
        else:
            # Add the channel_expression to analog input current channel of the Daqmx task
            self.task.ai_channels.add_ai_voltage_chan(
                physical_channel=analog_input_channel_expression,
                name_to_assign_to_channel="",
                terminal_config=ConstantsForVoltageMeasurement.INITIAL_AI_TERMINAL_CONFIGURATION,
                min_val=ConstantsForVoltageMeasurement.INITIAL_VOLTAGE_MINIMUM_VALUE_VOLTS,
                max_val=ConstantsForVoltageMeasurement.INITIAL_VOLTAGE_MAXIMUM_VALUE_VOLTS,
                units=ConstantsForVoltageMeasurement.INITIAL_AI_VOLTAGE_UNITS,
            )

    def close(self):
        """Closes measurement procedure and releases internal resources."""  # noqa: D202, W505 - No blank lines allowed after function docstring (auto-generated noqa), doc line too long (161 > 100 characters) (auto-generated noqa)

        if not self.is_task_initialized:
            return

        self.task.stop()
        self.task.close()

    def configure_and_measure(
        self, configuration: DcRmsVoltageMeasurementConfiguration
    ) -> Union[None, DcRmsVoltageMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
            configuration (DcRmsVoltageMeasurementConfiguration):
            A instance of `DcRmsVoltageMeasurementConfiguration` used to configure the measurement.

        Returns:
            DcRmsVoltageMeasurementResultData | None: An instance of `DcRmsVoltageMeasurementResultData`
              or `None` if no measure was performed.
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.task.stop()
            self.configure_all_channels(configuration.global_channel_parameters)
            for specific_channel_parameters in configuration.specific_channels_parameters:
                self.configure_specific_channel(specific_channel_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)
            self.task.start()

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(
                data, configuration.measurement_options.measurement_analysis_requirement
            )
        return None

    def configure_all_channels(self, parameters: VoltageRangeAndTerminalParameters):
        """Configures all channels used for voltage measurements.

        Args:
            parameters (VoltageRangeAndTerminalParameters):
            An instance of `VoltageRangeAndTerminalParameters` used to configure the channels.
        """  # noqa: D417 - Missing argument descriptions in the docstring (auto-generated noqa)
        for channel in self.task.ai_channels:
            channel.ai_term_cfg = parameters.terminal_configuration
            channel.ai_min = parameters.range_min_volts
            channel.ai_max = parameters.range_max_volts

    def configure_specific_channel(
        self, parameters: VoltageMeasurementChannelAndTerminalRangeParameters
    ):
        """Configures the specific channels used for voltage measurements.

        Args:
            parameters (VoltageMeasurementChannelAndTerminalRangeParameters):
            An instance of `VoltageMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.

        If the user provides Global Virtual Channel name in Initialize(),
        then he/she has to provide the Virtual channel name in Specific channel parameters as well.

        Similarly, if the user provides Physical channel name in Initialize(),
        then he/she has to provide the Physical channel name in Specific channel parameters.
        """  # noqa: D202, D417, W505 - No blank lines allowed after function docstring (auto-generated noqa), Missing argument descriptions in the docstring (auto-generated noqa), doc line too long (173 > 100 characters) (auto-generated noqa)

        if parameters.channel_name in (channel.name for channel in self.task.ai_channels):
            # if the specified channel is present in ai_channel_collection,
            # updates the voltage parameters of the channel
            self.task.ai_channels[
                parameters.channel_name
            ].ai_term_cfg = parameters.channel_parameters.terminal_configuration
            self.task.ai_channels[
                parameters.channel_name
            ].ai_min = parameters.channel_parameters.range_min_volts
            self.task.ai_channels[
                parameters.channel_name
            ].ai_max = parameters.channel_parameters.range_max_volts
        else:
            # otherwise, adds the channel.
            if self.contains_only_global_virtual_channels(
                channel_expression=parameters.channel_name
            ):
                # Global virtual channel
                self.add_global_channels(global_channel_expression=parameters.channel_name)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.VOLTAGE)
                for channel in self.task.ai_channels:
                    channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
                    channel.ai_min = parameters.channel_parameters.range_min_volts
                    channel.ai_max = parameters.channel_parameters.range_max_volts
            else:
                # Physical channel
                self.task.ai_channels.add_ai_voltage_chan(
                    physical_channel=parameters.channel_name,
                    terminal_config=parameters.channel_parameters.terminal_configuration,
                    min_val=parameters.channel_parameters.range_min_volts,
                    max_val=parameters.channel_parameters.range_max_volts,
                    units=ConstantsForVoltageMeasurement.INITIAL_AI_VOLTAGE_UNITS,
                )

    def configure_timing(self, parameters: SampleClockTimingParameters):
        """Configures the timing characteristics used for voltage measurements.

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
        """Configure the characteristics of triggers used for voltage measurements.

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
        """Acquires Data from DAQ channel for measurement of voltage.

        Returns:
            MeasurementData: An instance of `MeasurementData`
            that specifies the data acquired from DAQ channels.
        """
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan
        data_to_read = numpy.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=numpy.float64,
        )
        reader = nidaqmx.stream_readers.AnalogMultiChannelReader(self.task.in_stream)
        reader.read_many_sample(
            data=data_to_read,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        return MeasurementData(data_to_read)

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> DcRmsVoltageMeasurementResultData:
        """Proceeds to the analysis of DC Voltages from the measurement.

        Args:
             data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            DcRmsVoltageMeasurementResultData:
            An instance of `DcRmsVoltageMeasurementResultData`
            that specifies the measurement results.
        """
        # Check if sampling rate is 0 and raise error to avoid divide by 0 error.
        Guard.is_greater_than_zero(
            self.task.timing.samp_clk_rate, nameof(self.task.timing.samp_clk_rate)
        )
        delta_time_seconds = invert_value(self.task.timing.samp_clk_rate)

        # Initialization for DcRmsVoltageMeasurementResultData instance creation.
        voltage_waveforms = []
        acquisition_duration_seconds = 0.0
        dc_values_volts = []
        rms_values_volts = []

        for samples_per_channel, channel_name in zip(
            measurement_data.samples_per_channel,
            self.task.in_stream.channels_to_read.channel_names,
        ):
            # Creates an instance of AnalogWaveform and add it to waveforms.
            voltage_waveforms.append(
                AnalogWaveform(
                    channel_name=channel_name,
                    delta_time_seconds=delta_time_seconds,
                    samples=samples_per_channel,
                )
            )
            if (
                measurement_analysis_requirement
                == MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
            ):
                acquisition_duration_seconds += delta_time_seconds * len(samples_per_channel)
                # DC and RMS processing.
                dc_rms_processing_result = LabViewBasicDcRms.process_single_waveform_dc_rms(
                    waveform_samples=samples_per_channel,
                    waveform_sampling_period_seconds=delta_time_seconds,
                    dc_rms_processing_window=ConstantsForDcRmsVoltageMeasurement.DEFAULT_DC_RMS_PROCESSING_WINDOW,
                )

                dc_values_volts.append(dc_rms_processing_result.dc_value)
                rms_values_volts.append(dc_rms_processing_result.rms_value)

        return DcRmsVoltageMeasurementResultData(
            waveforms=voltage_waveforms,
            acquisition_duration_seconds=acquisition_duration_seconds,
            dc_values_volts=dc_values_volts,
            rms_values_volts=rms_values_volts,
        )
