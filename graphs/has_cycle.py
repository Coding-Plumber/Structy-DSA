# has cycle
# Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle.


# has_cycle({
#   "a": ["b"],
#   "b": ["c"],
#   "c": ["a"],
# }) # -> True
#

# Approach - need a way to monitor what nodes have been visited to detect a cycle using a set. Will also need to detect if we are currently in a cycle

# if we had the above as

# A > B
#   \ |
#     C

# If we start at A > B > C > A if we hit A again and it is in the visited set we know we have already been here.
# However if we had another node that wasnt linked

# However if we had A>B>C


def has_cycle(graph):
    visited = set()

    for starting_node in graph:
        if check_cycle(graph, starting_node, set(), visited):
            return True
    return False


def check_cycle(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if check_cycle(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)

    return False
