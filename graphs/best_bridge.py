# best bridge
# Write a function, best_bridge, that takes in a grid as an argument. The grid contains water (W) and land (L). There are exactly two islands in the grid. An island is a vertically or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.


# Approach - Search through graph and find 1 island, store those locations. Search for second island and work back to first keeping count value.


grid = [
    ["W", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "L"],
    ["L", "L", "L", "W", "L"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
]
# best_bridge(grid) # -> 1


from collections import deque


def best_bridge(grid):
    visited = set()
    found_island = False

    for r in range(len(grid)):
        if found_island:
            break
        for c in range(len(grid[0])):
            if grid[r][c] == "L":
                explore_land(grid, r, c, visited)
                found_island = True
                break

    main_island = set(visited)

    queue = deque([])
    for pos in main_island:
        r, c = pos
        queue.append((r, c, 0))

    while queue:
        r, c, distance = queue.popleft()
        deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        if grid[r][c] == "L" and (r, c) not in main_island:
            return distance - 1

        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = r + delta_row
            neighbor_col = c + delta_col
            neighbor_pos = (neighbor_row, neighbor_col)

            if (
                check_inbounds(grid, neighbor_row, neighbor_col)
                and neighbor_pos not in main_island
            ):
                queue.append((neighbor_row, neighbor_col, distance + 1))


def explore_land(grid, r, c, visited):
    if not check_inbounds(grid, r, c):
        return None

    pos = r, c

    if grid[r][c] == "W" or pos in visited:
        return None

    visited.add(pos)

    explore_land(grid, r + 1, c, visited)
    explore_land(grid, r - 1, c, visited)
    explore_land(grid, r, c + 1, visited)
    explore_land(grid, r, c - 1, visited)

    return visited


def check_inbounds(grid, r, c):
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    return row_inbounds and col_inbounds


# r = number of rows
# c = number of cols

# Time: O(rc)
# Space: O(rc)
