# tree path finder
# Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.
#
# You may assume that the tree contains unique values.


#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# path_finder(a, 'e') # -> [ 'a', 'b', 'e' ]


# Approach - we need to traverse the tree until we find the targe, then we can return that value with a list [] and add the previous values to it. If we dont find the target we need to
# return None. We need to ensure we only try append the values to the list if the target is found or it will cause an error because no list will exist.


# This version is the initial approach however large tests run slowly, the reason being is that when we hit the return case of [root.val, *tree_left] we are creating a new list each time # so it makes it O(n*n) or O(n^2) because every n operation we have another n operation


def path_finder_slower(root, target):
    if root is None:
        return None

    if root.val == target:
        return [root.val]

    tree_left = path_finder_slower(root.left, target)
    if tree_left is not None:
        return [root.val, *tree_left]

    tree_right = path_finder_slower(root.right, target)
    if tree_right is not None:
        return [root.val, *tree_right]

    return None


# Time: O(n^2)
# Space: O(n)


# This version is faster because we append it to the existing list which is within tho O(n) operation. Although at the end we have to reverse the list which is O(n) it is only done once
# and makes it O(n + n) which is still O(n)


def path_finder(root, target):
    result = _path_finder(root, target)

    if result is None:
        return None
    else:
        return result[::-1]


def _path_finder(root, target):
    if root is None:
        return None

    if root.val == target:
        return [root.val]

    tree_left = _path_finder(root.left, target)
    if tree_left is not None:
        tree_left.append(root.val)
        return tree_left

    tree_right = _path_finder(root.right, target)
    if tree_right is not None:
        tree_right.append(root.val)
        return tree_right

    return None


# Time: O(n)
# Space: O(n)
