# max root to leaf path sum
# Write a function, max_path_sum, that takes in the root of a binary tree that contains number values. The function should return the maximum sum of any root to leaf path within the tree.
#
# You may assume that the input tree is non-empty.


#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

# max_path_sum(a) # -> 18


# Approach - We need to handle both cases of the root being None and if we are at a root.val that is at a dead end ie left and right are none to return the current root.val because
# there is nothing left to return.

# The reason we also have to handle root is None is because if we are at say root = 4 although root.left is None root.right still has a path which we want to traverse.


def max_path_sum(root):
    if root is None:
        return float("-inf")

    if root.left is None and root.right is None:
        return root.val

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


# Time: O(n)
# Space: O(n)
