# merge lists
# Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.
#
# Do this in-place, by mutating the original Nodes.
#
# You may assume that both input lists are non-empty and contain increasing sorted numbers.

# a = Node(5)
# b = Node(7)A
# c = Node(10)
# d = Node(12)
# e = Node(20)
# f = Node(28)
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# # 5 -> 7 -> 10 -> 12 -> 20 -> 28
#
# q = Node(6)
# r = Node(8)
# s = Node(9)
# t = Node(25)
# q.next = r
# r.next = s
# s.next = t
# # 6 -> 8 -> 9 -> 25
#
# merge_lists(a, q)
# # 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28


def merge_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head
    curr_1 = head_1
    curr_2 = head_2

    while curr_1 is not None and curr_2 is not None:
        if curr_1.val < curr_2.val:
            tail.next = curr_1
            curr_1 = curr_1.next
        else:
            tail.next = curr_2
            curr_2 = curr_2.next

        tail = tail.next

    if curr_1 is not None:
        tail.next = curr_1
    if curr_2 is not None:
        tail.next = curr_2

    return dummy_head.next


# Time: O(min(n + m))
# Space: O(1)

# The main part of this solution is how we create a dummy_head which gives us a point to return, returning dummy_head.next gives us a return point of the new merged list
# Then inside the while loop we are assigning tail.next to point to the current lowest head ie
# cur_1 = 5, cur_2 = 6
# tail is set to point at 5 and we increase cur_1 to its next node
# curr_1 = 5 -> 7 -> 10 -> 12
#               ^
# increase tail to = 5
# next iteration
# cur_1 = 7, cur_2 = 6
# tail.next > 6
# curr_2 > 8
# tail moved to 6

# Then we exit the while loop once None has been hit on one or both nodes, we then assign the end node that isnt None as the remainder of the list


def merge_list_rec(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    if head_1.val < head_2.val:
        head_1.next = merge_list_rec(head_1.next, head_2)
        return head_1
    else:
        head_2.next = merge_list_rec(head_1, head_2.next)
        return head_2


# Time: O(min(n + m))
# Space: O(min(n + m))

# We set out our base cases similar to the iterative version
# then a comparison is set where we make our next call returning
# Best way to show this one is with an example

# head_1 = 1 -> 3 -> 5, head_2 = 2 -> 4 -> 6

# call0(1, 2): 1 < 2, so we choose 1 and make recursive call with (3, 2)
# call1(3, 2): 3 > 2, so we choose 2 and make recursive call with (3, 4)
# call2(3, 4): 3 < 4, so we choose 3 and make recursive call with (5, 4)
# call3(5, 4): 5 > 4, so we choose 4 and make recursive call with (5, 6)
# call4(5, 6): 5 < 6, so we choose 5 and make recursive call with (None, 6)
# call5(None, 6): head_1 is None, so we return 6
#
# Now, the functions return and link nodes:
#
# call4 returns: 5 is linked to 6, returns 5
# call3 returns: 4 is linked to 5, returns 4
# call2 returns: 3 is linked to 4, returns 3
# call1 returns: 2 is linked to 3, returns 2
# call0 returns: 1 is linked to 2, returns 1
#
# The final result is 1 → 2 → 3 → 4 → 5 → 6
#
