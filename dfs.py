from networkx import Graph
from enum import Enum
from util import call


class Color(Enum):
    WHITE = None
    GRAY = 1
    BLACK = 2


class DFS:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.colors = dict()

    def search(self, before=None, after=None):
        self.colors = dict()

        for i in range(len(self.graph.nodes)):
            if self.colors.get(i) is Color.WHITE.value:
                self._dfs(i, before=before, after=after)

    def _dfs(self, node: int, parent: int = -1, before=None, after=None):
        if before is not None:
            call(before, (self.graph, node, parent))
        self.colors.update({node: Color.GRAY})
        for neighbor in self.graph.neighbors(node):
            if self.colors.get(neighbor) not in [Color.GRAY, Color.BLACK]:
                self._dfs(neighbor, node, before, after)
        self.colors.update({node: Color.BLACK})
        if after is not None:
            call(after, (self.graph, node, parent))
