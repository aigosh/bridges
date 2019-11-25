from graph import generate_graph
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from util import measure_algorithm
from dfs import DFS
from bridge_finder import BridgeFinder
from random_search import Random2BridgeFinder
from sys import setrecursionlimit

if __name__ == '__main__':
    # graph = generate_graph(6, 0.3)
    # nx.draw_networkx(graph)
    # plt.draw()
    # plt.pause(120)
    setrecursionlimit(10000)

    sizes = list(np.linspace(10, 1000, dtype=np.int, num=100))
    graphs = [generate_graph(size, p=0.3) for size in sizes]

    time = measure_algorithm(BridgeFinder, graphs)
    plt.plot(sizes, time)
    plt.draw()
    plt.pause(120)

    time = measure_algorithm(Random2BridgeFinder, graphs, sort=sorted)
    plt.plot(sizes, time)
    plt.draw()
    plt.pause(120)
