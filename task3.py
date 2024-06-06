import networkx as nx
import matplotlib.pyplot as plt

# Reusing the graph from Task 1
G = nx.Graph()

nodes = ['Station', 'Mall', 'School', 'Hospital', 'Park', 'Library', 'University', 'Museum']
edges = [
    ('Station', 'Mall', 3),
    ('Station', 'School', 4),
    ('Station', 'Hospital', 1),
    ('Station', 'University', 2),
    ('Station', 'Museum', 7),
    ('Mall', 'Hospital', 5),
    ('School', 'Hospital', 2),
    ('School', 'Park', 7),
    ('Park', 'Library', 3),
    ('Library', 'University', 2),
    ('University', 'Museum', 6),
    ('University', 'School', 3),
    ('University', 'Park', 2),
    ('Museum', 'Mall', 4)
]

G.add_nodes_from(nodes)
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Function to find shortest paths using Dijkstra's algorithm
def find_all_shortest_paths(graph):
    shortest_paths = dict(nx.all_pairs_dijkstra_path(graph))
    return shortest_paths

# Find the shortest paths between all pairs of vertices
shortest_paths = find_all_shortest_paths(G)

# Display the shortest paths
for start_node, paths in shortest_paths.items():
    print(f"Shortest paths from {start_node}:")
    for target_node, path in paths.items():
        print(f"  to {target_node}: {path}")

# Visualize the graph
pos = nx.spring_layout(G)  # Positioning the nodes
weights = nx.get_edge_attributes(G, 'weight')

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=15, font_color='black', font_weight='bold', edge_color='grey')
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_color='red')
plt.title("City's Transportation Network with Weights")
plt.show()
