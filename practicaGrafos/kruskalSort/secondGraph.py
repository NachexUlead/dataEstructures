from kruskal import Graph

# Node values for Graph 2 (Right Graph)
node_values_2 = {"a": 1, "b": 2, "c": 3, "d": 4}

# Graph 2 (Right Graph)
g2 = Graph(4)
edges2 = [
    ("a", "b"), ("a", "c"),
    ("b", "c"), ("b", "d"),
    ("c", "d")
]

# Add edges with weights calculated from node values
for u, v in edges2:
    g2.addEdge(ord(u) - ord('a'), ord(v) - ord('a'), node_values_2[u] + node_values_2[v])

print("MST for Graph 2")
g2.KruskalMST()
