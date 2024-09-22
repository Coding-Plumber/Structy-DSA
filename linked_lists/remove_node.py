# remove node
# Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.
#
# Do this in-place.
#
# You may assume that the input list is non-empty.
#
# You may assume that the input list contains the target.
#
#
#
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
# remove_node(a, "c")
# # a -> b -> d -> e -> f


# Approach - Make two pointers, one at current (head) and one at head.next. Check if next == target_val and if so change curr.next to next.next bypassing the node that needs removing. One thing we will have to check for though is the first node will be bypassed so will need an initial check for the first node and if that is true we can automatically return.


def remove_node(head, target_val):
    curr = head
    next = curr.next

    if curr.val == target_val:
        curr = next
        return curr

    while next is not None:
        if next.val == target_val:
            curr.next = next.next
            return head
        curr = curr.next
        next = next.next

    return head


# Time: O(n)
# Space: O(1)


# We can also do this recursively, because we only need to change one node we can return it if the case of head.val == target_val and return head.next bypassing that current node in the chain


def remove_node_recursive(head, target_val):
    if head is None:
        return None

    if head.val == target_val:
        return head.next

    head.next = remove_node_recursive(head.next, target_val)
    return head


# Time: O(n)
# Space: O(n)
