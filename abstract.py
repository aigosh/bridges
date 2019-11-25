from networkx import Graph


class AbstractSearch:
    def __init__(self, graph: Graph, **kwargs):
        pass

    def search(self):
        raise NotImplementedError()
