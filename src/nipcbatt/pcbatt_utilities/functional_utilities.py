""" Provides a set of higher order function utilities routines."""


def repeat(times: int):
    """Returns a function which is repeated execution of inner function
       provided as argument.

    Args:
        times (int): number of times, function will be repeated.
    """

    def repeat_helper(f):
        def call_helper(*args):
            for _ in range(0, times):
                f(*args)

        return call_helper

    return repeat_helper
