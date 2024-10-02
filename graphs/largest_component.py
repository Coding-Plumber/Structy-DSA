# largest component
# Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.


# largest_component({
#   0: [8, 1, 5],
#   1: [0],
#   5: [0, 8],
#   8: [0, 5],
#   2: [3, 4],
#   3: [2, 4],
#   4: [3, 2]
# }) # -> 4


# Similar to the previous one except we need to keep track of each successful recursive call and increment if successful then just keep track of the largest value returned


def largest_component(graph):
    visited = set()
    highest_val = 0

    for node in graph:
        current_val = explore_size(graph, node, visited)
        if current_val > highest_val:
            highest_val = current_val

    return highest_val


def explore_size(graph, current, visited):
    if current in visited:
        return 0

    visited.add(current)

    size = 1
    for val in graph[current]:
        size += explore_size(graph, val, visited)

    return size


# Time: O(e)
# Space: O(n)
