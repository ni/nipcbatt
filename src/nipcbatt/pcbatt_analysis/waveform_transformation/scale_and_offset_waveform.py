"""Provides scale and offset waveform transformation API."""

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.waveform_transformation._waveform_transformation_internal import (
    _scale_and_offset_waveform,
)
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def scale(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a scale factor to given waveform samples, and returns new samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: new samples constituting transformed waveform.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    Guard.is_greater_than_zero(scale_factor, nameof(scale_factor))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_impl(
            waveform_samples, scale_factor, 0
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def apply_offset(
    waveform_samples: numpy.ndarray[numpy.float64], offset: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a vertical offset to given waveform samples, and returns new samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.

    Returns:
        numpy.ndarray[numpy.float64]: new samples constituting transformed waveform.
    """  # noqa: D202 - No blank lines allowed after function docstring (auto-generated noqa)

    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_impl(waveform_samples, 1, offset)
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def scale_inplace(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a scale factor to given waveform samples, and returns modified samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: modified input samples constituting transformed waveform.
    """
    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    Guard.is_greater_than_zero(scale_factor, nameof(scale_factor))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_inplace_impl(
            waveform_samples, scale_factor, 0
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def apply_offset_inplace(
    waveform_samples: numpy.ndarray[numpy.float64], offset: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a vertical offset to given waveform samples, and returns modified samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: modified input samples constituting transformed waveform.
    """
    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_inplace_impl(
            waveform_samples, 1, offset
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def scale_and_apply_offset(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a scale factor and vertical offset to given waveform samples,
    and returns new samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: new samples constituting transformed waveform.
    """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (283 > 100 characters) (auto-generated noqa)

    Guard.is_not_none(waveform_samples, nameof(waveform_samples))
    Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
    Guard.is_greater_than_zero(scale_factor, nameof(scale_factor))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_impl(
            waveform_samples, scale_factor, offset
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e


def scale_and_apply_offset_inplace(
    waveform_samples: numpy.ndarray[numpy.float64], scale_factor: float, offset: float
) -> numpy.ndarray[numpy.float64]:
    """Applies a scale factor and vertical offset to given waveform samples,
    and returns modified samples.

    Raises:
        PCBATTAnalysisException: occurs when waveform transformation fails for some reason.
        ValueError: occurs when `scale_factor` is less or equal zero.

    Returns:
        numpy.ndarray[numpy.float64]: modified input samples constituting transformed waveform.
    """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (283 > 100 characters) (auto-generated noqa)

    Guard.is_not_none(instance=waveform_samples, instance_name=nameof(waveform_samples))
    Guard.is_not_empty(iterable_instance=waveform_samples, instance_name=nameof(waveform_samples))
    Guard.is_greater_than_zero(scale_factor, nameof(scale_factor))
    try:
        return _scale_and_offset_waveform.scale_and_apply_offset_inplace_impl(
            waveform_samples, scale_factor, offset
        )
    except Exception as e:
        raise PCBATTAnalysisException(
            AnalysisLibraryExceptionMessage.SCALE_OFFSET_WAVEFORM_TRANSFORMATION_FAILED_FOR_SOME_REASON
        ) from e
