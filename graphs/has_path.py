# has path
# Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}

# has_path(graph, 'f', 'k') # True
# DFS


def has_path_recursive(graph, src, dst):
    if src == dst:
        return True

    for current in graph[src]:
        if has_path_recursive(graph, current, dst) == True:
            return True

    return False


# BFS
from collections import deque


def has_path(graph, src, dst):
    queue = deque([src])

    while queue:
        current = queue.popleft()

        if current == dst:
            return True

        for val in graph[current]:
            queue.append(val)

    return False
