"""Waveform DC voltage source and measure example with custom input parameters."""

import nidcpower
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
        stitle="Waveform CV Source and Measure (Custom Parameters)",
    )


def main():
    """Configures and executes waveform CV source and measure using custom parameters."""
    waveform_voltage_source_and_measure = dcpower.WaveformVoltageSourceAndMeasure()

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\custom_waveform_cv_source_and_measure_logger.txt")
    logger.attach(waveform_voltage_source_and_measure)

    # ======================= Initialize the SMU/PPS ============================
    waveform_voltage_source_and_measure.initialize(resource_name="SMU1/0")

    # ==================== Custom channel settings ==============================
    # Voltage level range: 6 V, current limit: 50 mA, current limit range: 100 mA.
    # Ramp 500 mV → 1 V → 500 mV, 200 ms per step, local sensing, output enabled.
    custom_channel_settings = dcpower.WaveformVoltageChannelSettings(
        voltage_level_range=6.0,
        current_limit_range=0.02,
        current_limit=0.02,
        step_time=0.100,
        sensing=nidcpower.Sense.LOCAL,
        enable_output=True,
        voltage_setpoints=[0.1, 1, 0.1],
    )

    # ==================== Custom execution settings ============================
    # Execute configure + source + measure in a single call; run full analysis.
    custom_execution_settings = dcpower.WaveformExecutionSettings(
        execution_type=dcpower.MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
        skip_analysis=False,
    )

    # ==================== Custom timing parameters =============================
    # Source delay: 200 ms, aperture time: 2 ms, custom transient response.
    custom_timing_parameters = dcpower.WaveformTimingParameters(
        source_delay=0.00,                  # Source delay = 200 ms
        aperture_time=0.001,                 # Aperture time = 2 ms
        transient_response=nidcpower.TransientResponse.NORMAL,  # Transient response = Normal
        voltage_gain_bandwidth=10000.0,      # Hz
        voltage_compensation_frequency=50000.0,  # Hz
        voltage_pole_zero_ratio=0.16,
        current_gain_bandwidth=50000.0,      # Hz
        current_compensation_frequency=250000.0,  # Hz
        current_pole_zero_ratio=5.0,
    )

    # ==================== Custom trigger parameters ============================
    # Disable source trigger; export the Source Complete Event to PXI_Trig0.
    custom_trigger_parameters = dcpower.TriggerParameters(
        source_trigger_behavior=dcpower.SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=dcpower.ExportEvent.NONE,
        event_signal_to_export=dcpower.EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="PXI_Trig0",
    )

    # ==================== Assemble the full parameter set ======================
    custom_parameters = dcpower.WaveformVoltageSourceAndMeasureParameters(
        voltage_channel_settings=custom_channel_settings,
        execution_settings=custom_execution_settings,
        timing_parameters=custom_timing_parameters,
        trigger_parameters=custom_trigger_parameters,
    )

    # ================= Execute source and measure ==============================
    results = waveform_voltage_source_and_measure.configure_and_measure(
        configuration=custom_parameters
    )

    # ===================== Close the SMU/PPS session ===========================
    waveform_voltage_source_and_measure.close()

    # Print the execution settings 
    print(results)

    # ===================== Plot voltage and current waveforms ==================
    plot_waveforms(results)


if __name__ == "__main__":
    main()
