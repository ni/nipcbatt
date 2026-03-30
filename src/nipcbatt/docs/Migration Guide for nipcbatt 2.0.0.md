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

### ❌ Old Style (Broken in 2.0.0)
```python
import nipcbatt

gen = nipcbatt.DcVoltageGeneration()
meas = nipcbatt.TimeDomainMeasurement()
dmm = nipcbatt.DcRmsVoltageMeasurement()
config = nipcbatt.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION
```

### ✅ New Style (Required in 2.0.0)
```python
from nipcbatt import daq, dmm

gen = daq.DcVoltageGeneration()
meas = daq.TimeDomainMeasurement()
dmm_meas = dmm.DcRmsVoltageMeasurement()
config = daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION
```

---

## Common Migration Patterns

### DAQmx: Generation and Measurement

| Aspect | Before (2.x) | After (2.0.0) |
|--------|------|--------|
| **Import** | `import nipcbatt` | `from nipcbatt import daq` |
| **Voltage Generation** | `nipcbatt.DcVoltageGeneration()` | `daq.DcVoltageGeneration()` |
| **Voltage Measurement** | `nipcbatt.DcRmsVoltageMeasurement()` | `daq.DcRmsVoltageMeasurement()` |
| **Default Config** | `nipcbatt.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION` | `daq.DEFAULT_DC_VOLTAGE_GENERATION_CONFIGURATION` |

### DMM Measurements

| Aspect | Before (2.x) | After (2.0.0) |
|--------|------|--------|
| **Import** | `import nipcbatt` | `from nipcbatt import dmm` |
| **Voltage Measurement** | `nipcbatt.DcRmsVoltageMeasurement()` | `dmm.DcRmsVoltageMeasurement()` |
| **Resistance Measurement** | `nipcbatt.DcRmsResistanceMeasurement()` | `dmm.DcRmsResistanceMeasurement()` |
| **Default Config** | `nipcbatt.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION` | `dmm.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION` |

### Switch and Communications

| Module | Before | After |
|--------|--------|-------|
| **Switch** | `import nipcbatt` → `nipcbatt.StaticDigitalPathGeneration()` | `from nipcbatt import switch` → `switch.StaticDigitalPathGeneration()` |
| **Communications** | `import nipcbatt` → `nipcbatt.I2cReadCommunication()` | `from nipcbatt import communications as comm` → `comm.I2cReadCommunication()` |
| **DMM Scan** | `import nipcbatt` → `nipcbatt.DmmScanPMPS()` | `from nipcbatt import dmm_scan` → `dmm_scan.DmmScanPMPS()` |

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

