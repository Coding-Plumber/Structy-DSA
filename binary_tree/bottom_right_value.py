# bottom right value
# Write a function, bottom_right_value, that takes in the root of a binary tree. The function should return the right-most value in the bottom-most level of the tree.
#
# You may assume that the input tree is non-empty.

#       3
#    /    \
#   11     10
#  / \      \
# 4   -2     1

# bottom_right_value(a) # -> 1


# Approach - Do a BFS and then we can return the last input either with the current node or last result in
from collections import deque


def bottom_right_value(root):
    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()

        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result[-1]


# Time: O(n)
# Space: O(n)

# We can slightly improve the space complexity by not saving the values in result and just returning the last node but both would still be O(n)
