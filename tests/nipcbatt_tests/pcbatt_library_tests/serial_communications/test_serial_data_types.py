"""This module provides Serial communication data types check."""

import importlib.metadata
import logging
import sys
import unittest

import pyvisa.constants
from varname import nameof

import nipcbatt


class TestSerialCommunicationParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SerialCommunicationParameters` class is ready to use.

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_serial_communication_parameters_init_fails_when_data_rate_bauds_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationParameters(
                    data_rate_bauds=0,
                    number_of_bits_in_data_frame=5,
                    delay_before_receive_response_milliseconds=100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value data_rate_bauds must be greater than 0.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_data_rate_bauds_is_lower_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationParameters(
                    data_rate_bauds=-7,
                    number_of_bits_in_data_frame=5,
                    delay_before_receive_response_milliseconds=100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value data_rate_bauds must be greater than 0.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_number_of_bits_in_data_frame_is_lower_than_four(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationParameters(
                    data_rate_bauds=115200,
                    number_of_bits_in_data_frame=2,
                    delay_before_receive_response_milliseconds=100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value of number_of_bits_in_data_frame must"
            + " be greater than or equal to 4 and less than or equal to 8.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_number_of_bits_in_data_frame_is_greater_than_eight(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationParameters(
                    data_rate_bauds=115200,
                    number_of_bits_in_data_frame=10,
                    delay_before_receive_response_milliseconds=100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value of number_of_bits_in_data_frame must"
            + " be greater than or equal to 4 and less than or equal to 8.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_delay_before_receive_response_milliseconds_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationParameters(
                    data_rate_bauds=115200,
                    number_of_bits_in_data_frame=5,
                    delay_before_receive_response_milliseconds=0,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value delay_before_receive_response_milliseconds must be greater than 0.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters_init_fails_when_delay_before_receive_response_milliseconds_is_lower_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationParameters(
                    data_rate_bauds=115200,
                    number_of_bits_in_data_frame=5,
                    delay_before_receive_response_milliseconds=-100,
                    parity=pyvisa.constants.Parity.none,
                    stop_bits=pyvisa.constants.StopBits.one,
                    flow_control=pyvisa.constants.ControlFlow.xon_xoff,
                )
            )

        self.assertEqual(
            "The value delay_before_receive_response_milliseconds must be greater than 0.",
            str(ctx.exception),
        )

    def test_serial_communication_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff

        # Act
        instance = nipcbatt.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )

        actual_data_rate_bauds = instance.data_rate_bauds
        actual_number_of_bits_in_data_frame = instance.number_of_bits_in_data_frame
        actual_delay_before_receive_response_milliseconds = (
            instance.delay_before_receive_response_milliseconds
        )
        actual_parity = instance.parity
        actual_stop_bits = instance.stop_bits
        actual_flow_control = instance.flow_control

        # Assert
        self.assertEqual(expected_data_rate_bauds, actual_data_rate_bauds)
        self.assertEqual(
            expected_number_of_bits_in_data_frame,
            actual_number_of_bits_in_data_frame,
        )
        self.assertEqual(
            expected_delay_before_receive_response_milliseconds,
            actual_delay_before_receive_response_milliseconds,
        )
        self.assertEqual(
            expected_parity,
            actual_parity,
        )
        self.assertEqual(
            expected_stop_bits,
            actual_stop_bits,
        )
        self.assertEqual(
            expected_flow_control,
            actual_flow_control,
        )


class TestSerialCommunicationConfiguration(unittest.TestCase):
    """Defines a test fixture that checks
    `SerialCommunicationConfiguration` class is ready to use.

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_serial_communication_configuration_init_fails_when_communication_parameters_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationConfiguration(
                    communication_parameters=None, command_to_send="HELO\r"
                )
            )

        # Assert
        self.assertEqual("The object communication_parameters is None.", str(ctx.exception))

    def test_serial_communication_configuration_init_fails_when_command_to_send_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff

        communication_parameters = nipcbatt.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationConfiguration(
                    communication_parameters=communication_parameters,
                    command_to_send=None,
                )
            )

        # Assert
        self.assertEqual(
            "The string value command_to_send is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_configuration_init_fails_when_command_to_send_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff

        communication_parameters = nipcbatt.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationConfiguration(
                    communication_parameters=communication_parameters,
                    command_to_send="",
                )
            )

        # Assert
        self.assertEqual(
            "The string value command_to_send is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_configuration_init_fails_when_command_to_send_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff

        communication_parameters = nipcbatt.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )
        # Act
        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SerialCommunicationConfiguration(
                    communication_parameters=communication_parameters,
                    command_to_send=" ",
                )
            )

        # Assert
        self.assertEqual(
            "The string value command_to_send is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_configuration(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationConfiguration.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_data_rate_bauds = 115200
        expected_number_of_bits_in_data_frame = 8
        expected_delay_before_receive_response_milliseconds = 100
        expected_parity = pyvisa.constants.Parity.none
        expected_stop_bits = pyvisa.constants.StopBits.one
        expected_flow_control = pyvisa.constants.ControlFlow.xon_xoff
        expected_command_to_send = "HELO\r"

        expected_communication_parameters = nipcbatt.SerialCommunicationParameters(
            data_rate_bauds=expected_data_rate_bauds,
            number_of_bits_in_data_frame=expected_number_of_bits_in_data_frame,
            delay_before_receive_response_milliseconds=(
                expected_delay_before_receive_response_milliseconds
            ),
            parity=expected_parity,
            stop_bits=expected_stop_bits,
            flow_control=expected_flow_control,
        )

        # Act
        instance = nipcbatt.SerialCommunicationConfiguration(
            communication_parameters=expected_communication_parameters,
            command_to_send=expected_command_to_send,
        )
        actual_communication_parameters = instance.communication_parameters
        actual_command_to_send = instance.command_to_send

        # Assert
        self.assertEqual(expected_communication_parameters, actual_communication_parameters)
        self.assertEqual(
            expected_command_to_send,
            actual_command_to_send,
        )


class TestSerialCommunicationData(unittest.TestCase):
    """Defines a test fixture that checks
    `SerialCommunicationData` class is ready to use.

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

        used_nidaqmx_version = importlib.metadata.version("nidaqmx")
        logging.debug("%s = %s", nameof(used_nidaqmx_version), used_nidaqmx_version)

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_serial_communication_data_init_fails_when_received_response_is_none(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(nipcbatt.SerialCommunicationData(received_response=None))

        # Assert
        self.assertEqual(
            "The string value received_response is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_data_init_fails_when_received_response_is_empty(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(nipcbatt.SerialCommunicationData(received_response=""))

        # Assert
        self.assertEqual(
            "The string value received_response is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_data_init_fails_when_received_response_is_whitespace(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange

        # Act
        with self.assertRaises(ValueError) as ctx:
            print(nipcbatt.SerialCommunicationData(received_response=" "))

        # Assert
        self.assertEqual(
            "The string value received_response is None, empty or whitespace.",
            str(ctx.exception),
        )

    def test_serial_communication_data(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_data_types.SerialCommunicationData.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        # Arrange
        expected_received_response = "HELO 0000 MP 300 1.11 5.27"

        # Act
        instance = nipcbatt.SerialCommunicationData(
            received_response=expected_received_response,
        )
        actual_received_response = instance.received_response

        # Assert
        self.assertEqual(expected_received_response, actual_received_response)


if __name__ == "__main__":
    unittest.main()
