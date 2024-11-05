"""Provides a set of csv related routines."""

import os
from typing import Iterable

import numpy
import pandas
from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def export_signal_to_csv_file(
    signal_csv_file_path: str,
    signal_samples: Iterable[float],
    signal_sampling_rate: float,
    x_axis_name: str,
    y_axis_name: str,
):
    """Exports a sequence of float elements into a csv file as a signal.

    Args:
        signal_csv_file_path (str): path where csv file will be placed.
        signal_samples (Iterable[float]): content of the second column.
        signal_sampling_rate (float): sampling rate of the signal,
            will be used to infere content of the second column.
        x_axis_name (str): name of the first column.
        y_axis_name (str): name of the second column.
    Raises:
        ValueError: is raised when one of the provided
            argument is not supported.
    """
    Guard.is_not_none(signal_csv_file_path, nameof(signal_csv_file_path))
    Guard.is_not_empty(signal_csv_file_path, nameof(signal_csv_file_path))
    Guard.is_not_none(signal_samples, nameof(signal_samples))
    Guard.is_greater_than_zero(signal_sampling_rate, nameof(signal_sampling_rate))

    Guard.is_not_none(x_axis_name, nameof(x_axis_name))
    Guard.is_not_empty(x_axis_name, nameof(x_axis_name))
    Guard.is_not_none(y_axis_name, nameof(y_axis_name))
    Guard.is_not_empty(y_axis_name, nameof(y_axis_name))

    signal_dates = [
        sample_index / signal_sampling_rate for sample_index in range(0, len(signal_samples))
    ]

    return export_columns_to_csv_file(
        csv_file_path=signal_csv_file_path,
        column1_data=signal_dates,
        column2_data=signal_samples,
        column1_name=x_axis_name,
        column2_name=y_axis_name,
    )


def export_columns_to_csv_file(
    csv_file_path: str,
    column1_data: Iterable[float],
    column2_data: Iterable[float],
    column1_name: str,
    column2_name: str,
):
    """Exports two columns of float elements into a csv file.

    Args:
        csv_file_path (str): path where csv file will be placed.
        column1_data (Iterable[float]): content of the first column.
        column2_data (Iterable[float]): content of the second column.
        column1_name (str): name of the first column.
        column2_name (str): name of the second column.
    Raises:
        ValueError: is raised when one of the provided
            argument is not supported.
    """
    Guard.is_not_none(csv_file_path, nameof(csv_file_path))
    Guard.is_not_empty(csv_file_path, nameof(csv_file_path))
    Guard.is_not_none(column1_data, nameof(column1_data))
    Guard.is_not_empty(column2_data, nameof(column2_data))
    Guard.is_not_none(column1_name, nameof(column1_name))
    Guard.is_not_empty(column2_name, nameof(column2_name))

    Guard.have_same_size(
        first_iterable_instance=column1_data,
        first_iterable_name=nameof(column1_data),
        second_iterable_instance=column2_data,
        second_iterable_name=nameof(column2_data),
    )

    write_data_frame: pandas.DataFrame = pandas.DataFrame(
        data={column1_name: column1_data, column2_name: column2_data}
    )
    write_data_frame.to_csv(path_or_buf=csv_file_path, index=False, sep=";")


def import_from_csv_file_2d_array(
    csv_file_path: str, header_is_present: bool, column_delimiter=";"
) -> tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
    """Imports from a csv file located at a given path a 2D array.

    Args:
        csv_file_path (str): path of the csv file.
        header_is_present (bool): indicates if csv file headers are present.

    Raises:
        ValueError: is raised when provided file path does not exist.
        IOError: is raised when csv file parsing fails for some reason.
        TypeError:
            is raised when csv file parsing succeeded but data conversion into 2D array fails.

    Returns:
        tuple[numpy.ndarray[numpy.float64], numpy.ndarray[numpy.float64]]:
            tuple first array represents first column of the csv file
            tuple second array represents second column of the csv file.
    """

    Guard.is_not_none(csv_file_path, nameof(csv_file_path))
    Guard.is_not_empty(csv_file_path, nameof(csv_file_path))

    if not os.path.exists(csv_file_path):
        raise ValueError(f"{nameof(csv_file_path)} ('{csv_file_path}') does not exist!")

    read_data_frame: pandas.DataFrame = None

    try:
        if header_is_present:
            read_data_frame = pandas.read_csv(
                filepath_or_buffer=csv_file_path,
                delimiter=column_delimiter,
                header="infer",
            )
        else:
            read_data_frame = pandas.read_csv(
                filepath_or_buffer=csv_file_path,
                delimiter=column_delimiter,
                header=None,
            )
    except Exception as e:
        raise IOError("Import of csv file failed for some reason!") from e

    try:
        column_1: numpy.ndarray[numpy.float64] = (
            read_data_frame[read_data_frame.columns[0]].astype(numpy.float64).array.to_numpy()
        )
        column_2: numpy.ndarray[numpy.float64] = (
            read_data_frame[read_data_frame.columns[1]].astype(numpy.float64).array.to_numpy()
        )

        return (column_1, column_2)
    except Exception as e:
        raise TypeError("Import of csv file failed due to data conversion error!") from e
