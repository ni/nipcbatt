"""Script that should be used to create venvs tree near src folder"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (180 > 100 characters) (auto-generated noqa)

import logging
import sys

import venv_tools

# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # create empty folders tree
    venv_tools.create_venvs_root_folder()

    # fill content of folders tree
    venv_tools.create_venvs_folders_content()
