"""DMM DC RMS Voltage mmeasurement example with custom input parameters."""

import nidmm

from nipcbatt.pcbatt_library import dmm
from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    Slope,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.dc_rms_voltage_measurements.dc_rms_voltage_data_types import (
    DcRmsVoltageMeasurementConfiguration,
    DcRmsVoltageMeasurementFunctionParameters,
    VoltageRangeAndFunctions,
)
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM DC RMS voltage measurement with logging.

    Returns:
        DcRmsVoltageMeasurementResultData: Measurement results including
            execution settings and measured voltage values.
    """
    dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\voltage_measurement_logger.txt")
    logger.attach(dmm_voltage_measurement)

    config = DcRmsVoltageMeasurementConfiguration(
        MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=5.0,
            slope=Slope.RISING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=VoltageRangeAndFunctions.DC_1V,
            resolution_in_digits=ResolutionInDigits.DIGITS_5_5,
        ),
        timing_parameters=TimingParameters(
            aperture_time_seconds=-1.0,
            settle_time_seconds=-1.0,
        ),
        ac_min_frequency=40.0,
    )
    # ======================= Initialize the DMM ============================
    dmm_voltage_measurement.initialize("DMM", 50)

    # ================= Default measurement configuration ===================
    measurement = dmm_voltage_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    dmm_voltage_measurement.close()

    # Print the measurement result
    print(measurement.dmm_execution_settings, measurement.measurement)


if __name__ == "__main__":
    main()
