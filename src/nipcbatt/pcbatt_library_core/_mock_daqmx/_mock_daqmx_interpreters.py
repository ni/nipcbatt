"""Provides mock version of nidaqmx interpreter and a set of interpreter classes related to Measurements."""  # noqa: W505 - doc line too long (108 > 100 characters) (auto-generated noqa)

import random
from enum import Enum
from typing import Any, Dict

import nidaqmx.constants
import nidaqmx.errors
import nidaqmx.utils
from nidaqmx._library_interpreter import LibraryInterpreter
from nidaqmx._task_modules.channels.channel import ChannelType

from nipcbatt.pcbatt_library_core._mock_daqmx._mock_daqmx_constants import (
    _DAQMX_ATTRIBUTES,
    _ConstantsForMockDAQmx,
)


class _MockInterpreter(LibraryInterpreter):
    """The interpreter defines methods used for interactions with DAQmx.
    During call of methods related to DAQmx (from Task, AIChannelCollection, Timing,...),
    a call of the interpreter occurs.
    Example when calling the method `add_ai_voltage_chan` of AIChannelCollection, the method
    `create_ai_voltage_chan` of the interpreter is called.
    """  # noqa: D205, W505 - 1 blank line required between summary line and description (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

    def __init__(self):
        super().__init__()
        self._analog_input_channels = {}
        self._digital_input_channels = {}
        self._counter_input_channels = {}
        self._analog_output_channels = {}
        self._digital_output_channels = {}
        self._counter_output_channels = {}
        self._timing = {}

    def create_task(self, session_name):
        """Called when the task is about to be created."""
        return id(self), True

    def get_task_attribute_string(self, task, attribute):
        """Called when invoke properties `nidaqmx.Task.name` or `nidaqmx.Task.channel_names`."""
        if attribute == 0x1276:
            # returns the task name.
            return ""
        if attribute == 0x1273:
            # returns the names of channels defined in task.
            channels = []
            channels.extend(list(self._analog_input_channels))
            channels.extend(list(self._analog_output_channels))
            channels.extend(list(self._digital_input_channels))
            channels.extend(list(self._digital_output_channels))
            channels.extend(list(self._counter_input_channels))
            channels.extend(list(self._counter_output_channels))

            return nidaqmx.utils.flatten_channel_string(channels)

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_task_attribute_uint32(self, task, attribute):
        """Called when invoke properties `nidaqmx.Task.number_of_channels`."""
        if attribute == 0x2181:
            # returns the number of channels defined in task.
            return (
                len(self._analog_input_channels)
                + len(self._analog_output_channels)
                + len(self._digital_input_channels)
                + len(self._digital_output_channels)
                + len(self._counter_input_channels)
                + len(self._counter_output_channels)
            )

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_read_attribute_string(self, task, attribute):
        """Called when invoke property `nidaqmx.Task.in_stream.channels_to_read`."""
        if attribute == 0x1823:
            # returns the names of channels defined in task.in_stream.
            channels = []
            channels.extend(list(self._analog_input_channels))
            channels.extend(list(self._digital_input_channels))
            channels.extend(list(self._counter_input_channels))

            return nidaqmx.utils.flatten_channel_string(channels)

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_read_attribute_uint32(self, task, attribute):
        """Called when invoke property `nidaqmx.Task.in_stream.di_num_booleans_per_chan`"""  # noqa: D202, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (279 > 100 characters) (auto-generated noqa)

        if attribute == 0x217C:
            number_of_booleans_per_channel = 0
            for channel_name in self._digital_input_channels:
                number_of_booleans_per_channel = max(
                    number_of_booleans_per_channel,
                    len(nidaqmx.utils.unflatten_channel_string(channel_name)),
                )
            return number_of_booleans_per_channel

    def get_write_attribute_uint32(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.out_stream.OutStream`."""
        if attribute == 0x217E:
            # returns the number of channels defined in task.out_stream.
            channels = []
            channels.extend(list(self._analog_output_channels))
            channels.extend(list(self._digital_output_channels))
            channels.extend(list(self._counter_output_channels))

            return len(channels)

        if attribute == 0x217F:
            # returns the number of channels defined in task.out_stream.
            number_of_booleans_per_channel = 0
            for channel_name in self._digital_output_channels:
                number_of_booleans_per_channel = max(
                    number_of_booleans_per_channel,
                    len(nidaqmx.utils.unflatten_channel_string(channel_name)),
                )

            return number_of_booleans_per_channel

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_system_info_attribute_string(self, attribute):
        """Called when invoke property nidaqmx.system.System.local().global_channels"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (198 > 100 characters) (auto-generated noqa)
        if attribute == 0x1265:
            # returns an expression describing the global channels defined in mock system.
            return ""

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    def get_chan_attribute_int32(self, task, channel: str, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self._get_attribute_value_from_channel_settings(channel, attribute)

    def get_chan_attribute_double(self, task, channel, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self._get_attribute_value_from_channel_settings(channel, attribute)

    def get_chan_attribute_string(self, task, channel, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        return self._get_attribute_value_from_channel_settings(channel, attribute)

    def get_timing_attribute_uint64(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        return _MockInterpreter._retrieve_attribute_value(self._timing, attribute)

    def get_timing_attribute_uint32(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        return _MockInterpreter._retrieve_attribute_value(self._timing, attribute)

    def get_timing_attribute_int32(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        return _MockInterpreter._retrieve_attribute_value(self._timing, attribute)

    def get_timing_attribute_double(self, task, attribute):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        return _MockInterpreter._retrieve_attribute_value(self._timing, attribute)

    def set_timing_attribute_uint32(self, task, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        _MockInterpreter._assign_attribute_value(self._timing, attribute, value)

    def set_timing_attribute_int32(self, task, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        _MockInterpreter._assign_attribute_value(self._timing, attribute, value)

    def set_timing_attribute_uint64(self, task, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.timing.Timing`."""
        _MockInterpreter._assign_attribute_value(self._timing, attribute, value)

    def set_chan_attribute_string(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def set_chan_attribute_int32(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def set_chan_attribute_uint32(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def set_chan_attribute_double(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def set_chan_attribute_bool(self, task, channel, attribute, value):
        """Called when invoke properties of `nidaqmx._task_modules.channels.channel.Channel`
        and its inherited classes (AIChannel, AOChannel, DIChannel,
        DOChannel, CIChannel and COChannel).
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        self._set_attribute_value_to_channel_settings(channel, attribute, value)

    def create_ai_voltage_chan(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        terminal_config,
        min_val,
        max_val,
        units,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_voltage_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.TERMINAL_CONFIG] = terminal_config
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.AI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAI.VOLTAGE.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_ai_current_chan(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        terminal_config,
        min_val,
        max_val,
        units,
        shunt_resistor_loc,
        ext_shunt_resistor_val,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_current_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.TERMINAL_CONFIG] = terminal_config
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.SHUNT_RESISTOR_LOC] = shunt_resistor_loc
            channel[_ConstantsForMockDAQmx.EXT_SHUNT_RESISTOR_VAL] = ext_shunt_resistor_val
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.AI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAI.VOLTAGE.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_ai_power_chan(
        self,
        task,
        physical_channel,
        voltage_setpoint,
        current_setpoint,
        output_enable,
        name_to_assign_to_channel,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_power_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.VOLTAGE_SETPOINT] = voltage_setpoint
            channel[_ConstantsForMockDAQmx.CURRENT_SETPOINT] = current_setpoint
            channel[_ConstantsForMockDAQmx.OUTPUT_ENABLE] = output_enable
            channel[_ConstantsForMockDAQmx.POWER_SENSE] = nidaqmx.constants.Sense.LOCAL.value
            channel[
                _ConstantsForMockDAQmx.PWR_IDLE_OUTPUT_BEHAVIOR
            ] = nidaqmx.constants.PowerIdleOutputBehavior.MAINTAIN_EXISTING_VALUE.value
            channel[_ConstantsForMockDAQmx.AI_MEAS_TYPE] = nidaqmx.constants.UsageTypeAI.POWER.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_airtd_chan(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        rtd_type,
        resistance_config,
        current_excit_source,
        current_excit_val,
        r_0,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_rtd_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.RTD_TYPE] = rtd_type
            channel[_ConstantsForMockDAQmx.RESISTANCE_CONFIG] = resistance_config
            channel[_ConstantsForMockDAQmx.EXCIT_SOURCE] = current_excit_source
            channel[_ConstantsForMockDAQmx.EXCIT_VAL] = current_excit_val
            channel[_ConstantsForMockDAQmx.R_0] = r_0
            channel[
                _ConstantsForMockDAQmx.AI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAI.TEMPERATURE_RTD.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_ai_thrmstr_chan_vex(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        resistance_config,
        voltage_excit_source,
        voltage_excit_val,
        a,
        b,
        c,
        r_1,
    ):
        """Called when method
        `nidaqmx._task_modules.ai_channel_collection.AIChannelCollection.add_ai_thrmstr_chan_vex`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_input_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[
                _ConstantsForMockDAQmx.TERMINAL_CONFIG
            ] = nidaqmx.constants.TerminalConfiguration.DEFAULT.value
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.RESISTANCE_CONFIG] = resistance_config
            channel[_ConstantsForMockDAQmx.EXCIT_SOURCE] = voltage_excit_source
            channel[_ConstantsForMockDAQmx.EXCIT_VAL] = voltage_excit_val
            channel[_ConstantsForMockDAQmx.THRMSTR_A] = a
            channel[_ConstantsForMockDAQmx.THRMSTR_B] = b
            channel[_ConstantsForMockDAQmx.THRMSTR_C] = c
            channel[_ConstantsForMockDAQmx.R_1] = r_1
            channel[
                _ConstantsForMockDAQmx.AI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAI.TEMPERATURE_THERMISTOR.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_INPUT.value

            self._analog_input_channels[physical_channel_name] = channel

    def create_ao_voltage_chan(
        self,
        task,
        physical_channel,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ao_channel_collection.AOChannelCollection.add_ao_voltage_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        physical_channels_names = nidaqmx.utils.unflatten_channel_string(physical_channel)
        for physical_channel_name in physical_channels_names:
            channel = (
                self._analog_output_channels[physical_channel_name]
                if physical_channel_name in self._analog_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = physical_channel_name
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.AO_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeAO.VOLTAGE.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.ANALOG_OUTPUT.value

            self._analog_output_channels[physical_channel_name] = channel

    def create_di_chan(self, task, lines, name_to_assign_to_lines, line_grouping):
        """Called when method
        `nidaqmx._task_modules.di_channel_collection.DIChannelCollection.add_di_chan`
        is called."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (391 > 100 characters) (auto-generated noqa)

        if "/line" not in lines:
            raise nidaqmx.errors.DaqError(
                _ConstantsForMockDAQmx.NO_LINE_DEFINED_IN_CHANNEL, -200376
            )

        line_grouping_value = nidaqmx.constants.LineGrouping(line_grouping)
        if line_grouping_value == nidaqmx.constants.LineGrouping.CHAN_FOR_ALL_LINES:
            channel = (
                self._digital_input_channels[lines] if lines in self._digital_input_channels else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = lines
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.DIGITAL_INPUT.value
            self._digital_input_channels[lines] = channel
        else:
            lines_names = nidaqmx.utils.unflatten_channel_string(lines)
            for line_name in lines_names:
                channel = (
                    self._digital_input_channels[line_name]
                    if line_name in self._digital_input_channels
                    else {}
                )
                channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = line_name
                channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.DIGITAL_INPUT.value
                self._digital_input_channels[line_name] = channel

    def create_do_chan(self, task, lines, name_to_assign_to_lines, line_grouping):
        """Called when method
        `nidaqmx._task_modules.do_channel_collection.DOChannelCollection.add_do_chan`
        is called."""  # noqa: D202, D205, D209, D415, W505 - No blank lines allowed after function docstring (auto-generated noqa), 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (391 > 100 characters) (auto-generated noqa)

        if "/line" not in lines:
            raise nidaqmx.errors.DaqError(
                _ConstantsForMockDAQmx.NO_LINE_DEFINED_IN_CHANNEL, -200376
            )

        line_grouping_value = nidaqmx.constants.LineGrouping(line_grouping)
        if line_grouping_value == nidaqmx.constants.LineGrouping.CHAN_FOR_ALL_LINES:
            channel = (
                self._digital_output_channels[lines]
                if lines in self._digital_output_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.DIGITAL_OUTPUT.value
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = lines
            self._digital_output_channels[lines] = channel
        else:
            lines_names = nidaqmx.utils.unflatten_channel_string(lines)
            for line_name in lines_names:
                channel = (
                    self._digital_output_channels[line_name]
                    if line_name in self._digital_output_channels
                    else {}
                )
                channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = line_name
                channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.DIGITAL_OUTPUT.value
                self._digital_output_channels[line_name] = channel

    def create_ci_count_edges_chan(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        edge,
        initial_count,
        count_direction,
    ):
        """Called when method
        `nidaqmx._task_modules.ci_channel_collection.CIChannelCollection.add_ci_count_edges_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_input_channels[counter_channel_name]
                if counter_channel_name in self._counter_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.COUNT_EDGES_ACTIVE_EDGE] = edge
            channel[_ConstantsForMockDAQmx.INITIAL_COUNT] = initial_count
            channel[_ConstantsForMockDAQmx.COUNT_DIRECTION] = count_direction
            channel[
                _ConstantsForMockDAQmx.CI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCI.COUNT_EDGES.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_INPUT.value

            self._counter_input_channels[counter_channel_name] = channel

    def create_ci_freq_chan(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        edge,
        meas_method,
        meas_time,
        divisor,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ci_channel_collection.CIChannelCollection.add_ci_freq_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_input_channels[counter_channel_name]
                if counter_channel_name in self._counter_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.FREQ_STARTING_EDGE] = edge
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.MEAS_METHOD] = meas_method
            channel[_ConstantsForMockDAQmx.MEAS_TIME] = meas_time
            channel[_ConstantsForMockDAQmx.DIVISOR] = divisor
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.CI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCI.COUNT_EDGES.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_INPUT.value

            self._counter_input_channels[counter_channel_name] = channel

    def create_ci_semi_period_chan(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        min_val,
        max_val,
        units,
        custom_scale_name,
    ):
        """Called when method
        `nidaqmx._task_modules.ci_channel_collection.CIChannelCollection.add_ci_semi_period_chan`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_input_channels[counter_channel_name]
                if counter_channel_name in self._counter_input_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.MIN_VAL] = min_val
            channel[_ConstantsForMockDAQmx.MAX_VAL] = max_val
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.CUSTOM_SCALE_NAME] = custom_scale_name
            channel[
                _ConstantsForMockDAQmx.CI_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCI.PULSE_WIDTH_DIGITAL_SEMI_PERIOD.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_INPUT.value

            self._counter_input_channels[counter_channel_name] = channel

    def create_co_pulse_chan_freq(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        units,
        idle_state,
        initial_delay,
        freq,
        duty_cycle,
    ):
        """Called when method
        `nidaqmx._task_modules.co_channel_collection.COChannelCollection.add_co_pulse_chan_freq`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_output_channels[counter_channel_name]
                if counter_channel_name in self._counter_output_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.IDLE_STATE] = idle_state
            channel[_ConstantsForMockDAQmx.INITIAL_DELAY] = initial_delay
            channel[_ConstantsForMockDAQmx.PULSE_FREQ] = freq
            channel[_ConstantsForMockDAQmx.PULSE_DUTY_CYC] = duty_cycle
            channel[
                _ConstantsForMockDAQmx.CTR_TIME_BASE_RATE
            ] = _ConstantsForMockDAQmx.DEFAULT_CTR_TIME_BASE_RATE.value
            channel[
                _ConstantsForMockDAQmx.CO_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCO.PULSE_FREQUENCY.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_OUTPUT.value

            self._counter_output_channels[counter_channel_name] = channel

    def create_co_pulse_chan_time(
        self,
        task,
        counter,
        name_to_assign_to_channel,
        units,
        idle_state,
        initial_delay,
        low_time,
        high_time,
    ):
        """Called when method
        `nidaqmx._task_modules.co_channel_collection.COChannelCollection.add_co_pulse_chan_time`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        counter_channels_names = nidaqmx.utils.unflatten_channel_string(counter)
        for counter_channel_name in counter_channels_names:
            channel = (
                self._counter_output_channels[counter_channel_name]
                if counter_channel_name in self._counter_output_channels
                else {}
            )
            channel[_ConstantsForMockDAQmx.CHANNEL_NAME] = counter_channel_name
            channel[_ConstantsForMockDAQmx.IDLE_STATE] = idle_state
            channel[_ConstantsForMockDAQmx.INITIAL_DELAY] = initial_delay
            channel[_ConstantsForMockDAQmx.UNITS] = units
            channel[_ConstantsForMockDAQmx.PULSE_LOW_TIME] = low_time
            channel[_ConstantsForMockDAQmx.PULSE_HIGH_TIME] = high_time
            channel[
                _ConstantsForMockDAQmx.CTR_TIME_BASE_RATE
            ] = _ConstantsForMockDAQmx.DEFAULT_CTR_TIME_BASE_RATE.value
            channel[
                _ConstantsForMockDAQmx.CO_MEAS_TYPE
            ] = nidaqmx.constants.UsageTypeCO.PULSE_TIME.value
            channel[_ConstantsForMockDAQmx.CHANNEL_TYPE] = ChannelType.COUNTER_OUTPUT.value

            self._counter_output_channels[counter_channel_name] = channel

    def cfg_samp_clk_timing(self, task, rate, source, active_edge, sample_mode, samps_per_chan):
        """Called when method
        `nidaqmx._task_modules.timing.Timing.cfg_samp_clk_timing`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)
        self._timing[_ConstantsForMockDAQmx.RATE] = rate
        self._timing[_ConstantsForMockDAQmx.SOURCE] = source
        self._timing[_ConstantsForMockDAQmx.ACTIVE_EDGE] = active_edge
        self._timing[_ConstantsForMockDAQmx.SAMPLE_MODE] = sample_mode
        self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN] = samps_per_chan

    def cfg_implicit_timing(self, task, sample_mode, samps_per_chan):
        """Called when method 'nidaqmx._task_modules.timing.Timing.cfg_implicit_timing'
        is called"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (313 > 100 characters) (auto-generated noqa)
        self._timing[_ConstantsForMockDAQmx.SAMPLE_MODE] = sample_mode
        self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN] = samps_per_chan
        self._timing[_ConstantsForMockDAQmx.SAMP_QUANT_SAMP_PER_CHAN] = samps_per_chan

    def reset_timing_attribute(self, task, attribute):
        _MockInterpreter._assign_attribute_value(self._timing, attribute, None)

    def stop_task(self, task):
        """Called when method `nidaqmx.Task.stop` is called."""

    def start_task(self, task):
        """Called when method `nidaqmx.Task.start` is called."""

    def clear_task(self, task):
        """Called when method `nidaqmx.Task.close` is called."""

    def task_control(self, task, action):
        """Called when method `nidaqmx.Task.control` is called."""

    def cfg_dig_edge_start_trig(self, task, trigger_source, trigger_edge):
        """Called when method
        `nidaqmx._task_modules.triggering.start_trigger.StartTrigger.cfg_dig_edge_start_trig`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)

    def cfg_anlg_edge_start_trig(self, task, trigger_source, trigger_slope, trigger_level):
        """Called when method
        `nidaqmx._task_modules.triggering.start_trigger.StartTrigger.cfg_anlg_edge_start_trig`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)

    def disable_start_trig(self, task):
        """Called when method
        `nidaqmx._task_modules.triggering.start_trigger.StartTrigger.disable_start_trig`
        is called."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (314 > 100 characters) (auto-generated noqa)

    def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples (float64) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_power_f64(
        self,
        task,
        num_samps_per_chan,
        timeout,
        fill_mode,
        read_voltage_array,
        read_current_array,
    ):
        """Reads voltage and current samples (float64) from channel(s) defined in task."""
        return read_voltage_array, read_current_array, num_samps_per_chan

    def read_counter_f64(self, task, num_samps_per_chan, timeout, read_array):
        """Reads counter samples (float64) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_counter_f64_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads counter samples (float64) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_counter_scalar_f64(self, task, timeout):
        """Reads counter sample (float64) from channel(s) defined in task."""
        return _ConstantsForMockDAQmx.DEFAULT_COUNTER_SAMPLE_F64.value

    def read_counter_u32(self, task, num_samps_per_chan, timeout, read_array):
        """Reads counter samples (uint32) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_counter_u32_ex(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads counter samples (uint32) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_counter_scalar_u32(self, task, timeout):
        """Reads counter sample (uint32) from channel(s) defined in task."""
        return _ConstantsForMockDAQmx.DEFAULT_COUNTER_SAMPLE_U32.value

    def read_ctr_freq(
        self,
        task,
        num_samps_per_chan,
        timeout,
        interleaved,
        read_array_frequency,
        read_array_duty_cycle,
    ):
        """Reads frequency samples from channel(s) defined in task."""
        return read_array_frequency, read_array_duty_cycle, num_samps_per_chan

    def read_ctr_freq_scalar(self, task, timeout):
        """Reads frequency sample from channel(s) defined in task."""
        return (
            _ConstantsForMockDAQmx.DEFAULT_COUNTER_FREQUENCY.value,
            _ConstantsForMockDAQmx.DEFAULT_COUNTER_FREQUENCY.value,
        )

    def read_ctr_time(
        self,
        task,
        num_samps_per_chan,
        timeout,
        interleaved,
        read_array_high_time,
        read_array_low_time,
    ):
        """Reads low time and high time samples from channel(s) defined in task."""
        return read_array_high_time, read_array_low_time, num_samps_per_chan

    def read_ctr_time_scalar(self, task, timeout):
        """Reads low time and high time sample from channel(s) defined in task."""
        return (
            _ConstantsForMockDAQmx.DEFAULT_LOW_TIME_SECONDS.value,
            _ConstantsForMockDAQmx.DEFAULT_HIGH_TIME_SECONDS.value,
        )

    def read_digital_u8(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples (uint8) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_digital_u16(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples (uint16) from channel(s) defined in task."""
        return read_array, num_samps_per_chan

    def read_digital_u32(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples (uint32) from channel(s) defined in task."""

    def read_digital_lines(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        """Reads data samples from channel(s) defined in task."""
        return read_array, num_samps_per_chan, num_samps_per_chan

    def write_analog_f64(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples (float64) to channel(s) defined in task."""
        return num_samps_per_chan

    def write_digital_u8(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples (uint8) to channel(s) defined in task."""
        return num_samps_per_chan

    def write_digital_u16(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples (uint16) to channel(s) defined in task."""
        return num_samps_per_chan

    def write_digital_u32(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples (uint32) to channel(s) defined in task."""
        return num_samps_per_chan

    def write_digital_scalar_u32(self, task, auto_start, timeout, value):
        """Writes data samples to channel(s) defined in task."""

    def write_digital_lines(
        self, task, num_samps_per_chan, auto_start, timeout, data_layout, write_array
    ):
        """Writes data samples to lines in channel(s) defined in task."""
        return num_samps_per_chan

    def write_ctr_freq_scalar(self, task, auto_start, timeout, frequency, duty_cycle):
        """Writes sample to channel defined in task"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

    def write_ctr_time_scalar(self, _handle, auto_start, timeout, high_time, low_time):
        """Writes sample to channel defined in task"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (165 > 100 characters) (auto-generated noqa)

    def wait_until_task_done(self, task, time_to_wait):
        """Waits until the task has completed its action."""

    def export_signal(self, task, signal_id, output_terminal) -> None:
        """Exports the clock or trigger signal to the specified terminal"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (186 > 100 characters) (auto-generated noqa)

    def _get_attribute_value_from_channel_settings(self, channel_expression, attribute):
        """Retrieves value of specific attribute of channel(s) defined in channel expression"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
        channels_names = nidaqmx.utils.unflatten_channel_string(channel_expression)

        # if list of channels names is empty, gets the setting to first defined channel.
        if not channels_names:
            return self._retrieve_attribute_value_from_first_channel(attribute)

        # take the first channel in the list.
        channel_name = channels_names[0]

        attribute_value = None
        if channel_name in self._analog_input_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._analog_input_channels, channel_name, attribute
            )
        elif channel_name in self._analog_output_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._analog_output_channels, channel_name, attribute
            )
        elif channel_name in self._digital_input_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._digital_input_channels, channel_name, attribute
            )
        elif channel_name in self._digital_output_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._digital_output_channels, channel_name, attribute
            )
        elif channel_name in self._counter_input_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._counter_input_channels, channel_name, attribute
            )
        elif channel_name in self._counter_output_channels:
            attribute_value = _MockInterpreter._retrieve_attribute_value_from_channel(
                self._counter_output_channels, channel_name, attribute
            )
        else:
            raise ValueError(
                _ConstantsForMockDAQmx.CHANNEL_NOT_DEFINED_ARGS1.value.format(channel_name)
            )

        return attribute_value

    def _set_attribute_value_to_channel_settings(self, channel_expression, attribute, value):
        """Retrieves value to specific attribute of channel(s) defined in channel expression"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)
        channels_names = nidaqmx.utils.unflatten_channel_string(channel_expression)

        # if list of channels names is empty, set the setting to all channels.
        if not channels_names:
            self._assign_attribute_value_to_channels(attribute, value)
            return

        # take the first channel in the list.
        channel_name = channels_names[0]

        if channel_name in self._analog_input_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._analog_input_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._analog_output_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._analog_output_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._digital_input_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._digital_input_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._digital_output_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._digital_output_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._counter_input_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._counter_input_channels,
                channel_name,
                attribute,
                value,
            )

        if channel_name in self._counter_output_channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                self._counter_output_channels,
                channel_name,
                attribute,
                value,
            )

    def _retrieve_attribute_value_from_first_channel(self, attribute: int):
        channel_settings = {}

        # if analog input channels list is not empty.
        if self._analog_input_channels:
            # gets the settings of the first analog input channel.
            channel_settings = next(self._analog_input_channels.values())
        elif self._analog_output_channels:
            channel_settings = next(self._analog_output_channels.values())
        elif self._digital_input_channels:
            channel_settings = next(self._digital_input_channels.values())
        elif self._digital_output_channels:
            channel_settings = next(self._digital_output_channels.values())
        elif self._counter_input_channels:
            channel_settings = next(self._counter_input_channels.values())
        elif self._counter_output_channels:
            channel_settings = next(self._counter_output_channels.values())
        else:
            raise LookupError(_ConstantsForMockDAQmx.NO_CHANNEL_DEFINED.value)

        return _MockInterpreter._retrieve_attribute_value(channel_settings, attribute)

    def _assign_attribute_value_to_channels(self, attribute: int, value: Any):
        # sets the setting to all analog input channels.
        _MockInterpreter._assign_attribute_value_to_channels(
            self._analog_input_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._analog_output_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._digital_input_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._digital_output_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._counter_input_channels, attribute, value
        )

        _MockInterpreter._assign_attribute_value_to_channels(
            self._counter_output_channels, attribute, value
        )

    @staticmethod
    def _assign_attribute_value_to_channels(  # noqa: F811 - redefinition of unused '_assign_attribute_value_to_channels' from line 1007 (auto-generated noqa)
        channels: Dict[str, Dict], attribute: int, value: Any
    ):
        for channel_name in channels:
            _MockInterpreter._assign_attribute_value_to_channel(
                channels, channel_name, attribute, value
            )

    @staticmethod
    def _retrieve_attribute_value_from_channel(
        channels: Dict[str, Dict], channel_name: str, attribute: int
    ):
        channel_characteristics = channels[channel_name]
        return _MockInterpreter._retrieve_attribute_value(channel_characteristics, attribute)

    @staticmethod
    def _retrieve_attribute_value(attributes: Dict[str, Any], attribute: int):
        attribute_name = _DAQMX_ATTRIBUTES[attribute]
        if attribute_name in attributes:
            return attributes[attribute_name]

        raise AttributeError(
            _ConstantsForMockDAQmx.ATTRIBUTE_NOT_DEFINED_ARGS2.value.format(
                attribute, hex(attribute)
            )
        )

    @staticmethod
    def _assign_attribute_value_to_channel(
        channels: Dict[str, Dict], channel_name: str, attribute: int, value: Any
    ):
        channel_characteristics = channels[channel_name]
        _MockInterpreter._assign_attribute_value(channel_characteristics, attribute, value)

    @staticmethod
    def _assign_attribute_value(attributes: Dict[str, Any], attribute: int, value: Any):
        attribute_name = _DAQMX_ATTRIBUTES[attribute]
        attributes[attribute_name] = value


class _ConstantsForMockInterpreters(Enum):
    DC_RMS_VOLTAGE_MEASUREMENT_INCERTAINTY = 0.01
    DC_RMS_CURRENT_MEASUREMENT_INCERTAINTY = 0.001
    POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY = 0.001


class _InterpreterDcRmsCurrentMeasurement(_MockInterpreter):
    """Defines interpreter used for DC-RMS Voltage Measurement."""

    def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        channels_characteristics = [
            channel_characteristics
            for _, channel_characteristics in self._analog_input_channels.items()
        ]

        # retrieve the smallest maximum voltage from channel(s)
        max_current_range = min(
            [
                channel_characteristics[_ConstantsForMockDAQmx.MAX_VAL]
                for channel_characteristics in channels_characteristics
            ]
        )

        for index_row in range(0, len(channels_characteristics)):
            # Build a current value between 0 and max_voltage_range.
            current_value = random.random() * max_current_range

            # assign a voltage value = voltage_value +/- 0.001
            for index_col in range(0, self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN]):
                read_array[index_row, index_col] = (
                    current_value
                    - _ConstantsForMockInterpreters.DC_RMS_CURRENT_MEASUREMENT_INCERTAINTY.value
                    / 2.0
                    + random.random()
                    * _ConstantsForMockInterpreters.DC_RMS_CURRENT_MEASUREMENT_INCERTAINTY.value
                )
        return read_array, num_samps_per_chan


class _InterpreterDcRmsVoltageMeasurement(_MockInterpreter):
    """Defines interpreter used for DC-RMS Voltage Measurement."""

    def read_analog_f64(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
        channels_characteristics = [
            channel_characteristics
            for _, channel_characteristics in self._analog_input_channels.items()
        ]

        # retrieve the smallest maximum voltage from channel(s)
        max_voltage_range = min(
            [
                channel_characteristics[_ConstantsForMockDAQmx.MAX_VAL]
                for channel_characteristics in channels_characteristics
            ]
        )

        for index_row in range(0, len(channels_characteristics)):
            # Build a voltage value between 0 and max_voltage_range.
            voltage_value = random.random() * max_voltage_range

            # assign a voltage value = voltage_value +/- 0.01
            for index_col in range(0, self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN]):
                read_array[index_row, index_col] = (
                    voltage_value
                    - _ConstantsForMockInterpreters.DC_RMS_VOLTAGE_MEASUREMENT_INCERTAINTY.value
                    / 2.0
                    + random.random()
                    * _ConstantsForMockInterpreters.DC_RMS_VOLTAGE_MEASUREMENT_INCERTAINTY.value
                )
        return read_array, num_samps_per_chan


class _InterpreterPowerSupplySourceAndMeasure(_MockInterpreter):
    """Defines interpreter used for Power Supply Source And Measure."""

    def read_power_f64(
        self,
        task,
        num_samps_per_chan,
        timeout,
        fill_mode,
        read_voltage_array,
        read_current_array,
    ):
        channel_characteristics = next(
            channel_characteristics
            for _, channel_characteristics in self._analog_input_channels.items()
        )
        voltage_setpoint = channel_characteristics[_ConstantsForMockDAQmx.VOLTAGE_SETPOINT]
        current_setpoint = channel_characteristics[_ConstantsForMockDAQmx.CURRENT_SETPOINT]
        for index in range(0, self._timing[_ConstantsForMockDAQmx.SAMP_PER_CHAN]):
            read_voltage_array[index] = (
                voltage_setpoint
                - _ConstantsForMockInterpreters.POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY.value
                / 2.0
                + random.random()
                * _ConstantsForMockInterpreters.POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY.value
            )
            read_current_array[index] = (
                current_setpoint
                - _ConstantsForMockInterpreters.POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY.value
                / 2.0
                + random.random()
                * _ConstantsForMockInterpreters.POWER_SUPPLY_SOURCE_AND_MEASURE_INCERTAINTY.value
            )
        return read_voltage_array, read_current_array, num_samps_per_chan
