from functools import partial
from typing import List, Type
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


def measure_algorithm(Algo: Type[AbstractSearch], graphs: List[Graph], sort=None):
    result = []
    for graph in graphs:
        algo = Algo(graph, sort=sort)
        start = time()
        algo.search()
        end = time()
        duration = end - start
        result.append(duration)
        print(len(graph.nodes), duration)
    return result
