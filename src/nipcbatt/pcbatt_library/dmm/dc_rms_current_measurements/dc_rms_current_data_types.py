"""DC-RMS current data types."""

from enum import Enum
from typing import Union

import nidmm

from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData


class CurrentRangeAndFunctions(Enum):
    """Defines the measurement function and range settings for current measurement."""

    DC_Current_Auto_Range = (nidmm.Function.DC_CURRENT, -1.0)
    DC_1uA = (nidmm.Function.DC_CURRENT, 0.000001)
    DC_10uA = (nidmm.Function.DC_CURRENT, 0.00001)
    DC_100uA = (nidmm.Function.DC_CURRENT, 0.0001)
    DC_1mA = (nidmm.Function.DC_CURRENT, 0.001)
    DC_10mA = (nidmm.Function.DC_CURRENT, 0.01)
    DC_20mA = (nidmm.Function.DC_CURRENT, 0.02)
    DC_100mA = (nidmm.Function.DC_CURRENT, 0.1)
    DC_200mA = (nidmm.Function.DC_CURRENT, 0.2)
    DC_1A = (nidmm.Function.DC_CURRENT, 1)
    DC_3A = (nidmm.Function.DC_CURRENT, 3)

    AC_Current_Auto_Range = (nidmm.Function.AC_CURRENT, -1.0)
    AC_100uA = (nidmm.Function.AC_CURRENT, 0.0001)
    AC_1mA = (nidmm.Function.AC_CURRENT, 0.001)
    AC_10mA = (nidmm.Function.AC_CURRENT, 0.01)
    AC_100mA = (nidmm.Function.AC_CURRENT, 0.1)
    AC_500mA = (nidmm.Function.AC_CURRENT, 0.5)
    AC_1A = (nidmm.Function.AC_CURRENT, 1)
    AC_3A = (nidmm.Function.AC_CURRENT, 3)


class DcRmsCurrentMeasurementFunctionParameters:
    """Defines parameters used for configuration of DC-RMS current measurement."""

    def __init__(
        self,
        measurement_function: CurrentRangeAndFunctions,
        resolution_in_digits: ResolutionInDigits,
    ) -> None:
        """Initializes measurement function parameters.

        Args:
            measurement_function (CurrentRangeAndFunctions):
                The current measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        """
        self._measurement_function = measurement_function
        self._resolution_in_digits = resolution_in_digits

    @property
    def measurement_function(self) -> CurrentRangeAndFunctions:
        """Gets the current measurement function and range setting.

        Returns:
            CurrentRangeAndFunctions: The configured current range and function.
        """
        return self._measurement_function

    @property
    def resolution_in_digits(self) -> ResolutionInDigits:
        """Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        """
        return self._resolution_in_digits


class DcRmsCurrentMeasurementConfiguration(PCBATestToolkitData):
    """Defines configuration parameters for current DC-RMS measurements."""

    def __init__(
        self,
        execution_type: MeasurementExecutionType,
        measurement_function_parameters: DcRmsCurrentMeasurementFunctionParameters,
        trigger_parameters: TriggerParameters,
        timing_parameters: TimingParameters,
        ac_min_frequency: float,
    ) -> None:
        """Initializes the current measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (DcRmsCurrentMeasurementFunctionParameters):
                The measurement function settings including current range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
            ac_min_frequency (float):
                Minimum frequency for AC current measurements in Hz (ignored for DC measurements).
        """
        self._execution_type = execution_type
        self._measurement_function_parameters = measurement_function_parameters
        self._trigger_parameters = trigger_parameters
        self._timing_parameters = timing_parameters
        self._ac_min_frequency = ac_min_frequency

    @property
    def execution_type(self) -> MeasurementExecutionType:
        """Gets the measurement execution type.

        Returns:
            MeasurementExecutionType: The execution mode (configure only, measure only, or both).
        """
        return self._execution_type

    @property
    def trigger_parameters(self) -> TriggerParameters:
        """Gets the trigger configuration parameters.

        Returns:
            TriggerParameters: The trigger settings for the measurement.
        """
        return self._trigger_parameters

    @property
    def measurement_function_parameters(self) -> DcRmsCurrentMeasurementFunctionParameters:
        """Gets the measurement function parameters.

        Returns:
            DcRmsCurrentMeasurementFunctionParameters: The current range, function,
            and resolution settings.
        """
        return self._measurement_function_parameters

    @property
    def timing_parameters(self) -> TimingParameters:
        """Gets the timing configuration parameters.

        Returns:
            TimingParameters: The aperture time and settle time settings.
        """
        return self._timing_parameters

    @property
    def ac_min_frequency(self) -> float:
        """Gets the minimum AC frequency setting.

        Returns:
            float: The minimum frequency for AC current measurements.
        """
        return self._ac_min_frequency


class DcRmsCurrentMeasurementResultData(PCBATestToolkitData):
    """Defines current DC-RMS results obtained from DMM DC-RMS Current Measurement."""

    def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None:
        """Initializes the current measurement result data.

        Args:
            dmm_execution_settings (dict):
                Dictionary containing the DMM configuration used during measurement.
            measurement (dict | None):
                Dictionary containing the measurement results,
                or None if only configuration was performed.
        """
        self._dmm_execution_settings = dmm_execution_settings
        self._measurement = measurement

    @property
    def dmm_execution_settings(self) -> dict:
        """Gets the DMM execution settings used during the measurement.

        Returns:
            dict: Dictionary with labeled keys and values including units for each setting.
        """
        return self._dmm_execution_settings

    @property
    def measurement(self) -> Union[dict, None]:
        """Gets the measurement result data.

        Returns:
            dict | None: Dictionary containing 'Measured_Value', 'Unit', and
                'Formatted_Measurement' keys, or None if only configuration was performed.
        """
        return self._measurement
