# longest streak
# Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.


# a = Node(5)
# b = Node(5)
# c = Node(7)
# d = Node(7)
# e = Node(7)
# f = Node(6)
#
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
#
# # 5 -> 5 -> 7 -> 7 -> 7 -> 6
#
# longest_streak(a) # 3

# Approach - Fairly straight forward, compare the previous value and current and hold the longest streak. Have to manage the node counting so it isnt behind by 1


def longest_streak(head):
    curr = head
    prev_val = None
    current_streak = 0
    max_streak = 0

    while curr is not None:
        if curr.val == prev_val:
            current_streak += 1
        else:
            current_streak = 1

        prev_val = curr.val

        if current_streak > max_streak:
            max_streak = current_streak

        curr = curr.next

    return max_streak


# Time: O(n)
# Space: O(1)
