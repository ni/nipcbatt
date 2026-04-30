"""DC constant voltage source and measure example with default input parameters."""

from nipcbatt import dcpower

def main():
    """Configures and executes DC CV source and measure using default constants."""
    dc_voltage_source_and_measure = dcpower.DCVoltageSourceAndMeasure()

    # ======================= Initialize the SMU/PPS ============================
    dc_voltage_source_and_measure.initialize(resource_name="PPS1/0")

    # ================= Default measurement configuration ===================
    execution_settings, measurement_results = dc_voltage_source_and_measure.configure_and_measure(
        configuration=dcpower.DEFAULT_DC_CV_SOURCE_AND_MEASURE_PARAMETERS
    )

    # ===================== Close the SMU/PPS session ===========================
    dc_voltage_source_and_measure.close()

    # Print the measurement results
    print(f"Execution Settings: {execution_settings}")
    print(f"Measurement Results: {measurement_results}")


if __name__ == "__main__":
    main()


