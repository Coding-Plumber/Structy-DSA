# pair sum

# Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such pair that sums to the target.

# pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)

# Nested loop is the go to brute force here which would be O(n * m)
# We can do it in 1 loop using a complement where we find out the remaining value needed and when we find that we can return them 2 indexes
# complement = target - i (3)
# That leaves us with 5 needed
# store = { 0:5, }
# We can then check against the store so when we get to 5 we have this
# store = { 0:5, 1:6 }
# We see we have 5 in the store so we return 0 and current index of 2


def pair_sum(numbers, target_sum):
    num_store = {}
    for i, num in enumerate(numbers):
        complement = target_sum - num

        if complement in num_store and i != num_store[complement]:
            return (num_store[complement], i)

        num_store[num] = i


# Time: O(n)
# Space: O(n)

# Notes - This one didn't need to be refactored and was the optimal solution
