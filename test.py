import numpy as np
from networkx import Graph, from_numpy_array, to_numpy_array
import networkx as nx
from dfs import DFS
from util import create_collector
from bridge_finder import BridgeFinder
from random_search import Random2BridgeFinder
from json import loads
import matplotlib.pyplot as plt


def test_dfs():
    _collect, collection = create_collector()

    def collect(data):
        node = data[1]
        return _collect(node)

    adj = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ])
    graph = from_numpy_array(adj)
    dfs = DFS(graph)
    dfs.search(before=collect)

    assert collection == [0, 1, 2]


def test_bridge_finder__no_bridge():
    adj = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ])
    graph = from_numpy_array(adj)
    finder = BridgeFinder(graph)
    bridges = finder.search()

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
    finder = BridgeFinder(graph)
    bridges = finder.search()

    assert bridges == [(0, 5)]


def test_random_search__one__two_bridge():
    adj = np.array([
        [0, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 0],
    ])
    graph = from_numpy_array(adj)
    finder = Random2BridgeFinder(graph)
    bridges = finder.search()

    assert bridges[0][5] == bridges[1][3]
    assert bridges[3][4] == bridges[4][5]
    assert bridges[1][2] == bridges[2][0]

    assert bridges[0][1] != bridges[1][2]
