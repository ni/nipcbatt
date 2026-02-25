"""DMM Resistance measurement example with custom input parameters."""

import nidmm

from nipcbatt import dmm
from nipcbatt.pcbatt_library.common.common_data_types import MeasurementExecutionType
from nipcbatt.pcbatt_library.dmm.common.common_data_types import (
    ResolutionInDigits,
    Slope,
    TimingParameters,
    TriggerParameters,
)
from nipcbatt.pcbatt_library.dmm.resistance_measurements.resistance_data_types import (
    ResistanceMeasurementConfiguration,
    ResistanceMeasurementFunctionParameters,
    ResistanceRangeAndFunctions,
)
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger


def main():
    """Configures and executes custom DMM resistance measurement with logging.

    Returns:
        ResistanceMeasurementResultData: Measurement results including
            execution settings and measured resistance values.
    """
    resistance_measurement = dmm.DcRmsResistanceMeasurement()

    logger = PcbattLogger(file="c:\\Temp\\resistance_measurement_logger.txt")

    logger.attach(resistance_measurement)

    config = ResistanceMeasurementConfiguration(
        execution_type=MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        trigger_parameters=TriggerParameters(
            trigger_source=nidmm.TriggerSource.IMMEDIATE,
            trigger_delay=-1.0,
            slope=Slope.FALLING_EDGE,
            enable_trigger=False,
        ),
        measurement_function_parameters=ResistanceMeasurementFunctionParameters(
            measurement_function=ResistanceRangeAndFunctions.TWO_W_RES_100k_Ohm,
            resolution_in_digits=ResolutionInDigits.DIGITS_6_5,
        ),
        timing_parameters=TimingParameters(aperture_time_seconds=-1.0, settle_time_seconds=-1.0),
        ac_min_frequency=40.0,
    )

    # ======================= Initialize the DMM ============================
    resistance_measurement.initialize("DMM", 50)

    # ================= Custom measurement configuration ===================
    measurement = resistance_measurement.configure_and_measure(configuration=config)

    # ===================== Close the DMM session ===========================
    resistance_measurement.close()

    # Print the measurement result
    print(measurement.dmm_execution_settings, measurement.measurement)
    print("executed succesfully")


if __name__ == "__main__":
    main()
