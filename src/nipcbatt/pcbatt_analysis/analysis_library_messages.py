"""Defines analysis library different kinds of messages."""

import dataclasses


@dataclasses.dataclass
class AnalysisLibraryExceptionMessage:
    """Defines analysis library exceptions messages content."""

    NATIVE_LIBRARY_LOAD_FAILED = "Failed to load native library"
    NATIVE_LIBRARY_FUNCTION_CALL_FAILED = "Failed to call function of native library"
    NATIVE_LIBRARY_IS_MISSING = "Native libray element is missing"
    NATIVE_INTEROP_IS_NOT_SUPPORTED_ON_CURRENT_PLATFORM = (
        "Native interop is not supported for current platform"
    )

    DC_RMS_PROCESSING_FAILED_FOR_SOME_REASON = "DC-RMS processing failed for some reason!"

    AMPLITUDE_AND_LEVELS_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Amplitude and levels processing failed for some reason!"
    )

    AMPLITUDE_AND_PHASE_SPECTRUM_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Amplitude and phase spectrum processing failed for some reason!"
    )

    FREQUENCY_DOMAIN_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Frequency domain processing failed for some reason!"
    )

    MULTIPLE_TONES_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Multiple tones processing failed for some reason!"
    )

    PULSE_MEASUREMENTS_PROCESSING_FAILED_FOR_SOME_REASON = (
        "Pulse measurements processing failed for some reason!"
    )

    PULSE_MEASUREMENTS_PROCESSING_REFERENCE_LEVELS_UNIT_IS_NOT_SUPPORTED = (
        "Pulse measurements processing does not support selected reference levels unit!"
    )

    PULSE_MEASUREMENTS_PROCESSING_REFERENCE_LEVELS_UNIT_PERCENT_REQUIRES_STATES_SETTINGS = (
        "Pulse measurements processing using reference levels in percent requires states settings!"
    )

    SINE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON = "Sine waveform creation failed for some reason!"

    SQUARE_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON = (
        "Square waveform creation failed for some reason!"
    )

    MULTIPLE_TONES_WAVEFORM_CREATION_FAILED_FOR_SOME_REASON = (
        "Multi-tones waveform creation failed for some reason!"
    )

    SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON = (
        "Scale and offset waveform transformations failed for some reason!"
    )
