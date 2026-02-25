"""DMM DC RMS Voltage mmeasurement example with default input parameters."""

from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes default DMM DC RMS voltage measurement with logging.

    Returns:
        DcRmsVoltageMeasurementResultData: Measurement results including
            execution settings and measured voltage values.
    """
    dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\voltage_measurement_logger.txt")
    logger.attach(dmm_voltage_measurement)
    
    # ======================= Initialize the DMM ============================
    dmm_voltage_measurement.initialize("DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = dmm_voltage_measurement.configure_and_measure(
        configuration=dmm.DEFAULT_DC_RMS_VOLTAGE_MEASUREMENT_CONFIGURATION
    )

    # ===================== Close the DMM session ===========================
    dmm_voltage_measurement.close()

    # Print the measurement result
    print(measurement.dmm_execution_settings, measurement.measurement)


if __name__ == "__main__":
    main()
