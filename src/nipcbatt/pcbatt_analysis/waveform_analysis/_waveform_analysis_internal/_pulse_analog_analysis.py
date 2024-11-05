"""Private module that provides a set of helper functions 
   for nipcbatt.pcbatt_analysis.pulse_analog_analysis module."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (357 > 100 characters) (auto-generated noqa)

from collections import namedtuple
from ctypes import (
    POINTER,
    byref,
    c_char_p,
    c_double,
    c_int,
    c_size_t,
    create_string_buffer,
)

import numpy

from nipcbatt.pcbatt_analysis import analysis_library_interop
from nipcbatt.pcbatt_analysis.analysis_library_exceptions import (
    PCBATTAnalysisCallNativeLibraryFailedException,
)
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)


def labview_get_last_error_message_impl() -> str:
    """Gets last error message hold by labview Pulse Measurements VI.

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException: Occurs when native function call fails
        for some reason.

    Returns:
        str: empty string when no error occured, elsewhere not empty string.
    """
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage(
    # char* output_error_message,
    # size_t output_error_message_length)

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage.argtypes = [
            # char* output_error_message
            c_char_p,
            # size_t output_error_message_length
            c_size_t,
        ]

        string_buffer_length = 1024
        string_buffer = create_string_buffer(string_buffer_length)

        # call native code
        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage(
            string_buffer, c_size_t(string_buffer_length)
        )

        if res_status != 0:
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage"
                + f" status = {res_status}"
            )

        return str(string_buffer.value.decode())

    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_GetLastErrorMessage"
        ) from e


TuplePulseReferenceLevels = namedtuple(
    typename="PulseReferenceLevels",
    field_names=[
        "reference_level_high",
        "reference_level_middle",
        "reference_level_low",
    ],
)

TuplePulseResultsExportAll = namedtuple(
    typename="PulseResultsExportedAll",
    field_names=[
        "pulse_center",
        "pulse_duration",
        "pulse_reference_level_high",
        "pulse_reference_level_middle",
        "pulse_reference_level_low",
        "period",
        "duty_cycle",
    ],
)

TuplePulseResultsExportIgnorePeriodicity = namedtuple(
    typename="PulseResultsExportIgnorePeriodicity",
    field_names=[
        "pulse_center",
        "pulse_duration",
        "pulse_reference_level_high",
        "pulse_reference_level_middle",
        "pulse_reference_level_low",
    ],
)


def labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_all_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    pulse_number: int,
    processing_polarity: int,
    reference_levels: TuplePulseReferenceLevels,
) -> TuplePulseResultsExportAll:
    """Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        PulseResultsExportAll: Tuple gathering, exported all pulse measurement results.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll(
    # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int inputPulseNumber,
    # const double* inputWaveformSamplesArray,
    # double inputReferenceLevelHigh,
    # double inputReferenceLevelMiddle,
    # double inputReferenceLevelLow,
    # double* outputProcessedPulseCenter,
    # double* outputProcessedPulseDuration,
    # double* outputProcessedPeriod,
    # double* outputProcessedDutyCycle,
    # double* outputActualReferenceLevelHigh,
    # double* outputActualReferenceLevelMiddle,
    # double* outputActualReferenceLevelLow);

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll.argtypes = [
            # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int inputPulseNumber
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double inputReferenceLevelHigh
            c_double,
            # double outputActualReferenceLevelMiddle
            c_double,
            # double inputReferenceLevelLow
            c_double,
            # double* outputProcessedPulseCenter,
            POINTER(c_double),
            # double* outputProcessedPulseDuration,
            POINTER(c_double),
            # double* outputProcessedPeriod,
            POINTER(c_double),
            # double* outputProcessedDutyCycle,
            POINTER(c_double),
            # double* outputActualReferenceLevelHigh,
            POINTER(c_double),
            # double* outputActualReferenceLevelMiddle,
            POINTER(c_double),
            # double* outputActualReferenceLevelLow
            POINTER(c_double),
        ]

        # call native code
        output_processed_pulse_center = c_double()
        output_processed_pulse_duration = c_double()
        output_processed_period = c_double()
        output_processed_duty_cycle = c_double()
        output_actual_reference_level_high = c_double()
        output_actual_reference_level_middle = c_double()
        output_actual_reference_level_low = c_double()

        input_waveform_sampling_period = c_double(waveform_sampling_period_seconds)
        input_waveform_length = c_size_t(waveform_samples.size)
        input_waveform_samples_array = waveform_samples.ctypes.data_as(POINTER(c_double))
        input_pulse_measurement_polarity = c_int(processing_polarity)
        input_pulse_number = c_int(pulse_number)
        input_reference_level_high = c_double(reference_levels.reference_level_high)
        input_reference_level_middle = c_double(reference_levels.reference_level_middle)
        input_reference_level_low = c_double(reference_levels.reference_level_low)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll(
            input_pulse_measurement_polarity,
            input_waveform_sampling_period,
            input_waveform_length,
            input_pulse_number,
            input_waveform_samples_array,
            input_reference_level_high,
            input_reference_level_middle,
            input_reference_level_low,
            byref(output_processed_pulse_center),
            byref(output_processed_pulse_duration),
            byref(output_processed_period),
            byref(output_processed_duty_cycle),
            byref(output_actual_reference_level_high),
            byref(output_actual_reference_level_middle),
            byref(output_actual_reference_level_low),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll"
                + f" status = {res_status}, error = {error_message}"
            )

        return TuplePulseResultsExportAll(
            pulse_center=output_processed_pulse_center.value,
            pulse_duration=output_processed_pulse_duration.value,
            pulse_reference_level_high=output_actual_reference_level_high.value,
            pulse_reference_level_middle=output_actual_reference_level_middle.value,
            pulse_reference_level_low=output_actual_reference_level_low.value,
            period=output_processed_period.value,
            duty_cycle=output_processed_duty_cycle.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll"
        ) from e


def labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_all_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    pulse_number: int,
    processing_polarity: int,
    amplitude_and_levels_processing_method: int,
    amplitude_and_levels_processing_histogram_size: int,
    reference_levels: TuplePulseReferenceLevels,
) -> TuplePulseResultsExportAll:
    """Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        PulseResultsExportAll: Tuple gathering, exported all pulse measurement results.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll(
    # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod,
    # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int inputPulseNumber,
    # int inputHistogramSize,
    # const double* inputWaveformSamplesArray,
    # double inputReferenceLevelHigh,
    # double inputReferenceLevelMiddle,
    # double inputReferenceLevelLow,
    # double* outputProcessedPulseCenter,
    # double* outputProcessedPulseDuration,
    # double* outputProcessedPeriod,
    # double* outputProcessedDutyCycle,
    # double* outputActualReferenceLevelHigh,
    # double* outputActualReferenceLevelMiddle,
    # double* outputActualReferenceLevelLow);

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll.argtypes = [
            # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod
            c_int,
            # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int inputPulseNumber
            c_int,
            # int inputHistogramSize,
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double inputReferenceLevelHigh
            c_double,
            # double outputActualReferenceLevelMiddle
            c_double,
            # double inputReferenceLevelLow
            c_double,
            # double* outputProcessedPulseCenter,
            POINTER(c_double),
            # double* outputProcessedPulseDuration,
            POINTER(c_double),
            # double* outputProcessedPeriod,
            POINTER(c_double),
            # double* outputProcessedDutyCycle,
            POINTER(c_double),
            # double* outputActualReferenceLevelHigh,
            POINTER(c_double),
            # double* outputActualReferenceLevelMiddle,
            POINTER(c_double),
            # double* outputActualReferenceLevelLow
            POINTER(c_double),
        ]

        # call native code
        output_processed_pulse_center = c_double()
        output_processed_pulse_duration = c_double()
        output_processed_period = c_double()
        output_processed_duty_cycle = c_double()
        output_actual_reference_level_high = c_double()
        output_actual_reference_level_middle = c_double()
        output_actual_reference_level_low = c_double()

        input_waveform_sampling_period = c_double(waveform_sampling_period_seconds)
        input_waveform_length = c_size_t(waveform_samples.size)
        input_waveform_samples_array = waveform_samples.ctypes.data_as(POINTER(c_double))
        input_amplitude_and_levels_processing_method = c_int(amplitude_and_levels_processing_method)
        input_histogram_size = c_int(amplitude_and_levels_processing_histogram_size)
        input_pulse_measurement_polarity = c_int(processing_polarity)
        input_pulse_number = c_int(pulse_number)
        input_reference_level_high = c_double(reference_levels.reference_level_high)
        input_reference_level_middle = c_double(reference_levels.reference_level_middle)
        input_reference_level_low = c_double(reference_levels.reference_level_low)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll(
            input_amplitude_and_levels_processing_method,
            input_pulse_measurement_polarity,
            input_waveform_sampling_period,
            input_waveform_length,
            input_pulse_number,
            input_histogram_size,
            input_waveform_samples_array,
            input_reference_level_high,
            input_reference_level_middle,
            input_reference_level_low,
            byref(output_processed_pulse_center),
            byref(output_processed_pulse_duration),
            byref(output_processed_period),
            byref(output_processed_duty_cycle),
            byref(output_actual_reference_level_high),
            byref(output_actual_reference_level_middle),
            byref(output_actual_reference_level_low),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll"
                + f" status = {res_status}, error = {error_message}"
            )

        return TuplePulseResultsExportAll(
            pulse_center=output_processed_pulse_center.value,
            pulse_duration=output_processed_pulse_duration.value,
            pulse_reference_level_high=output_actual_reference_level_high.value,
            pulse_reference_level_middle=output_actual_reference_level_middle.value,
            pulse_reference_level_low=output_actual_reference_level_low.value,
            period=output_processed_period.value,
            duty_cycle=output_processed_duty_cycle.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll"
        ) from e


def labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_no_periodicity_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    pulse_number: int,
    processing_polarity: int,
    reference_levels: TuplePulseReferenceLevels,
) -> TuplePulseResultsExportIgnorePeriodicity:
    """Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        PulseResultsExportAll: Tuple gathering, exported all pulse measurement results.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels_ExportAll(
    # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int inputPulseNumber,
    # const double* inputWaveformSamplesArray,
    # double inputReferenceLevelHigh,
    # double inputReferenceLevelMiddle,
    # double inputReferenceLevelLow,
    # double* outputProcessedPulseCenter,
    # double* outputProcessedPulseDuration,
    # double* outputActualReferenceLevelHigh,
    # double* outputActualReferenceLevelMiddle,
    # double* outputActualReferenceLevelLow);

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels.argtypes = [
            # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int inputPulseNumber
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double inputReferenceLevelHigh
            c_double,
            # double outputActualReferenceLevelMiddle
            c_double,
            # double inputReferenceLevelLow
            c_double,
            # double* outputProcessedPulseCenter,
            POINTER(c_double),
            # double* outputProcessedPulseDuration,
            POINTER(c_double),
            # double* outputActualReferenceLevelHigh,
            POINTER(c_double),
            # double* outputActualReferenceLevelMiddle,
            POINTER(c_double),
            # double* outputActualReferenceLevelLow
            POINTER(c_double),
        ]

        # call native code
        output_processed_pulse_center = c_double()
        output_processed_pulse_duration = c_double()
        output_actual_reference_level_high = c_double()
        output_actual_reference_level_middle = c_double()
        output_actual_reference_level_low = c_double()

        input_waveform_sampling_period = c_double(waveform_sampling_period_seconds)
        input_waveform_length = c_size_t(waveform_samples.size)
        input_waveform_samples_array = waveform_samples.ctypes.data_as(POINTER(c_double))
        input_pulse_measurement_polarity = c_int(processing_polarity)
        input_pulse_number = c_int(pulse_number)
        input_reference_level_high = c_double(reference_levels.reference_level_high)
        input_reference_level_middle = c_double(reference_levels.reference_level_middle)
        input_reference_level_low = c_double(reference_levels.reference_level_low)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels(
            input_pulse_measurement_polarity,
            input_waveform_sampling_period,
            input_waveform_length,
            input_pulse_number,
            input_waveform_samples_array,
            input_reference_level_high,
            input_reference_level_middle,
            input_reference_level_low,
            byref(output_processed_pulse_center),
            byref(output_processed_pulse_duration),
            byref(output_actual_reference_level_high),
            byref(output_actual_reference_level_middle),
            byref(output_actual_reference_level_low),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels"
                + f" status = {res_status}, error = {error_message}"
            )

        return TuplePulseResultsExportIgnorePeriodicity(
            pulse_center=output_processed_pulse_center.value,
            pulse_duration=output_processed_pulse_duration.value,
            pulse_reference_level_high=output_actual_reference_level_high.value,
            pulse_reference_level_middle=output_actual_reference_level_middle.value,
            pulse_reference_level_low=output_actual_reference_level_low.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Absolute_ReferenceLevels"
        ) from e


def labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_no_periodicity_impl(
    waveform_samples: numpy.ndarray[numpy.float64],
    waveform_sampling_period_seconds: float,
    pulse_number: int,
    processing_polarity: int,
    amplitude_and_levels_processing_method: int,
    amplitude_and_levels_processing_histogram_size: int,
    reference_levels: TuplePulseReferenceLevels,
) -> TuplePulseResultsExportIgnorePeriodicity:
    """Invokes native library Pulse Measurements processing LabVIEW VI

    Raises:
        PCBATTAnalysisCallNativeLibraryFailedException:
            Occurs when native dll call fails for some reason.

    Returns:
        TuplePulseResultsExportIgnorePeriodicity: Tuple gathering, exported all pulse measurement results.
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (106 > 100 characters) (auto-generated noqa)
    # Create native code DLL call
    # int PCBATT_INTEROP_API __cdecl
    # NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels_ExportAll(
    # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod,
    # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity,
    # double inputWaveformSamplingPeriod,
    # size_t inputWaveformSamplesArrayLength,
    # int inputPulseNumber,
    # int inputHistogramSize,
    # const double* inputWaveformSamplesArray,
    # double inputReferenceLevelHigh,
    # double inputReferenceLevelMiddle,
    # double inputReferenceLevelLow,
    # double* outputProcessedPulseCenter,
    # double* outputProcessedPulseDuration,
    # double* outputActualReferenceLevelHigh,
    # double* outputActualReferenceLevelMiddle,
    # double* outputActualReferenceLevelLow);

    try:
        dll_entries = analysis_library_interop.load_interop_api_library_entries()
        # specify signature
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels.restype = (
            c_int
        )
        dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels.argtypes = [
            # AmplitudeAndLevelsProcessingMethodEnum inputAmplitudeAndLevelsProcessingMethod
            c_int,
            # PulseAnalogMeasurementPolarityEnum inputPulseMeasurementPolarity
            c_int,
            # double inputWaveformSamplingPeriod
            c_double,
            # size_t inputWaveformSamplesArrayLength
            c_size_t,
            # int inputPulseNumber
            c_int,
            # int inputHistogramSize,
            c_int,
            # const double* inputWaveformSamplesArray
            POINTER(c_double),
            # double inputReferenceLevelHigh
            c_double,
            # double outputActualReferenceLevelMiddle
            c_double,
            # double inputReferenceLevelLow
            c_double,
            # double* outputProcessedPulseCenter,
            POINTER(c_double),
            # double* outputProcessedPulseDuration,
            POINTER(c_double),
            # double* outputActualReferenceLevelHigh,
            POINTER(c_double),
            # double* outputActualReferenceLevelMiddle,
            POINTER(c_double),
            # double* outputActualReferenceLevelLow
            POINTER(c_double),
        ]

        # call native code
        output_processed_pulse_center = c_double()
        output_processed_pulse_duration = c_double()
        output_actual_reference_level_high = c_double()
        output_actual_reference_level_middle = c_double()
        output_actual_reference_level_low = c_double()

        input_waveform_sampling_period = c_double(waveform_sampling_period_seconds)
        input_waveform_length = c_size_t(waveform_samples.size)
        input_waveform_samples_array = waveform_samples.ctypes.data_as(POINTER(c_double))
        input_amplitude_and_levels_processing_method = c_int(amplitude_and_levels_processing_method)
        input_histogram_size = c_int(amplitude_and_levels_processing_histogram_size)
        input_pulse_measurement_polarity = c_int(processing_polarity)
        input_pulse_number = c_int(pulse_number)
        input_reference_level_high = c_double(reference_levels.reference_level_high)
        input_reference_level_middle = c_double(reference_levels.reference_level_middle)
        input_reference_level_low = c_double(reference_levels.reference_level_low)

        res_status = dll_entries.NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels(
            input_amplitude_and_levels_processing_method,
            input_pulse_measurement_polarity,
            input_waveform_sampling_period,
            input_waveform_length,
            input_pulse_number,
            input_histogram_size,
            input_waveform_samples_array,
            input_reference_level_high,
            input_reference_level_middle,
            input_reference_level_low,
            byref(output_processed_pulse_center),
            byref(output_processed_pulse_duration),
            byref(output_actual_reference_level_high),
            byref(output_actual_reference_level_middle),
            byref(output_actual_reference_level_low),
        )

        if res_status != 0:
            error_message = labview_get_last_error_message_impl()
            raise PCBATTAnalysisCallNativeLibraryFailedException(
                message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
                + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels"
                + f" status = {res_status}, error = {error_message}"
            )

        return TuplePulseResultsExportIgnorePeriodicity(
            pulse_center=output_processed_pulse_center.value,
            pulse_duration=output_processed_pulse_duration.value,
            pulse_reference_level_high=output_actual_reference_level_high.value,
            pulse_reference_level_middle=output_actual_reference_level_middle.value,
            pulse_reference_level_low=output_actual_reference_level_low.value,
        )
    except Exception as e:
        raise PCBATTAnalysisCallNativeLibraryFailedException(
            message=f"{AnalysisLibraryExceptionMessage.NATIVE_LIBRARY_FUNCTION_CALL_FAILED}:"
            + "NI_PCBATT_InteropApi_LabVIEW_Analysis_ProcessSingleWaveformPulseAnalogMeasurement_Relative_ReferenceLevels"
        ) from e
