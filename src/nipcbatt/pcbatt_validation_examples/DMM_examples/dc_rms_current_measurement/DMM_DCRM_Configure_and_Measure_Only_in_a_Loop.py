"""DMM DC-RMS Current measurement in loop example with custom input parameters."""

import time

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
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.DcRmsCurrentMeasurementFunctionParameters(
            measurement_function=dmm.CurrentRangeAndFunctions.DC_1A,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_5_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )

    # Number of measurements to take in the loop
    number_of_measurements = 5

    # ======================= Initialize the DMM ============================
    dmm_current_measurement.initialize("Sim_DMM", 50)

    # ================= Configure once, then measure in a loop ===================
    config_only = dmm.DcRmsCurrentMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.CONFIGURE_ONLY,
        trigger_parameters=config.trigger_parameters,
        measurement_function_parameters=config.measurement_function_parameters,
        timing_parameters=config.timing_parameters,
        ac_min_frequency=config.ac_min_frequency,
    )

    measure_only = dmm.DcRmsCurrentMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.MEASURE_ONLY,
        trigger_parameters=config.trigger_parameters,
        measurement_function_parameters=config.measurement_function_parameters,
        timing_parameters=config.timing_parameters,
        ac_min_frequency=config.ac_min_frequency,
    )

    # Configure the DMM once before the loop
    dmm_current_measurement.configure_and_measure(configuration=config_only)

    # Measure in a loop
    for i in range(number_of_measurements):
        measurement = {}
        measurement["value"] = dmm_current_measurement.configure_and_measure(
            configuration=measure_only
        )
        print(measurement["value"])
        time.sleep(2)  # Wait for 2 seconds between measurements

    # ===================== Close the DMM session ===========================
    dmm_current_measurement.close()


if __name__ == "__main__":
    main()
