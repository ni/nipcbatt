"""Script that should be used to create venvs tree near src folder"""

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
