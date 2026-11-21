import networkx as nx
import matplotlib.pyplot as plt
from functools import cmp_to_key

def comparator(a, b):
    return a[2] - b[2]


def kruskals_mst(V, edges):

    edges = sorted(edges, key=cmp_to_key(comparator))

    dsu = DSU(V)
    cost = 0
    count = 0
    mst_edges = []

    for x, y, w in edges:

        if dsu.find(x) != dsu.find(y):
            dsu.union(x, y)

            cost += w
            count += 1

            mst_edges.append((x, y, w))

            if count == V - 1:
                break

    return cost, mst_edges


class DSU:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):

        s1 = self.find(x)
        s2 = self.find(y)

        if s1 != s2:

            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2

            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1

            else:
                self.parent[s2] = s1
                self.rank[s1] += 1


# Main program
if __name__ == '__main__':

    V = 4

    edges = [
        [0, 1, 10],
        [1, 3, 15],
        [2, 3, 4],
        [2, 0, 6],
        [0, 3, 5]
    ]

    # Find MST
    cost, mst_edges = kruskals_mst(V, edges)

    print("Minimum Spanning Tree Cost:", cost)
    print("Selected Edges:", mst_edges)

    # Create original graph
    G = nx.Graph()

    for i in range(V):
        G.add_node(i)

    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    # Create MST graph
    MST = nx.Graph()

    MST.add_nodes_from(range(V))

    for u, v, w in mst_edges:
        MST.add_edge(u, v, weight=w)

    # Graph layout
    pos = {
        0: (0, 0),
        1: (2, 0),
        2: (2, 2),
        3: (0, 2)
    }

    # Draw original graph
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='skyblue',
        node_size=1200,
        font_size=15,
        font_weight='bold',
        edge_color='gray',
        width=2
    )

    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels,
        font_size=12
    )

    plt.title("Original Weighted Graph", fontsize=14)

    # Draw MST
    plt.subplot(1, 2, 2)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        node_size=1200,
        font_size=15,
        font_weight='bold',
        edge_color='lightgray',
        width=1.5
    )

    # Highlight selected MST edges
    nx.draw_networkx_edges(
        MST,
        pos,
        edge_color='green',
        width=4
    )

    nx.draw_networkx_edge_labels(
        MST,
        pos,
        edge_labels=nx.get_edge_attributes(MST, 'weight'),
        font_size=12,
        font_color='green'
    )

    plt.title(f"Minimum Spanning Tree (Cost = {cost})", fontsize=14)

    plt.tight_layout()
    plt.show()