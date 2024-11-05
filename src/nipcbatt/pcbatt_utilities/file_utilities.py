""" Provides a set of file utilities routines."""

import os
from collections.abc import Iterable

from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def write_lines(text_file_path: str, text_file_encoding: str, text_lines: Iterable[str]):
    """Writes lines into a text file, input example ["line1", "line2", "line3"].

    Args:
        text_file_path (str): text file path.
        text_file_encoding (str): text file encoding.
        text_lines (Iterable[str]): text file lines.

    Raises:
        ValueError: occurs when one of the input arguments is None or empty string.
        IOError: occurs when reading text file fails for some reason.
    """
    Guard.is_not_none(instance=text_file_path, instance_name=nameof(text_file_path))
    Guard.is_not_empty(iterable_instance=text_file_path, instance_name=nameof(text_file_path))
    Guard.is_not_none(instance=text_lines, instance_name=nameof(text_lines))
    Guard.is_not_empty(iterable_instance=text_lines, instance_name=nameof(text_lines))

    try:
        with open(file=text_file_path, mode="w", encoding=text_file_encoding) as text_file:
            text_file.writelines(map(lambda line: f"{line}\n", text_lines))
    except Exception as e:
        raise IOError("Write text file failed for some reason!") from e


def read_lines(text_file_path: str, text_file_encoding: str) -> Iterable[str]:
    """Reads lines of a text file in a lazy way.

    Args:
        text_file_path (str): text file path.
        text_file_encoding (str): text file encoding.

    Raises:
        ValueError: occurs when one of the input arguments is None or empty string.
        IOError: occurs when reading text file fails for some reason.

    Returns:
        Iterable[str]: text file lines.

    Yields:
        Iterator[Iterable[str]]: text file lines exposed through iterator.
    """
    Guard.is_not_none(instance=text_file_path, instance_name=nameof(text_file_path))
    Guard.is_not_empty(iterable_instance=text_file_path, instance_name=nameof(text_file_path))

    if not os.path.exists(text_file_path):
        raise ValueError(f"{nameof(text_file_path)} does not exist!")

    try:
        with open(file=text_file_path, mode="r", encoding=text_file_encoding) as text_file:
            for text_file_line in text_file:
                yield text_file_line.strip()
    except Exception as e:
        raise IOError("Read text file failed for some reason!") from e


def file_exists(relative_or_absolute_file_path: str) -> bool:
    """Checks if a file exists.

    Raises:
        ValueError: occurs when one of the input arguments is None or empty string.
    """
    Guard.is_not_none_nor_empty_nor_whitespace(
        relative_or_absolute_file_path, nameof(relative_or_absolute_file_path)
    )

    return os.path.exists(relative_or_absolute_file_path)
