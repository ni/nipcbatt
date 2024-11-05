# pylint: disable=C0301
"""Provides a set of modules built on top of nidaqmx to perform PCBA electrical tests."""

# All classes inherited from PCBATestToolkitData, BuildingBlockUsingInstrument
# shall be imported here. By this way, the use of blocks in PCBA Test Toolkit
# is greatly facilitated. for that "import nipcbatt" imports all classes used
# for measurements, generations and device communications.
# Excample:
#
# import nipcbatt
#
# measurement = nipcbatt.DcRmsCurrentMeasurement()
# measurement.initialize()
# results = measurement.configure_and_measure(configuration=nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION)
# measurement.close()

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
    PCBATTAnalysisException,
    PCBATTAnalysisLoadNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import AnalysisLibraryExceptionMessage
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
    AmplitudeAndLevelsProcessingResult,
    LabViewAmplitudeAndLevels,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.dc_rms_analysis import (
    DcRmsProcessingResult,
    DcRmsProcessingWindow,
    LabViewBasicDcRms,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.frequency_domain_analysis import (
    LabViewFftSpectrumAmplitudePhase,
    LabViewFftSpectrumWindow,
    LabViewFrequencyDomainProcessing,
    LabViewMultipleTonesMeasurement,
    LabViewTonesSortingMode,
    MultipleTonesAmplitudePhaseSpectrumProcessingResult,
    MultipleTonesProcessingResult,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.pulse_analog_analysis import (
    LabViewPulseAnalogMeasurements,
    PulseAnalogMeasurementPercentLevelsSettings,
    PulseAnalogProcessingExportMode,
    PulseAnalogProcessingPolarity,
    PulseAnalogProcessingReferenceLevels,
    PulseAnalogProcessingReferenceLevelsUnit,
    PulseAnalogProcessingResult,
    WaveformPeriodicityAnalogProcessingResult,
)
from nipcbatt.pcbatt_communication_library.ni_845x_data_types import (
    DataMemoryAddressEndianness,
    DataMemoryAddressType,
    Ni845xI2cAddressingType,
    Ni845xPullupStatus,
    Ni845xVoltageLevel,
    SpiConfigurationClockPhase,
    SpiConfigurationClockPolarity,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_exceptions import (
    PCBATTCommunicationException,
)
from nipcbatt.pcbatt_communication_library.pcbatt_communication_messages import (
    PCBATTCommunicationExceptionMessages,
)
from nipcbatt.pcbatt_library.common.common_data_types import (
    AmplitudeSpectrum,
    AnalogWaveform,
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
    MeasurementAnalysisRequirement,
    MeasurementData,
    MeasurementExecutionType,
    MeasurementOptions,
    SampleClockTimingParameters,
    SampleTimingEngine,
    StartTriggerType,
)
from nipcbatt.pcbatt_library.common.communication_data_types import (
    MemoryAddressParameters,
    MemoryPageCharacteristics,
)
from nipcbatt.pcbatt_library.common.voltage_constants import ConstantsForVoltageMeasurement
from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_constants import (
    DEFAULT_DC_RMS_CURRENT_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_OPTIONS,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_TERMINAL_RANGE_PARAMETERS,
    DEFAULT_DC_RMS_CURRENT_SAMPLE_CLOCK_TIMING_PARAMETERS,
    ConstantsForDcRmsCurrentMeasurement,
)
from nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_data_types import (
    DcRmsCurrentMeasurementChannelAndTerminalRangeParameters,
    DcRmsCurrentMeasurementConfiguration,
    DcRmsCurrentMeasurementResultData,
    DcRmsCurrentMeasurementTerminalRangeParameters,
)
from nipcbatt.pcbatt_library.dc_rms_current_measurements.dc_rms_current_measurement import (
    DcRmsCurrentMeasurement,
)
from nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_constants import (
    DEFAULT_DC_RMS_VOLTAGE_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
    DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_OPTIONS,
    DEFAULT_DC_RMS_VOLTAGE_RANGE_AND_TERMINAL_PARAMETERS,
    DEFAULT_DC_RMS_VOLTAGE_SAMPLE_CLOCK_TIMING_PARAMETERS,
    ConstantsForDcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
    DcRmsVoltageMeasurementResultData,
)
from nipcbatt.pcbatt_library.dc_rms_voltage_measurements.dc_rms_voltage_measurement import (
    DcRmsVoltageMeasurement,
)
from nipcbatt.pcbatt_library.dc_voltage_generations.dc_voltage_data_types import (
    DcVoltageGenerationConfiguration,
)
from nipcbatt.pcbatt_library.dc_voltage_generations.dc_voltage_generation import DcVoltageGeneration
from nipcbatt.pcbatt_library.dc_voltage_generations.dc_voltage_generation_constants import (
    DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION,
    DEFAULT_VOLTAGE_GENERATION_CHANNEL_PARAMETERS,
    ConstantsForDcVoltageGeneration,
)
from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_constants import (
    ConstantsForDigitalClockGeneration,
)
from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_data_types import (
    DigitalClockGenerationConfiguration,
    DigitalClockGenerationCounterChannelParameters,
    DigitalClockGenerationData,
    DigitalClockGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.digital_clock_generations.digital_clock_generation import (
    DigitalClockGeneration,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_constants import (
    ConstantsForDigitalEdgeCountMeasurement,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_data_types import (
    DigitalEdgeCountHardwareTimerConfiguration,
    DigitalEdgeCountMeasurementCounterChannelParameters,
    DigitalEdgeCountMeasurementResultData,
    DigitalEdgeCountMeasurementTimingParameters,
    DigitalEdgeCountSoftwareTimerConfiguration,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_measurement_using_hardware_timer import (
    DigitalEdgeCountMeasurementUsingHardwareTimer,
)
from nipcbatt.pcbatt_library.digital_edge_count_measurements.digital_edge_count_measurement_using_software_timer import (
    DigitalEdgeCountMeasurementUsingSoftwareTimer,
)
from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_constants import (
    ConstantsForDigitalFrequencyMeasurement,
)
from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_data_types import (
    DigitalFrequencyMeasurementConfiguration,
    DigitalFrequencyMeasurementCounterChannelParameters,
    DigitalFrequencyMeasurementResultData,
    DigitalFrequencyRangeParameters,
)
from nipcbatt.pcbatt_library.digital_frequency_measurements.digital_frequency_measurement import (
    DigitalFrequencyMeasurement,
)
from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_constants import (
    ConstantsForDigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_data_types import (
    DigitalPulseGenerationConfiguration,
    DigitalPulseGenerationCounterChannelParameters,
    DigitalPulseGenerationData,
    DigitalPulseGenerationTimingParameters,
)
from nipcbatt.pcbatt_library.digital_pulse_generations.digital_pulse_generation import (
    DigitalPulseGeneration,
)
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_constants import (
    ConstantsForDigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_data_types import (
    DigitalPwmMeasurementConfiguration,
    DigitalPwmMeasurementCounterChannelParameters,
    DigitalPwmMeasurementData,
    DigitalPwmMeasurementRangeParameters,
    DigitalPwmMeasurementResultData,
    DigitalPwmMeasurementTimingParameters,
)
from nipcbatt.pcbatt_library.digital_pwm_measurements.digital_pwm_measurement import (
    DigitalPwmMeasurement,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternGenerationConfiguration,
    DynamicDigitalPatternGenerationData,
    DynamicDigitalStartTriggerParameters,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_generations.dynamic_digital_pattern_generation import (
    DynamicDigitalPatternGeneration,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_data_types import (
    DynamicDigitalPatternMeasurementConfiguration,
    DynamicDigitalPatternMeasurementResultData,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_measurement import (
    DynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_constants import (
    DEFAULT_FREQUENCY_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION,
    DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_OPTIONS,
    DEFAULT_FREQUENCY_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
    DEFAULT_FREQUENCY_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
    ConstantsForFrequencyDomainMeasurement,
)
from nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_data_types import (
    FrequencyDomainMeasurementConfiguration,
    FrequencyDomainMeasurementResultData,
    MultipleTonesMeasurementResultData,
)
from nipcbatt.pcbatt_library.frequency_domain_measurements.frequency_domain_measurement import (
    FrequencyDomainMeasurement,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_communication_constants import (
    DEFAULT_I2C_COMMUNICATION_PARAMETERS,
    DEFAULT_I2C_DEVICE_PARAMETERS,
    DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION,
    DEFAULT_I2C_READ_PARAMETERS,
    DEFAULT_I2C_WRITE_COMMUNICATION_CONFIGURATION,
    DEFAULT_I2C_WRITE_PARAMETERS,
    ConstantsForI2cCommunication,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_data_types import (
    I2cCommunicationParameters,
    I2cDeviceParameters,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_read_communication import I2cReadCommunication
from nipcbatt.pcbatt_library.i2c_communications.i2c_read_data_types import (
    I2cReadCommunicationConfiguration,
    I2cReadCommunicationData,
    I2cReadParameters,
)
from nipcbatt.pcbatt_library.i2c_communications.i2c_write_communication import I2cWriteCommunication
from nipcbatt.pcbatt_library.i2c_communications.i2c_write_data_types import (
    I2cWriteCommunicationConfiguration,
    I2cWriteParameters,
)
from nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_and_measure import (
    PowerSupplySourceAndMeasure,
)
from nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_constants import (
    DEFAULT_POWER_SUPPLY_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_POWER_SUPPLY_MEASUREMENT_OPTIONS,
    DEFAULT_POWER_SUPPLY_SAMPLE_CLOCK_TIMING_PARAMETERS,
    DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION,
    DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_TERMINAL_PARAMETERS,
    ConstantsForPowerSupplySourceMeasurement,
)
from nipcbatt.pcbatt_library.power_supply_source_and_measurements.power_supply_source_data_types import (
    PowerSupplySourceAndMeasureConfiguration,
    PowerSupplySourceAndMeasureData,
    PowerSupplySourceAndMeasureResultData,
    PowerSupplySourceAndMeasureTerminalParameters,
)
from nipcbatt.pcbatt_library.serial_communications.serial_communication import SerialCommunication
from nipcbatt.pcbatt_library.serial_communications.serial_communication_constants import (
    ConstantsForSerialCommunication,
)
from nipcbatt.pcbatt_library.serial_communications.serial_data_types import (
    SerialCommunicationConfiguration,
    SerialCommunicationData,
    SerialCommunicationParameters,
)
from nipcbatt.pcbatt_library.signal_voltage_generations.signal_voltage_data_types import (
    SignalVoltageGenerationMultipleTonesConfiguration,
    SignalVoltageGenerationMultipleTonesWaveParameters,
    SignalVoltageGenerationSineWaveConfiguration,
    SignalVoltageGenerationSineWaveParameters,
    SignalVoltageGenerationSquareWaveConfiguration,
    SignalVoltageGenerationSquareWaveParameters,
    SignalVoltageGenerationTimingParameters,
    ToneParameters,
)
from nipcbatt.pcbatt_library.signal_voltage_generations.signal_voltage_generation import (
    SignalVoltageGeneration,
)
from nipcbatt.pcbatt_library.signal_voltage_generations.signal_voltage_generation_constants import (
    DEFAULT_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION,
    DEFAULT_MULTI_TONE_GENERATION_PARAMETERS,
    DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION,
    DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_PARAMETERS,
    DEFAULT_SIGNAL_VOLTAGE_GENERATION_SQUARE_WAVE_PARAMETERS,
    DEFAULT_SIGNAL_VOLTAGE_GENERATION_TIMING_PARAMETERS,
    DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION,
    DEFAULT_TONE_PARAMETERS,
    DEFAULT_VOLTAGE_GENERATION_RANGE_PARAMETERS,
    ConstantsForSignalVoltageGeneration,
)
from nipcbatt.pcbatt_library.spi_communications.spi_communication_constants import (
    DEFAULT_SPI_COMMUNICATION_PARAMETERS,
    DEFAULT_SPI_DEVICE_PARAMETERS,
    DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION,
    DEFAULT_SPI_READ_PARAMETERS,
    DEFAULT_SPI_WRITE_COMMUNICATION_CONFIGURATION,
    DEFAULT_SPI_WRITE_PARAMETERS,
    ConstantsForSpiCommunication,
)
from nipcbatt.pcbatt_library.spi_communications.spi_data_types import (
    SpiCommunicationParameters,
    SpiDeviceParameters,
)
from nipcbatt.pcbatt_library.spi_communications.spi_read_communication import SpiReadCommunication
from nipcbatt.pcbatt_library.spi_communications.spi_read_data_types import (
    SpiReadCommunicationConfiguration,
    SpiReadCommunicationData,
    SpiReadParameters,
)
from nipcbatt.pcbatt_library.spi_communications.spi_write_communication import SpiWriteCommunication
from nipcbatt.pcbatt_library.spi_communications.spi_write_data_types import (
    SpiWriteCommunicationConfiguration,
    SpiWriteParameters,
)
from nipcbatt.pcbatt_library.static_digital_state_generations.static_digital_state_data_types import (
    StaticDigitalStateGenerationConfiguration,
    StaticDigitalStateGenerationData,
)
from nipcbatt.pcbatt_library.static_digital_state_generations.static_digital_state_generation import (
    StaticDigitalStateGeneration,
)
from nipcbatt.pcbatt_library.static_digital_state_measurements.static_digital_state_data_types import (
    StaticDigitalStateMeasurementResultData,
)
from nipcbatt.pcbatt_library.static_digital_state_measurements.static_digital_state_measurement import (
    StaticDigitalStateMeasurement,
)
from nipcbatt.pcbatt_library.synchronizations.synchronization_signal_routing import (
    SynchronizationSignalRouting,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_constants import (
    DEFAULT_BETA_OEFFICIENT_AND_SENSOR_RESISTANCE_PARAMETERS,
    DEFAULT_COEFFICIENTS_STEINHART_HART_PARAMETERS,
    DEFAULT_TEMPERATURE_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION,
    DEFAULT_TEMPERATURE_RTD_MEASUREMENT_TERMINAL_PARAMETERS,
    DEFAULT_TEMPERATURE_SAMPLE_CLOCK_TIMING_PARAMETERS,
    DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION,
    DEFAULT_TEMPERATURE_THERMISTOR_RANGE_AND_TERMINAL_PARAMETERS,
    DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION,
    DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_TERMINAL_PARAMETERS,
    ConstantsForTemperatureMeasurement,
    ConstantsForTemperatureMeasurementUsingRtd,
    ConstantsForTemperatureMeasurementUsingThermistor,
    ConstantsForTemperatureMeasurementUsingThermocouple,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_data_types import (
    BetaCoefficientAndSensorResistanceParameters,
    CoefficientsSteinhartHartParameters,
    SteinhartHartEquationOption,
    TemperatureMeasurementResultData,
    TemperatureRtdMeasurementChannelParameters,
    TemperatureRtdMeasurementConfiguration,
    TemperatureRtdMeasurementTerminalParameters,
    TemperatureThermistorChannelRangeAndTerminalParameters,
    TemperatureThermistorMeasurementConfiguration,
    TemperatureThermistorRangeAndTerminalParameters,
    TemperatureThermocoupleChannelRangeAndTerminalParameters,
    TemperatureThermocoupleMeasurementConfiguration,
    TemperatureThermocoupleMeasurementTerminalParameters,
    TemperatureThermocoupleRangeAndTerminalParameters,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement import (
    TemperatureMeasurement,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_rtd import (
    TemperatureMeasurementUsingRtd,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermistor import (
    TemperatureMeasurementUsingThermistor,
)
from nipcbatt.pcbatt_library.temperature_measurements.temperature_measurement_using_thermocouple import (
    TemperatureMeasurementUsingThermocouple,
)
from nipcbatt.pcbatt_library.time_domain_measurements.time_domain_constants import (
    DEFAULT_TIME_DOMAIN_DIGITAL_START_TRIGGER_PARAMETERS,
    DEFAULT_TIME_DOMAIN_MEASUREMENT_CONFIGURATION,
    DEFAULT_TIME_DOMAIN_MEASUREMENT_OPTIONS,
    DEFAULT_TIME_DOMAIN_RANGE_AND_TERMINAL_PARAMETERS,
    DEFAULT_TIME_DOMAIN_SAMPLE_CLOCK_TIMING_PARAMETERS,
    ConstantsForTimeDomainMeasurement,
)
from nipcbatt.pcbatt_library.time_domain_measurements.time_domain_data_types import (
    TimeDomainMeasurementConfiguration,
    TimeDomainMeasurementResultData,
)
from nipcbatt.pcbatt_library.time_domain_measurements.time_domain_measurement import (
    TimeDomainMeasurement,
)
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import (
    BuildingBlockUsingDAQmx,
    BuildingBlockUsingInstrument,
    BuildingBlockUsingVisa,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_library_core.pcbatt_library_exceptions import (
    PCBATTLibraryChannelNotCompatibleWithGenerationException,
    PCBATTLibraryChannelNotCompatibleWithMeasurementException,
    PCBATTLibraryException,
)
from nipcbatt.pcbatt_library_core.pcbatt_library_messages import PCBATTLibraryExceptionMessages
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
