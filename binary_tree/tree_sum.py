# tree sum
# Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

# tree_sum(a) # -> 21


# Approach - nice simple DFS recursion call summing the values of each side and returning the total of each side and the initial root.val


def tree_sum(root):
    if not root:
        return 0

    root_left = tree_sum(root.left)
    root_right = tree_sum(root.right)
    return root.val + root_left + root_right


# Time: O(n)
# Space: O(n)


# BFS with a while loop


def tree_sum_BFS(root):
    if not root:
        return 0

    sum = 0
    queue = [root]

    while queue:
        current = queue.pop(0)
        val = current.val

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        sum += val

    return sum


# Time: O(n)
# Space: O(n)
