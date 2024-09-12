# fibonacci
# Write a function, fibonacci, that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.
#
# The 0-th number of the sequence is 0.
#
# The 1-st number of the sequence is 1.
#
# To generate further numbers of the sequence, calculate the sum of previous two numbers.
#
# You must solve this recursively.

# Appoach - we need to recursively call at different depths to sum ie n -1 + n - 2 = n. We can recursively call at different levels till we hit the base case of the 0th node of 0


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Time O(n^2)
# Space: O(n)


# The time complexity is O(n^2) because each call branches into two recursive calls,
# creating a binary tree of calls until we hit the base cases.
# The number of calls grows exponentially with n

# The space complexity is O(n) because the miximum depth of the recursion stack
# is n, which occurs along the leftmost pathl of  the call tree.
