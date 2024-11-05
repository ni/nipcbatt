"""
Save environment config, inputs and outputs from pcbatt
"""
import os
from datetime import datetime
from pathlib import Path
from typing import Union
import sys
import inspect
import pkg_resources
import struct

import nipcbatt
from nipcbatt.pcbatt_utilities.csv_utilities import export_signal_to_csv_file


# Using Union because PEP 604 was implemented in 3.10
# https://peps.python.org/pep-0604/
def save_traces(
    config: Union[
        nipcbatt.DcRmsCurrentMeasurementConfiguration,
        nipcbatt.DcRmsVoltageMeasurementConfiguration,
        nipcbatt.PowerSupplySourceAndMeasureConfiguration,
        nipcbatt.TimeDomainMeasurementConfiguration,
        nipcbatt.TemperatureRtdMeasurementConfiguration,
        nipcbatt.TemperatureThermistorMeasurementConfiguration,
    ],
    file_name: str,
    result_data: Union[
        nipcbatt.DcRmsCurrentMeasurementResultData,
        nipcbatt.DcRmsVoltageMeasurementResultData,
        nipcbatt.PowerSupplySourceAndMeasureResultData,
        nipcbatt.TimeDomainMeasurementResultData,
        nipcbatt.TemperatureMeasurementResultData,
    ] = None,
    sampling_rate: int = 10000,
    unit: str = "Amplitude",
):
    """
    This method is use to save any types of confiuration and result_data from nipcbatt
    the file are stored in a folder called results one folder above the caller
    it creates a folder with the date month-day-year_hour-minute-seconde
    it stores all waveforms in different csv files and the rest in a txt

    Args:
        config (Any Configuration): Configuration from nipcbatt
        file_name (str): name use to save the traces
        result_data (Any ResultData, optional): Result data from nipcbatt. Defaults to None.
        sampling_rate (int, optional): sampling rate. Defaults to 10000.
        unit (str, optional): unit use for the waveforms. Defaults to 'Amplitude'.
    """

    # Retrieve the caller path
    stack = inspect.stack()
    first_caller = stack[1]
    caller_path = first_caller[1]
    caller_name = Path(os.path.basename(caller_path)).stem

    now = datetime.now()
    current_time = now.strftime("%m-%d-%Y_%H-%M-%S")

    # Get the name of the used file to store the result
    folder_name = caller_name
    # Create folder if don't exist
    parent_folder = os.path.dirname(os.path.dirname(caller_path))
    result_folder = os.path.join(parent_folder, "results", folder_name, current_time)
    os.makedirs(result_folder, exist_ok=True)

    text_file = os.path.join(result_folder, file_name + ".txt")

    f = open(text_file, mode="a", encoding="utf-8")

    # Using version_info instead version because it was too much information and some are confusing
    f.write(
        "Python : "
        + str(sys.version_info.major)
        + "."
        + str(sys.version_info.minor)
        + "."
        + str(sys.version_info.micro)
        + " "
    )
    f.write(str(struct.calcsize("P") * 8) + "bits\n")
    f.write("nipcbatt : " + pkg_resources.get_distribution("nipcbatt").version + "\n\n\n")

    if config:
        f.write("inputs :\n")
        for attribute in config.__dict__:
            element = getattr(config, attribute)
            f.write(attribute + ": " + str(element) + "\n")
        f.write("\n\n")

    if result_data:
        f.write("outputs :\n")
        for attribute in result_data.__dict__:
            element = getattr(result_data, attribute)
            if isinstance(element, nipcbatt.AnalogWaveform):
                # f'{element=}'.split('=')[0] get the name of the variable
                # example voltage_waveform
                file_name = file_name + attribute + ".csv"
                export_signal_to_csv_file(
                    signal_csv_file_path=os.path.join(result_folder, file_name),
                    signal_samples=element.samples.tolist(),
                    signal_sampling_rate=sampling_rate,
                    x_axis_name="Time(s)",
                    y_axis_name=unit,
                )
            # Check if it's a list and that all elements are nipcbatt.AnalogWaveform
            elif isinstance(element, list) and all(
                isinstance(item, nipcbatt.AnalogWaveform) for item in element
            ):
                for waveform in element:
                    # Replace / from channel names to _
                    file_name = "tdm_" + waveform.channel_name.replace("/", "_") + ".csv"
                    export_signal_to_csv_file(
                        signal_csv_file_path=os.path.join(result_folder, file_name),
                        signal_samples=waveform.samples.tolist(),
                        signal_sampling_rate=sampling_rate,
                        x_axis_name="Time(s)",
                        y_axis_name=unit,
                    )
            else:
                f.write(attribute + ": " + str(element) + "\n")
    f.close()
