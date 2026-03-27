# Migration Guide — API Mapping and Class/Method Discovery

This document helps migrate code to the explicit subpackage imports under the `nipcbatt` top-level package and provides a reproducible way to generate a complete list of classes and callable members exported by the package and its subpackages.


## Recommended import style
Prefer importing from explicit subpackages to make dependencies and behavior clearer and avoid name collisions:

```python
# Recommended
from nipcbatt import daq
drv = daq.DcVoltageGeneration()

# Or import only what's needed
from nipcbatt.daq import DcVoltageGeneration
drv = DcVoltageGeneration()
```

## API Reference — Available Classes by Subpackage

### `nipcbatt.daq` — DAQmx-based generation and measurement

**Generation Classes**
- `DcVoltageGeneration` — DC voltage waveform generation
- `SignalVoltageGeneration` — Arbitrary waveform generation (sine, square, multi-tone)  
- `DigitalClockGeneration` — Digital clock signal generation
- `DigitalPulseGeneration` — Digital pulse train generation
- `DynamicDigitalPatternGeneration` — Dynamic digital pattern generation
- `StaticDigitalStateGeneration` — Static digital logic state generation

**Measurement Classes**
- `DcRmsVoltageMeasurement` — DC/RMS voltage analog input measurement
- `DcRmsCurrentMeasurement` — DC/RMS current measurement (via shunt)
- `TimeDomainMeasurement` — Time-domain voltage measurement
- `FrequencyDomainMeasurement` — Frequency domain voltage measurement
- `TemperatureMeasurementUsingRtd` — Temperature via RTD sensor
- `TemperatureMeasurementUsingThermistor` — Temperature via thermistor sensor
- `TemperatureMeasurementUsingThermocouple` — Temperature via thermocouple sensor
- `DigitalFrequencyMeasurement` — Digital frequency measurement
- `DigitalEdgeCountMeasurementUsingSoftwareTimer` — Digital edge counting (software timer)
- `DigitalEdgeCountMeasurementUsingHardwareTimer` — Digital edge counting (hardware timer)
- `DigitalPwmMeasurement` — Digital PWM signal measurement
- `DynamicDigitalPatternMeasurement` — Dynamic digital pattern capture
- `StaticDigitalStateMeasurement` — Static digital logic state measurement

**Default Configurations**
- `DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION`
- `DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION`
- `DEFAULT_TIME_DOMAIN_MEASUREMENT_CONFIGURATION`
- `DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION`
- `DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION`
- `DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION`
- `DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION`
- `DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION`
- `DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION`
- `DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION`
- `DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION`
- `DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION`
- `DEFAULT_DIGITAL_CLOCK_GENERATION_CONFIGURATION`
- `DEFAULT_DIGITAL_PULSE_GENERATION_CONFIGURATION`

**Usage Example**
```python
from nipcbatt import daq
import nidaqmx.constants
import nipcbatt

# Signal Voltage Generation (Sine Wave)
gen = daq.SignalVoltageGeneration()
gen.initialize(analog_output_channel_expression="/Dev1/ao0")

timing_params = nipcbatt.AnalogWaveformGenerationTimingParameters(
    sampling_rate_hertz=1000.0,
    number_of_samples_per_channel=5000
)

gen_config = daq.SignalVoltageGenerationConfiguration(
    timing_parameters=timing_params,
    waveform_type=daq.WaveformType.SINE_WAVE,
    frequency_hertz=100.0,
    amplitude_volts=1.0,
    phase_radians=0.0
)
gen.configure_and_generate(gen_config)
gen.close()

# Time Domain Voltage Measurement
meas = daq.TimeDomainMeasurement()
meas.initialize(analog_input_channel_expression="/Dev1/ai0")

meas_timing = nipcbatt.AnalogWaveformMeasurementTimingParameters(
    sampling_rate_hertz=1000.0,
    number_of_samples_per_channel=5000,
    active_edge=nidaqmx.constants.Edge.RISING
)

meas_config = daq.TimeDomainMeasurementConfiguration(
    timing_parameters=meas_timing
)
result = meas.configure_and_measure(meas_config)
meas.close()
print(result)
```

---

### `nipcbatt.dmm` — NI-DMM instrument control

**Measurement Classes**
- `DcRmsVoltageMeasurement` — DC/RMS voltage measurement
- `DcRmsCurrentMeasurement` — DC/RMS current measurement
- `DcRmsResistanceMeasurement` — 2-wire or 4-wire resistance measurement
- `MixedMeasurement` — Combined voltage, current, and resistance measurements

**Configuration Classes**
- `DcRmsVoltageMeasurementFunctionParameters`
- `DcRmsCurrentMeasurementFunctionParameters`
- `ResistanceMeasurementFunctionParameters`
- `MixedMeasurementFunctionParameters`

**Default Configurations**
- `DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION`
- `DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_PARAMETERS`
- `DEFAULT_DC_RMS_VOLTAGE_TIMING_PARAMETERS`
- `DEFAULT_DC_RMS_VOLTAGE_TRIGGER_PARAMETERS`
- `DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION`
- `DEFAULT_DC_RMS_CURRENT_MEASUREMENT_PARAMETERS`
- `DEFAULT_DC_RMS_CURRENT_TIMING_PARAMETERS`
- `DEFAULT_DC_RMS_CURRENT_TRIGGER_PARAMETERS`
- `DEFAULT_RESISTANCE_MEASUREMENT_CONFIGURATION`
- `DEFAULT_RESISTANCE_MEASUREMENT_PARAMETERS`
- `DEFAULT_RESISTANCE_TIMING_PARAMETERS`
- `DEFAULT_RESISTANCE_TRIGGER_PARAMETERS`
- `DEFAULT_MIXED_MEASUREMENT_CONFIGURATION`
- `DEFAULT_MIXED_MEASUREMENT_PARAMETERS`
- `DEFAULT_MIXED_TIMING_PARAMETERS`
- `DEFAULT_MIXED_TRIGGER_PARAMETERS`

**Usage Example**
```python
from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

# DC-RMS Voltage Measurement
voltage_meas = dmm.DcRmsVoltageMeasurement()

# Attach logger to record configuration and results
logger = PcbattLogger(file="c:\\Temp\\voltage_measurement.txt")
logger.attach(voltage_meas)

voltage_meas.initialize(resource_name="Sim_DMM", powerline_frequency=50)

# Use default configuration or customize
measurement_result = voltage_meas.configure_and_measure(
    configuration=dmm.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION
)

voltage_meas.close()
print(measurement_result)

# Resistance Measurement (2-wire or 4-wire)
resistance_meas = dmm.DcRmsResistanceMeasurement()
logger2 = PcbattLogger(file="c:\\Temp\\resistance_measurement.txt")
logger2.attach(resistance_meas)

resistance_meas.initialize(resource_name="Sim_DMM", powerline_frequency=50)
resistance_result = resistance_meas.configure_and_measure(
    configuration=dmm.DEFAULT_RESISTANCE_MEASUREMENT_CONFIGURATION
)

resistance_meas.close()
print(resistance_result)
```

---

### `nipcbatt.switch` — NI-SWITCH relay control

**Generation Classes**
- `StaticDigitalPathGeneration` — Configure and close/open static relay paths

**Configuration Classes**
- `StaticDigitalPathGenerationChannelParameters` — Channel pair definition
- `StaticDigitalPathGenerationStateParameters` — Channel state (open/closed)
- `StaticDigitalPathGenerationTerminalAndStateSettings` — Terminal configuration
- `StaticDigitalPathGenerationTimingParameters` — Timing/debounce settings
- `StaticDigitalPathGenerationConfiguration` — Complete path configuration

**Default Configurations**
- `DEFAULT_STATIC_DIGITAL_PATH_GENERATION_CONFIGURATION`

**Usage Example**
```python
from nipcbatt import switch
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

generation = switch.StaticDigitalPathGeneration()

logger = PcbattLogger(file="c:\\Temp\\switch_logger.txt")
logger.attach(generation)

# Initialize with specific switch hardware
resource_name = "Sim_MUX"
topology = "2527/2-Wire Dual 16x1 Mux"
module_characteristics = generation.initialize(resource_name, topology)

# Configure path from ch0 to com0
p1, p2 = "ch0", "com0"
connect = True
max_wait_debounce = 100

channel_params = switch.StaticDigitalPathGenerationChannelParameters(p1, p2)
state = switch.StaticDigitalPathGenerationStateParameters(connect)
ts_settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(channel_params, state)
timing_settings = switch.StaticDigitalPathGenerationTimingParameters(max_wait_debounce)
config = switch.StaticDigitalPathGenerationConfiguration(ts_settings, timing_settings)

print(f'Connecting {p1} to {p2}')
path_status = generation.configure_and_generate(config)
generation.display_status(path_status)

generation.close()
```

---

### `nipcbatt.dmm_scan` — Combined DMM + SWITCH scanning

**Measurement Classes**
- `DmmScanPMPS` — Orchestrated DMM measurement across switch channels (PXI Mux + Shunt + DMM)

**Data Classes**
- `ScanResources` — Container for initialized mux, shunt, and DMM sessions
- `MeasurementResult` — Aggregate scan results (timing, formatted/raw measurements, settings)

**Default Configurations**
- Inherits DMM and Switch configurations; compose as needed

**Usage Example**
```python
from nipcbatt import dmm
from nipcbatt import dmm_scan

# Define scan configuration for multiple channels and functions
scan_configuration = [
    [0,  dmm.MixedRangeAndFunctions.DC_100mV,             dmm.ResolutionInDigits.DIGITS_6_5],
    [1,  dmm.MixedRangeAndFunctions.DC_1V,                dmm.ResolutionInDigits.DIGITS_5_5],
    [2,  dmm.MixedRangeAndFunctions.AC_2V,                dmm.ResolutionInDigits.DIGITS_4_5],
    [3,  dmm.MixedRangeAndFunctions.TWO_W_RES_10k_Ohm,    dmm.ResolutionInDigits.DIGITS_4_5],
    [16, dmm.MixedRangeAndFunctions.DC_100mA,             dmm.ResolutionInDigits.DIGITS_6_5],
    [17, dmm.MixedRangeAndFunctions.DC_10mA,              dmm.ResolutionInDigits.DIGITS_5_5],
]

# Create and initialize scanner (Mux + Shunt + DMM combo)
scan = dmm_scan.DmmScanPMPS()

mux_resource_name = "Sim_MUX"
mux_topology_name = "2527/2-Wire Dual 16x1 Mux"
shunt_resource_name = "Sim_SHUNT"
shunt_topology_name = "2568/31-SPST"
dmm_resource_name = "Sim_DMM"
powerline_freq = 50
verbose = True

resources = scan.initialize(
    mux_resource_name,
    mux_topology_name,
    shunt_resource_name,
    shunt_topology_name,
    dmm_resource_name,
    powerline_freq,
    close_all_shunts=True
)

# Execute scan across configured channels
result = scan.configure_and_measure(
    resources,
    scan_configuration,
    verbose=verbose
)

scan.close(resources)
print(result)
```

---

### `nipcbatt.pcbatt_library.communications` — I2C, SPI, and Serial communication

**I2C Communication Classes**
- `I2cReadCommunication` — Read data via I2C interface
- `I2cWriteCommunication` — Write data via I2C interface

**SPI Communication Classes**
- `SpiReadCommunication` — Read data via SPI interface
- `SpiWriteCommunication` — Write data via SPI interface

**Serial Communication Classes**
- `SerialCommunication` — Read/write via serial (RS-232) interface

**Default Configurations**
- `DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION`
- `DEFAULT_I2C_WRITE_COMMUNICATION_CONFIGURATION`
- `DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION`
- `DEFAULT_SPI_WRITE_COMMUNICATION_CONFIGURATION`

**Usage Example (NI-845x I2C)**
```python
import numpy
import nipcbatt.pcbatt_communication_library.ni_845x_i2c_communication_devices
import nipcbatt.pcbatt_communication_library.ni_845x_data_types

# Initialize I2C handler for USB-8452 device
i2c = (
    nipcbatt.pcbatt_communication_library.ni_845x_i2c_communication_devices
    .Ni845xI2cDevicesHandler()
)
i2c.open(device_name="USB-8452")

# Configure I2C settings
i2c.enable_pullup_resistors(enable=False)
i2c.set_timeout(timeout_milliseconds=40000)

# Set I2C address and communication parameters
i2c.configuration.address = 0x48  # LM75 temperature sensor address
seven_bits = (
    nipcbatt.pcbatt_communication_library.ni_845x_data_types
    .Ni845xI2cAddressingType(0)
)
i2c.configuration.addressing_type = seven_bits
i2c.configuration.clock_rate_kilohertz = 400

# Write and read I2C data
data_to_write = numpy.ndarray(shape=[0], dtype=numpy.ubyte)
result = i2c.write_and_read_data(
    data_bytes_to_be_written=data_to_write,
    number_of_bytes_to_read=2
)

print(f"I2C Read Result: {result}")
i2c.close()
```

---

### `nipcbatt.pcbatt_library.common` — Shared data types and enums

**Enumerations**
- `MeasurementExecutionType` — CONFIGURE_AND_MEASURE, CONFIGURE_ONLY, MEASURE_ONLY
- `MeasurementAnalysisRequirement` — SKIP_ANALYSIS, PROCEED_TO_ANALYSIS
- `StartTriggerType` — NO_TRIGGER, DIGITAL_TRIGGER
- `SampleTimingEngine` — TE0, TE1, AI, AUTO

**Data Classes**
- `MeasurementOptions` — Combines execution type and analysis requirement
- `SampleClockTimingParameters` — Sample clock configuration
- `DigitalStartTriggerParameters` — Digital trigger setup

**Usage Example**
```python
from nipcbatt.pcbatt_library.common import common_data_types as cdt

opts = cdt.MeasurementOptions(
    execution_option=cdt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
    measurement_analysis_requirement=cdt.MeasurementAnalysisRequirement.SKIP_ANALYSIS
)
```

---

## Backward-Compatible Direct Imports from `nipcbatt`

For backward compatibility with legacy code, many commonly-used classes remain accessible directly from the top-level `nipcbatt` namespace. However, this re-export mechanism may be deprecated in future releases. **New code should use explicit subpackage imports** as shown in the **API Reference** section above.

### Currently Available Direct Imports

The following classes and enumerations are re-exported at the top level and can be imported directly from `nipcbatt`:

```python
# DAQ Generation and Measurement
from nipcbatt import (
    # Generation
    DcVoltageGeneration,
    SignalVoltageGeneration,
    DigitalClockGeneration,
    DigitalPulseGeneration,
    DynamicDigitalPatternGeneration,
    StaticDigitalStateGeneration,
    # Measurement
    DcRmsVoltageMeasurement,
    DcRmsCurrentMeasurement,
    TimeDomainMeasurement,
    FrequencyDomainMeasurement,
    TemperatureMeasurementUsingRtd,
    TemperatureMeasurementUsingThermistor,
    TemperatureMeasurementUsingThermocouple,
    DigitalFrequencyMeasurement,
    DigitalEdgeCountMeasurementUsingSoftwareTimer,
    DigitalEdgeCountMeasurementUsingHardwareTimer,
    DigitalPwmMeasurement,
    DynamicDigitalPatternMeasurement,
    StaticDigitalStateMeasurement,
    # Default Configurations
    DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION,
    DEFAULT_SIGNAL_VOLTAGE_GENERATION_SINE_WAVE_CONFIGURATION,
    DEFAULT_SQUARE_WAVE_GENERATION_CONFIGURATION,
    DEFAULT_MULTI_TONE_GENERATION_CONFIGURATION,
    DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION,
    DEFAULT_TIME_DOMAIN_MEASUREMENT_CONFIGURATION,
    DEFAULT_FREQUENCY_DOMAIN_MEASUREMENT_CONFIGURATION,
    DEFAULT_TEMPERATURE_RTD_MEASUREMENT_CONFIGURATION,
    DEFAULT_TEMPERATURE_THERMISTOR_MEASUREMENT_CONFIGURATION,
    DEFAULT_TEMPERATURE_THERMOCOUPLE_MEASUREMENT_CONFIGURATION,
    DEFAULT_POWER_SUPPLY_SOURCE_AND_MEASURE_CONFIGURATION,
)

# DMM Measurement
from nipcbatt import (
    DcRmsVoltageMeasurement,
    DcRmsCurrentMeasurement,
    DcRmsResistanceMeasurement,
    MixedMeasurement,
    DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION,
    DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION,
    DEFAULT_RESISTANCE_MEASUREMENT_CONFIGURATION,
    DEFAULT_MIXED_MEASUREMENT_CONFIGURATION,
)

# Switch Control
from nipcbatt import (
    StaticDigitalPathGeneration,
    StaticDigitalPathGenerationChannelParameters,
    StaticDigitalPathGenerationStateParameters,
    StaticDigitalPathGenerationTerminalAndStateSettings,
    StaticDigitalPathGenerationTimingParameters,
    StaticDigitalPathGenerationConfiguration,
)

# Communications (I2C, SPI, Serial)
from nipcbatt import (
    I2cReadCommunication,
    I2cWriteCommunication,
    SpiReadCommunication,
    SpiWriteCommunication,
    SerialCommunication,
    DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION,
    DEFAULT_I2C_WRITE_COMMUNICATION_CONFIGURATION,
    DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION,
    DEFAULT_SPI_WRITE_COMMUNICATION_CONFIGURATION,
)

# DMM Scan
from nipcbatt import (
    DmmScanPMPS,
    ScanResources,
    MeasurementResult,
)

# Common Enums and Data Types
from nipcbatt import (
    MeasurementExecutionType,
    MeasurementAnalysisRequirement,
    StartTriggerType,
    SampleTimingEngine,
    MeasurementOptions,
    SampleClockTimingParameters,
    DigitalStartTriggerParameters,
)
```

### Legacy Usage Example

```python
# Legacy (still works)
import nipcbatt

gen = nipcbatt.DcVoltageGeneration()
gen.initialize(analog_output_channel_expression="Dev1/ao0")
gen.configure_and_generate(nipcbatt.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION)
gen.close()
```
