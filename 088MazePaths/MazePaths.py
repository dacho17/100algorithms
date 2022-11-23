def calculate_maze_paths(maze):
    combinations = [[0] * len(maze[0]) for _ in range(len(maze))]
    combinations[0][0] = 1
    for row in range (0, len(maze)):
        for col in range (0, len(maze[0])):
            if maze[row][col] == 1:
                combinations[row][col] = 0
                continue
            if row != 0:
                combinations[row][col] += combinations[row-1][col]
            if col != 0:
                combinations[row][col] += combinations[row][col - 1]
    return combinations[-1][-1]
