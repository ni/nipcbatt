"""This module provides SerialCommunication check."""

import importlib.metadata
import logging
import sys
import unittest

from varname import nameof

import nipcbatt


class TestSerialCommunication(unittest.TestCase):
    """Defines a test fixture that checks `SerialCommunication` class.

    Args:
        unittest.TestCase: Base class from which this class inherits.
    """

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

    @unittest.skip(
        "The execution of test is skipped"
        + " because it requires a serial device that responds to VISA query.",
    )
    def test_serial_communication(self):
        """Unit test of
        nipcbatt.pcbatt_library.serial_communications.serial_communication.SerialCommunication
        """
        with nipcbatt.SerialCommunication() as communication:
            communication.initialize("ASRL7::INSTR")

            communication_parameters = nipcbatt.SerialCommunicationParameters(
                data_rate_bauds=9600,
                number_of_bits_in_data_frame=8,
                delay_before_receive_response_milliseconds=100,
                parity=nipcbatt.ConstantsForSerialCommunication.DEFAULT_PARITY,
                stop_bits=nipcbatt.ConstantsForSerialCommunication.DEFAULT_STOP_BITS,
                flow_control=nipcbatt.ConstantsForSerialCommunication.DEFAULT_FLOW_CONTROL_MODE,
            )
            configuration = nipcbatt.SerialCommunicationConfiguration(
                communication_parameters=communication_parameters,
                command_to_send="*IDN?",
            )

            print(f"parameters = {configuration}")
            results = communication.configure_then_send_command_and_receive_response(
                configuration=configuration
            )
            print(f"results = {results}")
            self.assertIsNotNone(results)
            self.assertIsInstance(results, nipcbatt.SerialCommunicationData)


if __name__ == "__main__":
    unittest.main()
