"""Script that should be used to label pyproject file with specific plateform architecture"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (204 > 100 characters) (auto-generated noqa)

import logging
import os
import sys
from pathlib import Path

import toml
from colorama import Fore, Style
from varname import nameof

PROJECT_TOML_FILE_NAME = "pyproject.toml"
PROJECT_PY_ENTRY_NAME_PROJECT = "project"
PROJECT_PY_ENTRY_NAME_BDIST_WHEEL = ("tool", "distutils", "bdist_wheel")
PROJECT_PY_ENTRY_NAME_BDIST_WHEEL_PLAT_NAME = "plat-name"
PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA = ("tool", "setuptools", "package-data")
PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA_PCBATT_ANALYSIS = "pcbatt_analysis"

PLATFORM_TAG_WIN32 = "win32"
PLATFORM_TAG_WIN_AMD64 = "win_amd64"
SUPPORTED_PLATFORM_TAGS = [PLATFORM_TAG_WIN32, PLATFORM_TAG_WIN_AMD64]
SUPPORTED_PLATFORM_TAGS_DLL_PATHS = {
    PLATFORM_TAG_WIN32: [f"{PLATFORM_TAG_WIN32}/NI.*.dll"],
    PLATFORM_TAG_WIN_AMD64: [f"{PLATFORM_TAG_WIN_AMD64}/NI.*.dll"],
}


def transform_toml_pkg_plateform_architecture(
    plateform_architecture_tag: str, pyproject_file_path: str
):
    """Parses pyproject.toml and replaces plat-name entry

    Args:
        plateform_architecture_tag (str): platform architecture tag to write into pyproject file
        pyproject_file_path (str): path into pyproject file to add platform architecture tag into it
    """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (118 > 100 characters) (auto-generated noqa)
    logging.debug("Apply platform tag: %s", plateform_architecture_tag)

    parsed_data = toml.load(f=pyproject_file_path)

    # parse PACKAGE DATA PART
    tool_entry = parsed_data.get(PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA[0])
    if tool_entry is not None:
        setuptools_entry = tool_entry.get(PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA[1])

        if setuptools_entry is not None:
            logging.debug(
                "%s: %s",
                nameof(setuptools_entry),
                setuptools_entry,
            )

            package_data_entry = setuptools_entry.get(
                PROJECT_PY_ENTRY_NAME_SETUP_TOOLS_PACKAGE_DATA[2]
            )

            package_data_entry["*"] = SUPPORTED_PLATFORM_TAGS_DLL_PATHS[plateform_architecture_tag]

    # parse BDIST WHEEL PART
    tool_entry = parsed_data.get(PROJECT_PY_ENTRY_NAME_BDIST_WHEEL[0])

    if tool_entry is not None:
        distutils_entry = tool_entry.get(PROJECT_PY_ENTRY_NAME_BDIST_WHEEL[1])

        if distutils_entry is not None:
            logging.debug(
                "%s: %s",
                nameof(distutils_entry),
                distutils_entry,
            )

            bdist_wheel_entry = distutils_entry.get(PROJECT_PY_ENTRY_NAME_BDIST_WHEEL[2])

            platename_entry = bdist_wheel_entry.get(PROJECT_PY_ENTRY_NAME_BDIST_WHEEL_PLAT_NAME)

            if platename_entry is not None:
                logging.debug("%s: %s", nameof(platename_entry), platename_entry)
                bdist_wheel_entry[
                    PROJECT_PY_ENTRY_NAME_BDIST_WHEEL_PLAT_NAME
                ] = plateform_architecture_tag

    return parsed_data


def label_pyproject(plateform_architecture_tag: str) -> None:
    """Applies plateform architecture tag labeling to project toml file.

    Args:
        plateform_architecture_tag (str): architecture tag value
    """
    print(f"Labeling project toml with architecture tag {plateform_architecture_tag}:")
    pyproject_file_path = os.path.join(Path(__file__).parent.parent, PROJECT_TOML_FILE_NAME)

    if os.path.exists(pyproject_file_path):
        print(f"Transform file located at {pyproject_file_path} ...")

        transformed_toml_data = transform_toml_pkg_plateform_architecture(
            plateform_architecture_tag, pyproject_file_path
        )

        with open(pyproject_file_path, "w", encoding="utf8") as f:
            print(f"Write toml transformed data into {pyproject_file_path} ...")
            toml.dump(transformed_toml_data, f)


if __name__ == "__main__":
    try:
        args = sys.argv[1:]

        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug("args: %s", args)

        if len(args) == 1:
            arg0 = args[0]
            if arg0 in SUPPORTED_PLATFORM_TAGS:
                label_pyproject(arg0)
            else:
                raise RuntimeError(f"Platform tag {arg0} is not supported!")

        else:
            print("Usage: label_pyproject_with_platform_architecture.py platform_tag")
            print(f"Supported platform tags = {SUPPORTED_PLATFORM_TAGS}")
    except:  # noqa: E722 - do not use bare 'except' (auto-generated noqa)
        print(Fore.RED + "Failure: " + str(sys.exc_info()[0]))
        raise
    finally:
        print(Style.RESET_ALL)
