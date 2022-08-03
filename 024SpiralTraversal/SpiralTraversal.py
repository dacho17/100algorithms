import enum

class Direction(enum.Enum):
    Right = 1
    Down = 2
    Left = 3
    Up = 4

class Grid(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.current_traversal = None

    def __init_traversal(self):
        l = 0
        r = len(self.matrix[0]) - 1
        t = 0
        b = len(self.matrix) - 1
        return l, r, t, b

    def traverse_spirally(self):
        left_edge, right_edge, top_edge, bot_edge = self.__init_traversal()
        direction = Direction.Right

        res = []
        while top_edge <= bot_edge and left_edge <= right_edge:
            if direction == Direction.Right:
                for col in range(left_edge, right_edge + 1):
                    res.append(self.matrix[top_edge][col])
                top_edge += 1
                direction = Direction.Down
                continue
            elif direction == Direction.Down:
                for row in range(top_edge, bot_edge + 1):
                    res.append(self.matrix[row][right_edge])
                right_edge -= 1
                direction = Direction.Left
                continue
            elif direction == Direction.Left:
                for col in range(right_edge, left_edge - 1, -1):
                    res.append(self.matrix[bot_edge][col])
                bot_edge -= 1
                direction = Direction.Up
                continue
            elif direction == Direction.Up:
                for row in range(bot_edge, top_edge - 1, -1):
                    res.append(self.matrix[row][left_edge])
                left_edge += 1
                direction = Direction.Right
                continue
        return res
