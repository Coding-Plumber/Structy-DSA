# insert node
# Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.
#
# Do this in-place.
#
# You may assume that the input list is non-empty and the index is not greater than the length of the input list.

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
#
# a.next = b
# b.next = c
# c.next = d
#
# # a -> b -> c -> d
#
# insert_node(a, 'x', 2)
# # a -> b -> x -> c -> d

# Approach - Keep a count for iterations and if we match index then we have the correct insertation point. Take a curr.next copy, change curr.next to new_node and then add new_node.next
# to be the copy of the curr.next we just took


def insert_node(head, value, index):
    new_node = Node(value)

    if index == 0:
        new_node.next = curr
        return new_node

    curr = head
    count = 1

    while count <= index:

        if count == index:
            next = curr.next
            curr.next = new_node
            new_node.next = next

        curr = curr.next
        count += 1

    return head


def insert_node_recursive(head, value, index, count=1):
    if index == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node

    if head is None:
        return None

    if index == count:
        temp = head.next
        head.next = Node(value)
        head.next.next = temp
        return head

    head.next = insert_node_recursive(head.next, value, index, count + 1)

    return head


# Time: O(n)
# Space: O(n)

# Approach - Add a count for each recursive call increased by 1, when that matches with index we know we are at the right call. We can then insert the new node
