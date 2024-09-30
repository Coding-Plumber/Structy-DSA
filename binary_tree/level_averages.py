# level averages
# Write a function, level_averages, that takes in the root of a binary tree that contains number values. The function should return a list containing the average value of each level.

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

# level_averages(a) # -> [ 3, 7.5, 1 ]


# Similar to the last approach, get the values from each level then we can work out the average for each level to return.


# Note - this can also be done easier but using a inbuilt lib like so

# from statistics import mean
# for level in result:
#   averages.append(mean(level))


def level_averages(root):
    result = []
    values = _level_averages(root, result, 0)

    averages = []

    for level in result:
        total = sum(level)
        average_val = total / len(level)
        averages.append(average_val)

    return averages


def _level_averages(root, val_store, num_level):
    if root is None:
        return

    if len(val_store) == num_level:
        val_store.append([root.val])
    else:
        val_store[num_level].append(root.val)

    _level_averages(root.left, val_store, num_level + 1)
    _level_averages(root.right, val_store, num_level + 1)


# Time: O(n)
# Space: O(n)
