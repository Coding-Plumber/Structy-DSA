# # uncompress
# Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:
# <number><char>
# for example, '2c' or '3a'.
# The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

# uncompress("2c3a1t") # -> 'ccaaat'

# Approach - For loop through the string,
# have a variable of nums 1-9 to check against
# if char is a num then we store the num as a variable
# next iteration where we dont have a num
# we push to an array or string that amount of times
# might have to do some extra working out for storing nums if we say have the test case of 127y to ensure we have
# 127 saved as the variable and not just 7


def uncompress(s):
    num_store = ""
    result = ""
    nums = "123456789"
    loop_amount = 0

    for char in s:
        if char in nums:
            num_store += char
            continue

        loop_amount = int(num_store)

        for _ in range(loop_amount):
            result += char

        loop_amount = 0
        num_store = ""

    return result


# Time: O(n*m)
# Space: O(n*m)


# Refactored Version


def uncompress_refactor(s):
    result = []
    nums = "123456789"
    i = 0
    j = 0

    while j < len(s):
        if s[j] in nums:
            j += 1
        else:
            val = s[i:j]
            result.append(int(val) * s[j])
            j += 1
            i = j
    return "".join(result)


# Time: O(n*m)
# Space: O(n*m)

# Same speeds but using two pointer could be easier to understand


# similar methods - https://leetcode.com/problems/string-compression/description/
