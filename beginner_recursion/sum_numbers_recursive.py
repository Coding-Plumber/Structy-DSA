# sum numbers recursive
# Watch the Approach video first!
#
#  Write a function sumNumbersRecursive that takes in an array of numbers and returns the sum of all the numbers in the array. All elements will be integers. Solve this recursively.

# sum_numbers_recursive([5, 2, 9, 10]); # -> 26

# Approach - set base case for len nums == 0 then pass in the array split, first element and then the rest


def sum_numbers_recursive(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_numbers_recursive(numbers[1:])


# Time: O(n^2)
# Space: O(n)


# Learning Notes -


# This is O(n^2) because:
# 1. The function makes n recursive calls
# 2. In each call, it creates a new list numbers[1:], which is a slice of the original list.
# 3. Creating this slice takes O(n) time in Python as it needs to create a new list object
#    and copy references to the elements.
# 4. Where as in a loop it would go from n1, n2, ..., n9 each being 1 operation
# 5. When having to take a slice it's like doing:
#    n1, create slice, n2, create slice, ..., n9, create slice
# 6. This repeated slicing operation is what makes it O(n^2)
