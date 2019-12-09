from functools import partial
from typing import List, Union
from abstract import AbstractSearch
from networkx import Graph
from graph import generate_graph
from time import time


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


def measure_algorithm(algo: AbstractSearch, graphs: List[Graph]):
    result = []
    for graph in graphs:
        start = time()
        algo.search(graph)
        end = time()
        duration = end - start
        result.append(duration)
        print(len(graph.nodes), duration)
    return result


def identity(item):
    return item


def min_max(array: Union, key=None):
    if key is None:
        key = identity

    min_key = call(key, array[0])
    min_value = array[0]
    max_key = call(key, array[0])
    max_value = array[0]

    for i in range(len(array) - 1):
        item = array[i + 1]
        k = call(key, item)
        if k < min_key:
            min_key = k
            min_value = item
        if k > max_key:
            max_key = k
            max_value = item

    return min_key, max_key, min_value, max_value


def get_step(min_value: int, max_value: int, steps: int):
    return (max_value - min_value) / steps
