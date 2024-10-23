# minimum island
# Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.
#
# You may assume that the grid contains at least one island.


grid = [
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]

# minimum_island(grid) # -> 2


# Similar to the last approach, iterate through each graph index checking its inbounds and valid. If it is record the position and explore recursively from that location checking for linked island nodes


def minimum_island(grid):
    visited = set()
    smallest = float("inf")

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            count = explore(grid, r, c, visited)
            if count > 0 and count < smallest:
                smallest = count

    return smallest


def explore(grid, r, c, visited):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])

    if not row_inbound or not col_inbound:
        return 0

    if grid[r][c] == "W":
        return 0

    pos = (r, c)

    if pos in visited:
        return 0

    visited.add(pos)

    sum = 1

    sum += explore(grid, r - 1, c, visited)
    sum += explore(grid, r + 1, c, visited)
    sum += explore(grid, r, c - 1, visited)
    sum += explore(grid, r, c + 1, visited)
    return sum


# Time: O(rc)
# Space: O(rc)

# rows and cols
