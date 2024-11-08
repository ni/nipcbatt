"""Script that should be used to install visual code extensions 
for python development during PBCATT project"""  # noqa: D205, D209, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring closing quotes should be on a separate line (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (340 > 100 characters) (auto-generated noqa)

import os
from pathlib import Path

EXTENSIONS_FILE_NAME = "vscode.extensions.txt"


def main():
    """Executes vscode extensions installation from vscode.extensions.txt"""  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (187 > 100 characters) (auto-generated noqa)
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
