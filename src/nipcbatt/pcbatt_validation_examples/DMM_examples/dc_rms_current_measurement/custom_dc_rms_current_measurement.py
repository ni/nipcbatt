"""DMM DC-RMS Current measurement example with custom input parameters."""

import nidmm

import nipcbatt
from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM DC-RMS current measurement with logging."""
    dmm_current_measurement = dmm.DcRmsCurrentMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\current_measurement_logger.txt")
    logger.attach(dmm_current_measurement)

    config = dmm.DcRmsCurrentMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=5.0,
            slope=dmm.Slope.FALLING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=dmm.CurrentRangeAndFunctions.DC_1A,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_3_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )
    # ======================= Initialize the DMM ============================
    dmm_current_measurement.initialize("Sim_DMM", 50)

    # ================= Custom measurement configuration ===================
    measurement = dmm_current_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    dmm_current_measurement.close()

    # Print the measurement result
    print(measurement.dmm_execution_settings, measurement.measurement)
    print("executed succesfully")


if __name__ == "__main__":
    main()
