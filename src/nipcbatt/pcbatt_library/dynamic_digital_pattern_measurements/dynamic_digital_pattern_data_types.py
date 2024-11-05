""" Dynamic digital pattern data types """

import nidaqmx.constants
import numpy as np
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    DigitalStartTriggerParameters,
    DynamicDigitalPatternTimingParameters,
    MeasurementOptions,
)
from nipcbatt.pcbatt_library.dynamic_digital_pattern_measurements.dynamic_digital_pattern_constants import (
    ConstantsForDynamicDigitalPatternMeasurement,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class DynamicDigitalPatternMeasurementConfiguration(PCBATestToolkitData):
    """Defines a configuration for dynamic digital pattern measurement"""

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
        """
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
        """
        return self._measurement_options

    @property
    def timing_parameters(self) -> DynamicDigitalPatternTimingParameters:
        """
        :class:`DynamicDigitalPatternTimingParameters`:
            Gets a `DynamicDigitalPatternTimingParameters` instance
            that represents the settings of timing.
        """
        return self._timing_parameters

    @property
    def trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """
        return self._trigger_parameters


class DynamicDigitalPatternMeasurementResultData(PCBATestToolkitData):
    """Defines the values returned from the capture"""

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
        """

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
        """
        return self._daq_digital_waveform_from_port

    @property
    def waveforms(self) -> np.ndarray:
        """
        :type:'numpy.ndarray': Data captured from the measurement
        """
        return self._waveforms
