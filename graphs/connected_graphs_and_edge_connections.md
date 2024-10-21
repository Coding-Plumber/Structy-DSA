# Connected Graphs and Edge Calculations

## Introduction
In graph theory, a connected graph is a graph where there is a path between every pair of vertices. Understanding the maximum number of edges in such graphs is crucial for various applications.

## Maximum Edges in a Connected Graph

### Formula: n * (n - 1) / 2

Where:
- n is the number of vertices in the graph
- The result is the maximum number of edges

## Derivation of the Formula

1. In a fully connected graph, each vertex connects to every other vertex.
2. For n vertices, each vertex can connect to (n - 1) other vertices.
3. This gives us n * (n - 1) total connections.
4. However, this counts each edge twice (A to B and B to A).
5. To correct for this, we divide by 2: n * (n - 1) / 2

## Simplification to n^2 - n

The formula n * (n - 1) / 2 can be rewritten as:
(n^2 - n) / 2

This is because:
- n * (n - 1) expands to n^2 - n
- We still divide by 2 to account for duplicate counting

## Examples

1. For a graph with 4 vertices:
   - Maximum edges = 4 * (4 - 1) / 2 = 4 * 3 / 2 = 6 edges

2. For a graph with 5 vertices:
   - Maximum edges = 5 * (5 - 1) / 2 = 5 * 4 / 2 = 10 edges

## Why We Halve the Value

We halve the value to avoid counting the same edge twice. In an undirected graph:
- The edge from A to B is the same as the edge from B to A
- Without halving, we would count each edge twice

Example:
In a graph with 3 vertices (A, B, C), without halving:
1. A -> B, A -> C (2 edges from A)
2. B -> A, B -> C (2 edges from B)
3. C -> A, C -> B (2 edges from C)

Total: 6 edges

But in reality, there are only 3 unique edges:
1. A - B
2. A - C
3. B - C

By halving 6, we get the correct count of 3 edges.

## Conclusion

The formula n * (n - 1) / 2 or (n^2 - n) / 2 gives us the maximum number of edges in a connected graph with n vertices, accounting for the undirected nature of the edges and avoiding duplicate counting.
