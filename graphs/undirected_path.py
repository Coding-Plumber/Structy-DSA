# undirected path
# Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.

# edges = [
#   ('i', 'j'),
#   ('k', 'i'),
#   ('m', 'k'),
#   ('k', 'l'),
#   ('o', 'n')
# ]
#
# undirected_path(edges, 'j', 'm') # -> True


def undirected_path(edges, node_A, node_B):
    adjacency_list = create_adjacency_list(edges)
    check_graph = check_adjacency_list(adjacency_list, node_A, node_B, set())
    return check_graph == True


def check_adjacency_list(graph, node_A, node_B, visited):
    if node_A == node_B:
        return True

    if node_A in visited:
        return False
    visited.add(node_A)

    for node in graph[node_A]:
        if check_adjacency_list(graph, node, node_B, visited) == True:
            return True


def create_adjacency_list(edges):
    adjacency_list = {}

    for edge in edges:
        a, b = edge
        if a not in adjacency_list:
            adjacency_list[a] = []
        if b not in adjacency_list:
            adjacency_list[b] = []
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    return adjacency_list
