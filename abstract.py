from networkx import Graph


class AbstractSearch:
    def search(self, graph: Graph):
        raise NotImplementedError()
