"""Mixed mmeasurement example with default input parameters."""

from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes default Mixed measurement with logging."""
    dmm_mixed_measurement = dmm.MixedMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\mixed_measurement_logger.txt")
    logger.attach(dmm_mixed_measurement)

    # ======================= Initialize the DMM ============================
    dmm_mixed_measurement.initialize("Sim_DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = dmm_mixed_measurement.configure_and_measure(
        configuration=dmm.DEFAULT_MIXED_MEASUREMENT_CONFIGURATION
    )

    # ===================== Close the DMM session ===========================
    dmm_mixed_measurement.close()

    # Print the measurement result
    print(measurement.dmm_execution_settings, measurement.measurement)


if __name__ == "__main__":
    main()
