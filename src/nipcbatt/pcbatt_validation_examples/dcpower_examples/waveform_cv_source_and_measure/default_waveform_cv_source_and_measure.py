"""Waveform DC voltage source and measure example with default input parameters."""

import matplotlib.pyplot as plt

from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure import (
    WaveformVoltageSourceAndMeasure,
)
from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure_constants import (
    DEFAULT_WAVEFORM_CV_SOURCE_AND_MEASURE_PARAMETERS,
)
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def plot_waveforms(measurement_results: dict) -> None:
    """Plots voltage and current waveforms from measurement results.

    Args:
        measurement_results (dict): The measurement_results dict from
            WaveformVoltageSourceAndMeasureResultData.
    """
    waveform = measurement_results["waveform_measurements"]
    voltages = waveform["x_data"]
    currents = waveform["y_data"]
    dt = waveform["dt"]

    # Build time axis from dt and number of samples
    num_samples = len(voltages)
    time_axis = [i * dt for i in range(num_samples)]

    fig, (ax_voltage, ax_current) = plt.subplots(2, 1, sharex=True, figsize=(10, 6))
    fig.suptitle("Waveform CV Source and Measure")

    ax_voltage.plot(time_axis, voltages, color="steelblue")
    ax_voltage.set_ylabel("Voltage (V)")
    ax_voltage.set_title("Voltage Waveform")
    ax_voltage.grid(True)

    ax_current.plot(time_axis, currents, color="darkorange")
    ax_current.set_ylabel("Current (A)")
    ax_current.set_xlabel("Time (s)")
    ax_current.set_title("Current Waveform")
    ax_current.grid(True)

    sample_rate = measurement_results.get("Sample Rate (Hz)", "N/A")
    effective_step_time = measurement_results.get("Effective Step Time (Sec)", "N/A")
    total_time = measurement_results.get("Total Sequence Time (Sec)", "N/A")
    fig.text(
        0.01, 0.01,
        f"Sample Rate: {sample_rate} Hz  |  Step Time: {effective_step_time} s  |  Total Time: {total_time} s",
        fontsize=8,
    )

    plt.tight_layout()
    plt.show()


def main():
    """Configures and executes waveform CV source and measure using default constants."""
    waveform_voltage_source_and_measure = WaveformVoltageSourceAndMeasure()

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\waveform_cv_source_and_measure_logger.txt")
    logger.attach(waveform_voltage_source_and_measure)

    # ======================= Initialize the SMU/PPS ============================
    waveform_voltage_source_and_measure.initialize(resource_name="PPS1/0")

    # ================= Default measurement configuration ===================
    # Default voltage setpoints: [100 mV, 1 V, 100 mV]
    # Default step time: 100 ms, aperture time: 1 ms, step record length: 100
    results = waveform_voltage_source_and_measure.configure_and_measure(
        configuration=DEFAULT_WAVEFORM_CV_SOURCE_AND_MEASURE_PARAMETERS
    )

    # ===================== Close the SMU/PPS session ===========================
    waveform_voltage_source_and_measure.close()

    # Print the measurement results
    print(results)

    # ===================== Plot voltage and current waveforms ==================
    plot_waveforms(results.measurement_results)


if __name__ == "__main__":
    main()
