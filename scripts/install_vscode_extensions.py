"""Script that should be used to install visual code extensions 
for python development during PBCATT project"""

import os
from pathlib import Path

EXTENSIONS_FILE_NAME = "vscode.extensions.txt"


def main():
    """Executes vscode extensions installation from vscode.extensions.txt"""
    extensions_list_file_path = os.path.join(Path(__file__).parent, EXTENSIONS_FILE_NAME)

    with open(extensions_list_file_path, encoding="utf-16") as vscode_extensions_file:
        lines = vscode_extensions_file.readlines()

        for line in lines:
            print(f"Install of {line}")
            command = f"cmd.exe /c code --force --install-extension {line}"
            os.system(command)


# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    main()
