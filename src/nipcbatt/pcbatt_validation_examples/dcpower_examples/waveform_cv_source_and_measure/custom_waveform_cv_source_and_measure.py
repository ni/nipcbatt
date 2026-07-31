"""Waveform DC voltage source and measure example with custom input parameters."""

import matplotlib.pyplot as plt
import nidcpower

from nipcbatt.pcbatt_library.dcpower.common.common_data_types import (
    EventSignalToExport,
    ExecutionSettings,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure import (
    WaveformVoltageSourceAndMeasure,
)
from nipcbatt.pcbatt_library.dcpower.waveform_cv_source_and_measure.waveform_cv_source_and_measure_data_types import (
    VoltageChannelSettings,
    WaveformTimingParameters,
    WaveformVoltageSourceAndMeasureParameters,
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
    fig.suptitle("Waveform CV Source and Measure (Custom Parameters)")

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
    """Configures and executes waveform CV source and measure using custom parameters."""
    waveform_voltage_source_and_measure = WaveformVoltageSourceAndMeasure()

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\custom_waveform_cv_source_and_measure_logger.txt")
    logger.attach(waveform_voltage_source_and_measure)

    # ======================= Initialize the SMU/PPS ============================
    waveform_voltage_source_and_measure.initialize(resource_name="SMU1/0")

    # ==================== Custom channel settings ==============================
    # Voltage level range: 6 V, current limit: 50 mA, current limit range: 100 mA
    custom_channel_settings = VoltageChannelSettings(
        voltage_level_range=6.0,
        current_limit=0.050,
        current_limit_range=0.100,
    )

    # ==================== Custom execution settings ============================
    # Execute configure + source + measure in a single call; run full analysis.
    custom_execution_settings = ExecutionSettings(
        execution_type=MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
        skip_analysis=False,
    )

    # ==================== Custom timing parameters =============================
    # Ramp from 500 mV → 2.5 V → 500 mV with 200 ms step time and 2 ms aperture.
    custom_timing_parameters = WaveformTimingParameters(
        source_delay=0.200,                  # Step time = 200 ms
        aperture_time=0.002,                 # Aperture time = 2 ms
        step_size=0.00002,                   # Step size = 20 µs
        measure_record_length=100,           # 100 samples per record
        measure_when=nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE,
        transient_response=nidcpower.TransientResponse.FAST,
        voltage_gain_bandwidth=10000.0,      # Hz
        voltage_compensation_frequency=50000.0,  # Hz
        voltage_pole_zero_ratio=0.16,
        current_gain_bandwidth=50000.0,      # Hz
        current_compensation_frequency=250000.0,  # Hz
        current_pole_zero_ratio=5.0,
    )

    # ==================== Custom trigger parameters ============================
    # Disable source trigger; export the Source Complete Event to PXI_Trig0.
    custom_trigger_parameters = TriggerParameters(
        source_trigger_behavior=SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=ExportEvent.NONE,
        event_signal_to_export=EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="PXI_Trig0",
    )

    # ==================== Custom voltage setpoints =============================
    # Ramp up and back down: 500 mV → 1 V → 1.5 V → 2.5 V → 1.5 V → 1 V → 500 mV
    custom_voltage_setpoints = [0.1,1,0.1]

    # ==================== Assemble the full parameter set ======================
    custom_parameters = WaveformVoltageSourceAndMeasureParameters(
        voltage_channel_settings=custom_channel_settings,
        execution_settings=custom_execution_settings,
        timing_parameters=custom_timing_parameters,
        voltage_setpoints=custom_voltage_setpoints,
        trigger_parameters=custom_trigger_parameters,
    )

    # ================= Execute source and measure ==============================
    results = waveform_voltage_source_and_measure.configure_and_measure(
        configuration=custom_parameters
    )

    # ===================== Close the SMU/PPS session ===========================
    waveform_voltage_source_and_measure.close()

    # Print the measurement results
    print(results)

    # ===================== Plot voltage and current waveforms ==================
    plot_waveforms(results.measurement_results)


if __name__ == "__main__":
    main()
