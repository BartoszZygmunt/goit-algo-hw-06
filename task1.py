import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create the graph
G = nx.Graph()

# Step 2: Add nodes (locations) and edges (roads with distances)
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

# Adding nodes to the graph
G.add_nodes_from(nodes)

# Adding edges to the graph with weights
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Step 3: Visualize the graph
pos = nx.spring_layout(G)  # Positioning the nodes
weights = nx.get_edge_attributes(G, 'weight')

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=15, font_color='black', font_weight='bold', edge_color='grey')
nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_color='red')
plt.title("City's Transportation Network")
plt.show()

# Step 4: Analyze the graph's characteristics
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_vertices = dict(G.degree())

print(f"Number of vertices: {num_vertices}")
print(f"Number of edges: {num_edges}")
print("Degree of each vertex:")
for vertex, degree in degree_of_vertices.items():
    print(f"{vertex}: {degree}")
