from typing import Union
from util import call
import numpy as np


def radix_sort(collection: Union, key=None, base=10):
    result = [None] * len(collection)
    positions_count = int(np.log10(max(collection))) + 1
    for position in range(positions_count):
        counts = [0] * base
        for item in collection:
            k = item
            if key is not None:
                k = call(key, item)
            digit = _get_digit(k, base, position)
            counts[digit] += 1

        for i in range(1, len(counts)):
            counts[i] = counts[i] + counts[i - 1]

        for item in reversed(collection):
            k = item
            if key is not None:
                k = call(key, item)
            digit = _get_digit(k, base, position)
            counts[digit] -= 1
            new_position = counts[digit]
            result[new_position] = item
    return result


def _get_digit(number: np.int64, base: int, position: int):
    return (number // base ** position) % base
