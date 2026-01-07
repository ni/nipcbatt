# flake8: noqa
# noqa: E501
""" Defines class used for DC-RMS Current measurement on PCB points."""

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
from nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_constants import (
    ConstantsForDcRmsCurrentMeasurement,
)
from nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_data_types import (
    DcRmsCurrentMeasurementChannelAndTerminalRangeParameters,
    DcRmsCurrentMeasurementConfiguration,
    DcRmsCurrentMeasurementResultData,
    DcRmsCurrentMeasurementTerminalRangeParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class DcRmsCurrentMeasurement(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to perform DC and RMS current measurements on PCB points."""

    using_specific_channel = False

    def initialize(self, analog_input_channel_expression: str, use_specific_channel: bool = False):
        """Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """
        if self.is_task_initialized:
            return

        self.using_specific_channel = use_specific_channel
        # If using_specific_channel is True skip the initialization.
        # This is required as Current channels do not allow overwriting of min and max range values
        # To overcome this, channels will be initialized in configure_specific_channel()
        if self.using_specific_channel is True:
            pass
        # Else initialize channels with default values
        else:
            # If the input channel_expression contains global channel, then add them as global channels
            # and verify if the global channels are configured for current measurement.
            if self.contains_only_global_virtual_channels(
                channel_expression=analog_input_channel_expression
            ):
                self.add_global_channels(global_channel_expression=analog_input_channel_expression)
                self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
                self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.CURRENT)
            else:
                # Add the channel_expression to analog input current channel of the Daqmx task
                self.task.ai_channels.add_ai_current_chan(
                    physical_channel=analog_input_channel_expression,
                    name_to_assign_to_channel="",
                    terminal_config=ConstantsForDcRmsCurrentMeasurement.INITIAL_AI_TERMINAL_CONFIGURATION,
                    min_val=ConstantsForDcRmsCurrentMeasurement.INITIAL_CURRENT_RANGE_MINIMUM_AMPERES,
                    max_val=ConstantsForDcRmsCurrentMeasurement.INITIAL_CURRENT_RANGE_MAXIMUM_AMPERES,
                    units=ConstantsForDcRmsCurrentMeasurement.INITIAL_AI_CURRENT_UNITS,
                    shunt_resistor_loc=ConstantsForDcRmsCurrentMeasurement.INITIAL_SHUNT_RESISTOR_LOCATION,
                    ext_shunt_resistor_val=ConstantsForDcRmsCurrentMeasurement.INITIAL_EXTERNAL_SHUNT_RESISTOR_VALUE_OHMS,
                )

    def close(self):
        """Closes measurement procedure and releases internal resources."""

        if not self.is_task_initialized:
            return

        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(
        self, configuration: DcRmsCurrentMeasurementConfiguration
    ) -> Union[None, DcRmsCurrentMeasurementResultData]:
        """Configures and/or performs a measurement
           according to specific configuration parameters.

        Args:
        configuration (DcRmsCurrentMeasurementConfiguration): An instance of
            `DcRmsCurrentMeasurementConfiguration` used to configure the measurement.

        Returns:
            DcRmsCurrentMeasurementResultData | None:
              An instance of `DcRmsCurrentMeasurementResultData`
              or `None` if no measure was performed.
        """

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            if self.using_specific_channel is True:
                for specific_channel_parameters in configuration.specific_channels_parameters:
                    self.configure_specific_channel(specific_channel_parameters)
            else:
                self.configure_all_channels(configuration.global_channel_parameters)

            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            self.task.start()
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(
                data, configuration.measurement_options.measurement_analysis_requirement
            )

        self.task.start()
        return None

    def configure_all_channels(
        self, parameters: DcRmsCurrentMeasurementTerminalRangeParameters
    ) -> None:
        """Configures all channels for DC-RMS Current measurement.

        Args:
            parameters (DcRmsCurrentMeasurementTerminalRangeParameters):
                An instance of `DcRmsCurrentMeasurementTerminalRangeParameters`
                used to configure the channels.
        """
        for channel in self.task.ai_channels:
            channel.ai_min = parameters.range_min_amperes
            channel.ai_max = parameters.range_max_amperes
            channel.ai_term_cfg = parameters.terminal_configuration
            channel.ai_current_shunt_resistance = parameters.shunt_resistor_ohms

    def configure_specific_channel(
        self, parameters: DcRmsCurrentMeasurementChannelAndTerminalRangeParameters
    ) -> None:
        """Configures the range and terminal configurations
           for specific channels used for DC-RMS current measurement.

        Args:
            parameters (DcRmsCurrentMeasurementChannelAndTerminalRangeParameters):
                An instance of `DcRmsCurrentMeasurementChannelAndTerminalRangeParameters`
            used to configure the channels.
        """
        if self.contains_only_global_virtual_channels(channel_expression=parameters.channel_name):
            # Global virtual channel
            self.add_global_channels(global_channel_expression=parameters.channel_name)
            self.task.control(action=nidaqmx.constants.TaskMode.TASK_VERIFY)
            self.verify_measurement_type(nidaqmx.constants.UsageTypeAI.CURRENT)

            channel = self.task.ai_channels[parameters.channel_name]
            channel.ai_min = parameters.channel_parameters.range_min_amperes
            channel.ai_max = parameters.channel_parameters.range_max_amperes
            channel.ai_term_cfg = parameters.channel_parameters.terminal_configuration
            channel.ai_current_shunt_resistance = parameters.channel_parameters.shunt_resistor_ohms

        else:
            # Physical channel
            self.task.ai_channels.add_ai_current_chan(
                physical_channel=parameters.channel_name,
                terminal_config=parameters.channel_parameters.terminal_configuration,
                min_val=parameters.channel_parameters.range_min_amperes,
                max_val=parameters.channel_parameters.range_max_amperes,
                units=ConstantsForDcRmsCurrentMeasurement.INITIAL_AI_CURRENT_UNITS,
                shunt_resistor_loc=ConstantsForDcRmsCurrentMeasurement.INITIAL_SHUNT_RESISTOR_LOCATION,
                ext_shunt_resistor_val=parameters.channel_parameters.shunt_resistor_ohms,
            )

    def configure_timing(self, parameters: SampleClockTimingParameters):
        """Configures the timing characteristics used for Current measurements.
        Args:
            parameters (SampleClockTimingParameters):
            An instance of `SampleClockTimingParameters`
            used to configure the timing.
        """
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
        """Configure the characteristics of triggers used for Current measurements.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        """
        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def acquire_data_for_measurement_analysis(self) -> MeasurementData:
        """Acquires Data from DAQ channel for measurement of Current.

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
    ) -> DcRmsCurrentMeasurementResultData:
        """Proceeds to the analysis of DC and RMS current from the measurement data.

        Args:
            data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            DcRmsCurrentMeasurementResultData:
            An instance of `DcRmsCurrentMeasurementResultData`
            that specifies the measurement results.
        """
        # Check if sampling rate is 0 and raise error to avoid divide by 0 error.
        Guard.is_greater_than_zero(
            self.task.timing.samp_clk_rate, nameof(self.task.timing.samp_clk_rate)
        )

        delta_time_seconds = invert_value(self.task.timing.samp_clk_rate)
        acquisition_duration = (
            self.task.timing.samp_quant_samp_per_chan / self.task.timing.samp_clk_rate
        )

        # Initialization for DcRmsCurrentMeasurementResultData instance creation.
        current_waveforms = []
        calculated_dc_values = []
        calculated_rms_values = []

        # Get the Analog Waveform and calculate the DC and RMS current measurements
        # for every channel in the task.
        for samples_per_channel, channel_name_read in zip(
            measurement_data.samples_per_channel,
            self.task.in_stream.channels_to_read.channel_names,
        ):
            # Creates an instance of AnalogWaveform for a channel and add it to waveforms.
            current_waveforms.append(
                AnalogWaveform(
                    channel_name=channel_name_read,
                    delta_time_seconds=delta_time_seconds,
                    samples=samples_per_channel,
                )
            )

            if (
                measurement_analysis_requirement
                == MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
            ):
                # DC and RMS processing.
                dc_rms_processing_result = LabViewBasicDcRms.process_single_waveform_dc_rms(
                    waveform_samples=samples_per_channel,
                    waveform_sampling_period_seconds=delta_time_seconds,
                    dc_rms_processing_window=ConstantsForDcRmsCurrentMeasurement.DEFAULT_DC_RMS_PROCESSING_WINDOW,
                )

                # Obtains the DC value for the acquired samples for a channel and append to the list
                calculated_dc_values.append(dc_rms_processing_result.dc_value)

                # Obtains the RMS value for the acquired samples for a channel and append to the list
                calculated_rms_values.append(dc_rms_processing_result.rms_value)

        return DcRmsCurrentMeasurementResultData(
            waveforms=current_waveforms,
            acquisition_duration_seconds=acquisition_duration,
            dc_values_amperes=calculated_dc_values,
            rms_values_amperes=calculated_rms_values,
        )
