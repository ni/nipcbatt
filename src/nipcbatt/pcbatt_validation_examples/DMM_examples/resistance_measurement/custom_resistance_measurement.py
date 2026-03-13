"""Resistance measurement example with custom input parameters."""

import nidmm

import nipcbatt
from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom resistance measurement with logging."""
    resistance_measurement = dmm.DcRmsResistanceMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\resistance_measurement_logger.txt")

    logger.attach(resistance_measurement)

    config = dmm.ResistanceMeasurementConfiguration(
        execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=-1.0,
            slope=dmm.Slope.FALLING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.ResistanceMeasurementFunctionParameters(
            measurement_function=dmm.ResistanceRangeAndFunctions.TWO_W_RES_100k_Ohm,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_6_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0, settle_time_seconds=-1.0
        ),
    )

    # ======================= Initialize the DMM ============================
    resistance_measurement.initialize("Sim_DMM", 50)

    # ================= Custom measurement configuration ===================
    measurement = resistance_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    resistance_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()