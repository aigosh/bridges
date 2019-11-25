from networkx import Graph
from numpy.random import randint
from numpy import iinfo
import numpy as np
from dfs import Color
from util import call
from itertools import combinations


class Random2BridgeFinder:
    def __init__(self, graph: Graph, sort=sorted):
        self.graph = graph
        self.colors = None
        self.edge_codes = None
        self.edge_codes = None
        self.sort = sort

    def search(self):
        self.edge_codes = self._get_initial_codes()

        self._make_forest()
        self._fill_forest_codes()

        return self._get_bridges()

    def _get_initial_codes(self, value=None):
        nodes_count = len(self.graph)
        shape = (nodes_count, nodes_count)
        dtype = np.int64

        if value is None:
            dtype = None

        return np.full(shape, value, dtype=dtype)

    def _make_forest(self):
        self.colors = dict()

        for i in range(len(self.graph.nodes)):
            if self.colors.get(i) is Color.WHITE.value:
                self._make_tree(i)

    def _make_tree(self, node: int, parent: int = -1):
        self.colors.update({node: Color.GRAY})

        for neighbor in self.graph.neighbors(node):
            if self.colors.get(neighbor) not in [Color.GRAY, Color.BLACK]:
                self._make_tree(neighbor, node)
            else:
                if neighbor != parent:
                    high = iinfo(np.int64).max
                    code = randint(low=1, high=high, dtype=np.int64)
                    self.edge_codes[node][neighbor] = code
                    self.edge_codes[neighbor][node] = code

        self.colors.update({node: Color.BLACK})

    def _fill_forest_codes(self):
        for bit_position in reversed(range(64)):
            self.colors = dict()
            for i in range(len(self.graph.nodes)):
                if self.colors.get(i) is Color.WHITE.value:
                    self._fill_tree_codes(i, bit_position=bit_position)

    def _fill_tree_codes(self, node: int, parent: int = -1, bit_position: int = 0):
        self.colors.update({node: Color.GRAY})

        for neighbor in self.graph.neighbors(node):
            if self.colors.get(neighbor) not in [Color.GRAY, Color.BLACK]:
                self._fill_tree_codes(neighbor, node, bit_position)

        neighbors = list(self.graph.neighbors(node))
        codes = np.array(list(filter(lambda x: x != None, self.edge_codes[node][neighbors])))
        bit = np.sum((codes >> bit_position) & 1) & 1

        initial = self.edge_codes[node][parent] if self.edge_codes[node][parent] is not None else 0
        code = np.int64(initial) + np.int64(bit << bit_position)
        self.edge_codes[node][parent] = code
        self.edge_codes[parent][node] = code

        self.colors.update({node: Color.BLACK})

    def _get_bridges(self):
        edges = call(self.sort, self.graph.edges, key=lambda edge: self.edge_codes[edge])
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
