"""Lists venvs variables environment"""

import venv_tools

# le main est le nom du point d'entrée (script appelé)
if __name__ == "__main__":
    venvs_entries = venv_tools.get_supported_venvs_paths_table()

    print("Supported venvs environ variables:")
    for venv_entry in zip(list(venvs_entries.items()), range(1, len(venvs_entries) + 1)):
        print(f" {venv_entry[1]}- os.env['{venv_entry[0][0]}'] = {venv_entry[0][1]}")

    print("----")
    print("Found venvs environ variables:")

    found_env_variables_list = list(venv_tools.get_python_present_env_variable_names())

    if not found_env_variables_list:
        print(" There is no configured python environ variable")

    for venv_entry in zip(found_env_variables_list, range(1, len(found_env_variables_list) + 1)):
        print(f" {venv_entry[1]}- os.env['{venv_entry[0][0]}'] = {venv_entry[0][1]}")
