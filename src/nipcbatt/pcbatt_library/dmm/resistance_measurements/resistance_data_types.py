"""Resistance measurement data types."""

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


class ResistanceRangeAndFunctions(Enum):
    """Defines the measurement function and range settings for resistance measurement."""

    TWO_W_Resistance_Auto_Range = (nidmm.Function.TWO_WIRE_RES, -1.0)
    TWO_W_RES_100_Ohm = (nidmm.Function.TWO_WIRE_RES, 100)
    TWO_W_RES_1k_Ohm = (nidmm.Function.TWO_WIRE_RES, 1000)
    TWO_W_RES_10k_Ohm = (nidmm.Function.TWO_WIRE_RES, 10000)
    TWO_W_RES_100k_Ohm = (nidmm.Function.TWO_WIRE_RES, 100000)
    TWO_W_RES_1M_Ohm = (nidmm.Function.TWO_WIRE_RES, 1000000)
    TWO_W_RES_10M_Ohm = (nidmm.Function.TWO_WIRE_RES, 10000000)
    TWO_W_RES_100M_Ohm = (nidmm.Function.TWO_WIRE_RES, 100000000)
    TWO_W_RES_5G_Ohm = (nidmm.Function.TWO_WIRE_RES, 5000000000)

    FOUR_W_Resistance_Auto_Range = (nidmm.Function.FOUR_WIRE_RES, -1.0)
    FOUR_W_RES_100_Ohm = (nidmm.Function.FOUR_WIRE_RES, 100)
    FOUR_W_RES_1k_Ohm = (nidmm.Function.FOUR_WIRE_RES, 1000)
    FOUR_W_RES_10k_Ohm = (nidmm.Function.FOUR_WIRE_RES, 10000)
    FOUR_W_RES_100k_Ohm = (nidmm.Function.FOUR_WIRE_RES, 100000)
    FOUR_W_RES_1M_Ohm = (nidmm.Function.FOUR_WIRE_RES, 1000000)
    FOUR_W_RES_10M_Ohm = (nidmm.Function.FOUR_WIRE_RES, 10000000)


class ResistanceMeasurementFunctionParameters:
    """Defines parameters used for configuration of resistance measurement.."""

    def __init__(
        self,
        measurement_function: ResistanceRangeAndFunctions,
        resolution_in_digits: ResolutionInDigits,
    ) -> None:
        """Initializes measurement function parameters.

        Args:
            measurement_function (ResistanceRangeAndFunctions):
                The resistance measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        """
        self._measurement_function = measurement_function
        self._resolution_in_digits = resolution_in_digits

    @property
    def measurement_function(self) -> ResistanceRangeAndFunctions:
        """Gets the resistance measurement function and range setting.

        Returns:
            ResistanceRangeAndFunctions: The configured resistance range and function.
        """
        return self._measurement_function

    @property
    def resolution_in_digits(self) -> ResolutionInDigits:
        """Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        """
        return self._resolution_in_digits


class ResistanceMeasurementConfiguration(PCBATestToolkitData):
    """Defines configuration parameters for resistance measurements."""

    def __init__(
        self,
        execution_type: MeasurementExecutionType,
        measurement_function_parameters: ResistanceMeasurementFunctionParameters,
        trigger_parameters: TriggerParameters,
        timing_parameters: TimingParameters,
        ac_min_frequency: float,
    ) -> None:
        """Initializes the resistance measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (ResistanceMeasurementFunctionParameters):
                The measurement function settings including resistance range and resolution.
            trigger_parameters (TriggerParameters):
                Trigger configuration including source, delay, and enable/disable settings.
            timing_parameters (TimingParameters):
                Timing settings including aperture time and settle time.
            ac_min_frequency (float):
                Minimum frequency for AC voltage measurements in Hz (ignored for DC measurements).
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
    def measurement_function_parameters(self) -> ResistanceMeasurementFunctionParameters:
        """Gets the measurement function parameters.

        Returns:
            ResistanceMeasurementFunctionParameters: The resistance range, function,
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
            float: The minimum frequency for AC voltage measurements.
        """
        return self._ac_min_frequency


class ResistanceMeasurementResultData(PCBATestToolkitData):
    """Defines resistance measurement results obtained from DMM Resistance Measurement."""

    def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None:
        """Initializes the resistance measurement result data.

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
