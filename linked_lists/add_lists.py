#
# add lists
# Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.
#
# You must do this by traversing through the linked lists once.
#
#
#
# Say we wanted to compute 621 + 354 normally. The sum is 975:
#
#    621
#  + 354
#  -----
#    975
#
# Then, the reversed linked list format of this problem would appear as:
#
#     1 -> 2 -> 6
#  +  4 -> 5 -> 3
#  --------------
#     5 -> 7 -> 9
#
#


# Approach - keep track of the carry over 9 to add it to the next iteration, we then sum the values of the two heads + carry, if the sum is over 9 we carry over to the next
# loop. We then set and create the nodes. If the heads arent None we move them along.


def add_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head

    carry = 0
    current_1 = head_1
    current_2 = head_2

    while current_1 is not None or current_2 is not None or carry == 1:
        val_1 = 0 if current_1 is None else current_1.val
        val_2 = 0 if current_2 is None else current_2.val
        sum = val_1 + val_2 + carry
        carry = 1 if sum > 9 else 0
        digit = sum % 10

        tail.next = Node(digit)
        tail = tail.next

        if current_1 is not None:
            current_1 = current_1.next

        if current_2 is not None:
            current_2 = current_2.next

    return dummy_head.next


# Time: O(max(n, m))
# Space: O(max(n, m))


def add_lists_recursive(head_1, head_2, carry=0):
    if head_1 is None and head_2 is None and carry == 0:
        return None
    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val

    sum = val_1 + val_2 + carry
    digit = sum % 10
    next_carry = 1 if sum > 9 else 0

    result = Node(digit)
    next_1 = None if head_1 is None else head_1.next
    next_2 = None if head_2 is None else head_2.next

    result.next = add_lists_recursive(next_1, next_2, next_carry)
    return result


# Time: O(max(n, m))
# Space: O(max(n, m))


# Notes - a few edge cases to handle recursively with the values and next results, but pretty self explanatory.

# We keep calling until we have both heads None and also the carry as 0, if we dont have the carry as 0 we are missing out on adding the last node

# We can work out the overflow by using modulo which gives us the node for that call and passing 1 over to the next call (it will always be 1 if it carries because we are reversing the nums. So ie if we have 9 + 9 which is the max single values we can add 8 and carry the 1)

# We then handle the next again and because we arent returning if a head is None we have to handle it with None and pass it to result.next before we finally return the correct nodes


# #   621
# # + 354
# # -----
# #   975
#
# a1 = Node(1)
# a2 = Node(2)
# a3 = Node(6)
# a1.next = a2
# a2.next = a3
# # 1 -> 2 -> 6
#
# b1 = Node(4)
# b2 = Node(5)
# b3 = Node(3)
# b1.next = b2
# b2.next = b3
# # 4 -> 5 -> 3
#
# add_lists(a1, b1)
# # 5 -> 7 -> 9
