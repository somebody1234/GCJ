import networkx as nx
from itertools import product
from sys import argv

with open(argv[1]) as f:
    cases = f.readlines()[1:]

    for i, case in enumerate(cases):
        case = tuple([x == "+" for x in case[:-1]])
        l = len(case)
        G = nx.Graph()

        G.add_nodes_from(product([True, False], repeat=len(case)))

        for p in G:
            for n in range(1, l+1):
                G.add_edge(p, tuple(reversed([not k for k in p[:n]])) + p[n:])

        print("Case #{0}: {1}".format(i+1, nx.shortest_path_length(G, source=case, target=(True,)*l)))

G = nx.Graph()
