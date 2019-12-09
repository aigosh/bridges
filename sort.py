from typing import Union
from util import call, identity, min_max, get_step
import numpy as np


def radix_sort(collection: Union, key=None, base=10):
    result = [None] * len(collection)
    if key is None:
        key = identity
    max_item = max(collection, key=key)
    max_key = call(key, max_item)
    positions_count = int(np.log10(max_key)) + 1
    for position in range(positions_count):
        counts = [0] * base
        for item in collection:
            k = call(key, item)
            digit = _get_digit(k, base, position)
            counts[digit] += 1

        for i in range(1, len(counts)):
            counts[i] = counts[i] + counts[i - 1]

        for item in reversed(list(collection)):
            k = call(key, item)
            digit = _get_digit(k, base, position)
            counts[digit] -= 1
            new_position = counts[digit]
            result[new_position] = item
    return result


def _get_digit(number: np.int64, base: int, position: int):
    return (number // base ** position) % base


def bucket_sort(collection: Union, key=None):
    if len(collection) == 0:
        return collection

    if key is None:
        key = identity

    result = []
    min_value, max_value, _, _ = min_max(collection, key)
    bucket_count = int(np.floor(np.log(max_value - min_value)) + 1)
    step = get_step(min_value, max_value, bucket_count)

    buckets = [list() for _ in range(bucket_count)]

    for item in collection:
        k = call(key, item)
        bucket = _get_bucket(k, min_value, step, bucket_count)
        buckets[bucket].append(item)

    for bucket in buckets:
        part = sorted(bucket, key=key)
        result.extend(part)

    return result


def _get_bucket(value: int, min_value: int, step: int, bucket_count: int):
    index = int(np.floor((value - min_value) / step))
    return min([bucket_count - 1, index])
