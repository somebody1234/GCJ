#!/usr/bin/env python3

# uses networkx: https://networkx.github.io/

import networkx as nx
from itertools import product

def flip(s):
    return s[::-1].replace('-','.').replace('+','-').replace('.','+')

g = nx.Graph()

with open('B-small-attempt2.in') as f:
    data = [x for x in f.read().splitlines()]
    
done = []
    
for i in range(1, int(data[0])+1):
    case = data[i]
    LEN = len(case)
    if LEN not in done:
        for x in product('+-', repeat=LEN):
            node = ''.join(x)
            g.add_node(node)
            for j in range(1, LEN+1):
                next = flip(node[:j]) + node[j:]
                if node == next:
                    continue
                #print(node, next)
                g.add_edge(node, next)
        done.append(LEN)
    
    print("Case #{0}: {1}".format(i, nx.shortest_path_length(g, case, '+'*LEN)))