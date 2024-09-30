# Graph Introduction

## What is a graph?

A graph is just a collection of nodes and edges.

```
   (a)----->(b)
    |       |
    ⌄       ⌄
   (c)<----(d)
    |       
    ⌄       
   (e)<----(f)
```

Nodes are just 'things' and edges are relationships.

We could imagine the nodes as cities and the edges as roads to neighbouring cities.

## Types of Graphs

### Directed Graph 

Arrowheads showing a direction:

```
   (a)----->(b)
    |       |
    ⌄       ⌄
   (c)<----(d)
    |       
    ⌄       
   (e)<----(f)
```

### Undirected Graph 

No direction and free flowing:

```
   (a)------(b)
    |       |
   (c)-----(d)
    |       
   (e)-----(f)
```

Neighbour nodes are any nodes accessible through an edge.

## Adjacency List

Consider this graph:

```
    (a)----->(c)
     |       |
     ⌄       ⌄                       
    (b)<----(e)
     |       
     ⌄       
    (d)<----(f)
```

As an adjacency list, it would look like this:

```
{
    a: [b, c],
    b: [d], 
    c: [e], 
    d: [], 
    e: [b], 
    f: [d]
}
```

Here, 'e' is pointing at 'b', so we show that as `e: [b]`.
We also show nodes that don't point at other nodes in the adjacency list, like 'd' here is `d: []`.

## Must-know Algorithms for Graphs

### Depth-First Traversal

For this graph:

```
    (a)----->(c)
     |        |
     ⌄        ⌄                       
    (b)<-----(e)
     |       
     ⌄       
    (d)<----(f)
```

Depth-first traversal would route:
- a > b > d 
- a > c > e

### Breadth-First Traversal

For the same graph, breadth-first traversal would route:
- a > b 
- a > c 
- b > d 

#### Example of BFS in a Larger Graph

Starting from (x):

```
( ) - ( ) - ( ) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - (x) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - ( ) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - ( ) - ( ) - ( ) - ( )
```

It would reach out to as far left or right as it could go (the direction is determined by the code algorithm of which way it would go first, i.e., left or right):

```
( ) - ( ) - ( ) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - (x) - (x) - (x) - (x)
 |     |     |     |     |     |
( ) - ( ) - ( ) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - ( ) - ( ) - ( ) - ( )
```

Before then going as far down or up as it could go:

```
( ) - ( ) - ( ) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - (x) - (x) - (x) - (x)
 |     |     |     |     |     |
( ) - ( ) - ( ) - ( ) - ( ) - (x)
 |     |     |     |     |     |
( ) - ( ) - ( ) - ( ) - ( ) - (x)
```

Where it would then go as far left as it could go because it can't go right:

```
( ) - ( ) - ( ) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - (x) - (x) - (x) - (x)
 |     |     |     |     |     |
( ) - ( ) - ( ) - ( ) - ( ) - (x)
 |     |     |     |     |     |
(x) - (x) - (x) - (x) - (x) - (x)
```

And so forth.

#### Example of DFS in a Larger Graph

A depth-first search would reach outwards from its starting location like this:

```
( ) - ( ) - (x) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - (x) - (x) - (x) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - (x) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - ( ) - ( ) - ( ) - ( )
```

And keep expanding like so:

```
( ) - ( ) - (x) - ( ) - ( ) - ( )
 |     |     |     |     |     |
( ) - (x) - (x) - (x) - (x) - ( )
 |     |     |     |     |     |
( ) - (x) - (x) - (x) - ( ) - ( )
 |     |     |     |     |     |
( ) - ( ) - (x) - ( ) - ( ) - ( )
```

It will explore all directions evenly.

## Depth-First Stack Implementation

For this graph:

```
    (a)----->(c)
     |        |
     ⌄        ⌄                       
    (b)      (e)
     |       
     ⌄       
    (d)---->(f)
```

A stack would handle this like so:

1. stack = [a]
2. current = a (pop from stack)
3. stack = [c, b] (push a's neighbours)
4. current = b (pop from stack)
5. stack = [c, d] (push b's neighbour)
6. current = d (pop from stack)
7. stack = [c, f] (push d's neighbour)
8. current = f (pop from stack)

## Breadth-First Queue Implementation

For the same graph:

1. current = a
2. queue = [c, b] (enqueue a's neighbours)
3. current = c (dequeue from front)
4. queue = [b, e] (enqueue c's neighbour)
5. current = b (dequeue from front)
6. queue = [e, d] (enqueue b's neighbour)

This keeps it working in the breadth-first order.
