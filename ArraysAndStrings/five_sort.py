# five sort
# Write a function, five_sort, that takes in a list of numbers as an argument. The function should rearrange elements of the list such that all 5s appear at the end. Your function should perform this operation in-place by mutating the original list. The function should return the list.
#
# Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.

# Approach - two pointer, start with i at index[0] j at [-1] and do a check if i is 5 i can switch it with j and then update the location

# five_sort([12, 5, 1, 5, 12, 7])
# -> [12, 7, 1, 12, 5, 5]


def five_sort(nums):
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[j] == 5:
            j -= 1
        if nums[i] != 5:
            i += 1
        if nums[i] == 5 and nums[j] != 5:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            i += 1

    return nums


# Time: O(n)
# Space: O(1)

# Refactored and tidied up


def five_sort_refactored(nums):
    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[j] == 5:
            j -= 1
        elif nums[i] != 5:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums


# Notes fairly simple one just neatened it up with better python code
