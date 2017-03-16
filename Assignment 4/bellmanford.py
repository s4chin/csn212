#!/usr/bin/env python
import math
import random
import timeit

import pandas as pd
import seaborn as sns

MAX = float('Inf')

class Graph:
    def __init__(self, V, E):
        self.nodes = V
        self.edges = E

class Edge:
    def __init__(self, edge, weight):
        self.u = edge[0]
        self.v = edge[1]
        self.weight = weight

def ret_random_graph(v, e, weight, neg=True):
    """
    v = vertices, e = edges, weight = weight range [-weight, weight] for each edge
    e >= 2v for most paths to exist
    So here I assumed e >= 2v, I'm adding atleast 2 edges from each node.
    Also assuming e <= 2*(vC2) complete graph
    """
    allowed_weights = list(range(-1*weight, weight+1)) if neg else list(range(0, weight+1))
    allowed_weights.remove(0) # No edge of weight 0
    if e > v*(v-1):
        e = v*(v-1)
    if v == 1:
        v = 2
    if e < 2*v:
        e = 2*v
    print v, e
    V = [i for i in xrange(0, v)]
    E = []
    for node in V:
        for i in range(2):
            edge = [node, random.choice(V)]
            while edge in E or edge[0] == edge[1]:
                edge = [node, random.choice(V)]
            E.append(Edge(edge, random.choice(allowed_weights)))
    rem_edges = e-2*v
    while rem_edges > 0: # which it should be
        edge = [random.choice(V), random.choice(V)]
        while edge in E or edge[0] == edge[1]:
            edge = [random.choice(V), random.choice(V)]
            E.append(Edge(edge, random.choice(allowed_weights)))
        rem_edges = rem_edges-1
    return Graph(V, E)

def bellman_ford(g, source=0):
    start_time = timeit.default_timer()
    dist = [0 for i in range(len(g.nodes))]
    has_cycle = False

    for node in g.nodes:
        dist[node] = 0 if node == source else MAX

    for i in range(1, len(g.nodes)):
        for edge in g.edges:
            if dist[edge.u] + edge.weight < dist[edge.v]:
                dist[edge.v] = dist[edge.u] + edge.weight

    for edge in g.edges:
        if dist[edge.v] > dist[edge.u] + edge.weight:
            has_cycle = True
    elapsed = timeit.default_timer() - start_time
    return has_cycle, dist, elapsed

def print_graph():
    X = []
    Y = []
    # for i in [100, 600, 1100, 1600, 2100, 2600, 3100, 3600, 4100, 4600, 5100]:
    for i in [5000]:
        # for _ in range(3):
        for _ in range(35):
            v = int(math.floor(random.random()*i))
            e = int(math.floor(random.random()*(5*v-2*v)+2*v))
            print _, v, e
            neg = True if random.random() < 0.5 else False
            weight = 100
            has_cycle, dist, y = bellman_ford(ret_random_graph(v, e, weight, neg))
            X.append(v*e)
            Y.append(y)
    
    with open('data.txt', 'w') as f:
        f.write('|V|*|E| Time\n')
        for i in range(len(X)):
            f.write("%s %s\n" % (str(X[i]), str(Y[i])))
    
    # Fit linear regression line
    l = pd.DataFrame({
        '|V|*|E|':X,
        'Time':Y
    })
    plot = sns.lmplot('|V|*|E|', 'Time', l, ci=0)
    sns.plt.show() # This will show the plot, click save to save. Couldn't automate this.
    # (plot.get_figure()).savefig("linear_regression.png")

if __name__ == '__main__':
    # print bellman_ford(ret_random_graph(1000, 5000, 100, False))
    print_graph()
