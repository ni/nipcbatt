# pylint: disable=C0301
""" Temperature data types"""

from enum import Enum
from typing import List

import nidaqmx.constants
from varname import nameof

from nipcbatt.pcbatt_library.common.common_data_types import (
    AnalogWaveform,
    DigitalStartTriggerParameters,
    MeasurementExecutionType,
    SampleClockTimingParameters,
)
from nipcbatt.pcbatt_library_core.pcbatt_data_types import PCBATestToolkitData
from nipcbatt.pcbatt_utilities.guard_utilities import Guard


class TemperatureRtdMeasurementTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for temperature measurement using RTD."""

    def __init__(
        self,
        temperature_minimum_value_celsius_degrees: float,
        temperature_maximum_value_celsius_degrees: float,
        current_excitation_value_amperes: float,
        sensor_resistance_ohms: float,
        rtd_type: nidaqmx.constants.RTDType,
        excitation_source: nidaqmx.constants.ExcitationSource,
        resistance_configuration: nidaqmx.constants.ResistanceConfiguration,
        adc_timing_mode: nidaqmx.constants.ADCTimingMode,
    ) -> None:
        """Initializes an instance of `TemperatureRtdMeasurementTerminalParameters`
           with specific values.

        Args:
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            current_excitation_value_amperes (float): The amount of excitation
                to supply to the sensor, in Amperes.
                Refer to the sensor documentation to determine this value.
            sensor_resistance_ohms (float): The sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
            rtd_type (nidaqmx.constants.RTDType):
                The type of `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
                connected to the channel.
            excitation_source (nidaqmx.constants.ExcitationSource): The source of excitation.
            resistance_configuration (nidaqmx.constants.ResistanceConfiguration): The mode
                that represents the number of `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
                to use for resistive measurements.
            adc_timing_mode (nidaqmx.constants.ADCTimingMode): The
                `ADC Timing Mode <https://www.ni.com/docs/en-US/bundle/ni-daqmx-properties/page/daqmxprop/attr29f9.html>`.

        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees'
                is greater than or equal to `temperature_maximum_value_celsius_degrees`.
        """
        Guard.is_less_than(
            temperature_minimum_value_celsius_degrees,
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )

        self._temperature_minimum_value_celsius_degrees = temperature_minimum_value_celsius_degrees
        self._temperature_maximum_value_celsius_degrees = temperature_maximum_value_celsius_degrees
        self._current_excitation_value_amperes = current_excitation_value_amperes
        self._sensor_resistance_ohms = sensor_resistance_ohms
        self._rtd_type = rtd_type
        self._excitation_source = excitation_source
        self._resistance_configuration = resistance_configuration
        self._adc_timing_mode = adc_timing_mode

    @property
    def temperature_minimum_value_celsius_degrees(self) -> float:
        """
        :type:`float`: Gets the minimum value expected from the measurement, expressed in °C.
        """
        return self._temperature_minimum_value_celsius_degrees

    @property
    def temperature_maximum_value_celsius_degrees(self) -> float:
        """
        :type:`float`: Gets the minimum value expected from the measurement, expressed in °C.
        """
        return self._temperature_maximum_value_celsius_degrees

    @property
    def current_excitation_value_amperes(self) -> float:
        """
        :type:`float`: Gets the amount of excitation to supply to the sensor, in Amperes.
        """
        return self._current_excitation_value_amperes

    @property
    def sensor_resistance_ohms(self) -> float:
        """
        :type:`float`: Gets the sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
        """
        return self._sensor_resistance_ohms

    @property
    def rtd_type(self) -> nidaqmx.constants.RTDType:
        """
        :type:`float`: Gets the type of
            `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
            connected to the channel.
        """
        return self._rtd_type

    @property
    def excitation_source(self) -> nidaqmx.constants.ExcitationSource:
        """
        :type:`float`: Gets the source of excitation.
        """
        return self._excitation_source

    @property
    def resistance_configuration(self) -> nidaqmx.constants.ResistanceConfiguration:
        """
        :type:`float`: Gets the mode
            that represents the number of
            `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
            to use for resistive measurements.
        """
        return self._resistance_configuration

    @property
    def adc_timing_mode(self) -> nidaqmx.constants.ADCTimingMode:
        """
        :type:`float`: Gets the `ADC Timing Mode
            <https://www.ni.com/docs/en-US/bundle/ni-daqmx-properties/page/daqmxprop/attr29f9.html>`.
        """
        return self._adc_timing_mode


class TemperatureRtdMeasurementChannelParameters(PCBATestToolkitData):
    """Defines the parameters used to configure channels for temperature measurement using RTD."""

    def __init__(
        self,
        channel_name: str,
        sensor_resistance_ohms: float,
        current_excitation_value_amperes: float,
        rtd_type: nidaqmx.constants.RTDType,
        resistance_configuration: nidaqmx.constants.ResistanceConfiguration,
        excitation_source: nidaqmx.constants.ExcitationSource,
    ) -> None:
        """_summary_

        Args:
            channel_name (str):
                The name of the channel to configure.
            sensor_resistance_ohms (float): The sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
            current_excitation_value_amperes (float): The amount of excitation
                to supply to the sensor, in Amperes.
                Refer to the sensor documentation to determine this value.
            rtd_type (nidaqmx.constants.RTDType):
                The type of `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
                connected to the channel.
            resistance_configuration (nidaqmx.constants.ResistanceConfiguration): The mode
                that represents the number of
                `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
                to use for resistive measurements.
            excitation_source (nidaqmx.constants.ExcitationSource): The source of excitation.

        Raises:
            ValueError:
                Raised when `channel_name` is None or empty or whitespace.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))

        self._channel_name = channel_name
        self._sensor_resistance_ohms = sensor_resistance_ohms
        self._current_excitation_value_amperes = current_excitation_value_amperes
        self._rtd_type = rtd_type
        self._resistance_configuration = resistance_configuration
        self._excitation_source = excitation_source

    @property
    def channel_name(self) -> str:
        """
        :type:`str`: Gets the name of the channel to configure.
        """
        return self._channel_name

    @property
    def sensor_resistance_ohms(self) -> float:
        """
        :type:`float`: Gets the sensor resistance, in Ohms,
                at 0 degree Celsius (also called R0).
        """
        return self._sensor_resistance_ohms

    @property
    def current_excitation_value_amperes(self) -> float:
        """
        :type:`float`: Gets the amount of excitation to supply to the sensor, in Amperes.
        """
        return self._current_excitation_value_amperes

    @property
    def rtd_type(self) -> nidaqmx.constants.RTDType:
        """
        :type:`float`: Gets the type of
            `RTD <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/rtdtypes.html>`
            connected to the channel.
        """
        return self._rtd_type

    @property
    def resistance_configuration(self) -> nidaqmx.constants.ResistanceConfiguration:
        """
        :type:`float`: Gets the mode
            that represents the number of
            `wires <https://en.wikipedia.org/wiki/Resistance_thermometer#Wiring_configurations>`
            to use for resistive measurements.
        """
        return self._resistance_configuration

    @property
    def excitation_source(self) -> nidaqmx.constants.ExcitationSource:
        """
        :type:`float`: Gets the source of excitation.
        """
        return self._excitation_source


class TemperatureRtdMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Temperature measurement using RTD."""

    def __init__(
        self,
        global_channel_parameters: TemperatureRtdMeasurementTerminalParameters,
        specific_channels_parameters: List[TemperatureRtdMeasurementChannelParameters],
        measurement_execution_type: MeasurementExecutionType,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureRtdMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (TemperatureRtdMeasurementTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[TemperatureRtdMeasurementChannelParameters]):
                The list of instances of `TemperatureRtdMeasurementChannelParameters`
                used to configure channels.
            measurement_execution_type (MeasurementExecutionType):
                The type of measurement execution selected by user.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of TemperatureRtdMeasurementChannelParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=TemperatureRtdMeasurementChannelParameters,
        )
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_execution_type = measurement_execution_type
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> TemperatureRtdMeasurementTerminalParameters:
        """
        :class:`TemperatureRtdMeasurementChannelParameters`:
            Gets the settings of terminal for all channels."""
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[TemperatureRtdMeasurementChannelParameters]:
        """
        :class:`List[VoltageMeasurementChannelAndTerminalRangeParameters]`:
            Gets the list of instances of
            `TemperatureRtdMeasurementChannelParameters` used to configure channels.
        """
        return self._specific_channels_parameters

    @property
    def measurement_execution_type(self) -> MeasurementExecutionType:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """
        return self._measurement_execution_type

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """
        return self._digital_start_trigger_parameters


class SteinhartHartEquationOption(Enum):
    """Defines the option of to use coefficients
    in Steinhart-Hart equation used during channels configuration."""

    USE_STEINHART_HART_COEFFICIENTS = 0
    """Use coefficients A, B and C of the
       `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation."""

    USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE = 1
    """Use the `β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and the sensor resistance."""


class CoefficientsSteinhartHartParameters(PCBATestToolkitData):
    """Defines the parameters used to configure coefficients of
    the <Steinhart-Hart https://en.wikipedia.org/wiki/Thermistor#Steinhart.E2.80.93Hart_equation>
    for Temperature measurements."""

    def __init__(
        self,
        coefficient_steinhart_hart_a: float,
        coefficient_steinhart_hart_b: float,
        coefficient_steinhart_hart_c: float,
    ) -> None:
        """Initializes an instance of
        `CoefficientsSteinhartHartParameters` with specific values.

        Args:
            coefficient_steinhart_hart_a (float): The A coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
            coefficient_steinhart_hart_b (float): The B coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
            coefficient_steinhart_hart_c (float): The C coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        """
        self._coefficient_steinhart_hart_a = coefficient_steinhart_hart_a
        self._coefficient_steinhart_hart_b = coefficient_steinhart_hart_b
        self._coefficient_steinhart_hart_c = coefficient_steinhart_hart_c

    @property
    def coefficient_steinhart_hart_a(self) -> float:
        """
        :type:`float`:
            Gets the A coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        """
        return self._coefficient_steinhart_hart_a

    @property
    def coefficient_steinhart_hart_b(self) -> float:
        """
        :type:`float`:
            Gets the B coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        """
        return self._coefficient_steinhart_hart_b

    @property
    def coefficient_steinhart_hart_c(self) -> float:
        """
        :type:`float`:
            Gets the C coefficient in the
            `Steinhart-Hart <https://en.wikipedia.org/wiki/Steinhart%E2%80%93Hart_equation>` equation.
        """
        return self._coefficient_steinhart_hart_c


class BetaCoefficientAndSensorResistanceParameters(PCBATestToolkitData):
    """Defines the parameters for coefficients
    (`β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and sensor resistance)
    of Steinhart-Hart equation."""

    def __init__(
        self,
        coefficient_steinhart_hart_beta_kelvins: float,
        sensor_resistance_ohms: float,
    ) -> None:
        """Initializes an instance of
        `BetaCoefficientAndSensorResistanceParameters` with specific values.

        Args:
            coefficient_steinhart_hart_beta_kelvins (float):
            The `β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>`
            used with the Steinhart-Hart equation, in Kelvins.
            Coefficients A, B and C of the equation are computed from this coefficient.
            sensor_resistance_ohms (float):
            The sensor resistance, in Ohms, at 25 degrees Celsius (298.15 Kelvins).
            Coefficients A, B and C of the equation are computed from this coefficient.
        """
        self._coefficient_steinhart_hart_beta_kelvins = coefficient_steinhart_hart_beta_kelvins
        self._sensor_resistance_ohms = sensor_resistance_ohms

    @property
    def coefficient_steinhart_hart_beta_kelvins(self) -> float:
        """
        :type:`float`:
            Gets the `β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>`
            used with the Steinhart-Hart equation, in Kelvins.
            Coefficients A, B and C of the equation are computed from this coefficient.
        """
        return self._coefficient_steinhart_hart_beta_kelvins

    @property
    def sensor_resistance_ohms(self) -> float:
        """
        :type:`float`:
            Gets the sensor resistance, in Ohms, at 25 degrees Celsius (298.15 Kelvins).
            Coefficients A, B and C of the equation are computed from this coefficient.
        """
        return self._sensor_resistance_ohms


class TemperatureThermistorRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for temperature measurement using Thermistor."""

    def __init__(
        self,
        terminal_configuration: nidaqmx.constants.TerminalConfiguration,
        temperature_minimum_value_celsius_degrees: float,
        temperature_maximum_value_celsius_degrees: float,
        voltage_excitation_value_volts: float,
        thermistor_resistor_ohms: float,
        steinhart_hart_equation_option: SteinhartHartEquationOption,
        coefficients_steinhart_hart_parameters: CoefficientsSteinhartHartParameters,
        beta_coefficient_and_sensor_resistance_parameters: BetaCoefficientAndSensorResistanceParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermistorRangeAndTerminalParameters` with specific values.

        Args:
            terminal_configuration (nidaqmx.constants.TerminalConfiguration):
                The input terminal configuration parameter.
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            voltage_excitation_value_volts (float):
                The amount of voltage excitation to supply to the sensor, expressed in Volts.
                Refer to the sensor documentation to determine this value.
            thermistor_resistor_ohms (float):
                The reference resistor for the
                `thermistor <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/thermistors.html>`
                if you use voltage excitation, in Ohms.
            steinhart_hart_equation_option (SteinhartHartEquationOption):
                The option used to compute coefficients of Steinhart-Hart equation.
            coefficients_steinhart_hart_parameters (CoefficientsSteinhartHartParameters):
                An instance of `CoefficientsSteinhartHartParameters`
                representing the coefficients of the SteinHart-Hart equation.
            beta_coefficient_and_sensor_resistance_parameters (BetaCoefficientAndSensorResistanceParameters):
                An instance of `BetaCoefficientAndSensorResistanceParameters`
                representing the coefficients
                (`β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and sensor resistance)
                of Steinhart-Hart equation.

        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees`
                is greater than or equal to `temperature_maximum_value_celsius_degrees`,
                `coefficients_steinhart_hart_parameters` is None
                and `steinhart_hart_equation_option` is equal to
                `SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS`,
                `beta_coefficient_and_sensor_resistance_parameters` is None
                and `steinhart_hart_equation_option` is equal to
                `SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE`.
        """
        Guard.is_less_than(
            temperature_minimum_value_celsius_degrees,
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        if (
            steinhart_hart_equation_option
            == SteinhartHartEquationOption.USE_STEINHART_HART_COEFFICIENTS
        ):
            Guard.is_not_none(
                coefficients_steinhart_hart_parameters,
                nameof(coefficients_steinhart_hart_parameters),
            )
        if (
            steinhart_hart_equation_option
            == SteinhartHartEquationOption.USE_COEFFICIENT_BETA_AND_SENSOR_RESISTANCE
        ):
            Guard.is_not_none(
                beta_coefficient_and_sensor_resistance_parameters,
                nameof(beta_coefficient_and_sensor_resistance_parameters),
            )

        self._terminal_configuration = terminal_configuration
        self._temperature_minimum_value_celsius_degrees = temperature_minimum_value_celsius_degrees
        self._temperature_maximum_value_celsius_degrees = temperature_maximum_value_celsius_degrees
        self._voltage_excitation_value_volts = voltage_excitation_value_volts
        self._thermistor_resistor_ohms = thermistor_resistor_ohms
        self._steinhart_hart_equation_option = steinhart_hart_equation_option
        self._coefficients_steinhart_hart_parameters = coefficients_steinhart_hart_parameters
        self._beta_coefficient_and_sensor_resistance_parameters = (
            beta_coefficient_and_sensor_resistance_parameters
        )

    @property
    def terminal_configuration(self) -> nidaqmx.constants.TerminalConfiguration:
        """
        :class:`nidaqmx.constants.TerminalConfiguration`:
            Gets the input terminal configuration parameter.
        """
        return self._terminal_configuration

    @property
    def temperature_minimum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the minimum value expected from the measurement, expressed in °C.
        """
        return self._temperature_minimum_value_celsius_degrees

    @property
    def temperature_maximum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the maximum value expected from the measurement, expressed in °C.
        """
        return self._temperature_maximum_value_celsius_degrees

    @property
    def voltage_excitation_value_volts(self) -> float:
        """
        :type:`float`:
            Gets the amount of voltage excitation to supply to the sensor, expressed in Volts.
            Refer to the sensor documentation to determine this value.
        """
        return self._voltage_excitation_value_volts

    @property
    def thermistor_resistor_ohms(self) -> float:
        """
        :type:`float`:
            Gets the reference resistor for the
            `thermistor <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/measfunds/thermistors.html>`
            if you use voltage excitation, in Ohms.
        """
        return self._thermistor_resistor_ohms

    @property
    def steinhart_hart_equation_option(self) -> SteinhartHartEquationOption:
        """
        :class:`SteinhartHartEquationOption`:
            Gets the option used to compute coefficients of Steinhart-Hart equation.
        """
        return self._steinhart_hart_equation_option

    @property
    def coefficients_steinhart_hart_parameters(
        self,
    ) -> CoefficientsSteinhartHartParameters:
        """
        :class:`CoefficientsSteinhartHartParameters`:
            Gets an instance of `CoefficientsSteinhartHartParameters`
            representing the coefficients of the SteinHart-Hart equation.
        """
        return self._coefficients_steinhart_hart_parameters

    @property
    def beta_coefficient_and_sensor_resistance_parameters(self):
        """
        :class:`BetaCoefficientAndSensorResistanceParameters`:
            Gets an instance of `BetaCoefficientAndSensorResistanceParameters`
            representing the coefficients
            (`β coefficient <https://en.wikipedia.org/wiki/Thermistor#B_or_.CE.B2_parameter_equation>` and sensor resistance)
            of Steinhart-Hart equation.
        """
        return self._beta_coefficient_and_sensor_resistance_parameters


class TemperatureThermistorChannelRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines settings for channel and terminal used to configure temperature measurement based on thermistor."""

    def __init__(
        self,
        channel_name: str,
        channel_parameters: TemperatureThermistorRangeAndTerminalParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermistorChannelRangeAndTerminalParameters` with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (TemperatureThermistorRangeAndTerminalParameters): The settings of the channel.

        Raises:
            ValueError:
                Raised when `channel_name` is None or empty or whitespace,
                `channel_parameters` is None.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_not_none(channel_parameters, nameof(channel_parameters))

        self._channel_name = channel_name
        self._channel_parameters = channel_parameters

    @property
    def channel_name(self) -> str:
        """
        :type:`str`:
            Gets the name of the channel to configure.
        """
        return self._channel_name

    @property
    def channel_parameters(self) -> TemperatureThermistorRangeAndTerminalParameters:
        """
        :class:`TemperatureThermistorRangeAndTerminalParameters`:
            Gets the settings of the channel.
        """
        return self._channel_parameters


class TemperatureThermistorMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Temperature measurement using Thermistor."""

    def __init__(
        self,
        global_channel_parameters: TemperatureThermistorRangeAndTerminalParameters,
        specific_channels_parameters: List[TemperatureThermistorChannelRangeAndTerminalParameters],
        measurement_execution_type: MeasurementExecutionType,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureRtdMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (TemperatureThermistorMeasurementTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[TemperatureThermistorChannelRangeAndTerminalParameters]):
                The list of instances of `TemperatureThermistorChannelRangeAndTerminalParameters`
                used to configure channels.
            measurement_execution_type (MeasurementExecutionType):
                The type of measurement execution selected by user.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of TemperatureThermistorChannelRangeAndTerminalParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=TemperatureThermistorChannelRangeAndTerminalParameters,
        )
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_execution_type = measurement_execution_type
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> TemperatureThermistorRangeAndTerminalParameters:
        """
        :class:`TemperatureThermistorRangeAndTerminalParameters`:
            Gets the settings of terminal for all channels.
        """
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[TemperatureThermistorChannelRangeAndTerminalParameters]:
        """
        :class:`List[TemperatureThermistorChannelRangeAndTerminalParameters]`:
            Gets the list of instances of `TemperatureThermistorChannelRangeAndTerminalParameters`
            used to configure channels.
        """
        return self._specific_channels_parameters

    @property
    def measurement_execution_type(self) -> MeasurementExecutionType:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """
        return self._measurement_execution_type

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """
        return self._digital_start_trigger_parameters


class TemperatureThermocoupleMeasurementTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for temperature measurement using Thermocouple."""

    def __init__(
        self,
        temperature_minimum_value_celsius_degrees: float,
        temperature_maximum_value_celsius_degrees: float,
        thermocouple_type: nidaqmx.constants.ThermocoupleType,
        cold_junction_compensation_temperature: float,
        perform_auto_zero_mode: bool,
        auto_zero_mode: nidaqmx.constants.AutoZeroType,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermocoupleMeasurementTerminalParameters` with specific values.

        Args:
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            thermocouple_type (nidaqmx.constants.ThermocoupleType):
                Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
            cold_junction_compensation_temperature (float):
                Specifies the temperature of the cold junction, expressed in °C;
                if cold_junction_compensation_source is set as 'CONSTANT_USER_VALUE'.
            perform_auto_zero_mode (bool):
                The option used to Enable or Disable Auto zero mode.
            auto_zero_mode (nidaqmx.constants.AutoZeroType):
                The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType


        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees`
                is greater than or equal to `temperature_maximum_value_celsius_degrees`,
                `temperature_minimum_value_celsius_degrees` is None or not float,
                `temperature_maximum_value_celsius_degrees` is None or not float,
                `thermocouple_type` is None,
                'cold_junction_compensation_temperature' is None or not float,
                'perform_auto_zero_mode' is None,
                if 'perform_auto_zero_mode' is True and 'auto_zero_mode' is None.

        """
        Guard.is_not_none(
            temperature_minimum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_float(
            temperature_minimum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_not_none(
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_maximum_value_celsius_degrees),
        )
        Guard.is_float(
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_maximum_value_celsius_degrees),
        )
        Guard.is_less_than(
            temperature_minimum_value_celsius_degrees,
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_not_none(
            thermocouple_type,
            nameof(thermocouple_type),
        )
        Guard.is_not_none(
            cold_junction_compensation_temperature,
            nameof(cold_junction_compensation_temperature),
        )
        Guard.is_float(
            cold_junction_compensation_temperature,
            nameof(cold_junction_compensation_temperature),
        )
        Guard.is_not_none(
            perform_auto_zero_mode,
            nameof(perform_auto_zero_mode),
        )
        if perform_auto_zero_mode is True:
            Guard.is_not_none(
                auto_zero_mode,
                nameof(auto_zero_mode),
            )

        self._temperature_minimum_value_celsius_degrees = temperature_minimum_value_celsius_degrees
        self._temperature_maximum_value_celsius_degrees = temperature_maximum_value_celsius_degrees
        self._thermocouple_type = thermocouple_type
        self._cold_junction_compensation_temperature = cold_junction_compensation_temperature
        self._perform_auto_zero_mode = perform_auto_zero_mode
        self._auto_zero_mode = auto_zero_mode

    @property
    def temperature_minimum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the minimum value expected from the measurement, expressed in °C.
        """
        return self._temperature_minimum_value_celsius_degrees

    @property
    def temperature_maximum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the maximum value expected from the measurement, expressed in °C.
        """
        return self._temperature_maximum_value_celsius_degrees

    @property
    def thermocouple_type(self) -> nidaqmx.constants.ThermocoupleType:
        """
        :type:`nidaqmx.constants.ThermocoupleType`:
            Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
            Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
        """
        return self._thermocouple_type

    @property
    def cold_junction_compensation_temperature(self) -> float:
        """
        :type:`float`:
           Cold junction compensation temperature, expressed in °C.
        """
        return self._cold_junction_compensation_temperature

    @property
    def perform_auto_zero_mode(self) -> bool:
        """
        :class:`bool`:
            The option used to Enable or Disable Auto zero mode.
        """
        return self._perform_auto_zero_mode

    @property
    def auto_zero_mode(
        self,
    ) -> nidaqmx.constants.AutoZeroType:
        """
        :class:`nidaqmx.constants.AutoZeroType`:
            The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType
        """
        return self._auto_zero_mode


class TemperatureThermocoupleRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines the parameters used to configure terminal
    of all channels for temperature measurement using Thermocouple."""

    def __init__(
        self,
        temperature_minimum_value_celsius_degrees: float,
        temperature_maximum_value_celsius_degrees: float,
        thermocouple_type: nidaqmx.constants.ThermocoupleType,
        cold_junction_compensation_source: nidaqmx.constants.CJCSource,
        cold_junction_compensation_temperature: float,
        cold_junction_compensation_channel_name: str,
        perform_auto_zero_mode: bool,
        auto_zero_mode: nidaqmx.constants.AutoZeroType,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermocoupleRangeAndTerminalParameters` with specific values.

        Args:
            temperature_minimum_value_celsius_degrees (float):
                The minimum value expected from the measurement, expressed in °C.
            temperature_maximum_value_celsius_degrees (float):
                The maximum value expected from the measurement, expressed in °C.
            thermocouple_type (nidaqmx.constants.ThermocoupleType):
                Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
            cold_junction_compensation_source (nidaqmx.constants.CJCSource):
                Specify the source for cold junction compensation: [CONSTANT_USER_VALUE, SCANNABLE_CHANNEL, BUILT_IN]
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.CJCSource
            cold_junction_compensation_temperature (float):
                Specifies the temperature of the cold junction, expressed in °C;
                if cold_junction_compensation_source is set as 'CONSTANT_USER_VALUE'.
            cold_junction_compensation_channel_name (str):
                Specifies the channel that acquires the temperature of the thermocouple cold-junction
                if cold_junction_compensation_source is set as 'SCANNABLE_CHANNEL'.
            perform_auto_zero_mode (bool):
                The option used to Enable or Disable Auto zero mode.
            auto_zero_mode (nidaqmx.constants.AutoZeroType):
                The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType


        Raises:
            ValueError:
                Raised when `temperature_minimum_value_celsius_degrees`
                is greater than or equal to `temperature_maximum_value_celsius_degrees`,
                `temperature_minimum_value_celsius_degrees` is None or not float,
                `temperature_maximum_value_celsius_degrees` is None or not float,
                `thermocouple_type` is None,
                'cold_junction_compensation_source' is None,
                if cold_junction_compensation_source==CONSTANT_USER_VALUE, then
                    'cold_junction_compensation_temperature' is None or not float,
                if cold_junction_compensation_source==SCANNABLE_CHANNEL, then
                    'cold_junction_compensation_channel_name' is None, empty or whitespace,
                'perform_auto_zero_mode' is None,
                if 'perform_auto_zero_mode' is True and 'auto_zero_mode' is None.

        """
        Guard.is_not_none(
            temperature_minimum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_float(
            temperature_minimum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_not_none(
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_maximum_value_celsius_degrees),
        )
        Guard.is_float(
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_maximum_value_celsius_degrees),
        )
        Guard.is_less_than(
            temperature_minimum_value_celsius_degrees,
            temperature_maximum_value_celsius_degrees,
            nameof(temperature_minimum_value_celsius_degrees),
        )
        Guard.is_not_none(
            thermocouple_type,
            nameof(thermocouple_type),
        )
        Guard.is_not_none(
            cold_junction_compensation_source,
            nameof(cold_junction_compensation_source),
        )
        if cold_junction_compensation_source == nidaqmx.constants.CJCSource.CONSTANT_USER_VALUE:
            Guard.is_not_none(
                cold_junction_compensation_temperature,
                nameof(cold_junction_compensation_temperature),
            )
            Guard.is_float(
                cold_junction_compensation_temperature,
                nameof(cold_junction_compensation_temperature),
            )
        if cold_junction_compensation_source == nidaqmx.constants.CJCSource.SCANNABLE_CHANNEL:
            Guard.is_not_none_nor_empty_nor_whitespace(
                cold_junction_compensation_channel_name,
                nameof(cold_junction_compensation_channel_name),
            )
        Guard.is_not_none(
            perform_auto_zero_mode,
            nameof(perform_auto_zero_mode),
        )
        if perform_auto_zero_mode is True:
            Guard.is_not_none(
                auto_zero_mode,
                nameof(auto_zero_mode),
            )

        self._temperature_minimum_value_celsius_degrees = temperature_minimum_value_celsius_degrees
        self._temperature_maximum_value_celsius_degrees = temperature_maximum_value_celsius_degrees
        self._thermocouple_type = thermocouple_type
        self._cold_junction_compensation_source = cold_junction_compensation_source
        self._cold_junction_compensation_temperature = cold_junction_compensation_temperature
        self._cold_junction_compensation_channel_name = cold_junction_compensation_channel_name
        self._perform_auto_zero_mode = perform_auto_zero_mode
        self._auto_zero_mode = auto_zero_mode

    @property
    def temperature_minimum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the minimum value expected from the measurement, expressed in °C.
        """
        return self._temperature_minimum_value_celsius_degrees

    @property
    def temperature_maximum_value_celsius_degrees(self) -> float:
        """
        :type:`float`:
            Gets the maximum value expected from the measurement, expressed in °C.
        """
        return self._temperature_maximum_value_celsius_degrees

    @property
    def thermocouple_type(self) -> nidaqmx.constants.ThermocoupleType:
        """
        :type:`nidaqmx.constants.ThermocoupleType`:
            Enum for ThermocoupleType: (B,E,J,K,N,R,S,T);
            Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.ThermocoupleType
        """
        return self._thermocouple_type

    @property
    def cold_junction_compensation_source(self) -> nidaqmx.constants.CJCSource:
        """
        :type:`nidaqmx.constants.CJCSource`:
           Cold junction compensation Source.
           Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.CJCSource
        """
        return self._cold_junction_compensation_source

    @property
    def cold_junction_compensation_temperature(self) -> float:
        """
        :type:`float`:
           Cold junction compensation temperature, expressed in °C.
        """
        return self._cold_junction_compensation_temperature

    @property
    def cold_junction_compensation_channel_name(self) -> str:
        """
        :type:`str`:
           Specify the channel to use for Cold junction compensation.
        """
        return self._cold_junction_compensation_channel_name

    @property
    def perform_auto_zero_mode(self) -> bool:
        """
        :class:`bool`:
            The option used to Enable or Disable Auto zero mode.
        """
        return self._perform_auto_zero_mode

    @property
    def auto_zero_mode(
        self,
    ) -> nidaqmx.constants.AutoZeroType:
        """
        :class:`nidaqmx.constants.AutoZeroType`:
            The option to set when to perform an auto zero during acquisition.
                Reference: https://nidaqmx-python.readthedocs.io/en/latest/constants.html#nidaqmx.constants.AutoZeroType
        """
        return self._auto_zero_mode


class TemperatureThermocoupleChannelRangeAndTerminalParameters(PCBATestToolkitData):
    """Defines settings for channel and terminal used to configure temperature measurement based on thermocouple."""

    def __init__(
        self,
        channel_name: str,
        channel_parameters: TemperatureThermocoupleRangeAndTerminalParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermocoupleChannelRangeAndTerminalParameters` with specific values.

        Args:
            channel_name (str):
                The name of the channel to configure.
            channel_parameters (TemperatureThermocoupleRangeAndTerminalParameters): The settings of the channel.

        Raises:
            ValueError:
                Raised when `channel_name` is None or empty or whitespace,
                `channel_parameters` is None.
        """
        Guard.is_not_none_nor_empty_nor_whitespace(channel_name, nameof(channel_name))
        Guard.is_not_none(channel_parameters, nameof(channel_parameters))

        self._channel_name = channel_name
        self._channel_parameters = channel_parameters

    @property
    def channel_name(self) -> str:
        """
        :type:`str`:
            Gets the name of the channel to configure.
        """
        return self._channel_name

    @property
    def channel_parameters(self) -> TemperatureThermocoupleRangeAndTerminalParameters:
        """
        :class:`TemperatureThermocoupleRangeAndTerminalParameters`:
            Gets the settings of the channel.
        """
        return self._channel_parameters


class TemperatureThermocoupleMeasurementConfiguration(PCBATestToolkitData):
    """Defines parameters used for configuration of Temperature measurement using Thermocouple."""

    def __init__(
        self,
        global_channel_parameters: TemperatureThermocoupleMeasurementTerminalParameters,
        specific_channels_parameters: List[
            TemperatureThermocoupleChannelRangeAndTerminalParameters
        ],
        measurement_execution_type: MeasurementExecutionType,
        sample_clock_timing_parameters: SampleClockTimingParameters,
        digital_start_trigger_parameters: DigitalStartTriggerParameters,
    ) -> None:
        """Initializes an instance of
        `TemperatureThermocoupleMeasurementConfiguration` with specific values.

        Args:
            global_channel_parameters (TemperatureThermocoupleMeasurementTerminalParameters):
                The settings of terminal for all channels.
            specific_channels_parameters (List[TemperatureThermocoupleChannelRangeAndTerminalParameters]):
                The list of instances of `TemperatureThermocoupleChannelRangeAndTerminalParameters`
                used to configure channels.
            measurement_execution_type (MeasurementExecutionType):
                The type of measurement execution selected by user.
            sample_clock_timing_parameters (SampleClockTimingParameters):
                An instance of `SampleClockTimingParameters` that represents the settings of timing.
            digital_start_trigger_parameters (DigitalStartTriggerParameters):
                An instance of `DigitalStartTriggerParameters`
                that represents the settings of triggers.

        Raises:
            TypeError:
                Raised when `specific_channels_parameters`
                contains objects that are not type of TemperatureThermocoupleChannelRangeAndTerminalParameters.
            ValueError:
                Raised when `global_channel_parameters` is None,
                `specific_channels_parameters` is None,
                `sample_clock_timing_parameters` is None,
                `digital_start_trigger_parameters` is None,
        """
        Guard.is_not_none(global_channel_parameters, nameof(global_channel_parameters))
        Guard.is_not_none(specific_channels_parameters, nameof(specific_channels_parameters))
        Guard.all_elements_are_of_same_type(
            input_list=specific_channels_parameters,
            expected_type=TemperatureThermocoupleChannelRangeAndTerminalParameters,
        )
        Guard.is_not_none(sample_clock_timing_parameters, nameof(sample_clock_timing_parameters))
        Guard.is_not_none(
            digital_start_trigger_parameters, nameof(digital_start_trigger_parameters)
        )

        self._global_channel_parameters = global_channel_parameters
        self._specific_channels_parameters = specific_channels_parameters
        self._measurement_execution_type = measurement_execution_type
        self._sample_clock_timing_parameters = sample_clock_timing_parameters
        self._digital_start_trigger_parameters = digital_start_trigger_parameters

    @property
    def global_channel_parameters(
        self,
    ) -> TemperatureThermocoupleMeasurementTerminalParameters:
        """
        :class:`TemperatureThermocoupleMeasurementTerminalParameters`:
            Gets the settings of terminal for all channels.
        """
        return self._global_channel_parameters

    @property
    def specific_channels_parameters(
        self,
    ) -> List[TemperatureThermocoupleChannelRangeAndTerminalParameters]:
        """
        :class:`List[TemperatureThermocoupleChannelRangeAndTerminalParameters]`:
            Gets the list of instances of `TemperatureThermocoupleChannelRangeAndTerminalParameters`
            used to configure channels.
        """
        return self._specific_channels_parameters

    @property
    def measurement_execution_type(self) -> MeasurementExecutionType:
        """
        :class:`MeasurementExecutionType`:
            Gets the type of measurement execution selected by user.
        """
        return self._measurement_execution_type

    @property
    def sample_clock_timing_parameters(self) -> SampleClockTimingParameters:
        """
        :class:`SampleClockTimingParameters`:
            Gets a `SampleClockTimingParameters` instance
            that represents the settings of timing.
        """
        return self._sample_clock_timing_parameters

    @property
    def digital_start_trigger_parameters(self) -> DigitalStartTriggerParameters:
        """
        :class:`DigitalStartTriggerParameters`:
            Gets a `DigitalStartTriggerParameters` instance
            that represents the settings of triggers.
        """
        return self._digital_start_trigger_parameters


class TemperatureMeasurementResultData(PCBATestToolkitData):
    """Defines voltage temperature results obtained after waveform analysis."""

    def __init__(
        self,
        waveforms: List[AnalogWaveform],
        acquisition_duration_seconds: float,
        average_temperatures_celsius_degrees: List[float],
        average_temperatures_kelvin: List[float],
    ) -> None:
        """Initializes an instance of
           `TemperatureMeasurementResultData` with specific values.

        Args:
            waveforms (List[AnalogWaveform]):
                The list of waveforms acquired from channels defined for measurement
                and used to compute temperature.
            acquisition_duration_seconds (float):
                The duration of acquisition of samples for each configured channel.
            average_temperatures_celsius_degrees (List[float]):
                The list of average temperatures computed for each configured channel,
                expressed in celsius degrees.
            average_temperatures_kelvin (List[float]):
                The list of average temperatures computed for each configured channel,
                expressed in kelvin.

        Raises:
            ValueError:
                Raised when `waveforms` is None or empty,
                `average_temperatures_celsius` is None or empty,
                `average_temperatures_kelvin` is None or empty,
            TypeError:
                Raised when `waveforms` contains objects that are not `AnalogWaveform`,
                `acquisition_duration_seconds' is None,
                If the `acquisition_duration_seconds' is less than or equal to zero,
                `average_temperatures_celsius_degrees` contains objects that are not `float`,
                `average_temperatures_kelvin` contains objects that are not `float`
        """
        Guard.is_not_none(waveforms, nameof(waveforms))
        Guard.is_not_empty(waveforms, nameof(waveforms))
        Guard.is_not_none(
            acquisition_duration_seconds,
            nameof(acquisition_duration_seconds),
        )
        Guard.is_greater_than_zero(
            acquisition_duration_seconds, nameof(acquisition_duration_seconds)
        )
        Guard.is_not_none(
            average_temperatures_celsius_degrees,
            nameof(average_temperatures_celsius_degrees),
        )
        Guard.is_not_empty(
            average_temperatures_celsius_degrees,
            nameof(average_temperatures_celsius_degrees),
        )
        Guard.is_not_none(average_temperatures_kelvin, nameof(average_temperatures_kelvin))
        Guard.is_not_empty(average_temperatures_kelvin, nameof(average_temperatures_kelvin))
        Guard.all_elements_are_of_same_type(input_list=waveforms, expected_type=AnalogWaveform)
        Guard.all_elements_are_of_same_type(
            input_list=average_temperatures_celsius_degrees, expected_type=float
        )
        Guard.all_elements_are_of_same_type(
            input_list=average_temperatures_kelvin, expected_type=float
        )

        self._waveforms = waveforms
        self._acquisition_duration_seconds = acquisition_duration_seconds
        self._average_temperatures_celsius_degrees = average_temperatures_celsius_degrees
        self._average_temperatures_kelvin = average_temperatures_kelvin

    @property
    def waveforms(self) -> List[AnalogWaveform]:
        """
        :class:`List[AnalogWaveform]`:
            Gets list of waveforms acquired from channels defined for measurement
            and used to compute temperature.
        """
        return self._waveforms

    @property
    def acquisition_duration_seconds(self) -> float:
        """
        :type:`float`:
            Gets the duration of acquisition of samples for each configured channel.
        """
        return self._acquisition_duration_seconds

    @property
    def average_temperatures_celsius_degrees(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of average temperatures computed for each configured channel,
            expressed in celsius degrees.
        """
        return self._average_temperatures_celsius_degrees

    @property
    def average_temperatures_kelvin(self) -> List[float]:
        """
        :class:`List[float]`:
            Gets the list of average temperatures computed for each configured channel,
            expressed in kelvins.
        """
        return self._average_temperatures_kelvin
