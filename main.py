from graph import generate_graph
import matplotlib.pyplot as plt
import numpy as np
from util import measure_algorithm
from bridge_finder import BridgeFinder
from random_search import Random2BridgeFinder
from sys import setrecursionlimit
from sort import radix_sort

if __name__ == '__main__':
    # graph = generate_graph(6, 0.3)
    # nx.draw_networkx(graph)
    # plt.draw()
    # plt.pause(120)
    setrecursionlimit(10000)

    sizes = list(np.linspace(10, 200, dtype=np.int, num=20))
    graphs = [generate_graph(size, p=0.3) for size in sizes]
    bf = BridgeFinder()
    random_bf_std = Random2BridgeFinder()
    random_bf_radix = Random2BridgeFinder(sort=radix_sort)
    random_bf_bucket = Random2BridgeFinder()

    # time = measure_algorithm(bf, graphs)
    # plt.plot(sizes, time)
    # plt.draw()
    # plt.pause(120)
    #
    # time = measure_algorithm(random_bf_std, graphs)
    # plt.plot(sizes, time)
    # plt.draw()
    # plt.pause(120)

    time = measure_algorithm(random_bf_radix, graphs)
    plt.plot(sizes, time)
    plt.draw()
    plt.pause(120)
