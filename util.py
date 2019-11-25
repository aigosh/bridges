from functools import partial
from typing import List


def call(func, *args, **kwargs):
    return partial(func, *args, **kwargs)()


def create_collector():
    collection = []

    def collect(node):
        collection.append(node)

    return collect, collection


def group_by(collection: List, key=lambda x: x):
    result = dict()

    for item in collection:
        k = key(item)
        if result.get(k) is None:
            result.update({k: []})
        result.get(k).append(item)

    return result
