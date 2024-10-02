# connected components count
# Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. The function should return the number of connected components within the graph.


connected_components_count(
    {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}
)  # -> 2


# Approach - Need to cycle through the values keeping track of which have already been visited to avoid an infinite cycle.

# We can pass a node to a helper function which can then iterate through those. For example this one should return 2 because if we lay it out into a graph it looks like this

# Component 1:       Component 2:
#
#     1              3 --- 2
#     |              |     |
#     |              |     |
# 0 -- 5             |     |
# |  /               |     |
# | /                |     |
# 8                  4 ----

# We need a way to come out of the cycle when we come out of the first graph island and to increase a counter

# if we pass in graph[0] and cycle through those values and storing if they were visited or not
# we would go through 0, 8, 1, 5 which are all linked then if we return back we can increase a count because it must mean its a seperate unlinked graph cycle


def connected_components_count(graph):
    count = 0
    visited = set()
    for node in graph:
        if explore(graph, node, visited) == True:
            print(node)
            count += 1

    return count


def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for val in graph[current]:
        explore(graph, val, visited)

    return True


# Time: O(e)
# Space: O(n)

# Although we have two for loops we only cycle through the edges once. We return from any visited and only store at max the amount of nodes in the store.


# Time:
