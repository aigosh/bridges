from networkx import Graph
from abstract import AbstractSearch
from dfs import Color


class BridgeFinder(AbstractSearch):
    def __init__(self):
        self.colors = None
        self.tst = None
        self.tfn = None
        self.timer = None
        self.bridges = None

    def search(self, graph: Graph):
        self.colors = dict()
        self.tst = dict()
        self.tfn = dict()
        self.timer = 0
        self.bridges = []

        for i in range(len(graph.nodes)):
            if self.colors.get(i) is Color.WHITE.value:
                self._dfs(graph, i)
        return self.bridges

    def _dfs(self, graph: Graph,  node: int, parent: int = -1):
        self.colors.update({node: Color.GRAY})
        self.tst.update({node: self.timer})
        self.tfn.update({node: self.timer})
        self.timer += 1
        for neighbor in graph.neighbors(node):
            if self.colors.get(neighbor) is Color.WHITE.value:
                self._dfs(graph, neighbor, node)
                self.tfn.update({node: min([self.tfn.get(node), self.tfn.get(neighbor)])})

                if self.tfn.get(neighbor) > self.tst.get(node):
                    edge = (node, neighbor)
                    self.bridges.append(edge)

            else:
                if neighbor != parent:
                    self.tfn.update({node: min([self.tfn.get(node), self.tst.get(neighbor)])})
        self.colors.update({node: Color.BLACK})
