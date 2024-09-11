# palindrome recursive
# Write a function, palindrome, that takes in a string and returns a boolean indicating whether or not the string is the same forwards and backwards.
#
# You must solve this recursively.

# palindrome("pop") # -> True

# Approach - To recursively reverse the string and return s == reversed_s however i don't know if this is against the intention of the question because i will have to make a new function to call on.

# The correct way


def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])


# Notes - Tha main part of this is we repeatedly pass the middle of the string back to it to keep comparing the first and last element

# Time: O(n^2) - The slice adds extra complexity
# Space: O(n^2)
