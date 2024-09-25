# tree min value
# Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.
#
# You may assume that the input tree is non-empty.

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
# tree_min_value(a) # -> -2

# DFS


# Notes - Main part here is when we hit outside the recursive calls and start the return we need a value that is always going to be over ridden no matter the value
# for this we can use infinity in python it is float("inf)") which means whatever value we return is less than
def tree_min_value_recursive(root):
    if not root:
        return float("inf")

    tree_left = tree_min_value_recursive(root.left)
    tree_right = tree_min_value_recursive(root.right)

    return min(root.val, tree_left, tree_right)


# BFS Method

from collections import deque


def tree_min_value(root):

    queue = deque([root])
    lowest_val = float("inf")

    while queue:
        node = queue.popleft()

        if node.val < lowest_val:
            lowest_val = node.val

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return lowest_val
