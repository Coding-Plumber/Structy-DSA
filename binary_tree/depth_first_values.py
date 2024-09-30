# depth first values
# Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.
#

# Approach - Similar to a linked list, except we have a left and right instead of next. We can handle DFS with a stack, we append the left last because that is the one we want to prioritise otherwise it would change the return value


def depth_first_values(root):
    if not root:
        return []
    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        print(stack)

    return values


# Time: O(n)
# Space: O(n)


def depth_first_values_recursive(root):
    if not root:
        return []
    root_left = depth_first_values_recursive(root.left)
    root_right = depth_first_values_recursive(root.right)

    return [root.val, *root_left, *root_right]


# Time: O(n^2)
# Space: O(n)
