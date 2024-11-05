"""Holds common types of the package nipcbatt.pcbatt_analysis"""

import math
from enum import IntEnum

import numpy
from varname import nameof

from nipcbatt.pcbatt_analysis.common.base_types import AnalysisLibraryElement
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class SpectrumPhaseUnit(IntEnum):
    """Defines all supported phase units of `fft spectrum processing`"""

    RADIAN = 0
    "Default unit, radian"

    DEGREE = 1
    "Degree"


class SpectrumAmplitudeType(IntEnum):
    """Defines all supported amplitude kinds of `fft spectrum processing`"""

    PEAK = 0
    """`Peak` amplitude, ie, sqrt(2) * magnitude spectrum"""
    RMS = 1
    """`RMS` amplitude, ie, magnitude spectrum"""


class AmplitudePhaseSpectrum(AnalysisLibraryElement):
    """Defines Amplitude and phase spectrum processing results,
    amplitude can be `PEAK` or `RMS`"""

    def __init__(
        self,
        f0: float,
        df: float,
        frequencies_amplitudes: numpy.ndarray[float],
        spectrum_amplitude_type: SpectrumAmplitudeType,
        spectrum_amplitude_unit_is_db: bool,
        frequencies_phases: numpy.ndarray[float],
        spectrum_phase_unit: SpectrumPhaseUnit,
    ) -> None:
        """Initialize an instance of `AmplitudePhaseSpectrum`.

        Args:
            f0 (`float`): start frequency of the spectrum.
            df (`float`): frequency resolution of the spectrum.
            frequencies_amplitudes (`numpy.ndarray[float]`): amplitudes of the spectrum.
            spectrum_amplitude_type (`SpectrumAmplitudeType`): spectrum amplitude type.
            spectrum_amplitude_unit_is_db (`bool`): spectrum amplitude is expressed as gain (db).
            frequencies_phases (`numpy.ndarray[float]`):phases of the spectrum.
            spectrum_phase_unit(`SpectrumPhaseUnit`): unit of the spectrum phases.

        Raises:
            ValueError: occurs when input arrays `frequencies_amplitudes`,
            `frequencies_phases` are none or empty.
            occurs when `f0` is less than zero, `df` is less or equal zero.
            occurs when `frequencies_amplitudes` and `frequencies_phases` have not same size.
        """

        Guard.is_greater_than_or_equal_to_zero(f0, nameof(f0))
        Guard.is_greater_than_zero(df, nameof(df))

        Guard.is_not_none(frequencies_amplitudes, nameof(frequencies_amplitudes))
        Guard.is_not_empty(frequencies_amplitudes, nameof(frequencies_amplitudes))

        Guard.is_not_none(frequencies_phases, nameof(frequencies_phases))
        Guard.is_not_empty(frequencies_phases, nameof(frequencies_phases))

        Guard.have_same_size(
            first_iterable_instance=frequencies_amplitudes,
            first_iterable_name=nameof(frequencies_amplitudes),
            second_iterable_instance=frequencies_phases,
            second_iterable_name=nameof(frequencies_phases),
        )

        self._spectrum_start_frequency = f0
        self._spectrum_frequency_resolution = df
        self._spectrum_amplitudes = frequencies_amplitudes
        self._spectrum_amplitude_type = spectrum_amplitude_type
        self._spectrum_amplitude_unit_is_db = spectrum_amplitude_unit_is_db
        self._spectrum_phases = frequencies_phases
        self._spectrum_phase_unit = spectrum_phase_unit

    @property
    def spectrum_start_frequency(self) -> float:
        """Gets spectrum start frequency.

        Returns:
            float: start element of the frequency range.
        """
        return self._spectrum_start_frequency

    @property
    def spectrum_frequency_resolution(self) -> float:
        """Gets spectrum frequency resolution.

        Returns:
            float: resolution of the frequency range.
        """
        return self._spectrum_frequency_resolution

    @property
    def spectrum_frequencies(self) -> numpy.ndarray[float]:
        """Gets the array of frequencies axis of spectrum.

        Returns:
            `numpy.ndarray[float]`: X axis of the spectrum.
        """
        frequency_bins_count = self._spectrum_amplitudes.size

        frequencies_array = numpy.fromiter(
            map(
                lambda frequency_bin_index: self.spectrum_start_frequency
                + frequency_bin_index * self._spectrum_frequency_resolution,
                range(0, frequency_bins_count),
            ),
            dtype=float,
        )

        return frequencies_array

    @property
    def spectrum_amplitudes(self) -> numpy.ndarray[float]:
        """Gets the array of amplitude axis of the spectrum.

        Returns:
            `numpy.ndarray[float]`: Y axis of the amplitude spectrum.
        """
        return self._spectrum_amplitudes

    @property
    def spectrum_phases(self) -> numpy.ndarray[float]:
        """Gets the array of phases axis of the spectrum.

        Returns:
            `numpy.ndarray[float]`: Y axis of the phase spectrum.
        """
        return self._spectrum_phases

    @property
    def spectrum_amplitude_unit_is_db(self) -> bool:
        """Gets a boolean indicating if spectrum amplitudes are expressed in db.

        Returns:
            bool: True if amplitudes are expressed in db.
        """
        return self._spectrum_amplitude_unit_is_db

    @property
    def spectrum_amplitude_type(self) -> SpectrumAmplitudeType:
        """Gets an enumeration value indicating kind of the spectrum amplitudes,
        `RMS` or `PEAK`.

        Returns:
            SpectrumAmplitudeType:
            `RMS`, spectrum amplitudes are RMS amplitude ie complexe magnitude,
            `PEAK` spectrum amplitudes are PEAK amplitude ie sqrt(2) * RMS amplitude
        """
        return self._spectrum_amplitude_type

    @property
    def spectrum_phase_unit(self) -> SpectrumPhaseUnit:
        """Gets an enumeration value indicating unit of the spectrum phases.

        Returns:
            SpectrumPhaseUnit: `RADIAN` or `DEGREE`
        """
        return self._spectrum_phase_unit


class WaveformTone(AnalysisLibraryElement):
    """Defines waveform tone characteristics."""

    def __init__(
        self,
        frequency: float,
        amplitude: float,
        phase_radians: float,
    ) -> None:
        """Initialize an instance of `WaveformTone`.

        Raises:
            ValueError: occurs when frequency is less or equal zero,
                and occurs when amplitude is less or equal zero.

        Args:
            frequency (float): tone frequency, must be greater than zero.
            amplitude (float): tone amplitude, must be greater than zero.
            phase_radians (float): tone phase, in radians.
        """
        Guard.is_greater_than_zero(amplitude, nameof(amplitude))
        Guard.is_greater_than_zero(frequency, nameof(frequency))

        self._amplitude = amplitude
        self._frequency = frequency
        self._phase_radians = phase_radians

    @property
    def frequency(self) -> float:
        """Gets the frequency of the tone."""
        return self._frequency

    @property
    def amplitude(self) -> float:
        """Gets the amplitude of the tone."""
        return self._amplitude

    @property
    def phase_radians(self) -> float:
        """Gets waveform tone phase expressed in radian"""
        return self._phase_radians

    @property
    def phase_degrees(self) -> float:
        """Gets waveform tone phase expressed in degree"""
        return math.degrees(self.phase_radians)
