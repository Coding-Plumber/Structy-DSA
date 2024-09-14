# linked list find
# Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.
#
#
# a  = Node("a")
# # b = Node("b")
# c = Node("c")
# d  = Node("d")
#
# a.next = b
# b.next = c
# c.next = d
#
# a -> b -> c -> d

# linked_list_find(a, "c") # True

# Approach - can be done in the same while loop set up as before or again recursively


def linked_list_find(head, target):
    current = head

    while current != None:
        if current.val == target:
            return True

        current = current.next

    return False


# Time: O(n)
# Space: O(1)


def linked_list_find_recursive(head, target):
    if head == None:
        return False

    if head.val == target:
        return True

    return linked_list_find_recursive(head.next, target)


# Time: O(n)
# Space: O(n)
