from networkx import Graph
from enum import Enum
from abstract import AbstractSearch


class Color(Enum):
    WHITE = None
    GRAY = 1
    BLACK = 2


class DFS(AbstractSearch):
    def __init__(self):
        self.colors = dict()

    def search(self, graph: Graph):
        self.colors = dict()

        for i in range(len(graph.nodes)):
            if self.colors.get(i) is Color.WHITE.value:
                self._dfs(graph, i)

    def _dfs(self, graph: Graph, node: int, parent: int = -1):
        self.colors.update({node: Color.GRAY})
        for neighbor in graph.neighbors(node):
            if self.colors.get(neighbor) not in [Color.GRAY, Color.BLACK]:
                self._dfs(graph, neighbor, node)
        self.colors.update({node: Color.BLACK})
