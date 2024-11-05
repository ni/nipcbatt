""" Provides a set of iterable related utilities routines."""

import itertools
from collections.abc import Iterable

from varname import nameof

from nipcbatt.pcbatt_utilities.guard_utilities import Guard


def count(iterable_element: Iterable) -> tuple[int, Iterable]:
    """Counts the number of elements is hold by an iterable,
        input iterable should be no more used after a call to this function.

    Args:
        iterable_element (Iterable): input iterable elements count.

    Returns:
        tuple[int, Iterable]: number of elements contained in the input
            iterable and new iterable replacing the input one.
    """
    Guard.is_not_none(iterable_element, nameof(iterable_element))
    forked_iterators = itertools.tee(iterable_element)
    count_result = sum(1 for f in forked_iterators[1])
    return count_result, forked_iterators[0]
