from kruskal import Graph

# Node values for Graph 1 (Left Graph)
node_values_1 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

# Graph 1 (Left Graph)
g1 = Graph(6)
edges1 = [
    ("a", "b"), ("a", "f"), ("a", "e"),
    ("b", "c"), ("b", "f"), ("b", "e"),
    ("c", "d"), ("c", "e"),
    ("d", "e"),
    ("e", "f")
]

# Add edges with weights calculated from node values
for u, v in edges1:
    g1.addEdge(ord(u) - ord('a'), ord(v) - ord('a'),
               node_values_1[u] + node_values_1[v])

print("MST for Graph 1")
g1.KruskalMST()
