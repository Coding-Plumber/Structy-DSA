# zipper lists
# Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.
#
# Do this in-place, by mutating the original Nodes.
#
# You may assume that both input lists are non-empty.


# a = Node("a")
# b = Node("b")
# c = Node("c")
# a.next = b
# b.next = c
# # a -> b -> c
#
# x = Node("x")
# y = Node("y")
# z = Node("z")
# x.next = y
# y.next = z
# # x -> y -> z
#
# zipper_lists(a, x)
# # a -> x -> b -> y -> c -> z

# Approach - i originally planned this to be a while loop holding many temp variables to keep alternating however it got messy and im sure its still possible i decided to learn a better way.


def zipper_lists(head_1, head_2):
    tail = head_1
    curr_1 = head_1.next
    curr_2 = head_2
    count = 0

    while curr_1 is not None and curr_2 is not None:
        if count % 2 == 0:
            tail.next = curr_2  # x
            curr_2 = curr_2.next  # y
        else:
            tail.next = curr_1  #
            curr_1 = curr_1.next
        count += 1
        tail = tail.next

    if curr_1 is None:
        tail.next = curr_2
    if curr_2 is None:
        tail.next = curr_1

    return head_1


# n = length of list 1
# m = length of list 2
# Time: O(min(n + m))
# Space: O(1)

# O(min(n + m)) just means its the smallest of the 2 if the lists were of differnet lengths. If n = 30 and m = 100 it would go off n because once those 30 are done it has completed
# the algorithm.
