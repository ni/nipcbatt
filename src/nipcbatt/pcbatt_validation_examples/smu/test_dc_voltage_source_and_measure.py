import nidcpower

from nipcbatt.pcbatt_library.smu import DCVoltageSourceAndMeasure
from nipcbatt.pcbatt_library.smu import (
    DCVoltageSourceAndMeasureParameters,
    EventSignalToExport,
    ExportEvent,
    MeasurementExecutionType,
    SourceTriggerBehavior,
    TimingParameters,
    TriggerParameters,
    VoltageChannelSettings,
)


def test_dc_voltage_source_and_measure():
    dc_voltage_source_and_measure = DCVoltageSourceAndMeasure()
    dc_voltage_source_and_measure.initialize(resource_name="PPS1/0")

    voltage_channel_settings = VoltageChannelSettings(
        voltage_level=1.0,
        voltage_level_range=2.0,
        current_limit=0.01,
        current_limit_range=0.1,
        sensing=nidcpower.Sense.REMOTE,
        enable_output=True,
    )

    timing_parameters = TimingParameters(
        source_delay=0.1,
        aperture_time=0.02,
        transient_response=nidcpower.TransientResponse.NORMAL,
    )

    trigger_parameters = TriggerParameters(
        source_trigger_behavior=SourceTriggerBehavior.Disable_Source_Trigger,
        start_source_name="",
        export_event=ExportEvent.NONE,
        event_signal_to_export=EventSignalToExport.Source_Complete_Event,
        output_event_signal_terminal="",
    )

    configuration = DCVoltageSourceAndMeasureParameters(
        voltage_channel_settings=voltage_channel_settings,
        execution_type=MeasurementExecutionType.CONFIGURE_SOURCE_AND_MEASURE,
        timing_parameters=timing_parameters,
        trigger_parameters=trigger_parameters,
    )

    result = dc_voltage_source_and_measure.configure_and_measure(configuration=configuration)
    print(f"Execution Settings: {result}")

    dc_voltage_source_and_measure.close()


if __name__ == "__main__":
    test_dc_voltage_source_and_measure()