"""Module containing message strings."""


class PCBATTLibraryExceptionMessages:
    """Messages used in exception classes."""

    ANALOG_INPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1 = (
        "The analog input channel is not compatible with the specific measurement ({})."
    )

    ANALOG_OUTPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1 = (
        "The analog output channel is not compatible with the specific generation ({})."
    )

    CLASS_DOES_NOT_IMPLEMENT_METHOD_ARGS_2 = "The class {} does not implement the method {}."

    VISA_SERIAL_DEVICE_NOT_INITIALIZED = "VISA serial instrument not initialized"

    SECOND_ARGUMENT_OF_TYPE_INT_FLOAT_OR_STRING = (
        "Second argument must be a int or float value"
        + " for cold-junction compensation value,"
        + " or a string for cold-junction compensation channel name"
    )

    INVALID_NUMPY_ARRAY_TYPE_ARGS_1 = "The type of the numpy array is not of {}."

    GLOBAL_CHANNEL_PORT_NOT_SUPPORTED_ARGS_3 = (
        "Global Channel Port is not supported. {} represents a port with a width of {}. "
        + "Specify a range of digital lines, such as '{}/line0:31' as the global channel"
    )

    PHYSICAL_CHANNEL_PORT_NOT_SUPPORTED_ARGS_3 = (
        "Physical Channel Port is not supported. '{}' represents a port with a width of {}."
        + "Specify a range of digital lines, such as '{}/line0:31' as the physical channel"
    )

    MORE_THAN_ONE_CHANNEL_INVALID = "Multiple channels are not allowed for counter tasks."

    GLOBAL_CHANNEL_TOO_MANY_MODULES_ARGS_1 = (
        "Global channels input is invalid because multiple module global channels were"
        + "listed in the string. Global channels are supported only from a single module."
        + "\n Modules Listed: {}"
    )
