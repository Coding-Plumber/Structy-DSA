# tree levels
# Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each sublist represents a level of the tree.


#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# tree_levels(a) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]


# Approach - The main thing here is to keep track of the level and add to the array matching the level. We can also do this with a BFS iterative solution but we need to switch the order of the if statement of if node.left and if node.right to place them in the correct order.

# BFS Version -

from collections import deque
from typing import Any


def tree_levels(root):
    if root is None:
        return []

    q = deque([(root, 0)])

    result = []

    while q:
        node, level = q.popleft()

        if level == len(result):
            result.append([node.val])
        else:
            result[level].append(node.val)

        if node.left is not None:
            q.append((node.left, level + 1))
        if node.right is not None:
            q.append((node.right, level + 1))

    return result


# Time: O(n)
# Space: O(n)


def tree_levels_recursive(root):
    result = []
    levels = _tree_levels(root, result, 0)
    return result


def _tree_levels(root, result, level_num):
    if root is None:
        return

    if len(result) == level_num:
        result.append([root.val])
    else:
        result[level_num].append(root.val)

    _tree_left = _tree_levels(root.left, result, level_num + 1)
    _tree_right = _tree_levels(root.right, result, level_num + 1)


# Time: O(n)
# Space: O(n)
