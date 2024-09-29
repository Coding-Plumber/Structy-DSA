# all tree paths
# Write a function, all_tree_paths, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each subarray represents a root-to-leaf path in the tree.
# The order within an individual path must start at the root and end at the leaf, but the relative order among paths in the outer list does not matter.
# You may assume that the input tree is non-empty.


#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# all_tree_paths(a) # ->
# [
#   [ 'a', 'b', 'd' ],
#   [ 'a', 'b', 'e' ],
#   [ 'a', 'c', 'f' ]
# ]

# Approach - Hit a recursive base case where we return [], also need a base case if we hit a leaf node to return the values to the original base case []. Each recursive call we need to append the values of those calls and add the current root.val to those.

# ie if we go beyond d we return [] > d then [[d]] gets returned to b
# at root b left_path is [[d]] and right path is [[e]]
# we then need to add both of these paths to a [] and include the current val of b
# We would return this to a [[d, b], [e,b]]
# a would then have two paths of [[d,b], [e,b]] and [[c,f]]
# Then iterate through them appending them to one []


def all_tree_paths(root):
    paths = _all_tree_paths(root)
    for path in paths:
        path.reverse()
    return paths


def _all_tree_paths(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]

    all_paths = []

    tree_left = _all_tree_paths(root.left)
    for path in tree_left:
        path.append(root.val)
        all_paths.append(path)

    tree_right = _all_tree_paths(root.right)
    for path in tree_right:
        path.append(root.val)
        all_paths.append(path)

    return all_paths


# Time: O(n*log(n))
# Space: O(n*log(n))

# Explanation:
# 1. Tree Structure:
#    As the tree grows, each level potentially doubles in size:
#        a
#      /   \
#     b     c
#    / \   / \
#   d   e f   g

# 2. Time Complexity:
#    - We visit each node once (n operations)
#    - At each node, we process paths:
#      * Leaf nodes (d, e, f, g) process 1 path each
#      * Middle nodes (b, c) process more paths
#      * Root node (a) processes all paths
#    - On average, each node processes log(n) paths
#    - Total: n nodes * log(n) average work per node = n * log(n)

# 3. Space Complexity:
#    - We store all root-to-leaf paths
#    - Number of paths ≈ n/2 (half of nodes are leaves in a full binary tree)
#    - Each path length ≈ log(n) (tree height)
#    - Total space: (n/2) * log(n) = O(n * log(n))

# 4. Intuition:
#    - Lower nodes (near leaves) do fewer operations
#    - Higher nodes (near root) do more operations
#    - The difference in work between levels is logarithmic
#    - For each node (n), we're doing about log(n) work on average


# * - ≈ is a approximately equal to sign
