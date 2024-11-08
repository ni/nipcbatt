""" Provides a set of higher order function utilities routines."""


def repeat(times: int):
    """Returns a function which is repeated execution of inner function
       provided as argument.
    Args:
        times (int): number of times, function will be repeated.
    """  # noqa: D202, D205, D411, D415, W505 - 1 blank line required between summary line and description (auto-generated noqa), Missing blank line before section (auto-generated noqa), First line should end with a period, question mark, or exclamation point (auto-generated noqa), doc line too long (269 > 100 characters) (auto-generated noqa)

    def repeat_helper(f):
        def call_helper(*args):
            for _ in range(0, times):
                f(*args)

        return call_helper

    return repeat_helper
