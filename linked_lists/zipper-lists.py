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


# Recursive Version

# head_1 list = a, b, b
# head_2 list = x, y, z


def recursive_zipper_lists(head_1, head_2):
    # Set the base cases to end the recursive calls
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1

    # save the pointers to the next nodes
    next_1 = head_1.next
    next_2 = head_2.next

    # Here we do the switching of the nodes so for example a > x
    # The bit that takes some understanding is how head_2 takes the recursive leap of faith which ill explain below
    head_1.next = head_2
    head_2.next = recursive_zipper_lists(next_1, next_2)
    return head_1


# Time: O(min(n + m))
# Space: O(min(n + m))

# The space on this one because we have to store the recursive calls is increased from the iterative version

# Explanation - This one took a little understanding to try to fully understand how the recursive calls work

# The Base cases -

# Nothing special here that needs explaining its just the base cases of the recursive call which if both are None, None gets returned otherwise if one of the heads is None we return the
# alternate one

# Next Pointers

# Here we just save the variable of the next in the current list


# Switching the pointers
# we set head_1.next to head_2 - Originally it would have been a > b
# We switch this to go now from a > x


# The Recursive Leap
# This is where it can get a little confusing and i think the best way to explain it is show the recursive calls

# Original Call
# zipper(a , x)

# next_1 = b
# next_2 = y

# head_1.next = x   # a > x
# head_2.next = zipper(b, y)

# Call 1

# zipper(b, y)
# next_1 = c
# next_2 = z

# head_1.next = y
# head_2.next = zipper(c, z)

# Call 2

# zipper(c, z)

# next_1 = None
# next_2 = None

# head_1.next = z
# head_2.next = ziper(None, None)

# Call 3

# zipper(none, none)

# if head_1 is none and head_2 is none:
# return None

#########################
# RECURSIVE RECALL HERE #
#########################


# We back track and now start to return to the previous calls the call that called this zipper(none, none)

# Call 3 returning to call 2

# # Call 2

# zipper(c, z)

# next_1 = None
# next_2 = None

# head_1.next = z # c > z
# head_2.next now is returned as 'None'

# head_2.next = None  # z > None

# return C # here we return head_1 on the next line of the function which is 'C'


# We now return to call 1


# Call 1

# zipper(b, y)
# next_1 = c
# next_2 = z

# head_1.next = y       # b > y
# head_2.next = C # This now settles as the 'C' returned from the previous return       # y > c

# return b # again returning head_1


# Original call


# Original Call
# zipper(a , x)

# next_1 = b
# next_2 = y

# head_1.next = x   # a > x
# head_2.next = b   # b > y

# return head_1 of 'a' to the original invocation
# a > x > b > y > c > z


# Hopefull that makes sense....the best way is to draw it out and follow the recursive nature of the calls.
