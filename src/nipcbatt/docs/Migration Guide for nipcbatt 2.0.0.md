# Migration Guide for nipcbatt 2.0.0

## Overview: Breaking Change in 2.0.0

nipcbatt 2.0.0 introduces a **breaking change**: all classes must now be imported from **instrument-specific subpackages** instead of the top-level `nipcbatt` namespace.

### Organization by Instrument Type
- **`nipcbatt.daq`** — DAQmx-based generation/measurement (voltage, digital, temperature)
- **`nipcbatt.dmm`** — NI-DMM digital multimeter measurements
- **`nipcbatt.switch`** — NI-SWITCH relay control
- **`nipcbatt.dmm_scan`** — Multi-channel DMM + SWITCH scanning
- **`nipcbatt.communications`** — I2C, SPI, Serial communication

This change makes dependencies explicit and prevents naming conflicts.

---

## Quick Migration: Before and After

### ❌ Old format (Broken in 2.x)
```python
import nipcbatt

gen = nipcbatt.DcVoltageGeneration()
meas = nipcbatt.TimeDomainMeasurement()
dmm = nipcbatt.DcRmsVoltageMeasurement()
config = nipcbatt.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION
```

### ✅ Fix Required (2.x Onwards)
```python
from nipcbatt import daq, dmm

gen = daq.DcVoltageGeneration()
meas = daq.TimeDomainMeasurement()
dmm_meas = dmm.DcRmsVoltageMeasurement()
config = daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION
```

---

## Common Migration Patterns

### DAQ: Generation and Measurement

| Module | Before 2.x | 2.x Onwards |
|--------|------|--------|
| **Import** | `import nipcbatt` | `from nipcbatt import daq` |
| **DC Voltage Generation** | `nipcbatt.DcVoltageGeneration()` | `daq.DcVoltageGeneration()` |
| **Signal Voltage Generation** | `nipcbatt.SignalVoltageGeneration()` | `daq.SignalVoltageGeneration()` |
| **DC RMS Voltage Measurement** | `nipcbatt.DcRmsVoltageMeasurement()` | `daq.DcRmsVoltageMeasurement()` |
| **DC RMS Current Measurement** | `nipcbatt.DcRmsCurrentMeasurement()` | `daq.DcRmsCurrentMeasurement()` |
| **Time Domain Measurement** | `nipcbatt.TimeDomainMeasurement()` | `daq.TimeDomainMeasurement()` |
| **Frequency Domain Measurement** | `nipcbatt.FrequencyDomainMeasurement()` | `daq.FrequencyDomainMeasurement()` |
| **Temperature Measurement** | `nipcbatt.TemperatureMeasurement()` | `daq.TemperatureMeasurement()` |
| **Power Supply Source and Measure** | `nipcbatt.PowerSupplySourceAndMeasure()` | `daq.PowerSupplySourceAndMeasure()` |
| **Digital PWM Measurement** | `nipcbatt.DigitalPwmMeasurement()` | `daq.DigitalPwmMeasurement()` |
| **Digital Clock Generation** | `nipcbatt.DigitalClockGeneration()` | `daq.DigitalClockGeneration()` |
| **Digital Pulse Generation** | `nipcbatt.DigitalPulseGeneration()` | `daq.DigitalPulseGeneration()` |
| **Static Digital State Generation** | `nipcbatt.StaticDigitalStateGeneration()` | `daq.StaticDigitalStateGeneration()` |
| **Static Digital State Measurement** | `nipcbatt.StaticDigitalStateMeasurement()` | `daq.StaticDigitalStateMeasurement()` |
| **Dynamic Digital Pattern Generation** | `nipcbatt.DynamicDigitalPatternGeneration()` | `daq.DynamicDigitalPatternGeneration()` |
| **Dynamic Digital Pattern Measurement** | `nipcbatt.DynamicDigitalPatternMeasurement()` | `daq.DynamicDigitalPatternMeasurement()` |
| **Default Config** | `nipcbatt.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION` | `daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION` |


### Communications: I2C, SPI, and Serial

| Module | Before 2.x | 2.x Onwards |
|--------|------|--------|
| **Import** | `import nipcbatt` | `from nipcbatt import communications as comm` |
| **I2C Read** | `nipcbatt.I2cReadCommunication()` | `comm.I2cReadCommunication()` |
| **I2C Write** | `nipcbatt.I2cWriteCommunication()` | `comm.I2cWriteCommunication()` |
| **SPI Read** | `nipcbatt.SpiReadCommunication()` | `comm.SpiReadCommunication()` |
| **SPI Write** | `nipcbatt.SpiWriteCommunication()` | `comm.SpiWriteCommunication()` |
| **Serial** | `nipcbatt.SerialCommunication()` | `comm.SerialCommunication()` |
| **I2C Default Config** | `nipcbatt.DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION` | `comm.DEFAULT_I2C_READ_COMMUNICATION_CONFIGURATION` |
| **SPI Default Config** | `nipcbatt.DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION` | `comm.DEFAULT_SPI_READ_COMMUNICATION_CONFIGURATION` |

---

## What Still Works: Backward Compatibility Exceptions

Some core utilities and exceptions remain directly accessible from `nipcbatt` for backward compatibility, for example:

```python
from nipcbatt import (
    # Core exceptions (still available)
    PCBATTLibraryException,
    PCBATTAnalysisException,
    PCBATTCommunicationException,
    
    # Core data types (still available)
    PCBATestToolkitData,
    MeasurementOptions,
    MeasurementExecutionType,
    MeasurementAnalysisRequirement,
    
    # Building blocks (still available)
    BuildingBlockUsingDAQmx,
    BuildingBlockUsingInstrument,
    BuildingBlockUsingVisa,
)
```

However, **all measurement, generation, and communication classes MUST use instrument-specific imports.** refer "src\nipcbatt\__init__.py" for more info on available methods from nipcbatt.

---

## Best Practices

1. **Use explicit module imports** to make dependencies clear
2. **Use module aliases** for readability: `from nipcbatt import communications as comm`
3. **Handle name collisions** explicitly: `daq.DcRmsVoltageMeasurement()` vs. `dmm.DcRmsVoltageMeasurement()`
4. **Group related imports** for organization
5. **Never use** `from nipcbatt.daq import *` — be explicit about what you import

---

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `ImportError: cannot import name 'DcVoltageGeneration' from 'nipcbatt'` | Using top-level import | Use `from nipcbatt.daq import DcVoltageGeneration` |
| `AttributeError: module 'nipcbatt' has no attribute 'DcRmsVoltageMeasurement'` | Wrong import path | Use `from nipcbatt import daq` then `daq.DcRmsVoltageMeasurement()` |
| Cannot find configuration constant | Constants moved to submodules | Use `daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION` |
| Name collision between `daq` and `dmm` versions | Same class name in multiple modules | Be explicit: `daq.DcRmsVoltageMeasurement()` vs. `dmm.DcRmsVoltageMeasurement()` |

---

## Import Reference

```python
# DAQmx
from nipcbatt import daq
gen = daq.DcVoltageGeneration()
meas = daq.TimeDomainMeasurement()

# DMM
from nipcbatt import dmm
volt_meas = dmm.DcRmsVoltageMeasurement()
res_meas = dmm.DcRmsResistanceMeasurement()

# Switch
from nipcbatt import switch
relay = switch.StaticDigitalPathGeneration()

# Communications
from nipcbatt import communications as comm
i2c = comm.I2cReadCommunication()
serial = comm.SerialCommunication()

# DMM Scan
from nipcbatt import dmm_scan
scan = dmm_scan.DmmScanPMPS()
```

---

## Migration Checklist

- Update all `import nipcbatt` to `from nipcbatt import <module>`
- Update all class instantiations to use module prefix
- Update all default configuration imports
- Verify backward-compatible exceptions still import from `nipcbatt`

