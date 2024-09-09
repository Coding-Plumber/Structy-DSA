# compress

# Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

# 'aaa' compresses to '3a'
# cc' compresses to '2c'
# 't' should remain as 't'
# You can assume that the input only contains alphabetic characters.

# compress('ccaaatsss') # -> '2c3at3s'

# Approach - Use two pointer checking that i != j and then getting a count of the difference between them


def compress(s):
    s += "!"
    i = 0
    j = 0
    result = []

    print("len:", len(s))
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            val = j - i

            if val != 1:
                result.append(str(val))
                result.append(s[i])
            else:
                result.append(s[i])
            i = j
            j += 1
            print("j", j)

    return "".join(result)


# Adding the s += '!' so that it does the final iteration without j running out of range

# Time: O(n)
# Space: O(n)

# Leetcode similar - https://leetcode.com/problems/string-compression/description/
