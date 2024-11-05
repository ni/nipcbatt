"""Defines datatypes that are common to all pcba test toolkit building blocks."""

from enum import Enum
from typing import Iterable

import nidaqmx.constants
import numpy
from varname import nameof

from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard

MAXIMUM_NUMBER_OF_DIMENSIONS_IN_NUMPY_ARRAY = 2


class MeasurementExecutionType(Enum):
    """Defines the way the measurement is executed."""

    CONFIGURE_AND_MEASURE = 0
    """Configuration and procedure to measurement."""

    CONFIGURE_ONLY = 1
    """Configuration only."""

    MEASURE_ONLY = 2
    """Measurement procedure only."""


class MeasurementAnalysisRequirement(Enum):
    """Defines the way analysis is proceeded during measurement."""

    SKIP_ANALYSIS = 0
    """Skip analysis, analysis step is not required."""

    PROCEED_TO_ANALYSIS = 1
    """Proceed to analysis; analysis step is required."""


class SampleTimingEngine(Enum):
    """Defines which timing engine to use for the task."""

    TE0 = 0
    """TE0 engine."""

    TE1 = 1
    """TE1 engine."""

    AI = 2
    """AI engine."""

    AUTO = 3
    """Auto"""


class StartTriggerType(Enum):
    """Define the types used for start trigger during measurement."""

    NO_TRIGGER = 0
    """No trigger configured."""

    DIGITAL_TRIGGER = 1
    """Digital Start trigger."""


class MeasurementOptions(PCBATestToolkitData):
    """Defines the options for execution of measurement."""

    def __init__(
        self,
        execution_option: MeasurementExecutionType,
        measurement_analysis_requirement: MeasurementAnalysisRequirement,
    ) -> None:
        """Used to initialize an instance of `MeasurementOptions`.

        Args:
            execution_option (MeasurementExecutionType):
               The type of measurement execution selected by user.
            measurement_analysis_requirement (MeasurementAnalysisRequirement):
               The measurement analysis requirement selected by user.
        """
        self._execution_option = execution_option
        self._measurement_analysis_requirement = measurement_analysis_requirement

    @property
    def execution_option(self) -> MeasurementExecutionType:
        """Gets the type of measurement execution selected by user."""
        return self._execution_option

    @property
    def measurement_analysis_requirement(self) -> MeasurementAnalysisRequirement:
        """Gets the measurement analysis requirement selected by user."""
        return self._measurement_analysis_requirement


class SampleClockTimingParameters(PCBATestToolkitData):
    """Defines the settings of sample clock timing for measurement."""

    def __init__(
        self,
        sample_clock_source: str,
        sampling_rate_hertz: int,
        number_of_samples_per_channel: int,
        sample_timing_engine: SampleTimingEngine,
    ) -> None:
        """Used to initialize an instance of `SampleClockTimingParameters`.

        Args:
            sample_clock_source (str): The source of the clock.
            sampling_rate_hertz (int): The sampling rate (in Hz).
            number_of_samples_per_channel (int): The number of samples per channel.
            sample_timing_engine (SampleTimingEngine): The engine for sample timing.

        Raises:
            ValueError:
                Raised if `sample_clock_source` is None or empty or white space,
                if `sampling_rate_hertz` is less than or equal to zero.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(sample_clock_source, nameof(sample_clock_source))
        Guard.is_greater_than_zero(sampling_rate_hertz, nameof(sampling_rate_hertz))

        self._sample_clock_source = sample_clock_source
        self._sampling_rate_hertz = sampling_rate_hertz
        self._number_of_samples_per_channel = number_of_samples_per_channel
        self._sample_timing_engine = sample_timing_engine

    @property
    def sample_clock_source(self) -> str:
        """Gets the source of the clock."""
        return self._sample_clock_source

    @property
    def sampling_rate_hertz(self) -> int:
        """Gets the sampling rate (in Hz)."""
        return self._sampling_rate_hertz

    @property
    def number_of_samples_per_channel(self) -> int:
        """Gets the number of samples per channel."""
        return self._number_of_samples_per_channel

    @property
    def sample_timing_engine(self) -> SampleTimingEngine:
        """Gets the engine for sample timing."""
        return self._sample_timing_engine


class DynamicDigitalPatternTimingParameters(PCBATestToolkitData):
    """Defines the settings of sample clock edge for measurement."""

    def __init__(
        self,
        sample_clock_source: str = "OnboardClock",
        sampling_rate_hertz: float = 10000.0,
        number_of_samples_per_channel: int = 50,
        active_edge: nidaqmx.constants.Edge = nidaqmx.constants.Edge.RISING,
    ) -> None:
        """Used to initialize an instance of `DynamicDigitalPatternTimingParameters`.

        Args:
            sample_clock_source (str): The source of the clock.
            sampling_rate_hertz (float): The sampling rate (in Hz).
            number_of_samples_per_channel (int): The number of samples per channel.
            active_edge (nidaqmx.constants.Edge): The `nidaqmx.constants.Edge` value that specifies on which edge
            of a digital pulse to start acquiring samples.

        Raises:
            ValueError:
                Raised if `sample_clock_source` is None or empty or white space,
                if `sampling_rate_hertz` is None or less than zero,
                if 'number_of_samples_per_channel' is None or less than zero,
                if 'active_edge' is None.
        """
        # Input validation
        Guard.is_not_none_nor_empty_nor_whitespace(sample_clock_source, nameof(sample_clock_source))
        Guard.is_not_none(sampling_rate_hertz, nameof(sampling_rate_hertz))
        Guard.is_float(sampling_rate_hertz, nameof(sampling_rate_hertz))
        Guard.is_greater_than_or_equal_to_zero(sampling_rate_hertz, nameof(sampling_rate_hertz))
        Guard.is_not_none(number_of_samples_per_channel, nameof(number_of_samples_per_channel))
        Guard.is_greater_than_or_equal_to_zero(
            number_of_samples_per_channel, nameof(number_of_samples_per_channel)
        )
        Guard.is_not_none(active_edge, nameof(active_edge))

        self._sample_clock_source = sample_clock_source
        self._sampling_rate_hertz = sampling_rate_hertz
        self._number_of_samples_per_channel = number_of_samples_per_channel
        self._active_edge = active_edge

    @property
    def sample_clock_source(self) -> str:
        """Gets the source of the clock."""
        return self._sample_clock_source

    @property
    def sampling_rate_hertz(self) -> float:
        """Gets the sampling rate (in Hz)."""
        return self._sampling_rate_hertz

    @property
    def number_of_samples_per_channel(self) -> int:
        """Gets the number of samples per channel."""
        return self._number_of_samples_per_channel

    @property
    def active_edge(self) -> nidaqmx.constants.Edge:
        """Gets the engine for sample timing."""
        return self._active_edge


class DigitalStartTriggerParameters(PCBATestToolkitData):
    """Defines the settings of triggers for measurement."""

    def __init__(
        self,
        trigger_select: StartTriggerType,
        digital_start_trigger_source: str,
        digital_start_trigger_edge: nidaqmx.constants.Edge,
    ) -> None:
        """Initializes an instance of `DigitalStartTriggerParameters`.

        Args:
            trigger_select (StartTriggerType): The type of trigger
            digital_start_trigger_source (str): The source of digital start trigger.
            digital_start_trigger_edge (nidaqmx.constants.Edge):
                The `nidaqmx.constants.Edge` value that specifies on which edge
                of a digital pulse to start acquiring or generating samples.

        Raises:
            ValueError:
                Raised if `digital_start_trigger_source` is None or empty or white space.
        """
        if trigger_select == StartTriggerType.DIGITAL_TRIGGER:
            # Check argument digital_start_trigger_source
            # if trigger_select is StartTriggerType.DIGITAL_TRIGGER
            Guard.is_not_none_nor_empty_nor_whitespace(
                digital_start_trigger_source, nameof(digital_start_trigger_source)
            )
        self._trigger_select = trigger_select
        self._digital_start_trigger_source = digital_start_trigger_source
        self._digital_start_trigger_edge = digital_start_trigger_edge

    @property
    def trigger_select(self) -> StartTriggerType:
        """Gets the type of trigger."""
        return self._trigger_select

    @property
    def digital_start_trigger_source(self) -> str:
        """Gets the source of digital start trigger."""
        return self._digital_start_trigger_source

    @property
    def digital_start_trigger_edge(self) -> nidaqmx.constants.Edge:
        """Gets the `nidaqmx.constants.Edge` value
        that specifies on which edge
        of a digital pulse to start acquiring or generating samples."""
        return self._digital_start_trigger_edge


class MeasurementData(PCBATestToolkitData):
    """Defines the data captured for measurement."""

    def __init__(self, data_samples: numpy.ndarray) -> None:
        """Initializes an instance of `MeasurementData`.

        Args:
            samples (numpy.ndarray):
                The array containing the samples captured for measurement.
        Raises:
            ValueError:
                Raised when `samples` is None or empty.
        """
        Guard.is_not_none(data_samples, nameof(data_samples))
        Guard.is_not_empty(data_samples, nameof(data_samples))
        Guard.size_is_less_than_or_equal(
            data_samples.shape,
            MAXIMUM_NUMBER_OF_DIMENSIONS_IN_NUMPY_ARRAY,
            nameof(data_samples.shape),
        )

        self._data_samples = data_samples

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `MeasurementData` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """
        if isinstance(value_to_compare, self.__class__):
            return numpy.allclose(self._data_samples, value_to_compare._data_samples)

        return False

    @property
    def samples_per_channel(self) -> Iterable[numpy.ndarray[numpy.float64]]:
        """Gets a iterable instance on the samples array per channel."""

        if len(self._data_samples.shape) <= 1:
            yield self._data_samples
            return

        for samples_per_channel in self._data_samples:
            yield samples_per_channel


class AnalogWaveform(PCBATestToolkitData):
    """Define the structure of a waveform."""

    def __init__(
        self,
        channel_name: str,
        delta_time_seconds: float,
        samples: numpy.ndarray[float],
    ) -> None:
        """Used to initialize an instance of `AnalogWaveform`.

        Args:
            channel_name (str): The name of physical channel where samples were captured from.
            delta_time_seconds (float): The time between two samples (in seconds).
            samples (numpy.ndarray): The array of samples.

        Raises:
            ValueError: raised if `channel_name` is None or empty or white space
            or if `delta_time_seconds` if less than or equal to zero
            or if `samples` is none or empty.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_greater_than_zero(delta_time_seconds, nameof(delta_time_seconds))
        Guard.is_not_none(samples, nameof(samples))
        Guard.is_not_empty(samples, nameof(samples))

        self._channel_name = channel_name
        self._delta_time_seconds = delta_time_seconds
        self._samples = samples

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `AnalogWaveform` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """
        if isinstance(value_to_compare, self.__class__):
            return (
                self._channel_name == value_to_compare._channel_name
                and self._delta_time_seconds == value_to_compare._delta_time_seconds
                and numpy.allclose(self._samples, value_to_compare._samples)
            )

        return False

    @property
    def channel_name(self) -> str:
        """Gets the name of physical channel where samples were captured from."""
        return self._channel_name

    @property
    def delta_time_seconds(self) -> float:
        """Gets the time between two samples (in seconds)."""
        return self._delta_time_seconds

    @property
    def samples(self) -> numpy.ndarray[float]:
        """Gets the array of samples."""
        return self._samples


class AmplitudeSpectrum(PCBATestToolkitData):
    """Defines the structure of a frequency spectrum."""

    def __init__(
        self,
        channel_name: str,
        spectrum_start_frequency_hertz: float,
        spectrum_frequency_resolution_hertz: float,
        amplitudes: numpy.ndarray[float],
    ) -> None:
        """Used to initialize an instance of `AmplitudeSpectrum`.

        Args:
            channel_name (`str`): The name of physical channel where samples were captured from.
            spectrum_start_frequency_hertz (`float`):
                The frequency of start of spectrum, expressed in Hertz.
            spectrum_frequency_resolution_hertz (`float`):
                The frequency interval between two amplitude values, expressed in Hertz.
            amplitudes (`numpy.ndarray[float]`): The array of amplitudes.

        Raises:
            ValueError: raised if `channel_name` is None or empty or white space
            or if `spectrum_frequency_resolution_hertz` if less than or equal to zero
            or if `amplitudes` is None or empty.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_greater_than_zero(
            spectrum_frequency_resolution_hertz,
            nameof(spectrum_frequency_resolution_hertz),
        )
        Guard.is_not_none(amplitudes, nameof(amplitudes))
        Guard.is_not_empty(amplitudes, nameof(amplitudes))

        self._amplitudes = amplitudes
        self._spectrum_start_frequency_hertz = spectrum_start_frequency_hertz
        self._spectrum_frequency_resolution_hertz = spectrum_frequency_resolution_hertz
        self._channel_name = channel_name

    def __eq__(self, value_to_compare: object) -> bool:
        """instances equality.

        Args:
            value_to_compare (object): the instance of `AmplitudeSpectrum` to compare.

        Returns:
            bool: True if equals to `value_to_compare`.
        """
        if isinstance(value_to_compare, self.__class__):
            return (
                self._channel_name == value_to_compare._channel_name
                and self._spectrum_start_frequency_hertz
                == value_to_compare._spectrum_start_frequency_hertz
                and self._spectrum_frequency_resolution_hertz
                == value_to_compare._spectrum_frequency_resolution_hertz
                and numpy.allclose(self._amplitudes, value_to_compare._amplitudes)
            )

        return False

    @property
    def channel_name(self) -> str:
        """Gets the name of physical channel where samples were captured from."""
        return self._channel_name

    @property
    def spectrum_frequency_resolution_hertz(self) -> float:
        """Gets the frequency interval between two amplitude values, expressed in Hertz."""
        return self._spectrum_frequency_resolution_hertz

    @property
    def spectrum_start_frequency_hertz(self) -> float:
        """Gets the frequency of start of spectrum, expressed in Hertz."""
        return self._spectrum_start_frequency_hertz

    @property
    def amplitudes(self) -> numpy.ndarray[float]:
        """Gets the array of amplitudes."""
        return self._amplitudes
