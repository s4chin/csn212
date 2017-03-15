#!/usr/bin/env python
import random

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
    dist = [0 for i in range(len(g.nodes))]
    has_cycle = False

    for node in g.nodes:
        dist[node] = 0 if node == source else MAX

    for i in range(1, len(g.nodes)):
        for edge in g.edges:
            if dist[edge.u] + edge.weight < dist[edge.v]:
                dist[edge.v] = dist[edge.u] + edge.weight

    # If a node can still be relaxed, it means that there is a negative cycle
    for edge in g.edges:
        if dist[edge.v] > dist[edge.u] + edge.weight:
            has_cycle = True

    return has_cycle, dist

if __name__ == '__main__':
    print bellman_ford(ret_random_graph(1000, 5000, 100, False))
