from networkx import from_numpy_array
import numpy as np


def generate_graph(vertices_count, p=0.5):
    if not vertices_count:
        raise Exception('No vetices count specified')
    adj = np.random.rand(vertices_count, vertices_count)
    adj = np.flip(adj)
    adj = np.array(adj < p, dtype=np.int)
    np.fill_diagonal(adj, 0)

    return from_numpy_array(adj)
