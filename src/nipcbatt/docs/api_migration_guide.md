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

# Generation
gen = daq.DcVoltageGeneration()
gen.initialize(analog_output_channel_expression="Dev1/ao0")
gen.configure_and_generate(daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION)
gen.close()

# Measurement
meas = daq.DcVoltageMeasurement()
meas.initialize(analog_input_channel_expression="Dev1/ai0")
result = meas.configure_and_measure(daq.DEFAULT_DC_VOLTAGE_MEASUREMENT_CONFIGURATION)
meas.close()
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

meas = dmm.DcRmsVoltageMeasurement()
meas.initialize(resource_name="DMM1", powerline_frequency=50)
params = dmm.DcRmsVoltageMeasurementFunctionParameters(
    range_value=dmm.DcRmsVoltageRange.DC_10V,
    resolution=dmm.ResolutionInDigits.DIGITS_5_5
)
meas.configure_measurement_function(params)
result = meas.acquire_measurement()
meas.close()
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

gen = switch.StaticDigitalPathGeneration()
gen.initialize(resource_name="Switch1", topology_name="2527/2-Wire Dual 16x1 Mux")

params = switch.StaticDigitalPathGenerationChannelParameters("ch0", "com0")
state = switch.StaticDigitalPathGenerationStateParameters(True)  # True = close
settings = switch.StaticDigitalPathGenerationTerminalAndStateSettings(params, state)
timing = switch.StaticDigitalPathGenerationTimingParameters()
config = switch.StaticDigitalPathGenerationConfiguration(settings, timing)

gen.configure_and_generate(config)
gen.close()
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
from nipcbatt import dmm_scan

scanner = dmm_scan.DmmScanPMPS()
resources = scanner.initialize(
    mux_resource_name="Sim_MUX",
    shunt_resource_name="Sim_SHUNT",
    dmm_resource_name="Sim_DMM",
    close_all_shunts=True
)

# Define scan points: (channel, measurement_function, resolution)
scan_config = [
    (0, dmm_scan.MixedMeasurementFunction.DC_VOLTS, dmm_scan.ResolutionInDigits.DIGITS_5_5),
    (1, dmm_scan.MixedMeasurementFunction.DC_VOLTS, dmm_scan.ResolutionInDigits.DIGITS_5_5),
]

result = scanner.configure_and_measure(resources, scan_config, verbose=True)
scanner.close(resources)
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

**Usage Example**
```python
from nipcbatt.pcbatt_library.communications import i2c

reader = i2c.I2cReadCommunication()
reader.initialize(resource_name="PXI1Slot2", visa_resource_class="TCPIP")
config = i2c.DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION
result = reader.configure_and_communicate(config)
reader.close()
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
