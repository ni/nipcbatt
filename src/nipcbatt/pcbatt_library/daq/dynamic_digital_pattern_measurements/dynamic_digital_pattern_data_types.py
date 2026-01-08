""" Dynamic digital pattern data types """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (153 > 100 characters) (auto-generated noqa)

import nidaqmx.constants  # noqa: F401 - 'nidaqmx.constants' imported but unused (auto-generated noqa)
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
    MeasurementOptions,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_constants import (  # noqa: F401 - 'nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_constants.ConstantsForDynamicDigitalPatternMeasurement' imported but unused (auto-generated noqa)
    ConstantsForDynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DynamicDigitalPatternMeasurementConfiguration(PCBATestToolkitData):
    """Defines a configuration for dynamic digital pattern measurement"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (184 > 100 characters) (auto-generated noqa)

    def __init__(
        self,
        measurement_options: MeasurementOptions,
        timing_parameters: DynamicDigitalPatternTimingParameters,
        trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `DynamicDigitalPatternMeasurementConfiguration`.

        Args:
            measurement_options (MeasurementOptions):
                The type of measurement options selected by user.
            timing_parameters (DynamicDigitalPatternTimingParameters):
                An instance of `DynamicDigitalPatternTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters` that represents the settings of triggers.

        Raises:
            ValueError:
                'measurement_options' is None,
                `timing_parameters` is None,
                `trigger_parameters` is None,
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (110 > 100 characters) (auto-generated noqa)
        Guard.is_not_none(measurement_options, nameof(measurement_options))
        Guard.is_not_none(timing_parameters, nameof(timing_parameters))
        Guard.is_not_none(trigger_parameters, nameof(trigger_parameters))

        self._measurement_options = measurement_options
        self._timing_parameters = timing_parameters
        self._trigger_parameters = trigger_parameters

    @property
    def measurement_options(self) -> MeasurementOptions:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._measurement_options

    @property
    def timing_parameters(self) -> DynamicDigitalPatternTimingParameters:
        """
        :class:`DynamicDigitalPatternTimingParameters`:
            Gets a `DynamicDigitalPatternTimingParameters` instance
            that represents the settings of timing.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._timing_parameters

    @property
    def trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """  # noqa: D205, D212, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (299 > 100 characters) (auto-generated noqa)
        return self._trigger_parameters


class DynamicDigitalPatternMeasurementResultData(PCBATestToolkitData):
    """Defines the values returned from the capture"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

    def __init__(self, daq_digital_waveform_from_port: np.ndarray, waveforms: np.ndarray) -> None:
        """Initializes an instance of 'DynamicDigitalPatternMeasurementData'
        with specific values

        Args:
            daq_digital_waveform_from_port: Numpy ndarray
            waveforms: Numpy ndarray

        Raises: ValueError when,
            1) daq_digital_waveform_from_port is empty
            2) daq_digital_waveform_from_port is None
            3) waveforms is empty
            4) waveforms is none
        """  # noqa: D202, D205, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (287 > 100 characters) (auto-generated noqa)

        # input validation
        Guard.is_not_none(daq_digital_waveform_from_port, nameof(daq_digital_waveform_from_port))
        Guard.is_not_empty(daq_digital_waveform_from_port, nameof(daq_digital_waveform_from_port))
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))

        # assign to member variable
        self._daq_digital_waveform_from_port = daq_digital_waveform_from_port
        self._waveforms = waveforms

    @property
    def daq_digital_waveform_from_port(self) -> np.ndarray:
        """
        :type:'numpy.ndarray': Data captured from the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._daq_digital_waveform_from_port

    @property
    def waveforms(self) -> np.ndarray:
        """
        :type:'numpy.ndarray': Data captured from the measurement
        """  # noqa: D212, D415, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (211 > 100 characters) (auto-generated noqa)
        return self._waveforms
