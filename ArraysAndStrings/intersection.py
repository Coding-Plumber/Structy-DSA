# intersection
# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

# intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]

# Approach - The brute force approach would be to use a nested loop but it would fail the test cases for speed,
# we could use a set

# Using a brute force loop


def intersection(a, b):
    set_a = set(a)
    result = []

    for item in b:
        if item in a:
            result.append(item)
    return result


# Time: O(n*m)
# Space: O(n + m)


# This fails the large test cases however which was predicte with a > 2000 ms execution time out

# If we change it to a set thought it passes


def intersection_set(a, b):
    set_a = set(a)
    result = []

    for item in b:
        if item in set_a:
            result.append(item)
    return result


# Time: O(n + m)
# Space: O(n+m)


# Even though this is very similar and uses a set instead of an array, because sets use constant look up time its a LOT faster


# A one liner example
def intersection_one_liner(a, b):
    return list(set(a) & set(b))


# Time: O(n + m)
# Space: O(n + m)

# When using a '&' with sets it performs a set intersection. It returns a new set containing elements that are common to both sets.


# Using List comprehension
def intersection_list_comprehension(a, b):
    set_a = set(a)
    return [item for item in b if item in set_a]


# Time: O(n + m)
# Space: O(n + m)


# This reads like this -
# Declare item as the index of b iteration
# if item is also in set_a add it to this new list comprehension


# Leetcode alternative - https://leetcode.com/problems/intersection-of-two-arrays/description/
