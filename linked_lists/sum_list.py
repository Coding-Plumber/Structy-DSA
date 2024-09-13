# sum list
# Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.


# a = Node(2)
# b = Node(8)
# c  = Node(3)
# d = Node(-1)
# e  = Node(7)
#
# a .next = b
# b.next = c
# c .next = d
# d.next = e
#
# # 2 -> 8 -> 3 -> -1 -> 7
#
# sum_list(a) # 19


# Approach - Can do it in a while loop increasing head.next till == None whilst summing head.val which would be a better space complexity, also can be done recursively in a similar manner of recursively calling and keeping track of the sum


def iter_sum_list(head):
    total_sum = 0
    current = head
    while current is not None:
        total_sum += current.val
        current = current.next
    return total_sum


# Time: O(n)
# Space: O(1)


def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)


# Time: O(n)
# Space: O(n)
