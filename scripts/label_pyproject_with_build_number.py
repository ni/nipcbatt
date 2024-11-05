"""Script that should be used to label pyproject file with build number"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (185 > 100 characters) (auto-generated noqa)

import logging
import os
import sys
from pathlib import Path

import toml
from colorama import Fore, Style
from varname import nameof

PROJECT_TOML_FILE_NAME = "pyproject.toml"
PROJECT_PY_ENTRY_NAME_PROJECT = "project"
PROJECT_PY_ENTRY_NAME_VERSION = "version"


def transform_toml_pkg_version(build_number: int, pyproject_file_path: str):
    """Parses pyproject.toml and replaces last digit of version entry with build number

    Args:
        build_number (int): build counter value to write into pyproject file
        pyproject_file_path (str): path into pyproject file to add build number into it
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    parsed_data = toml.load(f=pyproject_file_path)

    logging.debug("pyproject: %s", parsed_data)

    project_entry = parsed_data.get(PROJECT_PY_ENTRY_NAME_PROJECT)

    if project_entry is not None:
        version_entry = project_entry.get("version")

        if version_entry is not None:
            logging.debug("found version:")
            logging.debug("%s: %s", nameof(version_entry), version_entry)

            package_version = parsed_data[PROJECT_PY_ENTRY_NAME_PROJECT][
                PROJECT_PY_ENTRY_NAME_VERSION
            ]
            str_tokens = package_version.split(sep=".")

            logging.debug("%s = %s", nameof(str_tokens), str_tokens)

            if str_tokens is not None and len(str_tokens) == 4:
                parsed_data[PROJECT_PY_ENTRY_NAME_PROJECT][
                    PROJECT_PY_ENTRY_NAME_VERSION
                ] = f"{str_tokens[0]}.{str_tokens[1]}.{str_tokens[2]}.{build_number}"

    return parsed_data


def label_pyproject(build_number: int) -> None:
    """Applies build number labeling to project toml file.

    Args:
        build_number (int): build counter value
    """
    print(f"Labeling project toml with build number {build_number}:")
    pyproject_file_path = os.path.join(Path(__file__).parent.parent, PROJECT_TOML_FILE_NAME)

    if os.path.exists(pyproject_file_path):
        print(f"Transform file located at {pyproject_file_path} ...")

        transformed_toml_data = transform_toml_pkg_version(build_number, pyproject_file_path)

        with open(pyproject_file_path, "w", encoding="utf8") as f:
            print(f"Write toml transformed data into {pyproject_file_path} ...")
            toml.dump(transformed_toml_data, f)


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("args: %s", args)

        if len(args) == 1:
            label_pyproject(build_number=int(args[0]))
        else:
            label_pyproject(build_number=0)
    except:  # noqa: E722 - do not use bare 'except' (auto-generated noqa)
        print(Fore.RED + "Failure: " + str(sys.exc_info()[0]))
        raise
    finally:
        print(Style.RESET_ALL)
