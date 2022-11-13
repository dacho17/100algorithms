def map_dfs(map, visited, y, x):
    if (y, x) in visited or map[y][x] == 0:
        return 0
    visited.add((y, x))
    size = 1
    if -1 < y + 1 < len(map):       # DOWN
        size += map_dfs(map, visited, y + 1, x)
    elif -1 < y - 1 < len(map):     # UP
        size += map_dfs(map, visited, y - 1, x)
    if -1 < x + 1 < len(map[y]):    # RIGHT
        size += map_dfs(map, visited, y, x + 1)
    if -1 < x - 1 < len(map):       # LEFT
        size += map_dfs(map, visited, y, x - 1)
    return size

def find_largest_island(map):
    largest, visited = 0, set()
    for i in range(len(map)):
        for j in range(len(map[i])):
            largest = max(largest, map_dfs(map, visited, i, j))
    return largest
