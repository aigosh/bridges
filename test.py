import numpy as np
from networkx import Graph, from_numpy_array, to_numpy_array
import networkx as nx
from dfs import DFS
from util import create_collector
from bridge_finder import BridgeFinder
from random_search import Random2BridgeFinder
from json import loads
import matplotlib.pyplot as plt
from sort import radix_sort


def test_dfs():
    adj = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ])
    graph = from_numpy_array(adj)
    dfs = DFS()
    dfs.search(graph)


def test_bridge_finder__no_bridge():
    adj = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ])
    graph = from_numpy_array(adj)
    finder = BridgeFinder()
    bridges = finder.search(graph)

    assert bridges == []


def test_bridge_finder__one_bridge():
    adj = np.array([
        [0, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 0],
    ])
    graph = from_numpy_array(adj)
    finder = BridgeFinder()
    bridges = finder.search(graph)

    assert bridges == [(0, 5)]


def test_random_search():
    adj = np.array([
        [0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 0],
    ])
    graph = from_numpy_array(adj)
    finder = Random2BridgeFinder()
    bridges = finder.search(graph)

    assert ((0, 5), (1, 3)) in bridges
    assert ((3, 4), (4, 5)) in bridges
    assert ((0, 2), (1, 2)) in bridges
    assert len(bridges) == 3


def test_radix_sort():
    arr = [8, 6, 7, 9, 0, 4, 5, 2, 3, 1]
    sorted_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = radix_sort(arr)

    assert sorted_arr == result
