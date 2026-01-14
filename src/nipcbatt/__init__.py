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
# results = measurement.configure_and_measure(configuration=nipcbatt.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION)  # noqa: W505 - doc line too long (118 > 100 characters) (auto-generated noqa)
# measurement.close()

from nipcbatt.pcbatt_library import daq 
from nipcbatt.pcbatt_library import dmm

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
    PCBATTAnalysisException,
    PCBATTAnalysisLoadNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
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
from nipcbatt.pcbatt_library.common.voltage_constants import (
    ConstantsForVoltageMeasurement,
)
from nipcbatt.pcbatt_library.common.voltage_data_types import (
    VoltageGenerationChannelParameters,
    VoltageMeasurementChannelAndTerminalRangeParameters,
    VoltageRangeAndTerminalParameters,
)

from nipcbatt.pcbatt_library_core.daq.pcbatt_building_blocks import (
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
from nipcbatt.pcbatt_library_core.pcbatt_library_messages import (
    PCBATTLibraryExceptionMessages,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard
