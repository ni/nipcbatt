"""Resistance measurement example with default input parameters."""

from nipcbatt import dmm
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes default resistance measurement with logging."""
    resistance_measurement = dmm.DcRmsResistanceMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\resistance_measurement_logger.txt")
    logger.attach(resistance_measurement)

    # ======================= Initialize the DMM ============================
    resistance_measurement.initialize("Sim_DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = resistance_measurement.configure_and_measure(
        configuration=dmm.DEFAULT_RESISTANCE_MEASUREMENT_CONFIGURATION
    )

    # ===================== Close the DMM session ===========================
    resistance_measurement.close()

    # Print the measurement result
    print(measurement)


if __name__ == "__main__":
    main()