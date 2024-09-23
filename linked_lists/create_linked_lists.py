# create linked list
# Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.


# create_linked_list(["h", "e", "y"])
# # h -> e -> y

# Approach - create a starting node we can return from, then loop through values assigning and creating new values from the current tail


def create_linked_list(values):
    dummy_head = Node(None)
    tail = dummy_head
    for val in values:
        tail.next = Node(val)
        tail = tail.next
    return dummy_head.next


# Time: O(n)
# Space: O(n)


def create_linked_list_recursive(values, count=0):
    if count == len(values):
        return None
    new_node = Node(values[count])
    new_node.next = create_linked_list_recursive(values, count + 1)
    return new_node


# Time: O(n)
# Space: O(n)

# Approach - keep a check on the cycle of the recursive calls with  a counter and use that to access the values index to create and assign the node from
