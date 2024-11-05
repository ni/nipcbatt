"""Defines unit tests related to nipcbatt.pcbatt_analysis.common_types module."""

import logging
import math
import os
import platform
import sys
import unittest
from pathlib import Path

import numpy
from parameterized import parameterized
from varname import nameof

from nipcbatt.pcbatt_analysis.common.common_types import (
    AmplitudePhaseSpectrum,
    SpectrumAmplitudeType,
    SpectrumPhaseUnit,
    WaveformTone,
)


class TestSpectrumAmplitudeType(unittest.TestCase):
    """Provides unit tests of `SpectrumAmplitudeType` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @parameterized.expand(
        [
            ("PEAK", SpectrumAmplitudeType.PEAK, 0),
            ("RMS", SpectrumAmplitudeType.RMS, 1),
        ]
    )
    def test_spectrum_amplitude_type_integer_values(
        self,
        case_name: str,
        actual_enum_value: SpectrumAmplitudeType,
        expected_int_value: int,
    ):
        """Test of enum `SpectrumAmplitudeType` integer values"""
        logging.debug("%s = %s", nameof(case_name), case_name)
        self.assertEqual(expected_int_value, actual_enum_value)


class TestSpectrumPhaseUnit(unittest.TestCase):
    """Provides unit tests of `SpectrumPhaseUnit` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

    @parameterized.expand(
        [
            ("RADIAN", SpectrumPhaseUnit.RADIAN, 0),
            ("DEGREE", SpectrumPhaseUnit.DEGREE, 1),
        ]
    )
    def test_spectrum_phase_unit_integer_values(
        self,
        case_name: str,
        actual_enum_value: SpectrumPhaseUnit,
        expected_int_value: int,
    ):
        """Test of pcbatt_analysis.frequency_domain_analysis.FftSpectrumPhaseUnit integer values"""
        logging.debug("%s = %s", nameof(case_name), case_name)
        self.assertEqual(expected_int_value, actual_enum_value)


class TestAmplitudePhaseSpectrum(unittest.TestCase):
    """Provides unit tests of `AmplitudePhaseSpectrum` class.

    Args:
        unittest (TestCase): test cases fixture.
    """

    @classmethod
    def setUpClass(cls):
        print("Setup test fixture")
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("python version = %s", str(sys.version))
        logging.debug("python path = %s", sys.executable)
        logging.debug("platform architecture = %s", platform.architecture())
        logging.debug("current script path = %s", __file__)

        # create tests output folder
        repository_dir_path = Path(__file__).parent.parent.parent.parent.parent
        cls.tests_output_folder_path = os.path.join(
            repository_dir_path,
            "tests_outputs",
            Path(__file__).stem,
            nameof(TestAmplitudePhaseSpectrum),
        )

        if not os.path.exists(cls.tests_output_folder_path):
            os.makedirs(cls.tests_output_folder_path, exist_ok=True)

    @parameterized.expand(
        [
            (
                "PEAK_NOT_DB_DEGREE",
                SpectrumAmplitudeType.PEAK,
                False,
                SpectrumPhaseUnit.DEGREE,
            ),
            (
                "RMS_DB_RADIAN",
                SpectrumAmplitudeType.RMS,
                True,
                SpectrumPhaseUnit.RADIAN,
            ),
        ]
    )
    def test_amplitude_phase_spectrum(
        self,
        case_name: str,
        expected_amplitude_type: SpectrumAmplitudeType,
        expected_amplitude_is_db: bool,
        expected_phase_unit: SpectrumPhaseUnit,
    ):
        """Test of `AmplitudePhaseSpectrum` class constructor."""
        logging.debug("%s = %s", nameof(case_name), case_name)

        # Act
        spectrum_instance = AmplitudePhaseSpectrum(
            f0=10,
            df=10,
            frequencies_amplitudes=numpy.array([0, 1, 2, 3]),
            spectrum_amplitude_type=expected_amplitude_type,
            spectrum_amplitude_unit_is_db=expected_amplitude_is_db,
            frequencies_phases=numpy.array([0, 0, 0, 0]),
            spectrum_phase_unit=expected_phase_unit,
        )

        spectrum_instance_repr = repr(spectrum_instance)
        logging.debug("%s = %s", nameof(spectrum_instance_repr), spectrum_instance_repr)

        # Assert
        self.assertIsNotNone(spectrum_instance)
        self.assertTrue(nameof(spectrum_instance.spectrum_amplitude_type) in spectrum_instance_repr)
        self.assertTrue(
            nameof(spectrum_instance.spectrum_amplitude_unit_is_db) in spectrum_instance_repr
        )

        self.assertTrue(nameof(spectrum_instance.spectrum_amplitudes) in spectrum_instance_repr)

        self.assertTrue(
            nameof(spectrum_instance.spectrum_frequency_resolution) in spectrum_instance_repr
        )
        self.assertTrue(nameof(spectrum_instance.spectrum_phase_unit) in spectrum_instance_repr)

        self.assertTrue(
            nameof(spectrum_instance.spectrum_start_frequency) in spectrum_instance_repr
        )

        self.assertEqual(4, spectrum_instance.spectrum_frequencies.size)
        self.assertEqual(4, spectrum_instance.spectrum_amplitudes.size)
        self.assertEqual(4, spectrum_instance.spectrum_phases.size)

        self.assertEqual(10, spectrum_instance.spectrum_frequencies[0])
        self.assertEqual(20, spectrum_instance.spectrum_frequencies[1])
        self.assertEqual(30, spectrum_instance.spectrum_frequencies[2])
        self.assertEqual(40, spectrum_instance.spectrum_frequencies[3])

        self.assertEqual(0, spectrum_instance.spectrum_amplitudes[0])
        self.assertEqual(1, spectrum_instance.spectrum_amplitudes[1])
        self.assertEqual(2, spectrum_instance.spectrum_amplitudes[2])
        self.assertEqual(3, spectrum_instance.spectrum_amplitudes[3])

        self.assertEqual(0, spectrum_instance.spectrum_phases[0])
        self.assertEqual(0, spectrum_instance.spectrum_phases[1])
        self.assertEqual(0, spectrum_instance.spectrum_phases[2])
        self.assertEqual(0, spectrum_instance.spectrum_phases[3])

        self.assertEqual(expected_amplitude_is_db, spectrum_instance.spectrum_amplitude_unit_is_db)

        self.assertEqual(expected_amplitude_type, spectrum_instance.spectrum_amplitude_type)

        self.assertEqual(expected_phase_unit, spectrum_instance.spectrum_phase_unit)


class TestWaveformTone(unittest.TestCase):
    """Defines a test fixture that checks
    `WaveformTone` class is ready to use.

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

    @classmethod
    def tearDownClass(cls):
        print("Teardown fixture")

    def test_waveform_tone(self):
        """Tests if an instance of `WaveformTone`
        is created with the specific values.
        """
        waveform_tone = WaveformTone(frequency=440, amplitude=1, phase_radians=math.pi / 2)

        logging.debug("%s = %s", nameof(waveform_tone), repr(waveform_tone))
        self.assertEqual(440, waveform_tone.frequency)
        self.assertEqual(1, waveform_tone.amplitude)
        self.assertEqual(math.pi / 2, waveform_tone.phase_radians)
        self.assertEqual(90, waveform_tone.phase_degrees)
