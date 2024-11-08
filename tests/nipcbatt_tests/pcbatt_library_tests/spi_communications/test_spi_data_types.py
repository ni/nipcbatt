"""This module provides SPI data types check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt


class TestSpiDeviceParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiDeviceParameters` class is ready to use.

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

    def test_spi_device_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiDeviceParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_voltage_level = nipcbatt.Ni845xVoltageLevel.VOLTAGE_LEVEL_25

        instance = nipcbatt.SpiDeviceParameters(
            voltage_level=expected_voltage_level,
        )

        actual_voltage_level = instance.voltage_level
        self.assertEqual(
            expected_voltage_level,
            actual_voltage_level,
        )


class TestSpiCommunicationParameters(unittest.TestCase):
    """Defines a test fixture that checks
    `SpiCommunicationParameters` class is ready to use.

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

    def test_spi_communication_parameters_init_fails_when_clock_rate_kilohertz_is_equal_to_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_chip_select = 50
        expected_clock_rate_kilohertz = 0

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiCommunicationParameters(
                    chip_select=expected_chip_select,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
                    clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
                )
            )

        self.assertEqual(
            "The value clock_rate_kilohertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_communication_parameters_init_fails_when_clock_rate_kilohertz_is_less_than_zero(
        self,
    ):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_chip_select = 50
        expected_clock_rate_kilohertz = -100

        with self.assertRaises(ValueError) as ctx:
            print(
                nipcbatt.SpiCommunicationParameters(
                    chip_select=expected_chip_select,
                    clock_rate_kilohertz=expected_clock_rate_kilohertz,
                    clock_phase=nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE,
                    clock_polarity=nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW,
                )
            )

        self.assertEqual(
            "The value clock_rate_kilohertz must be greater than 0.",
            str(ctx.exception),
        )

    def test_spi_communication_parameters(self):
        """Unit test of
        nipcbatt.pcbatt_library.spi_communications.spi_data_types.SpiCommunicationParameters.
        """  # noqa: D205, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (210 > 100 characters) (auto-generated noqa)
        expected_chip_select = 50
        expected_clock_rate_kilohertz = 100
        expected_clock_phase = nipcbatt.SpiConfigurationClockPhase.CLOCK_PHASE_SECOND_EDGE
        expected_clock_polarity = nipcbatt.SpiConfigurationClockPolarity.CLOCK_POLARITY_IDLE_LOW

        instance = nipcbatt.SpiCommunicationParameters(
            chip_select=expected_chip_select,
            clock_rate_kilohertz=expected_clock_rate_kilohertz,
            clock_phase=expected_clock_phase,
            clock_polarity=expected_clock_polarity,
        )

        actual_chip_select = instance.chip_select
        actual_clock_rate_kilohertz = instance.clock_rate_kilohertz
        actual_clock_phase = instance.clock_phase
        actual_clock_polarity = instance.clock_polarity

        self.assertEqual(expected_chip_select, actual_chip_select)
        self.assertEqual(
            expected_clock_rate_kilohertz,
            actual_clock_rate_kilohertz,
        )
        self.assertEqual(expected_clock_phase, actual_clock_phase)
        self.assertEqual(expected_clock_polarity, actual_clock_polarity)


if __name__ == "__main__":
    unittest.main()
