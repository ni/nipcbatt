"""DC constant voltage source and measure example with default input parameters."""

from nipcbatt import dcpower
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes DC CV source and measure using default constants."""
    dc_voltage_source_and_measure = dcpower.DCVoltageSourceAndMeasure()

    # PcbattLogger logs NI-DCPower configurations and measurement results
    # to the mentioned file path.
    logger = PcbattLogger(file="c:\\Temp\\dc_cv_source_and_measure_logger.txt")
    logger.attach(dc_voltage_source_and_measure)

    # ======================= Initialize the SMU/PPS ============================
    dc_voltage_source_and_measure.initialize(resource_name="PPS1/0")

    # ================= Default measurement configuration ===================
    results = dc_voltage_source_and_measure.configure_and_measure(
        configuration=dcpower.DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS
    )

    # ===================== Close the SMU/PPS session ===========================
    dc_voltage_source_and_measure.close()

    # Print the measurement results
    print(results)


if __name__ == "__main__":
    main()
