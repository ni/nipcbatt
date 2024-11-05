# pylint: disable=W0613
# remove it when arguments of initialize are used.
"""Defines class used for power supply source and measurement of voltage, current and power."""

import time

import nidaqmx.constants
import nidaqmx.stream_readers
import numpy
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementAnalysisRequirement,
    MeasurementExecutionType,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_constants import (
    ConstantsForPowerSupplySourceMeasurement,
)
from nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_data_types import (
    PowerSupplySourceAndMeasureConfiguration,
    PowerSupplySourceAndMeasureData,
    PowerSupplySourceAndMeasureResultData,
    PowerSupplySourceAndMeasureTerminalParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import BuildingBlockUsingDAQmx
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
from nipcbatt.pcbatt_utilities.numeric_utilities import invert_value


class PowerSupplySourceAndMeasure(BuildingBlockUsingDAQmx):
    """Defines a way that allows you to configure and perform power supply using a source and measure resulting voltage and current.

    Args:
        BuildingBlockUsingDAQmx (_type_): _description_
    """

    def initialize(self, power_channel_name: str):
        """Initializes the Power source and measurement with the specific channel

        Args:
            power_channel_name (str): Expression representing the name of a physical channel,
            or a global channel or the name of registered settings in DAQ System.
        """
        if self.is_task_initialized:
            return

        # There will be only once channel for Power Source and Measure
        # task at a time. Add the Power channel to the task.
        self.task.ai_channels.add_ai_power_chan(
            physical_channel=power_channel_name,
            voltage_setpoint=(
                ConstantsForPowerSupplySourceMeasurement.INITIAL_VOLTAGE_SETPOINT_VOLTS
            ),
            current_setpoint=(
                ConstantsForPowerSupplySourceMeasurement.INITIAL_CURRENT_SETPOINT_AMPERES
            ),
            output_enable=ConstantsForPowerSupplySourceMeasurement.INITIAL_OUTPUT_ENABLE,
        )

    def close(self):
        """Closes the measurement process and releases the internal resources"""
        if not self.is_task_initialized:
            return
        # Stop and close the daqmx task
        self.task.stop()
        self.task.close()

    def configure_and_measure(
        self, configuration: PowerSupplySourceAndMeasureConfiguration
    ) -> PowerSupplySourceAndMeasureResultData:
        """
        Configures and/or performs a measurement according to specific configuration parameters.

        Args:
            configuration (PowerSupplySourceAndMeasureConfiguration):
            A instance of `PowerSupplySourceAndMeasureConfiguration`
            used to configure the measurement.

        Returns:
            _type_: An instance of `PowerSupplySourceAndMeasureResultData
            ` or `None` if no measure was performed.
        """

        if configuration.measurement_options.execution_option in (
            MeasurementExecutionType.CONFIGURE_AND_MEASURE,
            MeasurementExecutionType.CONFIGURE_ONLY,
        ):
            self.configure_all_channels(configuration.terminal_parameters)
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

    def configure_all_channels(self, parameters: PowerSupplySourceAndMeasureTerminalParameters):
        """Configures all channels used for power supply source and measure measurements.

        Args:
            parameters (PowerSupplySourceAndMeasureTerminalParameters):
            An instance of `PowerSupplySourceAndMeasureTerminalParameters`
            used to configure the channels.
        """
        for channel in self.task.ai_channels:
            channel.pwr_voltage_setpoint = parameters.voltage_setpoint_volts
            channel.pwr_current_setpoint = parameters.current_setpoint_amperes
            channel.pwr_remote_sense = parameters.power_sense
            channel.pwr_idle_output_behavior = parameters.idle_output_behaviour
            channel.pwr_output_enable = parameters.enable_output

    def configure_timing(self, parameters: SampleClockTimingParameters):
        """Configure the timing characteristics used for Power supply sourcing and measurement.

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
            del self.task.timing.samp_timing_engine
        else:
            self.task.timing.samp_timing_engine = parameters.sample_timing_engine.value

    def configure_trigger(self, parameters: DigitalStartTriggerParameters):
        """Configure the characteristics of triggers used for Power supply sourcing and measurement.

        Args:
            parameters (DigitalStartTriggerParameters):
            An instance of `DigitalStartTriggerParameters`
            used to configure the channels.
        """
        self.task.stop()
        if parameters.trigger_select == StartTriggerType.NO_TRIGGER:
            self.task.triggers.start_trigger.disable_start_trig()
        else:
            self.task.triggers.start_trigger.cfg_dig_edge_start_trig(
                trigger_source=parameters.digital_start_trigger_source,
                trigger_edge=parameters.digital_start_trigger_edge,
            )

    def acquire_data_for_measurement_analysis(self) -> PowerSupplySourceAndMeasureData:
        """Acquires the voltage and current data from the DAQ channel
        for measurement of Power supply.

        Returns:
            PowerSupplySourceAndMeasureData: An instance of `PowerSupplySourceAndMeasureData`
            that contains array of voltage and current samples acquired from DAQ channels.
        """
        number_of_samples_per_channel_to_read = self.task.timing.samp_quant_samp_per_chan
        # Create pre-allocated numpy array to read the voltage samples from the daqmx buffer.
        voltage_data_to_read = numpy.zeros(
            shape=(number_of_samples_per_channel_to_read),
            dtype=numpy.float64,
        )
        # Create pre-allocated numpy array to read the current samples from the daqmx buffer.
        current_data_to_read = numpy.zeros(
            shape=(number_of_samples_per_channel_to_read),
            dtype=numpy.float64,
        )

        # Read current and voltage samples from the task channel reader.
        reader = nidaqmx.stream_readers.PowerSingleChannelReader(self.task.in_stream)
        reader.read_many_sample(
            voltage_data=voltage_data_to_read,
            current_data=current_data_to_read,
            number_of_samples_per_channel=number_of_samples_per_channel_to_read,
            timeout=10,
        )

        # If there are NaN values in numpy array, set them as 0.
        # This is a bug in samples representation of Power.
        for index in range(0, number_of_samples_per_channel_to_read):
            if numpy.isnan(voltage_data_to_read[index]):
                voltage_data_to_read[index] = 0
            if numpy.isnan(current_data_to_read[index]):
                current_data_to_read[index] = 0

        # Create an instance of PowerSupplySourceAndMeasureData
        # with the voltage and current samples read above.
        return PowerSupplySourceAndMeasureData(
            source_name=self.task.channel_names[0],
            voltage_samples=voltage_data_to_read,
            current_samples=current_data_to_read,
            sampling_rate_hertz=self.task.timing.samp_clk_rate,
        )

    def analyze_measurement_data(
        self,
        measurement_data: PowerSupplySourceAndMeasureData,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> PowerSupplySourceAndMeasureResultData:
        """Calls the analysis function for Power source and measure measurements.

        Args:
            data (PowerSupplySourceAndMeasureData):
                An instance of `PowerSupplySourceAndMeasureData`
                that specifies the voltage and current data acquired from DAQ channels.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
                An instance of 'MeasurementAnalysisRequirement' that specifies
                whether to Skip Analysis or Proceed to Analysis.

        Returns:
            PowerSupplySourceAndMeasureResultData:
                An instance of `PowerSupplySourceAndMeasureResultData`
                that specifies the measurement results.
        """
        Guard.is_not_none(measurement_data, nameof(measurement_data))

        # extract & convert sample rate to delta_t

        dt = invert_value(measurement_data.sampling_rate_hertz)

        # Generate voltage waveform
        voltage_waveform = AnalogWaveform("Voltage", dt, measurement_data.voltage_samples)

        # Generate current waveform
        current_waveform = AnalogWaveform("Current", dt, measurement_data.current_samples)

        max_voltage_level = 0.0
        max_current_level = 0.0
        max_power_level = 0.0
        average_power_level = 0.0
        acquisition_duration = 0.0

        if measurement_analysis_requirement == MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS:
            # Calculate max voltage level
            max_voltage_level = numpy.max(measurement_data.voltage_samples)

            # Calculate max current level
            max_current_level = numpy.max(measurement_data.current_samples)

            # generate power samples
            power_samples = numpy.multiply(
                measurement_data.voltage_samples, measurement_data.current_samples
            )

            # calculate power
            max_power_level = numpy.max(power_samples)
            average_power_level = numpy.mean(power_samples)

            # Calculate total duration
            acquisition_duration = dt * numpy.size(measurement_data.voltage_samples)

        # Create and return PowerSupplySourceAndMeasureData object
        return PowerSupplySourceAndMeasureResultData(
            voltage_waveform,
            current_waveform,
            max_voltage_level,
            max_current_level,
            max_power_level,
            average_power_level,
            acquisition_duration,
        )
