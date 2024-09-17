# get node value
# Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.
#
# If there is no node at the given index, then return None.


# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
#
# a.next = b
# b.next = c
# c.next = d

# a -> b -> c -> d

# get_node_value(a, 2) # 'c'


def get_node_value(head, index):
    current = head
    node = ""
    count = 0

    while current != None:
        if count == index:
            node = current.val
            return node

        count += 1
        current = current.next

    return node or None


# Time: O(n)
# Space: O(1)


def get_node_value_rec(head, index):
    if head is None:
        return None

    if index == 0:
        return head.val

    return get_node_value_rec(head.next, index - 1)


# Time: O(n)
# Space: O(n)


# Notes - the reason the recursive calls have higher space complexity is because it takes up n space on the call stack each iteartion where as the iterative one in the
# while loop is within the same scope call so it only uses O(1)
