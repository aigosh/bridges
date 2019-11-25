from networkx import Graph
from dfs import Color
from util import call


class BridgeFinder:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.colors = None
        self.tst = None
        self.tfn = None
        self.timer = None
        self.bridges = None

    def search(self, before=None, after=None):
        self.colors = dict()
        self.tst = dict()
        self.tfn = dict()
        self.timer = 0
        self.bridges = []

        for i in range(len(self.graph.nodes)):
            if self.colors.get(i) is Color.WHITE.value:
                self._dfs(i, before=before, after=after)
        return self.bridges

    def _dfs(self, node: int, parent: int = -1, before=None, after=None):
        if before is not None:
            call(before, self.graph, node, parent)
        self.colors.update({node: Color.GRAY})
        self.tst.update({node: self.timer})
        self.tfn.update({node: self.timer})
        self.timer += 1
        for neighbor in self.graph.neighbors(node):
            if self.colors.get(neighbor) is Color.WHITE.value:
                self._dfs(neighbor, node, before, after)
                self.tfn.update({node: min([self.tfn.get(node), self.tfn.get(neighbor)])})

                if self.tfn.get(neighbor) > self.tst.get(node):
                    edge = (node, neighbor)
                    self.bridges.append(edge)

            else:
                if neighbor != parent:
                    self.tfn.update({node: min([self.tfn.get(node), self.tst.get(neighbor)])})
        self.colors.update({node: Color.BLACK})
        if after is not None:
            call(after, self.graph, node, parent)
