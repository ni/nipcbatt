"""Module containing message strings."""


class PCBATTCommunicationExceptionMessages:
    """Messages used in exception classes."""

    ANALOG_INPUT_CHANNEL_NOT_COMPATIBLE_WITH_MEASUREMENT_ARGS_1 = (
        "The analog input channel is not compatible with the specific measurement ({})."
    )

    CLASS_DOES_NOT_IMPLEMENT_METHOD_ARGS_2 = "The class {} does not implement the method {}."

    VISA_SERIAL_DEVICE_NOT_INITIALIZED = "VISA serial instrument not initialized"

    SECOND_ARGUMENT_OF_TYPE_INT_FLOAT_OR_STRING = (
        "Second argument must be a int or float value"
        + " for cold-junction compensation value,"
        + " or a string for cold-junction compensation channel name"
    )

    INVALID_OS_ENVIRONMENT_FOR_PYTHON = (
        "Current Python interpreter is not running under Windows os "
        + "with 32bit or 64bit architecture."
    )

    LIBRARY_LOAD_FAILED_ARGS_2 = "Failed to load native library {}: {}."

    FUNCTION_CALL_FAILED_ARGS_2 = "Failed to call function {}: {}."

    INVALID_NUMPY_ARRAY_TYPE_ARGS_1 = "the type of the numpy array is not of {}."

    OPEN_METHOD_MUST_BE_CALLED_FIRST = "Open method must be called first."
