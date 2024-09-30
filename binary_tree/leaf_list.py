# leaf list
# Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# leaf_list(a) # -> [ 'd', 'e', 'f' ]

# DFS - very similar to last one, we need to search and append only the nodes without a left or right node which means it is a leaf node
# BFS - wouldnt work without additional handling of the levels which would be worse time complexity. If it was an unbalanced tree you would need additional edge cases to handle the deeper tree leaves first.


def leaf_list(root):
    leaves = []
    _leaf_list(root, leaves)
    return leaves


def _leaf_list(root, leaf_store):
    if root is None:
        return
    if root.left is None and root.right is None:
        leaf_store.append(root.val)

    _leaf_list(root.left, leaf_store)
    _leaf_list(root.right, leaf_store)


# Time: O(n)
# Space: O(n)


# DFS Itertively


def leaf_list_iter(root):
    if root is None:
        return []

    stack = [root]
    leaves = []

    while stack:
        node = stack.pop()

        if node.left is None and node.right is None:
            leaves.append(node.val)

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return leaves


# Time: O(n)
# Space: O(n)
