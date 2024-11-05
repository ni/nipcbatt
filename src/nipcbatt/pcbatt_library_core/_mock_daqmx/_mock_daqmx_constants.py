# pylint: disable=C0301
"""Constants for mock implementation of nidaqmx."""

from enum import Enum


class _ConstantsForMockDAQmx(Enum):
    """Constants used mock implementation of nidaqmx."""

    COUNT_EDGES_TERM = "count_edges_term"
    FREQ_TERM = "freq_term"
    SEMI_PERIOD_TERM = "semi_period_term"
    PULSE_TERM = "pulse_term"
    COUNT_EDGES_ACTIVE_EDGE = "count_edges_active_edge"
    INITIAL_COUNT = "initial_count"
    COUNT_DIRECTION = "count_direction"
    FREQ_STARTING_EDGE = "freq_starting_edge"
    SEMI_PERIOD_STARTING_EDGE = "semi_period_starting_edge"
    MEAS_METHOD = "meas_method"
    MEAS_TIME = "meas_time"
    DIVISOR = "divisor"
    IDLE_STATE = "idle_state"
    INITIAL_DELAY = "initial_delay"
    PULSE_FREQ = "pulse_freq"
    PULSE_DUTY_CYC = "pulse_duty_cyc"
    PULSE_LOW_TIME = "pulse_low_time"
    PULSE_HIGH_TIME = "pulse_high_time"
    CTR_TIME_BASE_RATE = "ctr_timebase_rate"
    UNITS = "units"
    MIN_VAL = "min_val"
    MAX_VAL = "max_val"
    TERMINAL_CONFIG = "terminal_config"
    POWER_SENSE = "power_sense"
    PWR_IDLE_OUTPUT_BEHAVIOR = "pwr_idle_output_behavior"
    ADC_TIMING_MODE = "adc_timing_mode"
    CURRENT_EXCIT_SOURCE = "current_excit_source"
    RESISTANCE_CONFIG = "resistance_config"
    EXCIT_VOLTAGE_OR_CURRENT = "excit_voltage_or_current"
    VOLTAGE_SETPOINT = "voltage_setpoint"
    CURRENT_SETPOINT = "current_setpoint"
    SHUNT_RESISTOR_LOC = "shunt_resistor_loc"
    EXCIT_SOURCE = "excit_source"
    EXT_SHUNT_RESISTOR_VAL = "ext_shunt_resistor_val"
    EXCIT_VAL = "excit_val"
    R_0 = "r_0"
    R_1 = "r_1"
    RTD_TYPE = "rtd_type"
    THRMSTR_A = "thrmstr_a"
    THRMSTR_B = "thrmstr_b"
    THRMSTR_C = "thrmstr_c"
    OUTPUT_ENABLE = "output_enable"
    SAMP_PER_CHAN = "samp_quant_samp_per_chan"
    SAMP_QUANT_SAMP_PER_CHAN = "samp_quant_samp_per_chan"
    RATE = "rate"
    SOURCE = "source"
    ACTIVE_EDGE = "active_edge"
    SAMPLE_MODE = "sample_mode"
    SAMP_TIMING_ENGINE = "samp_timing_engine"
    CUSTOM_SCALE_NAME = "custom_scale_name"
    AI_MEAS_TYPE = "ai_meas_type"
    AO_MEAS_TYPE = "ao_meas_type"
    DI_MEAS_TYPE = "di_meas_type"
    DO_MEAS_TYPE = "do_meas_type"
    CI_MEAS_TYPE = "ci_meas_type"
    CO_MEAS_TYPE = "co_meas_type"
    CHANNEL_TYPE = "channel_type"
    CHANNEL_NAME = "channel_name"

    ATTRIBUTE_NOT_DEFINED_ARGS2 = "attribute {} ({}) is not defined."
    CHANNEL_NOT_DEFINED_ARGS1 = "channel {} not defined."
    NO_CHANNEL_DEFINED = "no channel is defined in task."
    NO_LINE_DEFINED_IN_CHANNEL = "No digital line defined in channel."

    DEFAULT_CTR_TIME_BASE_RATE = 80000000.0
    DEFAULT_LOW_TIME_SECONDS = 0.5
    DEFAULT_HIGH_TIME_SECONDS = 0.5
    DEFAULT_COUNTER_FREQUENCY = 10.0
    DEFAULT_COUNTER_DUTY_CYCLE = 0.5
    DEFAULT_COUNTER_SAMPLE_F64 = 1.5
    DEFAULT_COUNTER_SAMPLE_U32 = 10


_DAQMX_ATTRIBUTES = {
    # used when invoke property nidaqmx._task_modules.channels.channel.Channel.chan_type
    0x187F: _ConstantsForMockDAQmx.CHANNEL_TYPE,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_count_edges_term
    0x18C7: _ConstantsForMockDAQmx.COUNT_EDGES_TERM,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_term
    0x18A2: _ConstantsForMockDAQmx.FREQ_TERM,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_semi_period_term
    0x18B0: _ConstantsForMockDAQmx.SEMI_PERIOD_TERM,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_term
    0x18E1: _ConstantsForMockDAQmx.PULSE_TERM,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_count_edges_active_edge
    0x697: _ConstantsForMockDAQmx.COUNT_EDGES_ACTIVE_EDGE,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_starting_edge
    0x799: _ConstantsForMockDAQmx.FREQ_STARTING_EDGE,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_semi_period_starting_edge
    0x22FE: _ConstantsForMockDAQmx.SEMI_PERIOD_STARTING_EDGE,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_meas_meth
    0x144: _ConstantsForMockDAQmx.MEAS_METHOD,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_meas_time
    0x145: _ConstantsForMockDAQmx.MEAS_TIME,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_div
    0x147: _ConstantsForMockDAQmx.DIVISOR,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_freq_units
    0x18A1: _ConstantsForMockDAQmx.UNITS,
    # used when invoke property nidaqmx._task_modules.channels.ci_channel.CIChannel.ci_min
    0x189D: _ConstantsForMockDAQmx.MIN_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ci_max
    0x189C: _ConstantsForMockDAQmx.MAX_VAL,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_freq
    0x1178: _ConstantsForMockDAQmx.PULSE_FREQ,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_duty_cyc
    0x1176: _ConstantsForMockDAQmx.PULSE_DUTY_CYC,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_ctr_timebase_rate
    0x18C2: _ConstantsForMockDAQmx.CTR_TIME_BASE_RATE,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_idle_state
    0x1170: _ConstantsForMockDAQmx.IDLE_STATE,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_low_time
    0x18BB: _ConstantsForMockDAQmx.PULSE_LOW_TIME,
    # used when invoke property nidaqmx._task_modules.channels.co_channel.COChannel.co_pulse_low_time
    0x18BA: _ConstantsForMockDAQmx.PULSE_HIGH_TIME,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_term_cfg
    0x1097: _ConstantsForMockDAQmx.TERMINAL_CONFIG,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_remote_sense
    0x31DB: _ConstantsForMockDAQmx.POWER_SENSE,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_idle_output_behavior
    0x31D8: _ConstantsForMockDAQmx.PWR_IDLE_OUTPUT_BEHAVIOR,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_adc_timing_mode
    0x29F9: _ConstantsForMockDAQmx.ADC_TIMING_MODE,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_excit_src
    0x17F4: _ConstantsForMockDAQmx.CURRENT_EXCIT_SOURCE,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_resistance_cfg
    0x1881: _ConstantsForMockDAQmx.RESISTANCE_CONFIG,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_excit_voltage_or_current
    0x17F6: _ConstantsForMockDAQmx.EXCIT_VOLTAGE_OR_CURRENT,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_min
    0x17DE: _ConstantsForMockDAQmx.MIN_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_max
    0x17DD: _ConstantsForMockDAQmx.MAX_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.current_shunt_resistance
    0x17F3: _ConstantsForMockDAQmx.EXT_SHUNT_RESISTOR_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_voltage_setpoint
    0x31D4: _ConstantsForMockDAQmx.VOLTAGE_SETPOINT,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_current_setpoint
    0x31D5: _ConstantsForMockDAQmx.CURRENT_SETPOINT,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_excit_val
    0x17F5: _ConstantsForMockDAQmx.EXCIT_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_rtd_r0
    0x1030: _ConstantsForMockDAQmx.R_0,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_rtd_type
    0x1032: _ConstantsForMockDAQmx.RTD_TYPE,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.thrmstr_a
    0x18C9: _ConstantsForMockDAQmx.THRMSTR_A,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.thrmstr_b
    0x18CB: _ConstantsForMockDAQmx.THRMSTR_B,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.thrmstr_c
    0x18CA: _ConstantsForMockDAQmx.THRMSTR_C,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.ai_thrmstr_r1
    0x1061: _ConstantsForMockDAQmx.R_1,
    # used when invoke property nidaqmx._task_modules.channels.ai_channel.AIChannel.pwr_output_enable
    0x31D6: _ConstantsForMockDAQmx.OUTPUT_ENABLE,
    # used when invoke property nidaqmx._task_modules.timing.Timing.samp_quant_samp_per_chan
    0x1300: _ConstantsForMockDAQmx.SAMP_QUANT_SAMP_PER_CHAN,
    # used when invoke property nidaqmx._task_modules.timing.Timing.samp_per_chan
    0x1310: _ConstantsForMockDAQmx.SAMP_PER_CHAN,
    # used when invoke property nidaqmx._task_modules.timing.Timing.samp_clk_rate
    0x1344: _ConstantsForMockDAQmx.RATE,
    # used when invoke property nidaqmx._task_modules.timing.Timing.samp_timing_engine
    0x2A26: _ConstantsForMockDAQmx.SAMP_TIMING_ENGINE,
    # used when invoke property nidaqmx._task_modules.channels.ao_channel.AOChannel.ao_min
    0x1187: _ConstantsForMockDAQmx.MIN_VAL,
    # used when invoke property nidaqmx._task_modules.channels.ao_channel.AOChannel.ao_max
    0x1186: _ConstantsForMockDAQmx.MAX_VAL,
    # used when invoke property nidaqmx._task_modules.channels.channel.Channel.physical_name
    0x18F5: _ConstantsForMockDAQmx.CHANNEL_NAME,
    # used when invoke property nidaqmx._task_modules.channels.ao_channel.AOChannel.ao_term_cfg
    0x188E: _ConstantsForMockDAQmx.TERMINAL_CONFIG,
}
"""The dictionnary makes a relation between attribute IDs and the attributes stored in dictionnaries of the interpreter"""
