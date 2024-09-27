# tree value count
# Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.


#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

# tree_value_count(a,  6) # -> 3

# Fairly straight forward for the BFS iterative solution. For the DFS recursive method we just need to go down both sides of the tree and sum the amount at the end of both sides but also
# to handle if the initial root.val == target


def tree_value_count_recursive(root, target):
    if root is None:
        return 0

    match = 1 if root.val == target else 0

    return (
        match
        + tree_value_count(root.left, target)
        + tree_value_count(root.right, target)
    )


# Time: O(n)
# Space: O(n)


from collections import deque


def tree_value_count(root, target):
    if not root:
        return 0

    queue = deque([root])
    count = 0

    while queue:
        node = queue.popleft()
        if node.val == target:
            count += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return count


# Time: O(n)
# Space: O(n)
