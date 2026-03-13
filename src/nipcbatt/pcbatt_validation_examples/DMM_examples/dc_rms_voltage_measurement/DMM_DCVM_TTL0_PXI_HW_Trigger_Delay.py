"""Signal Voltage Generation connected to DMM DC-RMS Voltage Measurement.""" 
### Ensure correct hardware and corresponding trigger names before running this example

import threading
import time

import nidaqmx.constants
import nidmm

import nipcbatt
from nipcbatt import dmm, daq
from nipcbatt.pcbatt_utilities.pcbatt_logger import PcbattLogger

def main():
    # Initialize SVG and DMM
    svg = daq.SignalVoltageGeneration()
    svg.initialize(channel_expression="Sim_DAQ/ao0")

    dmm_voltage_measurement = dmm.DcRmsVoltageMeasurement()
    dmm_voltage_measurement.initialize("Sim_DMM", 50.0)

    # Add logger to DMM
    logger = PcbattLogger(file="c:\\Temp\\svg_dmm_logger.txt")
    logger.attach(dmm_voltage_measurement)

    # SVG parameters configuration
    voltage_generation_range_parameters = nipcbatt.VoltageGenerationChannelParameters(
        range_min_volts=-10.0,
        range_max_volts=10.0,
    )

    svg_timing_parameters = daq.SignalVoltageGenerationTimingParameters(
        sample_clock_source="OnboardClock",
        sampling_rate_hertz=100000,
        generated_signal_duration_seconds=4.0,  
    )

    svg_trigger_parameters = nipcbatt.DigitalStartTriggerParameters(
        trigger_select=nipcbatt.StartTriggerType.NO_TRIGGER,
        digital_start_trigger_source="",
        digital_start_trigger_edge=nidaqmx.constants.Edge.RISING,
    )

    svg_tone_parameters = daq.ToneParameters(
        tone_frequency_hertz=100,   
        tone_amplitude_volts=10.0,   
        tone_phase_radians=0,
    )

    svg_waveform_parameters = daq.SignalVoltageGenerationSineWaveParameters(
        generated_signal_offset_volts=0,
        generated_signal_tone_parameters=svg_tone_parameters,
    )

    svg.configure_all_channels(parameters=voltage_generation_range_parameters)
    svg.configure_timing(parameters=svg_timing_parameters)
    svg.configure_trigger(parameters=svg_trigger_parameters)

    # Route AO start-trigger → PXI_Trig0
    svg.route_start_trigger_signal_to_terminal("PXI_Trig0")

    # Configure DMM to wait for trigger on PXI_Trig0
    dmm_config = dmm.DcRmsVoltageMeasurementConfiguration(
        execution_type=nipcbatt.MeasurementExecutionType.CONFIGURE_AND_MEASURE,
        measurement_function_parameters=dmm.DcRmsVoltageMeasurementFunctionParameters(
            measurement_function=dmm.VoltageRangeAndFunctions.AC_20V,
            resolution_in_digits=dmm.ResolutionInDigits.DIGITS_5_5,
        ),
        trigger_parameters=dmm.TriggerParameters(
            trigger_source=nidmm.TriggerSource.PXI_TRIG0,  
            trigger_delay=1.0,                              
            slope=dmm.Slope.RISING_EDGE,
            enable_trigger=True,
        ),
        timing_parameters=dmm.TimingParameters(
            aperture_time_seconds=-1.0,  
            settle_time_seconds=-1.0,    
        ),
        ac_min_frequency=40.0,
    )

    # DMM voltage measurement in background thread 
    dmm_result    = {}

    def _dmm_measure():
        dmm_result["value"] = dmm_voltage_measurement.configure_and_measure(
            configuration=dmm_config
        )

    dmm_thread = threading.Thread(target=_dmm_measure, daemon=True)
    dmm_thread.start()

    # 2 seconds wait
    time.sleep(2.0)

    svg.generate_voltage_sine_waveform(
        signal_parameters=svg_waveform_parameters,
        timing_parameters=svg_timing_parameters,
    )

    # Wait for DMM thread to complete 
    dmm_thread.join(timeout=15.0)

    # Close resources
    svg.close()
    dmm_voltage_measurement.close()

    print(dmm_result["value"])


if __name__ == "__main__":
    main()