"""DC constant voltage source and measure example with custom input parameters."""

import nidcpower

from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes DC CV source and measure using custom parameters."""
    dc_voltage_source_and_measure = dcpower.DCVoltageSourceAndMeasure()

    # Configure custom voltage channel settings
    voltage_channel_settings = dcpower.VoltageChannelSettings(
        voltage_level=1.0,
        voltage_level_range=2.0,
        current_limit=0.01,
        current_limit_range=0.1,
        sensing=nidcpower.Sense.REMOTE,
        enable_output=True,
    )

    # Configure custom timing parameters
    timing_parameters = dcpower.TimingParameters(
        source_delay=0.1,
        aperture_time=0.02,
        transient_response=nidcpower.TransientResponse.NORMAL,
    )

    # Configure custom trigger parameters
    trigger_parameters = dcpower.TriggerParameters(
        source_trigger_behavior=dcpower.SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=dcpower.ExportEvent.Route_Event,
        event_signal_to_export=dcpower.EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="",
    )

    # Build the full measurement configuration
    configuration = dcpower.DCVoltageSourceAndMeasureParameters(
        voltage_channel_settings=voltage_channel_settings,
        execution_settings=dcpower.ExecutionSettings(
            execution_type=dcpower.MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
            skip_analysis=False,
        ),
        timing_parameters=timing_parameters,
        trigger_parameters=trigger_parameters,
    )
    # ======================= Initialize the SMU/PPS ============================
    dc_voltage_source_and_measure.initialize(resource_name="PPS1/0")

    # PcbattLogger logs NI-DCPower configurations and measurement results to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\dc_cv_source_and_measure_logger.csv")
    logger.attach(dc_voltage_source_and_measure)

    # ================== Custom measurement configuration ===================
    results = dc_voltage_source_and_measure.configure_and_measure(
        configuration=configuration
    )

    # ===================== Close the SMU/PPS session ===========================
    dc_voltage_source_and_measure.close()

    # Print the measurement results
    print(results)


if __name__ == "__main__":
    main()