"""Waveform DC voltage source and measure example with default input parameters."""

import numpy as np

import nipcbatt.pcbatt_utilities.plotter as pl
from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def plot_waveforms(results) -> None:
    """Plots voltage and current waveforms from a measurement result.

    Args:
        results (WaveformVoltageSourceAndMeasureResultData): Result returned by
            ``WaveformVoltageSourceAndMeasure.configure_and_measure``.
    """
    voltage_waveform = results.voltage_waveform[0]
    current_waveform = results.current_waveform[0]
    time_axis = np.arange(len(voltage_waveform.samples)) * voltage_waveform.delta_time_seconds

    pl.plot_two(
        y1=voltage_waveform.samples,
        y2=current_waveform.samples,
        x1=time_axis,
        title1="Voltage Waveform",
        ylabel1="Voltage (V)",
        xlabel1="Time (s)",
        x2=time_axis,
        title2="Current Waveform",
        ylabel2="Current (A)",
        xlabel2="Time (s)",
        stitle="Waveform CV Source and Measure",
    )


def main():
    """Configures and executes waveform CV source and measure using default constants."""
    waveform_voltage_source_and_measure = dcpower.WaveformVoltageSourceAndMeasure()

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\waveform_cv_source_and_measure_logger.txt")
    logger.attach(waveform_voltage_source_and_measure)

    # ======================= Initialize the SMU/PPS ============================
    waveform_voltage_source_and_measure.initialize(resource_name="SMU1/0")

    # ================= Default measurement configuration ===================
    results = waveform_voltage_source_and_measure.configure_and_measure(
        configuration=dcpower.DEFAULT_WAVEFORM_CV_SOURCE_AND_MEASURE_PARAMETERS
    )

    # ===================== Close the SMU/PPS session ===========================
    waveform_voltage_source_and_measure.close()

    # Print the measurement results
    print(results)

    # ===================== Plot voltage and current waveforms ==================
    plot_waveforms(results)


if __name__ == "__main__":
    main()
