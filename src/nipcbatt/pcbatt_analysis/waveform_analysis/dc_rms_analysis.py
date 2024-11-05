"""Provides DC-RMS analysis tools"""

from enum import IntEnum
from typing import Iterable

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.waveform_analysis._waveform_analysis_internal import (
    _dc_rms_analysis,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DcRmsProcessingResult(AnalysisLibraryElement):
    """Defines DC-RMS processing results"""

    def __init__(self, dc_value: float, rms_value: float) -> None:
        """Initialize an instance of DC-RMS processing result.

        Args:
            dc_value (float): DC value obtained after processing waveform.
            rms_value (float): RMS value obtained after processing waveform.
        """
        self._dc_value = dc_value
        self._rms_value = rms_value

    @property
    def dc_value(self) -> float:
        """Gets DC value obtained after processing waveform.

        Returns:
            float: DC value.
        """
        return self._dc_value

    @property
    def rms_value(self) -> float:
        """Gets RMS value obtained after processing waveform.

        Returns:
            float: RMS value.
        """
        return self._rms_value


class DcRmsProcessingWindow(IntEnum):
    """Defines DC-RMS processing window"""

    RECTANGULAR = 0
    """No windows is applied."""

    HANN = 1
    """Hann window is applied."""

    LOW_SIDE_LOBE = 2
    """Low side lobe window is applied, see LabVIEW documentation for more details."""


class LabViewBasicDcRms(AnalysisLibraryElement):
    """Provides DC-RMS processing based on LabVIEW Basic DC-RMS VI"""

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occured error of
        DC-RMS processing labview VI.

        Returns:
            str: Empty string when no error occured, elsewhere not empty string.
        """
        return _dc_rms_analysis.labview_get_last_error_message_impl()

    @staticmethod
    def process_single_waveform_dc_rms(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        dc_rms_processing_window: DcRmsProcessingWindow,
    ) -> DcRmsProcessingResult:
        """Processes DC-RMS of a given waveform samples using LabVIEW VI.

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): single waveform samples.
            waveforms_sampling_period_seconds (float): sampling rate of the single waveform.
            dc_rms_processing_window (DcRmsProcessingWindow): DC-RMS processing window.

        Returns:
            DcRmsProcessingResult: An object that holds result of DC-RMS
            processing result using LabVIEW VI.
        """

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        try:
            tuple_result = _dc_rms_analysis.labview_process_single_waveform_dc_rms_impl(
                waveform_samples,
                waveform_sampling_period_seconds,
                dc_rms_processing_window,
            )

            # Build object from tuple
            return DcRmsProcessingResult(tuple_result[0], tuple_result[1])
        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.DC_RMS_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e

    @staticmethod
    def process_multiple_waveforms_dc_rms(
        waveforms_samples: Iterable[numpy.ndarray[numpy.float64]],
        waveforms_sampling_period_seconds: float,
        dc_rms_processing_window: DcRmsProcessingWindow,
    ) -> Iterable[DcRmsProcessingResult]:
        """Processes DC-RMS of given waveforms samples provided as iterable object using LabVIEW VI

        Args:
            waveforms_samples (Iterable[numpy.ndarray[numpy.float64]]): iterable of single waveforms
            waveforms_sampling_period_seconds (float): common sampling rate of all waveforms
            dc_rms_processing_window (DcRmsProcessingWindow): DC-RMS processing window

        Returns:
            Iterable[DcRmsProcessingResult]: An iterable of objects that hold result of
            DC-RMS processing of each input waveform using LabVIEW VI.
        """

        Guard.is_not_none(waveforms_samples, nameof(waveforms_samples))
        Guard.is_greater_than_zero(
            waveforms_sampling_period_seconds, nameof(waveforms_sampling_period_seconds)
        )
        for waveform_samples in waveforms_samples:
            yield LabViewBasicDcRms.process_single_waveform_dc_rms(
                waveform_samples,
                waveforms_sampling_period_seconds,
                dc_rms_processing_window,
            )
