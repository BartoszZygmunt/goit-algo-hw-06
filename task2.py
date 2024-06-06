import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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

# Function to perform DFS
def dfs(graph, start, target, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path.append(start)
    visited.add(start)
    
    if start == target:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, target, path.copy(), visited.copy())
            if result is not None:
                return result
    return None

# Function to perform BFS
def bfs(graph, start, target):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node in visited:
            continue
        
        for neighbor in graph[node]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
            
            if neighbor == target:
                return new_path
        
        visited.add(node)
    
    return None

# Test the algorithms
start_node = 'Station'
target_node = 'Park'

dfs_path = dfs(G, start_node, target_node)
bfs_path = bfs(G, start_node, target_node)

print(f"DFS path from {start_node} to {target_node}: {dfs_path}")
print(f"BFS path from {start_node} to {target_node}: {bfs_path}")


# DFS (Depth-First Search):
# DFS explores as far down a branch as possible before backtracking. 
# In this case, DFS followed the path from 'Station' to 'Mall', then to 'Hospital', then to 'School', and finally to 'Park'. 
# This resulted in a longer path, as it didn't prioritize finding the shortest path first.

# BFS (Breadth-First Search):
# BFS explores all the neighbors of a node level by level. 
# It guarantees finding the shortest path (in terms of the number of edges). 
# In this case, BFS found a shorter path from 'Station' to 'School', and then directly to 'Park'.


