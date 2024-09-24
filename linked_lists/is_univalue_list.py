# is univalue list
# Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.
#
# You may assume that the input list is non-empty.
#
# a = Node(7)
# b = Node(7)
# c = Node(7)
#
# a.next = b
# b.next = c
#
# # 7 -> 7 -> 7
#
# is_univalue_list(a) # True
#


# Approach - a simple while loop checking against head and if not the same val return False


def is_univalue_list(head):
    curr = head

    while curr is not None:
        if curr.val != head.val:
            return False
        curr = curr.next
    return True


# Time: O(n)
# Space: O(1)


def is_univalue_list_recursive(head, prev_val=None):
    if head is None:
        return True
    if prev_val is None or head.val == prev_val:
        return is_univalue_list_recursive(head.next, head.val)
    else:
        return False


# Time: O(n)
# Space: O(n)


# Notes - if head is None it means we have reached the end without hitting False, otherwise we check for head.val == prev_val and if so we go again.
# we pass the previous value to check against the current head.val
# If these dont match we return False
