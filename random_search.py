from networkx import Graph
from numpy.random import randint
from numpy import iinfo
import numpy as np
from dfs import Color
from util import call
from itertools import combinations
from abstract import AbstractSearch


class Random2BridgeFinder(AbstractSearch):
    def __init__(self, sort=sorted):
        self.colors = None
        self.edge_codes = None
        self.edge_codes = None
        self.sort = sort

    def search(self, graph: Graph):
        self.edge_codes = self._get_initial_codes(graph)

        self._make_forest(graph)
        self._fill_forest_codes(graph)

        return self._get_bridges(graph)

    def _get_initial_codes(self, graph: Graph, value=None):
        nodes_count = len(graph)
        shape = (nodes_count, nodes_count)
        dtype = np.int64

        if value is None:
            dtype = None

        return np.full(shape, value, dtype=dtype)

    def _make_forest(self, graph: Graph):
        self.colors = dict()

        for i in range(len(graph.nodes)):
            if self.colors.get(i) is Color.WHITE.value:
                self._make_tree(graph, i)

    def _make_tree(self, graph: Graph, node: int, parent: int = -1):
        self.colors.update({node: Color.GRAY})

        for neighbor in graph.neighbors(node):
            if self.colors.get(neighbor) not in [Color.GRAY, Color.BLACK]:
                self._make_tree(graph, neighbor, node)
            else:
                if neighbor != parent:
                    high = iinfo(np.int64).max
                    code = randint(low=1, high=high, dtype=np.int64)
                    self.edge_codes[node][neighbor] = code
                    self.edge_codes[neighbor][node] = code

        self.colors.update({node: Color.BLACK})

    def _fill_forest_codes(self, graph: Graph):
        for bit_position in reversed(range(64)):
            self.colors = dict()
            for i in range(len(graph.nodes)):
                if self.colors.get(i) is Color.WHITE.value:
                    self._fill_tree_codes(graph, i, bit_position=bit_position)

    def _fill_tree_codes(self, graph: Graph, node: int, parent: int = -1, bit_position: int = 0):
        self.colors.update({node: Color.GRAY})

        for neighbor in graph.neighbors(node):
            if self.colors.get(neighbor) not in [Color.GRAY, Color.BLACK]:
                self._fill_tree_codes(graph, neighbor, node, bit_position)

        neighbors = list(graph.neighbors(node))
        codes = np.array(list(filter(lambda x: x != None, self.edge_codes[node][neighbors])))
        bit = np.sum((codes >> bit_position) & 1) & 1

        initial = self.edge_codes[node][parent] if self.edge_codes[node][parent] is not None else 0
        code = np.int64(initial) + np.int64(bit << bit_position)
        self.edge_codes[node][parent] = code
        self.edge_codes[parent][node] = code

        self.colors.update({node: Color.BLACK})

    def _get_bridges(self, graph: Graph):
        edges = call(self.sort, graph.edges, key=lambda x: self.edge_codes[x])
        result = []
        i = 0
        while i < len(edges):
            edge = edges[i]
            code = self.edge_codes[edge]
            part = []
            while i < len(edges) and self.edge_codes[edges[i]] == code:
                part.append(edges[i])
                i += 1
            if len(part) > 1:
                result.extend(combinations(part, 2))

        return result
