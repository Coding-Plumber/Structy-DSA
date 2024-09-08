# most frequent char
# Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.

# most_frequent_char('bookeeper') # -> 'e'


# Approach Thoughts - Hash Map to hold the values ie count = {'a' : 2, 'b' : 3, 'c': 5} then return the highest value


def most_frequent_char(s):
    return char_counter(s)


def char_counter(s):
    count = {}
    highest_val = 0
    str_for_hv = ""

    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    for val in count:
        if count[val] > highest_val:
            highest_val = count[val]
            str_for_hv = val

    return str_for_hv


# Time: O(n + m) = O(n)
# Space: O(n)

# Notes - possible a way to return the highest value directly in python dict but i couldnt remember it and also highest value will be fine as 0 in this case but could also be used as -infinity or None maybe better here


# Refactored Approach
def most_frequent_char_refcator(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    best = None
    for char in s:
        if best is None or count[char] > count[best]:
            best = char

    return best


# Time: O(n + n) = O(2n) = O(n)
# Space: O(n)


# Notes -
