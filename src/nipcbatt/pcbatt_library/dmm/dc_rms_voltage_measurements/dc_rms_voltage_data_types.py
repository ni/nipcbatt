"""DC-RMS voltage data types."""

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


class VoltageRangeAndFunctions(Enum):
    """Defines the measurement function and range settings for voltage measurement."""

    DC_Voltage_Auto_Range = (nidmm.Function.DC_VOLTS, -1.0)
    DC_100mV = (nidmm.Function.DC_VOLTS, 0.1)
    DC_1V = (nidmm.Function.DC_VOLTS, 1)
    DC_10V = (nidmm.Function.DC_VOLTS, 10)
    DC_100V = (nidmm.Function.DC_VOLTS, 100)
    DC_300V = (nidmm.Function.DC_VOLTS, 300)

    AC_Voltage_Auto_Range = (nidmm.Function.AC_VOLTS, -1.0)
    AC_50mV = (nidmm.Function.AC_VOLTS, 0.05)
    AC_200mV = (nidmm.Function.AC_VOLTS, 0.2)
    AC_500mV = (nidmm.Function.AC_VOLTS, 0.5)
    AC_2V = (nidmm.Function.AC_VOLTS, 2)
    AC_5V = (nidmm.Function.AC_VOLTS, 5)
    AC_20V = (nidmm.Function.AC_VOLTS, 20)
    AC_50V = (nidmm.Function.AC_VOLTS, 50)
    AC_300V = (nidmm.Function.AC_VOLTS, 300)


class DcRmsVoltageMeasurementFunctionParameters(PCBATestToolkitData):
    """Defines parameters used for configuration of DC-RMS voltage measurement."""

    def __init__(
        self,
        measurement_function: VoltageRangeAndFunctions,
        resolution_in_digits: ResolutionInDigits,
    ) -> None:
        """Initializes measurement function parameters.

        Args:
            measurement_function (VoltageRangeAndFunctions):
                The voltage measurement function and range setting.
            resolution_in_digits (ResolutionInDigits):
                The measurement resolution in digits.
        """
        self._measurement_function = measurement_function
        self._resolution_in_digits = resolution_in_digits

    @property
    def measurement_function(self) -> VoltageRangeAndFunctions:
        """Gets the voltage measurement function and range setting.

        Returns:
            VoltageRangeAndFunctions: The configured voltage range and function.
        """
        return self._measurement_function

    @property
    def resolution_in_digits(self) -> ResolutionInDigits:
        """Gets the measurement resolution in digits.

        Returns:
            ResolutionInDigits: The configured resolution setting.
        """
        return self._resolution_in_digits


class DcRmsVoltageMeasurementConfiguration(PCBATestToolkitData):
    """Defines configuration parameters for voltage DC-RMS measurements."""

    def __init__(
        self,
        execution_type: MeasurementExecutionType,
        measurement_function_parameters: DcRmsVoltageMeasurementFunctionParameters,
        trigger_parameters: TriggerParameters,
        timing_parameters: TimingParameters,
        ac_min_frequency: float,
    ) -> None:
        """Initializes the voltage measurement configuration.

        Args:
            execution_type (MeasurementExecutionType):
                Specifies whether to configure only, measure only, or both configure and measure.
            measurement_function_parameters (DcRmsVoltageMeasurementFunctionParameters):
                The measurement function settings including voltage range and resolution.
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
    def measurement_function_parameters(self) -> DcRmsVoltageMeasurementFunctionParameters:
        """Gets the measurement function parameters.

        Returns:
            DcRmsVoltageMeasurementFunctionParameters: The voltage range, function,
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


class DcRmsVoltageMeasurementResultData(PCBATestToolkitData):
    """Defines voltage DC-RMS results obtained from DMM DC-RMS Voltage Measurement."""

    def __init__(self, dmm_execution_settings: dict, measurement: Union[dict, None]) -> None:
        """Initializes the voltage measurement result data.

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
