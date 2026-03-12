"""DMM DC-RMS Voltage measurement example with custom input parameters."""

import nidmm

import nipcbatt
from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM DC-RMS voltage measurement with logging."""
    dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\voltage_measurement_logger.txt")
    logger.attach(dmm_voltage_measurement)

    config = dmm.DcRmsVoltageMeasurementConfiguration(
        nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=5.0,
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=dmm.VoltageRangeAndFunctions.DC_1V,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_5_5,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )
    # ======================= Initialize the DMM ============================
    dmm_voltage_measurement.initialize("Sim_DMM", 50)

    # ================= Custom measurement configuration ===================
    measurement = dmm_voltage_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    dmm_voltage_measurement.close()

    # Print the measurement result
    print(measurement.dmm_execution_settings, measurement.measurement)


if __name__ == "__main__":
    main()