# shortest path
# Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1. You can assume that A and B exist as nodes in the graph.


# edges = [
#   ['w', 'x'],
#   ['x', 'y'],
#   ['z', 'y'],
#   ['z', 'v'],
#   ['w', 'v']
# ]
#
# shortest_path(edges, 'w', 'z') # -> 2


# The best approach here is BFS because we are trying to find the smallest path which is closest to the starting node. With BFS it will check all neighboring nodes first where as DFS will go as deep as it can before working backwards. DFS can be used here and in some use cases would be faster but overall i think its more suited to BFS.


from collections import deque


def shortest_path(edges, node_A, node_B):
    graph = build_adjacency_graph(edges)

    visited = set(node_A)
    queue = deque([(node_A, 0)])

    while queue:
        node, level = queue.popleft()

        if node == node_B:
            return level

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return -1


def build_adjacency_graph(edges):
    graph = {}

    for edge in edges:
        node_a, node_b = edge

        if node_a not in graph:
            graph[node_a] = []
        if node_b not in graph:
            graph[node_b] = []

        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    return graph


# Time: O(e)
# Space: O(n)


# DFS Version


def shortest_path(edges, node_A, node_B):
    graph = build_adjacency_graph(edges)
    visited = set()

    def dfs(current, target, level):
        if current == target:
            return level

        if current in visited:
            return float("inf")

        visited.add(current)

        shortest = float("inf")
        for neighbor in graph[current]:
            result = dfs(neighbor, target, level + 1)
            shortest = min(shortest, result)

        visited.remove(current)  # see note below

        return shortest

    result = dfs(node_A, node_B, 0)
    return result if result != float("inf") else -1


def build_adjacency_graph(edges):
    graph = {}

    for edge in edges:
        node_a, node_b = edge

        if node_a not in graph:
            graph[node_a] = []
        if node_b not in graph:
            graph[node_b] = []

        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    return graph


# Time: O(e)
# Space: O(n)

# Note - we remove the current from visited because an example below if we have a built adjacecny list like so

# {'w': ['x', 'v'], 'x': ['w', 'y'], 'y': ['x', 'z'], 'z': ['y', 'v'], 'v': ['z', 'w']}
