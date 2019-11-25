from networkx import Graph
from enum import Enum
from abstract import AbstractSearch


class Color(Enum):
    WHITE = None
    GRAY = 1
    BLACK = 2


class DFS(AbstractSearch):
    def __init__(self, graph: Graph, **kwargs):
        super().__init__(graph, **kwargs)
        self.graph = graph
        self.colors = dict()

    def search(self):
        self.colors = dict()

        for i in range(len(self.graph.nodes)):
            if self.colors.get(i) is Color.WHITE.value:
                self._dfs(i)

    def _dfs(self, node: int, parent: int = -1):
        self.colors.update({node: Color.GRAY})
        for neighbor in self.graph.neighbors(node):
            if self.colors.get(neighbor) not in [Color.GRAY, Color.BLACK]:
                self._dfs(neighbor, node)
        self.colors.update({node: Color.BLACK})
