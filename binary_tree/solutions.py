# how high
# Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.
#
# The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.
#
# If the tree is empty, return -1.


# Approach - We need to return the edges rather than the nodes themselves, if we go beyond a node that doesnt contribute to the height so we can start our return with -1
# then for each return we can add +1 and the highest value of left vs right traversal


def how_high(node):
    if node is None:
        return -1

    return 1 + max(how_high(node.left), how_high(node.right))


# Time: O(n)
# Space: O(n)
