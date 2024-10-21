# island count
# Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.


# grid = [
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'W', 'W', 'L', 'W'],
#   ['W', 'W', 'L', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['L', 'L', 'W', 'W', 'W'],
# ]
#
# island_count(grid) # -> 3


# Iterate through the grid locations and call on a helper function that can check the adjacent indexes


def island_count(grid):
    visited = set()

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited) == True:
                count += 1

    return count


def explore(grid, r, c, visited):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return False

    if grid[r][c] == "W":
        return False

    pos = (r, c)
    if pos in visited:
        return False

    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True


# Time: O(rc)
# Space: O(rc)

# Note - the reason its O(r*c) is because we have two for loops and then under that is a recursive call, however because we return from already visited calls and we can never visit the same location twice its still a constant amount. For example at worst case if all indexes == 'L' we would visit them in one go and couldnt return with other calls.
