# tree includes
# Write a function, tree_includes, that takes in the root of a binary tree and a target value. The function should return a boolean indicating whether or not the value is contained in the tree.


#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# tree_includes(a, "e") # -> True


# Approac - Can do this with recursive DFS checking each call stack and comparing root.val to target and if so returning True. If we dont find it we return False


def tree_includes(root, target):
    if not root:
        return False
    if root.val is target:
        return True
    tree_left = tree_includes(root.left, target)
    tree_right = tree_includes(root.right, target)
    return tree_left or tree_right is True


# Time: O(n)
# Space: O(n)


from collections import deque


def tree_includes_bfs(root, target):
    if not root:
        return False

    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node.val is target:
            return True

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return False


# Time: O(n)
# Space: O(n)
