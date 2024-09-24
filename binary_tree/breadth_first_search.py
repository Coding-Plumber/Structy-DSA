# breadth first values
# Write a function, breadth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.


# Approach - We will use a queue but we need to add them and access them from the front in a FIFO (first in first out) style of stack. We can do this by popping from index 0 and appending as we go which will look something like this


# q = [a]
# v = []

# q = [b, c]
# v = [a]

# q = [c, d, e]
# v = [a, b]

# q = [d,e,f]
# v = [a, b, c]


def breadth_first_values(root):
    if not root:
        return []

    queue = [root]
    values = []

    while queue:
        node = queue.pop(0)
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return values


# Time: O(n^2)
# Space: O(n)

# The time is O(n^2) because each time we have to access the front of the list it is O(n) to do so.


# This is a inbuilt python library that allows us to use deque. Using this changes the Time complexity to O(n) because deque documentation states it uses O(1) so we dont need to use pop(0) which is O(n) time.

from collections import deque


def breadth_first_values_deque(root):
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()
        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return values


# Time: O(n)
# Space: O(n)


# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
#
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f
#
# #      a
# #    /   \
# #   b     c
# #  / \     \
# # d   e     f
#
# breadth_first_values(a)
# #    -> ['a', 'b', 'c', 'd', 'e', 'f']
