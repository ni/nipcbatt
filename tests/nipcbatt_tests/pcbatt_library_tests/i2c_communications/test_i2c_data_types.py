"""This module provides I2C data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt


class TestI2cDeviceParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cDeviceParameters` class is ready to use.

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

    def test_i2c_device_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cDeviceParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_enable_i2c_pullup_resistor = False
        expected_voltage_level = nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_25

        instance = nipcbatt.I2cDeviceParameters(
            enable_i2c_pullup_resistor=expected_enable_i2c_pullup_resistor,
            voltage_level=expected_voltage_level,
        )

        actual_enable_i2c_pullup_resistor = instance.enable_i2c_pullup_resistor
        actual_voltage_level = instance.voltage_level
        self.assertEqual(expected_enable_i2c_pullup_resistor, actual_enable_i2c_pullup_resistor)
        self.assertEqual(
            expected_voltage_level,
            actual_voltage_level,
        )


class TestI2cCommunicationParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `I2cCommunicationParameters` class is ready to use.

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

    def test_i2c_communication_parameters_init_fails_when_device_address_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = -50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = 100
        expected_ack_poll_timeout_milliseconds = 1000

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cCommunicationParameters(
                    device_address=expected_device_address,
                    addressing_type=expected_addressing_type,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
                )
            )

        self.assertEqual(
            "The value device_address must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_i2c_communication_parameters_init_fails_when_ack_poll_timeout_milliseconds_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = 50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = 100
        expected_ack_poll_timeout_milliseconds = -1000

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cCommunicationParameters(
                    device_address=expected_device_address,
                    addressing_type=expected_addressing_type,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
                )
            )

        self.assertEqual(
            "The value ack_poll_timeout_milliseconds must be greater than or equal to 0.",
            str(ctx.exception),
        )

    def test_i2c_communication_parameters_init_fails_when_clock_rate_kilohertz_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = 50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = 0
        expected_ack_poll_timeout_milliseconds = 1000

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cCommunicationParameters(
                    device_address=expected_device_address,
                    addressing_type=expected_addressing_type,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
                )
            )

        self.assertEqual(
            "The value clock_rate_kilohertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_communication_parameters_init_fails_when_clock_rate_kilohertz_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = 50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = -100
        expected_ack_poll_timeout_milliseconds = 1000

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.I2cCommunicationParameters(
                    device_address=expected_device_address,
                    addressing_type=expected_addressing_type,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
                )
            )

        self.assertEqual(
            "The value clock_rate_kilohertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_i2c_communication_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.i2c_communications.i2c_data_types.I2cCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_device_address = 50
        expected_addressing_type = nipcbatt.Ni845xI2cAddressingType.ADDRESSING_10_BIT
        expected_clock_rate_kilohertz = 100
        expected_ack_poll_timeout_milliseconds = 1000

        instance = nipcbatt.I2cCommunicationParameters(
            device_address=expected_device_address,
            addressing_type=expected_addressing_type,
            clock_rate_kilohertz=expected_clock_rate_kilohertz,
            ack_poll_timeout_milliseconds=expected_ack_poll_timeout_milliseconds,
        )

        actual_device_address = instance.device_address
        actual_addressing_type = instance.addressing_type
        actual_clock_rate_kilohertz = instance.clock_rate_kilohertz
        actual_ack_poll_timeout_milliseconds = instance.ack_poll_timeout_milliseconds
        self.assertEqual(expected_device_address, actual_device_address)
        self.assertEqual(
            expected_addressing_type,
            actual_addressing_type,
        )
        self.assertEqual(
            expected_clock_rate_kilohertz,
            actual_clock_rate_kilohertz,
        )
        self.assertEqual(
            expected_ack_poll_timeout_milliseconds,
            actual_ack_poll_timeout_milliseconds,
        )


if __name__ == "__main__":
    unittest.main()
