"""DMM Mixed mmeasurement example with custom input parameters."""

import nidmm

import nipcbatt
from nipcbatt.pcbatt_library import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM mixed measurement with logging."""
    dmm_mixed_measurement = dmm.MixedMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\mixed_measurement_logger.txt")
    logger.attach(dmm_mixed_measurement)

    config = dmm.MixedMeasurementConfiguration(
        execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=2.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.MixedMeasurementFunctionParameters(
            measurement_function=dmm.MixedRangeAndFunctions.AC_Current_Auto_Range,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_5_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )
    # ======================= Initialize the DMM ============================
    dmm_mixed_measurement.initialize("Sim_DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = dmm_mixed_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    dmm_mixed_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()
