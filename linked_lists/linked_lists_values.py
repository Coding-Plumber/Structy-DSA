# linked list values
# Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.
#
# Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive! -AZ


# Approach - This can be done two ways either in a while loop moving current along to current.next after appending it to a list to return or recursively


def linked_list_values(head):
    result = []

    current = head

    while current != None:
        result.append(current.val)
        current = current.next

    return result


# Time: O(n)
# Space: O(n)


# Recursive method


def linked_list_values_recursive(head):
    result = []
    _linked_list_values(head, result)
    return result


def _linked_list_values(head, result):
    if head == None:
        return
    result.append(head.val)
    _linked_list_values(head.next, result)


# Time: O(n)
# Space: O(n) - However we do use O(n) space on the call stack also


# The recursive one works by passing the function an array and then it recursively calls on itself appending head.val to result
# We hit the base case of None and start to return. The values are all stored in result so once the recursive calls have ended we can
# then return result with the new values.
