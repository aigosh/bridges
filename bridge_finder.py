from networkx import Graph
from abstract import AbstractSearch
from dfs import Color


class BridgeFinder(AbstractSearch):
    def __init__(self, graph: Graph, **kwargs):
        super().__init__(graph, **kwargs)
        self.graph = graph
        self.colors = None
        self.tst = None
        self.tfn = None
        self.timer = None
        self.bridges = None

    def search(self):
        self.colors = dict()
        self.tst = dict()
        self.tfn = dict()
        self.timer = 0
        self.bridges = []

        for i in range(len(self.graph.nodes)):
            if self.colors.get(i) is Color.WHITE.value:
                self._dfs(i)
        return self.bridges

    def _dfs(self, node: int, parent: int = -1):
        self.colors.update({node: Color.GRAY})
        self.tst.update({node: self.timer})
        self.tfn.update({node: self.timer})
        self.timer += 1
        for neighbor in self.graph.neighbors(node):
            if self.colors.get(neighbor) is Color.WHITE.value:
                self._dfs(neighbor, node)
                self.tfn.update({node: min([self.tfn.get(node), self.tfn.get(neighbor)])})

                if self.tfn.get(neighbor) > self.tst.get(node):
                    edge = (node, neighbor)
                    self.bridges.append(edge)

            else:
                if neighbor != parent:
                    self.tfn.update({node: min([self.tfn.get(node), self.tst.get(neighbor)])})
        self.colors.update({node: Color.BLACK})
