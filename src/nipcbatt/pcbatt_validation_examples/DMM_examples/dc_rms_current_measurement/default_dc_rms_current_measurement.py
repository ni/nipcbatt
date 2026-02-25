"""DMM DC RMS Current measurement example with default input parameters."""

from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes default DMM DC RMS current measurement with logging.

    Returns:
        DcRmsCurrentMeasurementResultData: Measurement results including
            execution settings and measured current values.
    """
    dmm_current_measurement = dmm.DcRmsCurrentMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\current_measurement_logger.txt")
    logger.attach(dmm_current_measurement)
    
    # ======================= Initialize the DMM ============================
    dmm_current_measurement.initialize("DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = dmm_current_measurement.configure_and_measure(
        configuration=dmm.DEFAULT_DC_RMS_CURRENT_MEASUREMENT_CONFIGURATION
    )

    # ===================== Close the DMM session ===========================
    dmm_current_measurement.close()

    # Print the measurement result
    print(measurement.dmm_execution_settings, measurement.measurement)
    print("executed succesfully")


if __name__ == "__main__":
    main()
