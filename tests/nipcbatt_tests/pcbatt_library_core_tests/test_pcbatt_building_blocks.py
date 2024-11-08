# pylint: disable=C0116, W0201, W0613, W0231
"""This module provides unit tests of module pcbatt_building_blocks
   present in package pcbatt_core located in src."""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (345 > 100 characters) (auto-generated noqa)
import importlib.metadata
import logging
import sys
import unittest
from dataclasses import (  # noqa: F401 - 'dataclasses.dataclass' imported but unused (auto-generated noqa)
    dataclass,
)
from enum import Enum  # noqa: F401 - 'enum.Enum' imported but unused (auto-generated noqa)

import nidaqmx
from nidaqmx import utils  # noqa: F401 - 'nidaqmx.utils' imported but unused (auto-generated noqa)
from nidaqmx._task_modules.ai_channel_collection import AIChannelCollection
from nidaqmx._task_modules.ao_channel_collection import (  # noqa: F401 - 'nidaqmx._task_modules.ao_channel_collection.AOChannelCollection' imported but unused (auto-generated noqa)
    AOChannelCollection,
)
from nidaqmx._task_modules.channels.channel import (  # noqa: F401 - 'nidaqmx._task_modules.channels.channel.Channel' imported but unused (auto-generated noqa)
    Channel,
)
from nidaqmx._task_modules.ci_channel_collection import CIChannelCollection
from nidaqmx._task_modules.co_channel_collection import COChannelCollection
from nidaqmx._task_modules.di_channel_collection import DIChannelCollection
from nidaqmx._task_modules.do_channel_collection import DOChannelCollection
from nidaqmx._task_modules.export_signals import (  # noqa: F401 - 'nidaqmx._task_modules.export_signals.ExportSignals' imported but unused (auto-generated noqa)
    ExportSignals,
)
from nidaqmx._task_modules.in_stream import InStream
from nidaqmx._task_modules.out_stream import OutStream
from nidaqmx._task_modules.timing import Timing
from nidaqmx._task_modules.triggers import Triggers
from nidaqmx.constants import ChannelType, Edge, UsageTypeAI
from nidaqmx.errors import DaqError
from varname import nameof

import nipcbatt.pcbatt_utilities.reflection_utilities
from nipcbatt.pcbatt_library_core.pcbatt_building_blocks import (
    BuildingBlockUsingDAQmx,
    BuildingBlockUsingInstrument,
)


class TestInstrument:
    """Defines the instrument used in TestAbstractBuildingBlockUsingInstrument fixture"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (200 > 100 characters) (auto-generated noqa)

    def close(self):
        pass


class ChildClassForTests(BuildingBlockUsingInstrument):
    """chlid class of BuildingBlockUsingInstrument
     that defines minimum required implementations

    Args:
        BuildingBlockUsingInstrument: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    @property
    def is_instrument_initialized(self) -> bool:
        """Checks whether the instance of TestInstrument is initialized.

        Returns:
            bool: True, if the instance of TestInstrument is initialized.
        """
        return not isinstance(self._instrument, type(None))

    @property
    def instrument(self) -> TestInstrument:
        """Defines the instance of TestInstrument.

        Returns:
            TestInstrument: the type of instrument.
        """
        return self._instrument

    @property
    def name(self):
        return "blah"

    @classmethod
    def _instrument_factory(cls) -> TestInstrument:
        """Creates an instance of TestInstrument.
        Returns:
            TestInstrument: the type of instrument.
        """  # noqa: D205, D411, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), doc line too long (171 > 100 characters) (auto-generated noqa)
        return TestInstrument()

    def close(self):
        pass


class ChildClassInitWithIntFloat(ChildClassForTests):
    """Chlid class of ChildClassForTests(BuildingBlockUsingInstrument).
     It uses initialization with an int argument and a string argument.

    Args:
        ChildClassForTests: Base class from which this class inherits.
    """  # noqa: D205, W505 - 1 blank line required between summary line and description (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

    def initialize(self, int_param: int, str_param: str):
        """Initializes the building block with specific values.

        Args:
            int_param (int): the int argument
            str_param (str): the string argument
        """
        self.int_param = int_param
        self.str_param = str_param


class ChildClassInitWithVarious(ChildClassForTests):
    """Chlid class of ChildClassForTests(BuildingBlockUsingInstrument).
       It uses initialization with variatic argument(s).

    Args:
        ChildClassForTests: Base class from which this class inherits.
    """  # noqa: D205, W505 - 1 blank line required between summary line and description (auto-generated noqa), doc line too long (104 > 100 characters) (auto-generated noqa)

    def initialize(self, *args, **kwnargs):
        """Initializes the building block with variatic arguments."""
        self.args = args
        self.kwnargs = kwnargs


class ChannelNames(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    def __init__(self, n):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self.channel_names = ["x"] * n


class ChannelsToRead(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    def __init__(self, n):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self.channels_to_read = ChannelNames(n)
        self._task = Task()
        self.di_num_booleans_per_chan = 1


class Task(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    def __init__(self):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self._handle = 1
        self._interpreter = MockDAQmxTask.Interpreter()
        self.channels = DIChannel()

    def _calculate_num_samps_per_chan(self, one):
        return 1

    def _raise_invalid_write_num_chans_error(self, one, two):
        if two == 10:
            raise ValueError("num chans error!")


class Name(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    @property
    def name(self):
        return "One"


class DIChannel(ChildClassForTests):
    """x"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (122 > 100 characters) (auto-generated noqa)

    def __iter__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        channel_list = [Name()] * self.num_channels
        self.a = iter(channel_list)
        return self.a

    def __next__(self):  # noqa: D105 - Missing docstring in magic method (auto-generated noqa)
        return self.a

    def __init__(self):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self.num_channels = 3
        self.channel_names = ["One"]

    def add_di_chan(self, ch_exp, two, three):
        if "line" not in ch_exp:
            raise DaqError("Need channel", 1)
        x = int(ch_exp[-1]) + 1
        y = int(ch_exp[-3])
        self.num_channels = x - y


class OStream(  # noqa: D101 - Missing docstring in public class (auto-generated noqa)
    ChildClassForTests
):
    def __init__(self):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        self._task = Task()


class MockDAQmxTask(nidaqmx.Task):
    """defines methods used to simulate instruments though DAQmx.

    Args:
        nidaqmx.Task: the class from which this class inherits.
    """

    class Interpreter:
        "Empty class creates to deal with mock interpreter bugs"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (175 > 100 characters) (auto-generated noqa)

        def __init__(self):
            "Do nothing"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (135 > 100 characters) (auto-generated noqa)
            self.num_channels = 0

        def add_global_chans_to_task(self, one, two):
            if two == "":
                raise DaqError("This be error", 1)

        def stop_task(self, handle):
            "Stops the task (does nothing)"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (154 > 100 characters) (auto-generated noqa)

        def create_do_chan(self, handle, lines, name_to_assign_to_lines, line_grouping):
            "Do nothing"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (135 > 100 characters) (auto-generated noqa)

        def create_di_chan(self, handle, lines, name_to_assign_to_lines, line_grouping):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def create_ai_thrmcpl_chan(self, one, two, three, four, five, six, seven, eight, nine, ten):
            if ten == "" and eight == 10113:
                raise DaqError("channel is None", 1)

            if ten is None and nine is not None:
                raise DaqError("channel is None", 1)

        def add_ci_freq_chan(
            self, one, two, three, four, five, six, seven, eight, nine, ten, eleven
        ):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def create_ci_freq_chan(
            self, one, two, three, four, five, six, seven, eight, nine, ten, eleven
        ):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def create_co_pulse_chan_freq(self, one, two, three, four, five, six, seven, eight):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def create_co_pulse_chan_time(self, one, two, three, four, five, six, seven, eight):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def get_task_attribute_uint32(self, one, two):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def get_read_attribute_uint32(self, one, two):
            return 1

        def task_control(self, handle, action):
            "Do nothing"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (135 > 100 characters) (auto-generated noqa)

        def get_task_attribute_string(self, handle, x=int(1273)):
            return "stuff"

        def get_read_attribute_string(self, handle, two):
            return "One"

        def set_read_attribute_string(self, handle, d1823, val):
            self.num_channels = val

        def set_chan_attribute_int32(self, one, two, three, four):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def get_chan_attribute_int32(self, one, two, three):
            if three == 6271:
                return ChannelType.ANALOG_INPUT
            if three == 1685:
                return UsageTypeAI.TEMPERATURE_THERMOCOUPLE

        def write_many_sample_port_uint32(self, data):
            "yep"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (217 > 100 characters) (auto-generated noqa)

        def cfg_samp_clk_timing(
            self,
            rate,
            source,
            active_edge=Edge.RISING,
            sample_mode=1,
            samps_per_chan=1,
            stuff=1,
        ):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def cfg_dig_edge_start_trig(self, source, edge, stuff):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def write_digital_u32(self, one, two, three, four, five, six):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def get_timing_attribute_double(self, one, two):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def set_chan_attribute_double(self, handle, two, three, four):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def start_task(self, one):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def disable_start_trig(self, one):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def read_analog_f64(self, one, two, three, four, five):
            return [1.0], [1.0]

        def write_ctr_freq_scalar(self, one, two, three, four, five):
            "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (224 > 100 characters) (auto-generated noqa)

        def write_ctr_time_scalar(self, one, two, three, four, five):
            return 100.0

        def read_counter_scalar_f64(self, handle, timeout):
            return 100.0

        def read_counter_f64_ex(self, handle, timeout, three, four, five):
            return [100.0, 100.0]

        def read_digital_lines(self, task, num_samps_per_chan, timeout, fill_mode, read_array):
            return [[1] * len(read_array), 1, 1]

    def __init__(self, new_task_name="", *, grpc_options=None):
        """Does not call Task.__init__ (it requires DAQmx to be installed)."""  # noqa: D402, W505 - First line should not be the function's "signature" (auto-generated noqa), doc line too long (168 > 100 characters) (auto-generated noqa)
        self._interpreter = self.Interpreter()
        self._handle = ""
        self._do_channels = DOChannelCollection("", self._interpreter)
        self._co_channels = COChannelCollection("", self._interpreter)
        self._ci_channels = CIChannelCollection("", self._interpreter)
        self._di_channels = DIChannelCollection("", self._interpreter)
        self._timing = Timing("", self._interpreter)
        self._triggers = Triggers("", self._interpreter)
        self._out_stream = OutStream(self, self._interpreter)
        self._in_stream = InStream(self, self._interpreter)
        self._di_channels = DIChannel()
        self._ai_channels = AIChannelCollection("", self._interpreter)
        # self.number_of_channels = 2

    @property
    def in_stream(self):
        self.num_channels = self.di_channels.num_channels
        self.channels_to_read = ChannelsToRead(self.num_channels)
        return self.channels_to_read

    @property
    def number_of_channels(self):
        return 1

    @property
    def out_stream(self):
        return OStream()

    def close(self):
        """Closes the task (does nothing)."""

    def __del__(self):
        """Called when the instance is deleted (does nothing)."""

    @property
    def channels(self):
        class Channels:
            "placeholder class"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (142 > 100 characters) (auto-generated noqa)

            def __init__(self):
                self.channel_names = DIChannel()
                self.co_pulse_freq = 1
                self.co_pulse_duty_cyc = 0.5
                self.co_ctr_timebase_rate = 1.0
                self.co_pulse_high_time = 0.5
                self.co_pulse_low_time = 0.5
                self.number_of_channels = 2

        return Channels()

    @property
    def channel_names(self):
        return None

    @property
    def do_channels(self):
        class DOChannel:
            def __init__(self):
                self.num_channels = 1

            def add_do_chan(self, exp):
                return [DOChannel()]

        return DOChannel()

    @property
    def ci_channels(self):
        class CI_Channels:  # noqa: N801 - class name 'CI_Channels' should use CapWords convention (auto-generated noqa)
            def __init__(self):
                self.channel_names = "Channel_One"

            def add_ci_freq_chan(self, one, two):
                self.channel_names = one

            def add_ci_semi_period_chan(
                self, counter, name_to_assign_to_channel, min_val, max_val, units
            ):
                self.channel_names = "Channel_One"

        return CI_Channels()

    def set_num_channels(self, n):
        self.num_channels = n

    @property
    def di_channels(self):
        return self._di_channels

    @property
    def timing(self):
        class Time:
            "placeholder class"  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (142 > 100 characters) (auto-generated noqa)

            def __init__(self):
                self.samp_clk_rate = 1
                self.samp_quant_samp_per_chan = 1

            def cfg_samp_clk_timing(
                self,
                rate,
                source,
                active_edge=Edge.RISING,
                sample_mode=1,
                samps_per_chan=1,
            ):
                "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (228 > 100 characters) (auto-generated noqa)

            def cfg_implicit_timing(self, sample_mode="one", samps_per_chan="two"):
                "do nothing"  # noqa: D403, D415, W505 - First word of the first line should be properly capitalized (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (228 > 100 characters) (auto-generated noqa)

        return Time()


class TestBuildingBlockUsingInstrument(unittest.TestCase):
    """Defines a test fixture that checks child classes of
    BuildingBlockUsingInstrument are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (206 > 100 characters) (auto-generated noqa)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_child_initalization_without_arguments(self):
        block = ChildClassForTests()
        self.assertIsInstance(block, ChildClassForTests)

        block = ChildClassInitWithIntFloat()
        self.assertIsInstance(block, ChildClassInitWithIntFloat)

    def test_child_instrument(self):
        block = ChildClassForTests()
        self.assertIsNot(block.instrument, None)
        self.assertIsInstance(block.instrument, TestInstrument)

    def test_child_initalization_with_fixed_arguments(self):
        expected_int = 3.0
        expected_string = "Test_string"
        block = ChildClassInitWithIntFloat(expected_int, expected_string)
        self.assertIsInstance(block, ChildClassInitWithIntFloat)
        actual_int = block.int_param
        actual_string = block.str_param
        self.assertEqual(expected_int, actual_int)
        self.assertEqual(expected_string, actual_string)

    def test_child_initialazation_with_various_arguments(self):
        arg_1 = "test_argument_1"
        arg_2 = 2.8
        arg_3 = [45.9, "test_argument_3"]

        block = ChildClassInitWithVarious(arg_1, arg_2, arg_3)

        expected = 3
        actual = len(block.args)
        self.assertEqual(first=expected, second=actual)

        expected = arg_1
        actual = block.args[0]
        self.assertEqual(first=expected, second=actual)

        expected = arg_2
        actual = block.args[1]
        self.assertEqual(first=expected, second=actual)

        self.assertIsInstance(arg_3, list)

        expected = 2
        actual = len(block.args[2])
        self.assertEqual(first=expected, second=actual)

        expected = 45.9
        actual = block.args[2][0]
        self.assertEqual(first=expected, second=actual)

        expected = "test_argument_3"
        actual = block.args[2][1]
        self.assertEqual(first=expected, second=actual)


def instrument_factory() -> MockDAQmxTask:
    """Creates an instance of MockDAQmxTask."""
    return MockDAQmxTask()


class BuildingBlockUsingDAQmxForTests(BuildingBlockUsingDAQmx):
    """Chlid class of BuildingBlockUsingDAQmx(BuildingBlockUsingInstrument).

    Args:
        BuildingBlockUsingDAQmx: Base class from which this class inherits.
    """

    def initialize(self):
        """Initializes the building block with specific values."""

    def close(self):
        """Closes the building block and releases its internal resources."""


class TestBuildingBlockUsingDAQmx(unittest.TestCase):
    """Defines a test fixture that checks child classes of BuildingBlockUsingDAQmx are ready to use.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

    def setUp(self):
        nipcbatt.pcbatt_utilities.reflection_utilities.substitute_method(
            cls=BuildingBlockUsingDAQmx,
            method=instrument_factory,
            method_name="_instrument_factory",
        )

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)

        used_numpy_version = importlib.metadata.version("numpy")
        logging.debug("%s = %s", nameof(used_numpy_version), used_numpy_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_child_initalization_without_arguments(self):
        block = BuildingBlockUsingDAQmxForTests()
        self.assertIsInstance(block, BuildingBlockUsingDAQmxForTests)
        self.assertIsInstance(block.task, MockDAQmxTask)


if __name__ == "__main__":
    unittest.main()
