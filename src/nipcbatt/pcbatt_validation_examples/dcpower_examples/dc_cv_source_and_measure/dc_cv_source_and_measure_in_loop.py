"""DC constant voltage source and measure example running in a loop."""

import time

import nidcpower

from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures DC CV source once, then measures repeatedly in a loop."""
    dc_voltage_source_and_measure = dcpower.DCVoltageSourceAndMeasure()

    # Configure voltage channel settings
    voltage_channel_settings = dcpower.VoltageChannelSettings(
        voltage_level=1.0,
        voltage_level_range=1.0,
        current_limit=0.01,
        current_limit_range=0.1,
        sensing=nidcpower.Sense.REMOTE,
        enable_output=True,
    )

    # Configure timing parameters
    timing_parameters = dcpower.TimingParameters(
        source_delay=0.1,
        aperture_time=0.02,
        transient_response=nidcpower.TransientResponse.NORMAL,
    )

    # Configure trigger parameters
    trigger_parameters = dcpower.TriggerParameters(
        source_trigger_behavior=dcpower.SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=dcpower.ExportEvent.Route_Event,
        event_signal_to_export=dcpower.EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="",
    )

    def configuration(
        execution_type: dcpower.MeasurementExecutionType,
    ) -> dcpower.DCVoltageSourceAndMeasureParameters:
        """Builds a DCVoltageSourceAndMeasureParameters with shared channel/timing/trigger settings."""
        return dcpower.DCVoltageSourceAndMeasureParameters(
            voltage_channel_settings=voltage_channel_settings,
            execution_settings=dcpower.ExecutionSettings(
                execution_type=execution_type,
                skip_analysis=False,
            ),
            timing_parameters=timing_parameters,
            trigger_parameters=trigger_parameters,
        )

    # ======================= Initialize the SMU/PPS ====================
    dc_voltage_source_and_measure.initialize(resource_name="PPS1/0")

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\dc_cv_source_and_measure_in_loop_logger.txt")
    logger.attach(dc_voltage_source_and_measure)

    # ======================= Configure only ============================
    dc_voltage_source_and_measure.configure_and_measure(
        configuration=configuration(dcpower.MeasurementExecutionType.CONFIGURE_ONLY)
    )

    # ======================= Start source only =========================
    dc_voltage_source_and_measure.configure_and_measure(
        configuration=configuration(dcpower.MeasurementExecutionType.START_SOURCE_ONLY)
    )
    # Note: when the execution type is set to "configure_only" or "start_source_only" mode,
    #  the return data will contain valid values for "execution_settings" only and
    # "measurement_results" will be NaN after the execution.

    # ======================= Measure only in loop ======================
    num_iterations = 5
    for iteration in range(num_iterations):
        results = dc_voltage_source_and_measure.configure_and_measure(
            configuration=configuration(dcpower.MeasurementExecutionType.MEASURE_ONLY)
        )
        print(f"Iteration {iteration + 1}/{num_iterations}: {results}")
        time.sleep(1)  # Optional delay between measurements
        # Note: when the execution type is set to  "measure_only" or "configure_and_measure" mode,
        # the return data will contain valid values for both "execution_settings" and
        # "measurement_results" after the execution.

    # ======================= Close the SMU/PPS session =================
    dc_voltage_source_and_measure.close()


if __name__ == "__main__":
    main()
