# reverse list
# Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
#
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
#
# # a -> b -> c -> d -> e -> f
#
# reverse_list(a) # f -> e -> d -> c -> b -> a


# Approach - We need to create a store value for the next pointer so we can switch it. For example:
# a > b > c
# we need to hold the state of prev but also for the first node it has to be set to None to signal the end of the linked list
# so we start with prev = None outside the while loop we will set
# we then need to get the next node therefore we set next = current.next // 'b'
# current.next = prev // 'None'
# prev = current // 'a'
# current.next = next // 'b'

# This sends us to b in the node list and we can then switch the vaules so we now get

# next = c // store the next node in the list
# curr.next = prev // sets it to previous node of a
# prev = current // store the current node value as previous for next iteration
# current = c // moves the iteration forward

# We would now have something like this c > b > a > None


def reverse_list(head):
    current = head  # a
    prev = None  # None

    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


# Time: O(n)
# Space: O(1)


# Recursive method - actually looks a lot nicer and makes it easier to understand (imo) just slightly worse space complexity again because of the call stacks


def reverse_list_rec(head, prev=None):
    if head is None:
        return prev
    next = head.next  # get next node
    head.next = prev  # set prev node
    return reverse_list_rec(next, head)


# Time: O(n)
# Space: O(n)
