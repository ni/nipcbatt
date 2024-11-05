""" Defines class used for Time domain measurement on PCB points."""

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    LabViewAmplitudeAndLevels,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import LabViewBasicDcRms
from nipcbatt.pcbatt_analysis.waveform_analysis.pulse_analog_analysis import (
    LabViewPulseAnalogMeasurements,
    PulseAnalogMeasurementPercentLevelsSettings,
    PulseAnalogProcessingReferenceLevels,
)
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
from nipcbatt.pcbatt_library.common.voltage_constants import ConstantsForVoltageMeasurement
from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.time_domain_measurements.time_domain_constants import (
    ConstantsForTimeDomainMeasurement,
)
from nipcbatt.pcbatt_library.time_domain_measurements.time_domain_data_types import (
    TimeDomainMeasurementConfiguration,
    TimeDomainMeasurementResultData,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value

# Temporary value. To be removed after implementation of Time domain analysis.
DEFAULT_NUMERIC_RESULT_VALUE = 0.0


class TimeDomainMeasurement(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to perform Time domain measurements on PCB points."""

    def initialize(self, analog_input_channel_expression: str):
        """Initializes the measurement with the specific channels

        Args:
            analog_input_channel_expression (str):
                Expression representing the name of a physical channel,
                or a global channel in DAQ System.
        """
        if self.is_task_initialized:
            return

        if self.contains_only_global_virtual_channels(
            channel_expression=analog_input_channel_expression
        ):
            # If the input channel_expression contains global channel,
            # then add them as global channels
            # and verify if the global channels are configured for current measurement.
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
        """Closes measurement procedure and releases internal resources."""
        if not self.is_task_initialized:
            return

        # Stop and close the DAQmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(self, configuration: TimeDomainMeasurementConfiguration):
        """Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (TimeDomainMeasurementConfiguration):
            A instance of `TimeDomainMeasurementConfiguration` used to configure the measurement.

        Returns:
            TimeDomainMeasurementResultData | None: An instance of `TimeDomainMeasurementResultData`
              or `None` if no measure was performed.
        """
        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.configure_all_channels(configuration.global_channel_parameters)
            for specific_channel_parameters in configuration.specific_channels_parameters:
                self.configure_specific_channel(specific_channel_parameters)
            self.configure_timing(configuration.sample_clock_timing_parameters)
            self.configure_trigger(configuration.digital_start_trigger_parameters)

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.MEASURE_ONLY,
        ):
            data = self.acquire_data_for_measurement_analysis()
            return self.analyze_measurement_data(
                data, configuration.measurement_options.measurement_analysis_requirement
            )

        self.task.start()
        return None

    def configure_all_channels(self, parameters: VoltageRangeAndTerminalParameters):
        """Configures all channels used for voltage measurements.

        Args:
            parameters (VoltageRangeAndTerminalParameters):
            An instance of `VoltageRangeAndTerminalParameters` used to configure the channels.
        """
        # for each channel defined in analog input channels list,
        # sets terminal configuration and voltage range.
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
        """
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

    def configure_timing(self, parameters: SampleClockTimingParameters) -> None:
        """Configures the timing characteristics used for time domain measurements.

        Args:
            parameters:An instance of `SampleClockTimingParameters` used to configure the timing.
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

    def configure_trigger(self, parameters: DigitalStartTriggerParameters) -> None:
        """Configures the characteristics of triggers used for time domain measurements.

        Args:
            parameters (DigitalStartTriggerParameters): An instance of
            `DigitalStartTriggerParameters` used to
        configure the channels.
        """

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
        # Builds the shape of numpy array (number of channels, number of samples)
        number_of_channels = len(self.task.in_stream.channels_to_read.channel_names)
        number_of_samples_per_channel = self.task.timing.samp_quant_samp_per_chan

        # Build the numpy array.
        samples_array = numpy.zeros(
            shape=(number_of_channels, number_of_samples_per_channel),
            dtype=numpy.float64,
        )

        # Reads data and fill numpy array.
        reader = nidaqmx.stream_readers.AnalogMultiChannelReader(self.task.in_stream)
        reader.read_many_sample(
            data=samples_array,
            number_of_samples_per_channel=number_of_samples_per_channel,
        )

        return MeasurementData(samples_array)

    def analyze_measurement_data(
        self,
        measurement_data: MeasurementData,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> TimeDomainMeasurementResultData:
        """Proceeds to the analysis of Voltages from the measurement.

        Args:
            data (MeasurementData):
                An instance of `MeasurementData`
                that specifies the data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            TimeDomainMeasurementResultData:
                An instance of `TimeDomainMeasurementResultData`
                that specifies the measurement results.
        """
        # Check if sampling rate is 0 and raise error to avoid divide by 0 error.
        Guard.is_greater_than_zero(
            self.task.timing.samp_clk_rate, nameof(self.task.timing.samp_clk_rate)
        )
        delta_time_seconds = invert_value(self.task.timing.samp_clk_rate)

        # Initialization for DcRmsVoltageMeasurementResultData instance creation.
        waveforms = []
        acquisition_duration_seconds = 0.0
        mean_dc_voltage_values_volts = []
        vpp_amplitudes_volts = []
        voltage_waveforms_frequencies_hertz = []
        voltage_waveforms_periods_seconds = []
        voltage_waveforms_duty_cycles_percent = []

        for channel_samples, channel_name in zip(
            measurement_data.samples_per_channel,
            self.task.in_stream.channels_to_read.channel_names,
        ):
            # Creates an instance of AnalogWaveform and add it to waveforms.
            waveforms.append(
                AnalogWaveform(
                    channel_name=channel_name,
                    delta_time_seconds=delta_time_seconds,
                    samples=channel_samples,
                )
            )

            if (
                measurement_analysis_requirement
                == MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS
            ):
                acquisition_duration_seconds += delta_time_seconds * len(channel_samples)

                # DC-RMS analysis
                current_channel_samples_dc_rms = LabViewBasicDcRms.process_single_waveform_dc_rms(
                    waveform_samples=channel_samples,
                    waveform_sampling_period_seconds=delta_time_seconds,
                    dc_rms_processing_window=ConstantsForTimeDomainMeasurement.DEFAULT_DC_RMS_PROCESSING_WINDOW,
                )

                mean_dc_voltage_values_volts.append(current_channel_samples_dc_rms.dc_value)

                # Amplitude and levels analysis
                current_channel_samples_amplitude_and_levels = LabViewAmplitudeAndLevels.process_single_waveform_amplitude_and_levels(
                    waveform_samples=channel_samples,
                    waveform_sampling_period_seconds=delta_time_seconds,
                    amplitude_and_levels_processing_method=ConstantsForTimeDomainMeasurement.DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_METHOD,
                    histogram_size=ConstantsForTimeDomainMeasurement.DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_HISTOGRAM_SIZE,
                )

                vpp_amplitudes_volts.append(current_channel_samples_amplitude_and_levels.amplitude)

                # Periodic waveform analysis (pulse + frequency + periods)
                try:
                    pulse_processing_result = LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                        waveform_samples=channel_samples,
                        waveform_sampling_period_seconds=delta_time_seconds,
                        waveform_t0=0,
                        pulse_number=1,
                        processing_polarity=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_POLARITY,
                        reference_levels_unit=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_REFERENCE_LEVELS_UNIT,
                        reference_levels=PulseAnalogProcessingReferenceLevels(
                            reference_level_high=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_HIGH,
                            reference_level_middle=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_MIDDLE,
                            reference_level_low=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_REFERENCE_LEVEL_LOW,
                        ),
                        export_mode=ConstantsForTimeDomainMeasurement.DEFAULT_PULSE_PROCESSING_EXPORT_MODE,
                        percent_levels_settings=PulseAnalogMeasurementPercentLevelsSettings(
                            amplitude_and_levels_processing_method=ConstantsForTimeDomainMeasurement.DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_METHOD,
                            histogram_size=ConstantsForTimeDomainMeasurement.DEFAULT_AMPLITUDE_AND_LEVELS_PROCESSING_HISTOGRAM_SIZE,
                        ),
                    )

                    voltage_waveforms_frequencies_hertz.append(
                        pulse_processing_result.waveform_periodicity_processing_result.frequency
                    )
                    voltage_waveforms_periods_seconds.append(
                        pulse_processing_result.waveform_periodicity_processing_result.period
                    )
                    voltage_waveforms_duty_cycles_percent.append(
                        pulse_processing_result.waveform_periodicity_processing_result.duty_cycle_percent
                    )
                except PCBATTAnalysisException:
                    pass

        return TimeDomainMeasurementResultData(
            waveforms=waveforms,
            acquisition_duration_seconds=acquisition_duration_seconds,
            mean_dc_voltage_values_volts=mean_dc_voltage_values_volts,
            vpp_amplitudes_volts=vpp_amplitudes_volts,
            voltage_waveforms_frequencies_hertz=voltage_waveforms_frequencies_hertz,
            voltage_waveforms_periods_seconds=voltage_waveforms_periods_seconds,
            voltage_waveforms_duty_cycles_percent=voltage_waveforms_duty_cycles_percent,
        )
