""" Implementation of PcbattLogger """  # noqa: D415, W505 - First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (149 > 100 characters) (auto-generated noqa)

import types
from datetime import datetime
from typing import List

# pylint: disable=C0301,W0212,W0105

# https://pylint.readthedocs.io/en/latest/user_guide/messages/convention/line-too-long.html
# https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/protected-access.html


class PcbattLogger:
    """
    Class for logging inputs and outputs of methods.
    The goal is to log most informations without slowing down the caller.
    """  # noqa: D205, D212, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (193 > 100 characters) (auto-generated noqa)

    def __init__(self, file: str, methods: List[str] = None):
        """
        Initializes the PcbattLogger with a file path.
        methods default values is ['configure_and_measure', 'configure_and_generate']

        Args:
            file (str): The file path where the logs will be stored.
            methods (List[str], optional): List of methods to log. Defaults values : ['configure_and_measure', 'configure_and_generate'].
        """  # noqa: D205, D212, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (137 > 100 characters) (auto-generated noqa)
        # https://pylint.readthedocs.io/en/latest/user_guide/messages/warning/dangerous-default-value.html
        if methods is None:
            methods = ["configure_and_measure", "configure_and_generate"]
        self.methods = methods
        self._modules = {}
        self.set_file(file)

    @staticmethod
    def _logger_txt(module, original_method, self, configuration):
        """
        A static method to log inputs and outputs of methods into txt format.

        Args:
            module: The module whose method is being logged.
            original_method: The original method to call.
            configuration: The input configuration passed to the method.
            self: The PcbattLogger instance.

        Returns:
            The result returned by the original method.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        if configuration:
            result = original_method(configuration)
        else:
            result = original_method()

        with open(self.__file, mode="a", encoding="utf-8") as f:
            f.write("Module : " + str(module.__class__).rsplit(".", maxsplit=1)[-1][:-2] + "\n")
            f.write("Channel names : " + str(module.task.channel_names) + "\n")
            if configuration:
                f.write("Inputs :\n")
                f.write(str(configuration) + "\n\n")
            if result:
                f.write("Outputs :\n")
                f.write(str(result) + "\n\n\n\n")
        return result

    @staticmethod
    def _logger_csv(module, original_method, self, configuration):
        """
        A static method to log inputs and outputs of methods into csv format.
        This method is just an example how to log in different format and needs modifications.

        Args:
            module: The module whose method is being logged.
            original_method: The original method being called.
            configuration: The input configuration passed to the method.
            self: The PcbattLogger instance.

        Returns:
            The result returned by the original method.
        """  # noqa: D205, D212, W505 - 1 blank line required between summary line and description (auto-generated noqa), Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (197 > 100 characters) (auto-generated noqa)
        result = original_method(configuration)

        with open(self.__file, mode="a", encoding="utf-8") as f:
            f.write("Module : " + str(module.__class__).rsplit(".", maxsplit=1)[-1][:-2] + "\n")
            f.write("Channel names :" + str(module.task.channel_names) + "\n")
            if configuration:
                f.write("Inputs\n")
                f.write(str(configuration) + "\n")
            if result:
                f.write("Outputs\n")
                f.write(str(result) + "\n")
        return result

    def _monkey_patch(self, module):
        """
        A method to monkey patch module methods for logging.

        Args:
            module: The module to be patched.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        # Retrieve all methods from module
        attributes = dir(module)
        # Monkey-patch the method
        for method in self.methods:
            if method in attributes:
                if self.__file.endswith(".csv"):
                    setattr(
                        module,
                        method,
                        types.MethodType(
                            lambda cls, configuration=None: PcbattLogger._logger_csv(
                                module, self._modules[module], self, configuration
                            ),
                            module,
                        ),
                    )
                else:
                    setattr(
                        module,
                        method,
                        types.MethodType(
                            lambda cls, configuration=None: PcbattLogger._logger_txt(
                                module, self._modules[module], self, configuration
                            ),
                            module,
                        ),
                    )

    def attach(self, module):
        """
        Attaches a module to log its method calls.

        Args:
            module: The module to be attached.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        # Retrieve all methods from module
        attributes = dir(module)
        # Save wanted method
        for method in self.methods:
            if method in attributes:
                self._modules[module] = getattr(module, method)
        self._monkey_patch(module)

    def remove(self, module):
        """
        Removes a module from logging.

        Args:
            module: The module to be removed.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        # Retrieve all methods from module
        attributes = dir(module)
        # Remove monkey patching
        for method in self.methods:
            if method in attributes:
                setattr(module, method, self._modules[module])
        # Remove from the list of monkey patched classes
        if module in self._modules:
            self._modules.pop(module)

    def set_file(self, file: str):
        """
        Sets the file path for logging.

        Args:
            file (str): The file path where the logs will be stored.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        self.__file = file
        now = datetime.now()
        current_time = now.strftime("%m-%d-%Y %H:%M:%S")
        # Always write the current date and time when changing the file
        with open(self.__file, mode="a", encoding="utf-8") as f:
            f.write("Current time : " + current_time + "\n")

    def get_modules(self) -> List[str]:
        """
        Retrieves the names of all attached modules.

        Returns:
            List[str]: The names of all attached modules.
        """  # noqa: D212, W505 - Multi-line docstring summary should start at the first line (auto-generated noqa), doc line too long (109 > 100 characters) (auto-generated noqa)
        # Get all classes names
        # Split them with a . and get the last value
        # Remove the two last characters
        return [str(x.__class__).rsplit(".", maxsplit=1)[-1][:-2] for x in self._modules]
