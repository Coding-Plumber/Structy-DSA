# longest path
# Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.


graph = {
    "a": ["c", "b"],
    "b": ["c"],
    "c": [],
    "q": ["s", "r"],
    "r": ["s"],
    "s": [],
}
# longest_path(graph) # -> 2

# Approach - we first iterate through the graph and find the end nodes. We store those in a object(distance) like {a:0}, we then go through the graph calling on a helper function. If the node passed is already in the obj we can return it instantly and go to the next value. If not in obj we can continue we set a value tracker for largest value and then go through the graph[nodes] values. We recursively call on each neighbor value keeping track of the largest.

# if we had the acyclic graph from above it would look like this

# a > c
# | /^
# v
# b

# q > s
# | /^
# v
# r


# we would first pass in A to the helper graph
# this will be our lowest call for this node which we will build off, we will recursively DFS through the links in it
# next we search through the neighbors, so 'c' which will return 0 because its already in distances base case.
# Next up is b which will then call on c and start the return
# b has nothing else so we will set distance[b] as 0 + 1
# when we return back to the initial call of 'a' and go to the next neighbor 'b' we have already explored that so we can do distance[a] = largest (1) + 1

# We then return to the original call of the function, call on b instantly return, same for c until we do the same process on q


def longest_path(graph):
    distance = {}

    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 0

    for node in graph:
        traverse_graph(graph, node, distance)

    return max(distance.values())


def traverse_graph(graph, node, distance):
    if node in distance:
        return distance[node]

    largest = 0
    for neighbor in graph[node]:
        count = traverse_graph(graph, neighbor, distance)
        if count > largest:
            largest = count

    distance[node] = largest + 1
    return distance[node]


# e = # edges
# n = # nodes
# Time: O(e)
# Space: O(n)
