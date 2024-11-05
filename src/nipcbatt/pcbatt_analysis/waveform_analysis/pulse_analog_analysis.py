"""Provides pulse analog analysis tools"""

from enum import IntEnum
from typing import Iterable, Optional

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.analysis_library_exceptions import PCBATTAnalysisException
from nipcbatt.pcbatt_analysis.analysis_library_messages import (
    AnalysisLibraryExceptionMessage,
)
from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_analysis.waveform_analysis._waveform_analysis_internal import (
    _pulse_analog_analysis,
)
from nipcbatt.pcbatt_analysis.waveform_analysis.amplitude_and_levels_analysis import (
    AmplitudeAndLevelsProcessingMethod,
)
from nipcbatt.pcbatt_utilities import numeric_utilities
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class WaveformPeriodicityAnalogProcessingResult(AnalysisLibraryElement):
    """Defines pulse periodicity related measurements analog processing results"""

    def __init__(self, period: float, duty_cycle: float) -> None:
        """Initialize an instance of waveform periodicty processing result.

        Args:
            period (float): period value obtained after processing waveform.
            duty_cycle (float): duty cycle value obtained after processing waveform,
                expressed as ratio [0,1].
        """
        Guard.is_greater_than_zero(period, nameof(period))
        Guard.is_greater_than_or_equal_to_zero(duty_cycle, nameof(duty_cycle))

        self._period = period
        self._duty_cycle = duty_cycle

    @property
    def period(self) -> float:
        """Gets period value obtained after processing waveform.

        Returns:
            float: period value.
        """
        return self._period

    @property
    def frequency(self) -> float:
        """Gets frequency value obtained after processing waveform.

        Returns:
            float: period value.
        """
        return numeric_utilities.invert_value(self._period)

    @property
    def duty_cycle(self) -> float:
        """Gets duty cycle value obtained after processing waveform expressed as ratio in [0,1].

        Returns:
            float: duty cycle ratio value.
        """
        return self._duty_cycle

    @property
    def duty_cycle_percent(self) -> float:
        """Gets duty cycle value obtained after processing waveform expressed as percentage.

        Returns:
            float: duty cycle ratio value.
        """
        return self._duty_cycle * 100


class PulseAnalogProcessingResult(AnalysisLibraryElement):
    """Defines pulse measurements analog processing results"""

    def __init__(
        self,
        pulse_center: float,
        pulse_duration: float,
        pulse_reference_level_high: float,
        pulse_reference_level_middle: float,
        pulse_reference_level_low: float,
        period: float = None,
        duty_cycle: float = None,
    ) -> None:
        """Initialize an instance of pulse analog processing result.

        Args:
            pulse_center (float): pulse center is defined as (Tr+Tf)/2
            pulse_duration (float): pulse duration is the time difference in seconds between
                the first two mid ref level crossings of the analyzed pulse,
                pulse duration is also known as pulse width.
            pulse_reference_level_high (float):
                absolute high reference level used to evaluate pulse center.
            pulse_reference_level_middle (float):
                absolute middle reference level used to evaluate pulse center.
            pulse_reference_level_low (float):
                absolute low reference level used to evaluate pulse center.
            period (float, optional):
                time between adjacent mid ref level crossings the same direction in seconds.
                Defaults to None.
            duty_cycle (float, optional): fraction of period according to analyzed pulse.
                Defaults to None.
        """

        Guard.is_greater_than_or_equal_to_zero(pulse_duration, nameof(pulse_duration))

        self._pulse_center = pulse_center
        self._pulse_duration = pulse_duration
        self._pulse_reference_level_high = pulse_reference_level_high
        self._pulse_reference_level_middle = pulse_reference_level_middle
        self._pulse_reference_level_low = pulse_reference_level_low

        if duty_cycle is not None and period is not None:
            self._periodicity_processing_result = WaveformPeriodicityAnalogProcessingResult(
                period, duty_cycle
            )
        else:
            self._periodicity_processing_result = None

    @property
    def pulse_center(self) -> float:
        """Gets center date obtained after processing waveform pulse.

        Returns:
            float: Pulse center date expressed in seconds.
        """
        return self._pulse_center

    @property
    def pulse_duration(self) -> float:
        """Gets pulse width obtained after processing waveform pulse.

        Returns:
            float: Pulse width expressed in seconds.
        """
        return self._pulse_duration

    @property
    def pulse_reference_level_high(self) -> float:
        """Gets high reference level used when processed waveform pulse.

        Returns:
            float: High reference level value.
        """
        return self._pulse_reference_level_high

    @property
    def pulse_reference_level_middle(self) -> float:
        """Gets middle reference level used when processed waveform pulse.

        Returns:
            float: Middle reference level value.
        """
        return self._pulse_reference_level_middle

    @property
    def pulse_reference_level_low(self) -> float:
        """Gets low reference level used when processed waveform pulse.

        Returns:
            float: Low reference level value.
        """
        return self._pulse_reference_level_low

    @property
    def waveform_periodicity_processing_result(
        self,
    ) -> Optional[WaveformPeriodicityAnalogProcessingResult]:
        """Gets periodicity analysis results obtained when processed waveform pulses, can be None.

        Returns:
            Optional[WaveformPeriodicityAnalogProcessingResult]:
                periodicity analysis results obtained when processed waveform
        """
        return self._periodicity_processing_result


class PulseAnalogProcessingPolarity(IntEnum):
    """Defines pulse analog processing polarity."""

    LOW = 0
    """Pulse state is defined by low level."""

    HIGH = 1
    """Pulse state is defined by high level."""


class PulseAnalogProcessingReferenceLevelsUnit(IntEnum):
    """Defines pulse analog processing reference levels unit."""

    ABSOLUTE = 0
    """The waveform level is an absolute value, for example, 5V."""

    RELATIVE_PERCENT = 1
    """The waveform level is a relative value, for example, 
        90% of maximum value contained in waveform."""


class PulseAnalogProcessingExportMode(IntEnum):
    """Defines labview pulse processing export mode."""

    ALL = 0
    """All pulse characteristics are processed."""

    IGNORE_WAVEFORM_PERIODICITY_ANALYSIS = 1
    """All pulse characteristics are processed, except period, frequency and duty cycle elements."""


class PulseAnalogProcessingReferenceLevels(AnalysisLibraryElement):
    """Defines reference levels that will be used to locate pulse when
    analyzing waveform.
    """

    def __init__(
        self,
        reference_level_high: float,
        reference_level_middle: float,
        reference_level_low: float,
    ):
        self._reference_level_high = reference_level_high
        self._reference_level_middle = reference_level_middle
        self._reference_level_low = reference_level_low

    @property
    def reference_level_high(self) -> float:
        """Gets high reference level used when processed waveform pulse.

        Returns:
            float: High reference level value.
        """
        return self._reference_level_high

    @property
    def reference_level_middle(self) -> float:
        """Gets middle reference level used when processed waveform pulse.

        Returns:
            float: Middle reference level value.
        """
        return self._reference_level_middle

    @property
    def reference_level_low(self) -> float:
        """Gets low reference level used when processed waveform pulse.

        Returns:
            float: Low reference level value.
        """
        return self._reference_level_low


class PulseAnalogMeasurementPercentLevelsSettings(AnalysisLibraryElement):
    """Defines settings to use when reference levels
    required for pulse analysis are expressed as percentage."""

    def __init__(
        self,
        amplitude_and_levels_processing_method: AmplitudeAndLevelsProcessingMethod,
        histogram_size: int,
    ) -> None:
        """Initialize an instance of `PulseAnalogMeasurementPercentLevelsSettings`.

        Args:
            amplitude_and_levels_processing_method (AmplitudeAndLevelsProcessingMethod):
                Amplitude and levels processing method.
            histogram_size (int):
                Number of bins of the histogram when amplitude and levels processing choose to use
                histogram based algorithm.
        """
        Guard.is_greater_than_zero(value=histogram_size, value_name=nameof(histogram_size))

        self._amplitude_and_levels_processing_method = amplitude_and_levels_processing_method
        self._histogram_size = histogram_size

    @property
    def amplitude_and_levels_processing_method(self) -> int:
        """Gets method that will be used when processing waveform states.

        Returns:
            int: Amplitude and levels processing method.
        """
        return self._amplitude_and_levels_processing_method

    @property
    def histogram_size(self) -> int:
        """Gets histogram size, ie, bins count, that will be used when processing waveform states.

        Returns:
            int: histogram bins count.
        """
        return self._histogram_size


class LabViewPulseAnalogMeasurements(AnalysisLibraryElement):
    """Provides pulse analog processing based on ``LabVIEW Pulse Measurements`` VI"""

    @staticmethod
    def get_last_error_message() -> str:
        """Gets the message content of the last occured error of
        ``Pulse Measurements`` labview VI.

        Returns:
            str: Empty string when no error occured, elsewhere not empty string.
        """

        return _pulse_analog_analysis.labview_get_last_error_message_impl()

    @staticmethod
    def process_single_waveform_multiple_pulse_measurements(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        waveform_t0: float,
        export_mode: PulseAnalogProcessingExportMode,
        processing_polarity: PulseAnalogProcessingPolarity,
        reference_levels_unit: PulseAnalogProcessingReferenceLevelsUnit,
        reference_levels: PulseAnalogProcessingReferenceLevels,
        percent_levels_settings: Optional[PulseAnalogMeasurementPercentLevelsSettings],
    ) -> Iterable[PulseAnalogProcessingResult]:
        """Processes multiple pulse measurements of a
        given single waveform samples using LabVIEW VI.

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): single waveform samples.
            waveform_sampling_period_seconds (float): sampling rate of the single waveform
            waveform_t0 (float): waveform start date t0.
            export_mode (PulseAnalogProcessingExportMode):
                pulse analysis results exportation mode.
            processing_polarity (PulseAnalogProcessingPolarity):
                pulse polarity that will be analyzed (high or low),
                when high, rising edge crossing middle level
                    then falling edge crossing middle level are analyzed,
                when low, falling edge crossing middle level
                    then rising edge crossing middle level are analyzed.
            reference_levels_unit (PulseAnalogProcessingReferenceLevelsUnit):
                unit of the reference levels.
            reference_levels (PulseAnalogProcessingReferenceLevels):
                reference levels that will be used to delimit pulse phases in waveform.
            percent_levels_settings (Optional[PulseAnalogMeasurementPercentLevelsSettings]):
                state settings when reference levels unit is percent, igonred if absolute.

        Raises:
            ValueError:
                Occurs when one of provided input arguments is invalid.
            PCBATTAnalysisException:
                Occurs when analysis fails for some reason.

        Returns:
            Iterable[PulseAnalogProcessingResult]: an object that holds multiple results of pulse
            processing result using LabVIEW VI.
        """

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))

        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        pulse_number = 0
        stop_pulse_analysis = False

        while not stop_pulse_analysis:
            pulse_number = pulse_number + 1
            try:
                yield LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                    waveform_samples,
                    waveform_sampling_period_seconds,
                    waveform_t0,
                    pulse_number,
                    export_mode,
                    processing_polarity,
                    reference_levels_unit,
                    reference_levels,
                    percent_levels_settings,
                )
            except PCBATTAnalysisException:
                stop_pulse_analysis = True

    @staticmethod
    def process_single_waveform_pulse_measurements(
        waveform_samples: numpy.ndarray[numpy.float64],
        waveform_sampling_period_seconds: float,
        waveform_t0: float,
        pulse_number: int,
        export_mode: PulseAnalogProcessingExportMode,
        processing_polarity: PulseAnalogProcessingPolarity,
        reference_levels_unit: PulseAnalogProcessingReferenceLevelsUnit,
        reference_levels: PulseAnalogProcessingReferenceLevels,
        percent_levels_settings: Optional[PulseAnalogMeasurementPercentLevelsSettings],
    ) -> PulseAnalogProcessingResult:
        """Processes pulse measurements of a given single waveform samples using LabVIEW VI.

        Args:
            waveform_samples (numpy.ndarray[numpy.float64]): single waveform samples.
            waveform_sampling_period_seconds (float): sampling rate of the single waveform
            waveform_t0 (float): waveform start date t0.
            pulse_number (int): index of the pulse that will be analyzed (starts from 1).
            export_mode (PulseAnalogProcessingExportMode):
                pulse analysis results exportation mode.
            processing_polarity (PulseAnalogProcessingPolarity):
                pulse polarity that will be analyzed (high or low),
                when high, rising edge crossing middle level
                    then falling edge crossing middle level are analyzed,
                when low, falling edge crossing middle level
                    then rising edge crossing middle level are analyzed.
            reference_levels_unit (PulseAnalogProcessingReferenceLevelsUnit):
                unit of the reference levels.
            reference_levels (PulseAnalogProcessingReferenceLevels):
                reference levels that will be used to delimit pulse phases in waveform.
            percent_levels_settings (Optional[PulseAnalogMeasurementPercentLevelsSettings]):
                state settings when reference levels unit is percent, igonred if absolute.

        Raises:
            ValueError:
                Occurs when one of provided input arguments is invalid.
            PCBATTAnalysisException:
                Occurs when analysis fails for some reason.

        Returns:
            PulseAnalogProcessingResult: An object that holds result of pulse
            processing result using LabVIEW VI.
        """

        Guard.is_not_none(waveform_samples, nameof(waveform_samples))
        Guard.is_not_empty(waveform_samples, nameof(waveform_samples))
        Guard.is_greater_than_zero(pulse_number, nameof(pulse_number))

        Guard.is_greater_than_zero(
            waveform_sampling_period_seconds, nameof(waveform_sampling_period_seconds)
        )

        try:
            if reference_levels_unit == PulseAnalogProcessingReferenceLevelsUnit.ABSOLUTE:
                # hold absolute levels based analysis, percent settings is not required
                if export_mode == PulseAnalogProcessingExportMode.ALL:
                    processing_result_as_tuple = _pulse_analog_analysis.labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_all_impl(
                        waveform_samples=waveform_samples,
                        waveform_sampling_period_seconds=waveform_sampling_period_seconds,
                        pulse_number=pulse_number,
                        processing_polarity=processing_polarity,
                        reference_levels=_pulse_analog_analysis.TuplePulseReferenceLevels(
                            reference_level_high=reference_levels.reference_level_high,
                            reference_level_middle=reference_levels.reference_level_middle,
                            reference_level_low=reference_levels.reference_level_low,
                        ),
                    )
                    return PulseAnalogProcessingResult(
                        processing_result_as_tuple.pulse_center,
                        processing_result_as_tuple.pulse_duration,
                        processing_result_as_tuple.pulse_reference_level_high,
                        processing_result_as_tuple.pulse_reference_level_middle,
                        processing_result_as_tuple.pulse_reference_level_low,
                        processing_result_as_tuple.period,
                        processing_result_as_tuple.duty_cycle,
                    )

                processing_result_as_tuple = _pulse_analog_analysis.labview_process_single_waveform_pulse_measurements_ref_levels_absolute_export_no_periodicity_impl(
                    waveform_samples=waveform_samples,
                    waveform_sampling_period_seconds=waveform_sampling_period_seconds,
                    pulse_number=pulse_number,
                    processing_polarity=processing_polarity,
                    reference_levels=_pulse_analog_analysis.TuplePulseReferenceLevels(
                        reference_level_high=reference_levels.reference_level_high,
                        reference_level_middle=reference_levels.reference_level_middle,
                        reference_level_low=reference_levels.reference_level_low,
                    ),
                )
                return PulseAnalogProcessingResult(
                    processing_result_as_tuple.pulse_center + waveform_t0,
                    processing_result_as_tuple.pulse_duration,
                    processing_result_as_tuple.pulse_reference_level_high,
                    processing_result_as_tuple.pulse_reference_level_middle,
                    processing_result_as_tuple.pulse_reference_level_low,
                )
            elif reference_levels_unit == PulseAnalogProcessingReferenceLevelsUnit.RELATIVE_PERCENT:
                # check reference levels are percent values
                # hold relative percent levels based analysis
                # percent settings is required
                if percent_levels_settings is None:
                    raise PCBATTAnalysisException(
                        AnalysisLibraryExceptionMessage.PULSE_MEASUREMENTS_PROCESSING_REFERENCE_LEVELS_UNIT_PERCENT_REQUIRES_STATES_SETTINGS
                    )

                # hold relative levels based analysis, percent settings is not required
                if export_mode == PulseAnalogProcessingExportMode.ALL:
                    processing_result_as_tuple = _pulse_analog_analysis.labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_all_impl(
                        waveform_samples=waveform_samples,
                        waveform_sampling_period_seconds=waveform_sampling_period_seconds,
                        pulse_number=pulse_number,
                        processing_polarity=processing_polarity,
                        amplitude_and_levels_processing_method=percent_levels_settings.amplitude_and_levels_processing_method,
                        amplitude_and_levels_processing_histogram_size=percent_levels_settings.histogram_size,
                        reference_levels=reference_levels,
                    )
                    return PulseAnalogProcessingResult(
                        processing_result_as_tuple.pulse_center + waveform_t0,
                        processing_result_as_tuple.pulse_duration,
                        processing_result_as_tuple.pulse_reference_level_high,
                        processing_result_as_tuple.pulse_reference_level_middle,
                        processing_result_as_tuple.pulse_reference_level_low,
                        processing_result_as_tuple.period,
                        processing_result_as_tuple.duty_cycle,
                    )
                else:
                    processing_result_as_tuple = _pulse_analog_analysis.labview_process_single_waveform_pulse_measurements_ref_levels_relative_export_no_periodicity_impl(
                        waveform_samples=waveform_samples,
                        waveform_sampling_period_seconds=waveform_sampling_period_seconds,
                        pulse_number=pulse_number,
                        processing_polarity=processing_polarity,
                        amplitude_and_levels_processing_method=percent_levels_settings.amplitude_and_levels_processing_method,
                        amplitude_and_levels_processing_histogram_size=percent_levels_settings.histogram_size,
                        reference_levels=reference_levels,
                    )
                    return PulseAnalogProcessingResult(
                        processing_result_as_tuple.pulse_center + waveform_t0,
                        processing_result_as_tuple.pulse_duration,
                        processing_result_as_tuple.pulse_reference_level_high,
                        processing_result_as_tuple.pulse_reference_level_middle,
                        processing_result_as_tuple.pulse_reference_level_low,
                    )

            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.PULSE_MEASUREMENTS_PROCESSING_REFERENCE_LEVELS_UNIT_IS_NOT_SUPPORTED
            )

        except Exception as e:
            raise PCBATTAnalysisException(
                AnalysisLibraryExceptionMessage.PULSE_MEASUREMENTS_PROCESSING_FAILED_FOR_SOME_REASON
            ) from e

    @staticmethod
    def process_multiple_waveforms_pulse_measurements(
        waveforms_samples: Iterable[numpy.ndarray[numpy.float64]],
        waveforms_sampling_period_seconds: float,
        waveforms_t0: Iterable[float],
        pulse_number: int,
        export_mode: PulseAnalogProcessingExportMode,
        processing_polarity: PulseAnalogProcessingPolarity,
        reference_levels_unit: PulseAnalogProcessingReferenceLevelsUnit,
        reference_levels: PulseAnalogProcessingReferenceLevels,
        percent_levels_settings: Optional[PulseAnalogMeasurementPercentLevelsSettings],
    ) -> Iterable[PulseAnalogProcessingResult]:
        """Processes pulse measurement of a given multiple waveforms samples using LabVIEW VI.

        Args:
            waveforms_samples (Iterable[numpy.ndarray[numpy.float64]]): multiple waveforms samples.
            waveforms_sampling_period_seconds (float): common sampling rate of all waveforms.
            waveforms_t0 (Iterable[float]): for each waveform start date t0.
            pulse_number (int): index of the pulse that will be analyzed (starts from 1).
            export_mode (PulseAnalogProcessingExportMode): pulse analysis results exportation mode.
            processing_polarity (PulseAnalogProcessingPolarity): pulse polarity that will
                be analyzed (high or low).
            reference_levels_unit (PulseAnalogProcessingReferenceLevelsUnit):
                unit of the reference levels.
            reference_levels (PulseAnalogProcessingReferenceLevels):
                reference levels that will be used to delimit pulse phases in waveforms.
            percent_levels_settings (Optional[PulseAnalogMeasurementPercentLevelsSettings]):
                state settings when reference levels unit is percent, igonred if absolute.

        Returns:
            Iterable[PulseAnalogProcessingResult]: An iterable of objects that hold result of
            pulse measurements processing of each input waveform using LabVIEW VI.

        Raises:
            ValueError:
                Occurs when one of provided input arguments is invalid.
            PCBATTAnalysisException:
                Occurs when analysis fails for some reason.

        Yields:
            Iterator[Iterable[PulseAnalogProcessingResult]]: objects that hold result of
            pulse measurements processing of each input waveform using LabVIEW VI.
        """
        Guard.is_not_none(waveforms_samples, nameof(waveforms_samples))
        Guard.is_greater_than_zero(
            waveforms_sampling_period_seconds, nameof(waveforms_sampling_period_seconds)
        )

        Guard.have_same_size(
            first_iterable_instance=waveforms_samples,
            first_iterable_name=nameof(waveforms_samples),
            second_iterable_instance=waveforms_t0,
            second_iterable_name=nameof(waveforms_t0),
        )
        Guard.is_greater_than_zero(pulse_number, nameof(pulse_number))

        for waveform_samples, waveform_t0 in zip(waveforms_samples, waveforms_t0):
            yield LabViewPulseAnalogMeasurements.process_single_waveform_pulse_measurements(
                waveform_samples,
                waveforms_sampling_period_seconds,
                waveform_t0,
                pulse_number,
                export_mode,
                processing_polarity,
                reference_levels_unit,
                reference_levels,
                percent_levels_settings,
            )
