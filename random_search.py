from networkx import Graph, to_numpy_array
from numpy.random import randint
from numpy import iinfo
import numpy as np
from dfs import Color


class Random2BridgeFinder:
    def __init__(self, graph: Graph, sort=np.sort):
        self.graph = graph
        self.colors = None
        self.edge_codes = None
        self.edge_codes = None
        self.sort = sort

    def search(self):
        # self.edge_codes = self._get_initial_codes(0)
        self.edge_codes = self._get_initial_codes(None)

        self._make_forest()
        self._fill_forest_codes()
        return self.edge_codes

    def _get_initial_codes(self, value=0):
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
        for j in reversed(range(64)):
            self.colors = dict()
            for i in range(len(self.graph.nodes)):
                if self.colors.get(i) is Color.WHITE.value:
                    self._fill_tree_codes(i, iteration=j)

    def _fill_tree_codes(self, node: int, parent: int = -1, iteration: int = 0):
        self.colors.update({node: Color.GRAY})

        for neighbor in self.graph.neighbors(node):
            if self.colors.get(neighbor) not in [Color.GRAY, Color.BLACK]:
                self._fill_tree_codes(neighbor, node, iteration)

        neighbors = list(self.graph.neighbors(node))
        numbers = np.array(list(filter(lambda x: x != None, self.edge_codes[node][neighbors])))
        number = np.sum((numbers >> iteration) & 1) & 1

        initial = self.edge_codes[node][parent] if self.edge_codes[node][parent] != None else 0
        code = np.int64(initial) + np.int64(number << iteration)
        self.edge_codes[node][parent] = code
        self.edge_codes[parent][node] = code

        self.colors.update({node: Color.BLACK})
