"""Example implementation demonstrating power-up sequencing using DC voltage library."""

import time

import matplotlib.pyplot as plt
import nidaqmx.constants
import nidcpower
import numpy as np

import nipcbatt
from nipcbatt import daq, dcpower


def main():
    """Execute a two-channel DC CV power-up sequence with DAQ sync.

    Sequence
    --------
    1. Pre-configure the TDVM (CONFIGURE_ONLY, armed for HW trigger from SMU2).
    2. Initialize SMU1 (rail 1) and SMU2 (rail 2).
    3. Configure both channels (CONFIGURE_ONLY) with output disabled.
    4. Start both sources in software (START_SOURCE_ONLY, outputs still off).
    5. Wait 10 ms to let the sources settle before enabling outputs.
    6. Enable rail-1 output (SMU1).
    7. Wait 100 ms (inter-rail sequencing delay).
    8. Enable rail-2 output (SMU2) — this also fires the TDVM start trigger.
    9. Wait 500 ms to allow the rails to reach steady state.
    10. Measure both channels (MEASURE_ONLY) and close DC power sessions.
    11. Collect the TDVM waveforms (MEASURE_ONLY) and close the DAQ session.
    12. Plot all eight acquired voltage waveforms vs. time.
    """
    dc_voltage_1 = dcpower.DCVoltageSourceAndMeasure()
    dc_voltage_2 = dcpower.DCVoltageSourceAndMeasure()

    # --- Channel 1 settings ---
    voltage_channel_settings_1 = dcpower.VoltageChannelSettings(
        voltage_level=1.0,
        voltage_level_range=1.0,
        current_limit=0.1,
        current_limit_range=0.1,
        sensing=nidcpower.Sense.REMOTE,
        enable_output=False,
    )
    timing_parameters_1 = dcpower.TimingParameters(
        source_delay=0.1,
        aperture_time=0.02,
        transient_response=nidcpower.TransientResponse.FAST,
    )
    trigger_parameters_1 = dcpower.TriggerParameters(
        source_trigger_behavior=dcpower.SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=dcpower.ExportEvent.NONE,
        event_signal_to_export=dcpower.EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="",
    )

    # --- Channel 2 settings ---
    voltage_channel_settings_2 = dcpower.VoltageChannelSettings(
        voltage_level=1.0,
        voltage_level_range=1.0,
        current_limit=0.01,
        current_limit_range=0.1,
        sensing=nidcpower.Sense.REMOTE,
        enable_output=False,
    )
    timing_parameters_2 = dcpower.TimingParameters(
        source_delay=0.1,
        aperture_time=0.02,
        transient_response=nidcpower.TransientResponse.FAST,
    )
    trigger_parameters_2 = dcpower.TriggerParameters(
        source_trigger_behavior=dcpower.SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=dcpower.ExportEvent.NONE,
        event_signal_to_export=dcpower.EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="",
    )

    def make_config_1(
        execution_type: dcpower.MeasurementExecutionType,
    ) -> dcpower.DCVoltageSourceAndMeasureParameters:
        """Returns channel-1 parameters for the given execution type."""
        return dcpower.DCVoltageSourceAndMeasureParameters(
            voltage_channel_settings=voltage_channel_settings_1,
            execution_settings=dcpower.ExecutionSettings(
                execution_type=execution_type,
                skip_analysis=False,
            ),
            timing_parameters=timing_parameters_1,
            trigger_parameters=trigger_parameters_1,
        )

    def make_config_2(
        execution_type: dcpower.MeasurementExecutionType,
    ) -> dcpower.DCVoltageSourceAndMeasureParameters:
        """Returns channel-2 parameters for the given execution type."""
        return dcpower.DCVoltageSourceAndMeasureParameters(
            voltage_channel_settings=voltage_channel_settings_2,
            execution_settings=dcpower.ExecutionSettings(
                execution_type=execution_type,
                skip_analysis=False,
            ),
            timing_parameters=timing_parameters_2,
            trigger_parameters=trigger_parameters_2,
        )

    # ======================== TDVM configuration region ==========================

    tdvm = daq.TimeDomainMeasurement()
    tdvm.initialize(analog_input_channel_expression="DAQ/ai0:7")

    global_channel_parameters = daq.VoltageRangeAndTerminalParameters(
        terminal_configuration=nidaqmx.constants.TerminalConfiguration.RSE,
        range_min_volts=-10,
        range_max_volts=10,
    )

    sample_clock_timing_parameters = nipcbatt.SampleClockTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=10000,
        number_of_samples_per_channel=20000,  # Default is 1000, but we want a larger window to capture the power-up sequence
        sample_timing_engine=nipcbatt.SampleTimingEngine.AUTO,
    )

    specific_channels_parameters = []

    measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    digital_start_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.DIGITAL_TRIGGER,
        digital_start_trigger_source="/SMU2/Engine0/StartTrigger",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    tdvm_config = daq.TimeDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=measurement_options,
        sample_clock_timing_parameters=sample_clock_timing_parameters,
        digital_start_trigger_parameters=digital_start_trigger_parameters,
    )

    # endregion tdvm configure only
    tdvm.configure_and_measure(configuration=tdvm_config)

    # ========================= Initialize ==================================
    dc_voltage_1.initialize(resource_name="SMU1/0")
    dc_voltage_2.initialize(resource_name="SMU2/0")

    # ========================= Configure only ==============================
    dc_voltage_1.configure_and_measure(
        configuration=make_config_1(dcpower.MeasurementExecutionType.CONFIGURE_ONLY)
    )
    dc_voltage_2.configure_and_measure(
        configuration=make_config_2(dcpower.MeasurementExecutionType.CONFIGURE_ONLY)
    )

    # ========================= Start source only ===========================
    dc_voltage_1.configure_and_measure(
        configuration=make_config_1(dcpower.MeasurementExecutionType.START_SOURCE_ONLY)
    )
    dc_voltage_2.configure_and_measure(
        configuration=make_config_2(dcpower.MeasurementExecutionType.START_SOURCE_ONLY)
    )

    # =========================== Delay before start source  =======================
    time.sleep(0.010)  # Time delay to allow the source to start before enabling output

    dc_voltage_1.enable_output(True)

    # ====================== Time adjustment between rails ==========================
    time.sleep(0.100)  # Time delay to be used to adjust the delay between the power supplies

    dc_voltage_2.enable_output(True)

    # ========================= Delay before turn-off source ========================
    time.sleep(0.500)  # Time delay to have delay before the measurement and turn off source

    # ========================= Measure only ================================
    dc_cv_measurements_1 = dc_voltage_1.configure_and_measure(
        configuration=make_config_1(dcpower.MeasurementExecutionType.MEASURE_ONLY)
    )
    dc_cv_measurements_2 = dc_voltage_2.configure_and_measure(
        configuration=make_config_2(dcpower.MeasurementExecutionType.MEASURE_ONLY)
    )

    # ========================= Close sessions ==============================
    dc_voltage_1.close()
    dc_voltage_2.close()

    # # ========================= TDVM measure only ============================
    tdvm_measurement_options = nipcbatt.MeasurementOptions(
        execution_option=nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        measurement_analysis_requirement=nipcbatt.MeasurementAnalysisRequirement.PROCEED_TO_ANALYSIS,
    )

    tdvm_measure_only_config = daq.TimeDomainMeasurementConfiguration(
        global_channel_parameters=global_channel_parameters,
        specific_channels_parameters=specific_channels_parameters,
        measurement_options=tdvm_measurement_options,
        sample_clock_timing_parameters=sample_clock_timing_parameters,
        digital_start_trigger_parameters=digital_start_trigger_parameters,
    )

    tdvm_result_data = tdvm.configure_and_measure(configuration=tdvm_measure_only_config)

    tdvm.close()

    #  Print results
    print("DC CV Measurements (Channel 1):", dc_cv_measurements_1)
    print("DC CV Measurements (Channel 2):", dc_cv_measurements_2)

    tdvm_w0 = tdvm_result_data.waveforms[0].samples.tolist()
    tdvm_w1 = tdvm_result_data.waveforms[1].samples.tolist()
    tdvm_w2 = tdvm_result_data.waveforms[2].samples.tolist()
    tdvm_w3 = tdvm_result_data.waveforms[3].samples.tolist()
    tdvm_w4 = tdvm_result_data.waveforms[4].samples.tolist()
    tdvm_w5 = tdvm_result_data.waveforms[5].samples.tolist()
    tdvm_w6 = tdvm_result_data.waveforms[6].samples.tolist()
    tdvm_w7 = tdvm_result_data.waveforms[7].samples.tolist()

    tdvm_delta_time_seconds = tdvm_result_data.waveforms[0].delta_time_seconds
    tdvm_time_seconds = (
        np.arange(len(tdvm_result_data.waveforms[0].samples.tolist())) * tdvm_delta_time_seconds
    )

    plt.plot(tdvm_time_seconds, tdvm_w0, label="TDVM ai0")
    plt.plot(tdvm_time_seconds, tdvm_w1, label="TDVM ai1")
    plt.plot(tdvm_time_seconds, tdvm_w2, label="TDVM ai2")
    plt.plot(tdvm_time_seconds, tdvm_w3, label="TDVM ai3")
    plt.plot(tdvm_time_seconds, tdvm_w4, label="TDVM ai4")
    plt.plot(tdvm_time_seconds, tdvm_w5, label="TDVM ai5")
    plt.plot(tdvm_time_seconds, tdvm_w6, label="TDVM ai6")
    plt.plot(tdvm_time_seconds, tdvm_w7, label="TDVM ai7")
    plt.title("Voltage Waveform")
    plt.ylabel("Voltage (V)")
    plt.xlabel("Time (s)")
    plt.xticks(np.linspace(0, tdvm_time_seconds[-1], 11))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
