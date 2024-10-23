# knight attack
# A knight and a pawn are on a chess board. Can you figure out the minimum number of moves required for the knight to travel to the same position of the pawn? On a single move, the knight can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction. This means that on a single move, a knight has eight possible positions it can move to.
#
# Write a function, knight_attack, that takes in 5 arguments:
#
# n, kr, kc, pr, pc
#
# n = the length of the chess board
# kr = the starting row of the knight
# kc = the starting column of the knight
# pr = the row of the pawn
# pc = the column of the pawn
# The function should return a number representing the minimum number of moves required for the knight to land ontop of the pawn. The knight cannot move out-of-bounds of the board. You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7. If it is not possible for the knight to attack the pawn, then return None.


# knight_attack(8, 1, 1, 2, 2) # -> 2


from collections import deque


def knight_attack(n, kr, kc, pr, pc):
    visited = set()
    visited.add((kr, kc))
    queue = deque([(kr, kc, 0)])

    while queue:
        r, c, distance = queue.popleft()

        if r == pr and c == pc:
            return distance

        valid_positions = check_knight(r, c, n)
        for position in valid_positions:
            nr, nc = position
            if position not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, distance + 1))

    return None


def check_knight(r, c, n):
    positions = [
        (r + 2, c + 1),
        (r - 2, c + 1),
        (r + 2, c - 1),
        (r - 2, c - 1),
        (r + 1, c + 2),
        (r - 1, c + 2),
        (r + 1, c - 2),
        (r - 1, c - 2),
    ]

    valid_positions = []

    for pos in positions:
        r, c = pos
        if 0 <= r < n and 0 <= c < n:
            valid_positions.append((r, c))

    return valid_positions


# Time: O(n^2)
# Space: O(n^2)
